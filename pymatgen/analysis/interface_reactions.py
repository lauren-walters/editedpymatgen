# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

"""
This module provides a class to predict and analyze interfacial reactions between two
solids, with or without an open element (e.g., flowing O2).

Please consider citing one or both of the following papers if you use this
code in your own work.

References:

    Richards, W. D., Miara, L. J., Wang, Y., Kim, J. C., &amp; Ceder, G. (2015).
    Interface stability in solid-state batteries. Chemistry of Materials, 28(1),
    266–273. https://doi.org/10.1021/acs.chemmater.5b04082

    Xiao, Y., Wang, Y., Bo, S.-H., Kim, J. C., Miara, L. J., &amp; Ceder, G. (2019).
    Understanding interface stability in solid-state batteries.
    Nature Reviews Materials, 5(2), 105–126. https://doi.org/10.1038/s41578-019-0157-5

"""

import os
import json
import warnings

from typing import List, Tuple
import numpy as np

from monty.json import MSONable
from monty.dev import deprecated
from pymatgen.util.plotting import pretty_plot
from pymatgen.util.string import latexify, htmlify

import pandas
from plotly.graph_objects import Scatter, Figure

from pymatgen.analysis.phase_diagram import PhaseDiagram, GrandPotentialPhaseDiagram
from pymatgen.analysis.reaction_calculator import Reaction
from pymatgen.core.composition import Composition

__author__ = "Yihan Xiao, Matthew McDermott"
__maintainer__ = "Matthew McDermott"
__email__ = "mcdermott@lbl.gov"
__date__ = "Sep 1, 2021"

with open(os.path.join(os.path.dirname(__file__), "..", "util", "plotly_interface_rxn_layouts.json")) as f:
    plotly_layouts = json.load(f)


class InterfacialReactivity(MSONable):
    """
    Class for modeling an interface between two solids and its possible reactions.
    The two reactants are provided as Composition objects (c1 and c2), along with the
    relevant compositional PhaseDiagram object. Possible reactions are calculated by
    finding all points along a tie-line between c1 and c2 where there is a "kink" in
    the phase diagram; i.e. a point or facet of the phase diagram.

    Please consider citing one or both of the following papers if you use this code
    in your own work.

    References:
        Richards, W. D., Miara, L. J., Wang, Y., Kim, J. C., &amp; Ceder, G. (2015).
        Interface stability in solid-state batteries. Chemistry of Materials, 28(1),
        266–273. https://doi.org/10.1021/acs.chemmater.5b04082

        Xiao, Y., Wang, Y., Bo, S.-H., Kim, J. C., Miara, L. J., &amp; Ceder, G. (2019).
        Understanding interface stability in solid-state batteries.
        Nature Reviews Materials, 5(2), 105–126.
        https://doi.org/10.1038/s41578-019-0157-5
    """

    EV_TO_KJ_PER_MOL = 96.4853

    def __init__(
        self,
        c1: Composition,
        c2: Composition,
        pd: PhaseDiagram,
        norm: bool = True,
        use_hull_energy: bool = False,
        **kwargs
    ):
        """
        Args:
            c1: Reactant 1 composition
            c2: Reactant 2 composition
            pd: Phase diagram object built from all elements in composition c1 and c2.
            norm: Whether or not the total number of atoms in composition
                of reactant will be normalized to 1.
            use_hull_energy: Whether or not use the convex hull energy for
                a given composition for reaction energy calculation. If false,
                the energy of ground state structure will be used instead.
                Note that in case when ground state can not be found for a
                composition, convex hull energy will be used associated with a
                warning message.
        """
        bypass_grand_warning = kwargs.get("bypass_grand_warning", False)

        if isinstance(pd, GrandPotentialPhaseDiagram) and not bypass_grand_warning:
            raise ValueError(
                "Please use the GrandPotentialInterfacialReactivity "
                "class for interfacial reactions with open elements!"
            )

        self.c1 = c1
        self.c2 = c2
        self.pd = pd
        self.norm = norm
        self.use_hull_energy = use_hull_energy

        self.c1_original = c1
        self.c2_original = c2
        self.comp1 = c1
        self.comp2 = c2

        # Factor is the compositional ratio between composition self.c1 and
        # processed composition self.comp1. For example, the factor for
        # Composition('SiO2') and  Composition('O') is 2.0. This factor will be used
        # to convert mixing ratio in self.comp1 - self.comp2 tie line to that in
        # self.c1 - self.c2 tie line.
        self.factor1 = 1.0
        self.factor2 = 1.0

        if self.norm:
            self.c1 = c1.fractional_composition
            self.c2 = c2.fractional_composition
            self.comp1 = self.comp1.fractional_composition
            self.comp2 = self.comp2.fractional_composition

        if not bypass_grand_warning:
            # Computes energies for reactants in different scenarios.
            if self.use_hull_energy:
                self.e1 = self.pd.get_hull_energy(self.comp1)
                self.e2 = self.pd.get_hull_energy(self.comp2)
            else:
                self.e1 = self._get_entry_energy(self.pd, self.comp1)
                self.e2 = self._get_entry_energy(self.pd, self.comp2)

    def get_kinks(self) -> List[Tuple[int, float, float, str, float]]:
        """
        Finds all the kinks in mixing ratio where reaction products changes
        along the tie-line of composition self.c1 and composition self.c2.

        Returns:
            Zip object of tuples (index, mixing ratio,
                                  reaction energy per atom in eV/atom,
                                  reaction formula,
                                  reaction energy per mol of reaction
                                  formula in kJ/mol).
        """
        c1_coord = self.pd.pd_coords(self.comp1)
        c2_coord = self.pd.pd_coords(self.comp2)

        n1 = self.comp1.num_atoms
        n2 = self.comp2.num_atoms

        critical_comp = self.pd.get_critical_compositions(self.comp1, self.comp2)
        x_kink, energy_kink, react_kink, energy_per_rxt_formula = [], [], [], []

        if (c1_coord == c2_coord).all():
            x_kink = [0, 1]
            energy_kink = [self._get_energy(x) for x in x_kink]
            react_kink = [self._get_reaction(x) for x in x_kink]
            num_atoms = [(x * self.comp1.num_atoms + (1 - x) * self.comp2.num_atoms) for x in x_kink]
            energy_per_rxt_formula = [
                energy_kink[i]
                * self._get_elmt_amt_in_rxn(react_kink[i])
                / num_atoms[i]
                * InterfacialReactivity.EV_TO_KJ_PER_MOL
                for i in range(2)
            ]
        else:
            for i in reversed(critical_comp):
                # Gets mixing ratio x at kinks.
                c = self.pd.pd_coords(i)
                x = np.linalg.norm(c - c2_coord) / np.linalg.norm(c1_coord - c2_coord)
                # Modifies mixing ratio in case compositions self.comp1 and
                # self.comp2 are not normalized.
                x = x * n2 / (n1 + x * (n2 - n1))
                n_atoms = x * self.comp1.num_atoms + (1 - x) * self.comp2.num_atoms
                # Converts mixing ratio in comp1 - comp2 tie line to that in
                # c1 - c2 tie line.
                x_converted = self._convert(x, self.factor1, self.factor2)
                x_kink.append(x_converted)
                # Gets reaction energy at kinks
                normalized_energy = self._get_energy(x)
                energy_kink.append(normalized_energy)
                # Gets balanced reaction at kinks
                rxt = self._get_reaction(x)
                react_kink.append(rxt)
                rxt_energy = normalized_energy * self._get_elmt_amt_in_rxn(rxt) / n_atoms
                energy_per_rxt_formula.append(rxt_energy * self.EV_TO_KJ_PER_MOL)
        index_kink = range(1, len(critical_comp) + 1)

        return list(zip(index_kink, x_kink, energy_kink, react_kink, energy_per_rxt_formula))

    def plot(self, backend: str = "plotly") -> Figure:
        """
        Plots reaction energy as a function of mixing ratio x in self.c1 - self.c2
        tie line.

        Args:
            backend: Plotting library used to create plot. Defaults to "plotly".
            Can alternatively be set to "matplotlib"

        Returns:
            Plot of reaction energies as a function of mixing ratio
        """

        if backend.lower() == "plotly":
            fig = self._get_plotly_figure()
        elif backend.lower() in ["matplotlib", "mpl", "plt"]:
            fig = self._get_matplotlib_figure()
        else:
            raise ValueError("The provided backend is not a valid option!")

        return fig

    def get_dataframe(self):
        """

        Returns:

        """
        rxns = [
            {
                "Atomic fraction": round(ratio, 3),
                "Reaction": rxn,
                "E$_{\textrm{rxn}}$ (kJ/mol)": round(rxn_energy, 1),
                "E$_{\textrm{rxn}}$ (eV/atom)": round(reactivity, 3),
            }
            for _, ratio, reactivity, rxn, rxn_energy in self.get_kinks()
        ]

        df = pandas.DataFrame(rxns)
        return df

    def get_critical_original_kink_ratio(self):
        """
        Returns a list of molar mixing ratio for each kink between ORIGINAL
        (instead of processed) reactant compositions. This is the
        same list as mixing ratio obtained from get_kinks method
        if self.norm = False.

        Returns:
            A list of floats representing molar mixing ratios between
            the original reactant compositions for each kink.
        """
        ratios = []
        if self.c1_original == self.c2_original:
            return [0, 1]
        reaction_kink = [k[3] for k in self.get_kinks()]
        for rxt in reaction_kink:
            ratios.append(abs(self._get_original_composition_ratio(rxt)))
        return ratios

    def _get_original_composition_ratio(self, reaction):
        """
        Returns the molar mixing ratio between the reactants with ORIGINAL (
        instead of processed) compositions for a reaction.

        Args:
            reaction (Reaction): Reaction object that contains the original
                reactant compositions.

        Returns:
            The molar mixing ratio between the original reactant
            compositions for a reaction.
        """
        if self.c1_original == self.c2_original:
            return 1
        c1_coeff = reaction.get_coeff(self.c1_original) if self.c1_original in reaction.reactants else 0
        c2_coeff = reaction.get_coeff(self.c2_original) if self.c2_original in reaction.reactants else 0
        return c1_coeff * 1.0 / (c1_coeff + c2_coeff)

    def _get_energy(self, x):
        """
        Computes reaction energy in eV/atom at mixing ratio x : (1-x) for
        self.comp1 : self.comp2.

        Args:
            x (float): Mixing ratio x of reactants, a float between 0 and 1.

        Returns:
            Reaction energy.
        """
        return self.pd.get_hull_energy(self.comp1 * x + self.comp2 * (1 - x)) - self.e1 * x - self.e2 * (1 - x)

    def _get_reactants(self, x):
        # Uses original composition for reactants.
        if np.isclose(x, 0):
            reactants = [self.c2_original]
        elif np.isclose(x, 1):
            reactants = [self.c1_original]
        else:
            reactants = list(set([self.c1_original, self.c2_original]))

        return reactants

    def _get_reaction(self, x):
        """
        Generates balanced reaction at mixing ratio x : (1-x) for
        self.comp1 : self.comp2.

        Args:
            x (float): Mixing ratio x of reactants, a float between 0 and 1.

        Returns:
            Reaction object.
        """
        mix_comp = self.comp1 * x + self.comp2 * (1 - x)
        decomp = self.pd.get_decomposition(mix_comp)

        reactants = self._get_reactants(x)

        product = [Composition(k.name) for k, v in decomp.items()]
        reaction = Reaction(reactants, product)

        x_original = self._get_original_composition_ratio(reaction)

        if np.isclose(x_original, 1):
            reaction.normalize_to(self.c1_original, x_original)
        else:
            reaction.normalize_to(self.c2_original, 1 - x_original)

        return reaction

    def _get_elmt_amt_in_rxn(self, rxn):
        """
        Computes total number of atoms in a reaction formula for elements
        not in external reservoir. This method is used in the calculation
        of reaction energy per mol of reaction formula.

        Args:
            rxn (Reaction): a reaction.

        Returns:
            Total number of atoms for non_reservoir elements.
        """
        return sum([rxn.get_el_amount(e) for e in self.pd.elements])

    def _get_plotly_figure(self):
        kinks = list(map(list, zip(*self.get_kinks())))
        _, x, energy, reactions, _ = kinks

        lines = Scatter(
            x=x,
            y=energy,
            mode="lines",
            name="Lines",
            line=dict(color="navy", dash="solid", width=5.0),
            hoverinfo="none",
        )

        annotations = self._get_plotly_annotations(x, energy, reactions)

        min_idx = energy.index(min(energy))

        x_min = x.pop(min_idx)
        e_min = energy.pop(min_idx)
        rxn_min = reactions.pop(min_idx)

        labels = [
            rf"{htmlify(str(r))} <br>" + "\u0394" + f"E<sub>rxn</sub> =" f" {round(e, 3)} eV/atom"
            for r, e in zip(reactions, energy)
        ]

        markers = Scatter(
            x=x,
            y=energy,
            mode="markers",
            name="Reactions",
            hoverinfo="text",
            hovertext=labels,
            marker=dict(
                color="black",
                size=12,
                opacity=0.8,
                line=dict(color="black", width=3),
            ),
            hoverlabel=dict(bgcolor="navy"),
        )

        min_label = rf"{htmlify(str(rxn_min))} <br>" + "\u0394" + f"E<sub>rxn</sub> =" f" {round(e_min, 3)} eV/atom"

        minimum = Scatter(
            x=[x_min],
            y=[e_min],
            mode="markers",
            hoverinfo="text",
            hovertext=[min_label],
            marker=dict(color="darkred", size=24, symbol="star"),
            name="Suggested reaction",
        )

        data = [lines, markers, minimum]

        layout = plotly_layouts["default_interface_rxn_layout"]
        layout["xaxis"]["title"] = self._get_xaxis_title(latex=False)
        layout["annotations"] = annotations

        fig = Figure(data=data, layout=layout)
        return fig

    def _get_matplotlib_figure(self):
        plt = pretty_plot(8, 5)
        plt.xlim([-0.1, 1.1])

        kinks = list(zip(*self.get_kinks()))
        _, x, energy, reactions, _ = kinks

        plt.plot(x, energy, "o-", markersize=8, c="navy", zorder=1)
        plt.scatter(self.minimum[0], self.minimum[1], marker="*", c="red", s=400, zorder=2)

        for x_coord, y_coord, rxn in zip(x, energy, reactions):
            products = ", ".join([latexify(p.reduced_formula) for p in rxn.products])
            plt.annotate(
                products,
                xy=(x_coord, y_coord),
                xytext=(10, -30),
                textcoords="offset points",
                ha="right",
                va="bottom",
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
            )

        if self.norm:
            plt.ylabel("Energy (eV/atom)")
        else:
            plt.ylabel("Energy (eV/f.u.)")

        plt.xlabel(self._get_xaxis_title())
        plt.ylim(self.minimum[1] - 0.025)

        return plt.gcf()

    def _get_xaxis_title(self, latex=True):
        if latex:
            f1 = latexify(self.c1.reduced_formula)
            f2 = latexify(self.c2.reduced_formula)
            title = f"$x$ in $x${f1} + $(1-x)${f2}"
        else:
            f1 = htmlify(self.c1.reduced_formula)
            f2 = htmlify(self.c2.reduced_formula)
            title = f"<i>x</i> in <i>x</i>{f1} + (1-<i>x</i>){f2}"

        return title

    @staticmethod
    def _get_plotly_annotations(x, y, reactions):
        annotations = []
        for x_coord, y_coord, rxn in zip(x, y, reactions):
            products = ", ".join([htmlify(p.reduced_formula) for p in rxn.products])
            annotation = dict(x=x_coord, y=y_coord, text=products, font=dict(size=18), ax=-25, ay=55)
            annotations.append(annotation)
        return annotations

    @staticmethod
    def _get_entry_energy(pd: PhaseDiagram, composition: Composition):
        """
        Finds the lowest entry energy for entries matching the composition.
        Entries with non-negative formation energies are excluded. If no
        entry is found, use the convex hull energy for the composition.

        Args:
            pd: Phase diagram object
            composition: Composition object that the target entry should match

        Returns:
            The lowest entry energy among entries matching the composition.
        """
        candidate = [
            i.energy_per_atom
            for i in pd.qhull_entries
            if i.composition.fractional_composition == composition.fractional_composition
        ]

        if not candidate:
            warnings.warn(
                "The reactant " + composition.reduced_formula + " has no matching entry with negative formation"
                " energy, instead convex hull energy for this"
                " composition will be used for reaction energy "
                "calculation. "
            )
            return pd.get_hull_energy(composition)
        min_entry_energy = min(candidate)
        return min_entry_energy * composition.num_atoms

    @staticmethod
    def _convert(x, factor1, factor2):
        """
        Converts mixing ratio x in comp1 - comp2 tie line to that in
        c1 - c2 tie line.

        Args:
            x (float): Mixing ratio x in comp1 - comp2 tie line, a float
                between 0 and 1.
            factor1 (float): Compositional ratio between composition c1 and
                processed composition comp1. E.g., factor for
                Composition('SiO2') and Composition('O') is 2.0.
            factor2 (float): Compositional ratio between composition c2 and
                processed composition comp2.

        Returns:
            Mixing ratio in c1 - c2 tie line, a float between 0 and 1.
        """
        return x * factor2 / ((1 - x) * factor1 + x * factor2)

    @staticmethod
    def _reverse_convert(x, factor1, factor2):
        """
        Converts mixing ratio x in c1 - c2 tie line to that in
        comp1 - comp2 tie line.

        Args:
            x (float): Mixing ratio x in c1 - c2 tie line, a float between
                0 and 1.
            factor1 (float): Compositional ratio between composition c1 and
                processed composition comp1. E.g., factor for
                Composition('SiO2') and Composition('O') is 2.
            factor2 (float): Compositional ratio between composition c2 and
                processed composition comp2.

        Returns:
            Mixing ratio in comp1 - comp2 tie line, a float between 0 and 1.
        """
        return x * factor1 / ((1 - x) * factor2 + x * factor1)

    @staticmethod
    def get_chempot_correction(element, temp, pres):
        """
        Get the normalized correction term Δμ for chemical potential of a gas
        phase consisting of element at given temperature and pressure,
        referenced to that in the standard state (T_std = 298.15 K,
        T_std = 1 bar). The gas phase is limited to be one of O2, N2, Cl2,
        F2, H2. Calculation formula can be found in the documentation of
        Materials Project website.

        Args:
            element (string): The string representing the element.
            temp (float): The temperature of the gas phase.
            pres (float): The pressure of the gas phase.

        Returns:
            The correction of chemical potential in eV/atom of the gas
            phase at given temperature and pressure.
        """
        if element not in ["O", "N", "Cl", "F", "H"]:
            return 0
        std_temp = 298.15
        std_pres = 1e5
        ideal_gas_const = 8.3144598
        # Cp and S at standard state in J/(K.mol). Data from NIST-JANAF tables
        # Tables: O-029, N-O23, Cl-073, F-054, H-050

        Cp_dict = {"O": 29.376, "N": 29.124, "Cl": 33.949, "F": 31.302, "H": 28.836}

        S_dict = {"O": 205.147, "N": 191.609, "Cl": 223.079, "F": 202.789, "H": 130.680}
        Cp_std = Cp_dict[element]
        S_std = S_dict[element]
        PV_correction = ideal_gas_const * temp * np.log(pres / std_pres)
        TS_correction = (
            -Cp_std * (temp * np.log(temp) - std_temp * np.log(std_temp))
            + Cp_std * (temp - std_temp) * (1 + np.log(std_temp))
            - S_std * (temp - std_temp)
        )

        dG = PV_correction + TS_correction
        # Convert to eV/molecule unit.
        dG /= 1000 * InterfacialReactivity.EV_TO_KJ_PER_MOL
        # Normalize by number of atoms in the gas molecule. For elements
        # considered, the gas molecules are all diatomic.
        dG /= 2
        return dG

    @property
    def labels(self):
        """
        Returns a dictionary containing kink information:
        {index: 'x= mixing_ratio energy= reaction_energy reaction_equation'}.
        E.g., {1: 'x= 0.0 energy = 0.0 Mn -> Mn',
               2: 'x= 0.5 energy = -15.0 O2 + Mn -> MnO2',
               3: 'x= 1.0 energy = 0.0 O2 -> O2'}.
        """
        return {
            j: "x= " + str(round(x, 4)) + " energy in eV/atom = " + str(round(energy, 4)) + " " + str(reaction)
            for j, x, energy, reaction, _ in self.get_kinks()
        }

    @property
    def minimum(self):
        """
        Finds the minimum reaction energy E_min and corresponding
        mixing ratio x_min.

        Returns:
            Tuple (x_min, E_min).
        """
        return min([(x, energy) for _, x, energy, _, _ in self.get_kinks()], key=lambda i: i[1])

    @property
    def products(self):
        """
        List of formulas of potential products. E.g., ['Li','O2','Mn'].
        """
        products = set()
        for _, _, _, react, _ in self.get_kinks():
            products = products.union({k.reduced_formula for k in react.products})
        return list(products)

    @deprecated(products)
    def get_products(self):
        """

        Returns:

        """
        return self.products


class GrandPotentialInterfacialReactivity(InterfacialReactivity):
    """
    Extends upon InterfacialReactivity to allow for modelling possible reactions
    at the interface between two solids in the presence of an open element. The
    thermodynamics of the open system are provided by the user via the
    GrandPotentialPhaseDiagram class.
    """

    def __init__(
        self,
        c1: Composition,
        c2: Composition,
        grand_pd: GrandPotentialPhaseDiagram,
        pd_non_grand: PhaseDiagram,
        include_no_mixing_energy: bool = False,
        norm: bool = True,
        use_hull_energy: bool = True,
    ):
        """
        Args:
            c1: Reactant 1 composition
            c2: Reactant 2 composition
            grand_pd: Grand potential phase diagram object built from all elements in
                composition c1 and c2.
            pd:
            norm: Whether or not the total number of atoms in composition
                of reactant will be normalized to 1.
            include_no_mixing_energy: No_mixing_energy for a reactant is the
                opposite number of its energy above grand potential convex hull. In
                cases where reactions involve elements reservoir, this param
                determines whether no_mixing_energy of reactants will be included
                in the final reaction energy calculation. By definition, if pd is
                not a GrandPotentialPhaseDiagram object, this param is False.
            pd_non_grand: PhaseDiagram object but not
                GrandPotentialPhaseDiagram object built from elements in c1 and c2.
            use_hull_energy: Whether or not use the convex hull energy for
                a given composition for reaction energy calculation. If false,
                the energy of ground state structure will be used instead.
                Note that in case when ground state can not be found for a
                composition, convex hull energy will be used associated with a
                warning message.
        """
        # if include_no_mixing_energy is True, pd should be a
        # GrandPotentialPhaseDiagram object and pd_non_grand should be given.
        is_grand = isinstance(grand_pd, GrandPotentialPhaseDiagram)

        if include_no_mixing_energy and not is_grand:
            raise ValueError("Please provide grand phase diagram to compute" " no_mixing_energy!")
        if include_no_mixing_energy and not pd_non_grand:
            raise ValueError("Please provide non-grand phase diagram to " "compute no_mixing_energy!")
        if is_grand and use_hull_energy and not pd_non_grand:
            raise ValueError("Please provide non-grand phase diagram if" " you want to use convex hull energy.")

        super().__init__(c1=c1, c2=c2, pd=grand_pd, norm=norm,
                         use_hull_energy=use_hull_energy, bypass_grand_warning=True)

        self.pd_non_grand = pd_non_grand

        # Excludes element(s) from reservoir.
        self.comp1 = Composition({k: v for k, v in c1.items() if k not in grand_pd.chempots})
        self.comp2 = Composition({k: v for k, v in c2.items() if k not in grand_pd.chempots})
        # Calculate the factors in case where self.grand = True and
        # self.norm = True.

        factor1 = self.comp1.num_atoms / c1.num_atoms
        factor2 = self.comp2.num_atoms / c2.num_atoms

        if self.norm:
            self.factor1 = factor1
            self.factor2 = factor2

        if include_no_mixing_energy:
            # Computing grand potentials needs compositions containing
            # element(s) from reservoir, so self.c1 and self.c2 are used.
            self.e1 = self._get_grand_potential(self.c1)
            self.e2 = self._get_grand_potential(self.c2)
        else:
            self.e1 = self.pd.get_hull_energy(self.comp1)
            self.e2 = self.pd.get_hull_energy(self.comp2)

    def get_no_mixing_energy(self):
        """
        Generates the opposite number of energy above grand potential
        convex hull for both reactants.

        Returns:
            [(reactant1, no_mixing_energy1),(reactant2,no_mixing_energy2)].
        """

        energy1 = self.pd.get_hull_energy(self.comp1) - self._get_grand_potential(self.c1)
        energy2 = self.pd.get_hull_energy(self.comp2) - self._get_grand_potential(self.c2)

        unit = "eV/f.u."
        if self.norm:
            unit = "eV/atom"

        return [
            (self.c1_original.reduced_formula + " ({0})".format(unit), energy1),
            (self.c2_original.reduced_formula + " ({0})".format(unit), energy2),
        ]

    def _get_reactants(self, x):
        reactants = super()._get_reactants(x)
        reactants += [Composition(e.symbol) for e, v in self.pd.chempots.items()]

        return reactants

    def _get_grand_potential(self, composition):
        """
        Computes the grand potential Phi at a given composition and
        chemical potential(s).

        Args:
            composition (Composition): Composition object.

        Returns:
            Grand potential at a given composition at chemical potential(s).
        """
        if self.use_hull_energy:
            grand_potential = self.pd_non_grand.get_hull_energy(composition)
        else:
            grand_potential = InterfacialReactivity._get_entry_energy(self.pd_non_grand, composition)
        grand_potential -= sum([composition[e] * mu for e, mu in self.pd.chempots.items()])
        if self.norm:
            # Normalizes energy to the composition excluding element(s)
            # from reservoir.
            grand_potential /= sum([composition[el] for el in composition if el not in self.pd.chempots])
        return grand_potential
