from enum import Enum
from typing import TypeVar


# TODO: add type annotations
# BlockType = TypeVar('BlockType', bound=str)

class CellKeyword(Enum):
    """
    Enum defining valid keywords for CASTEP .cell files.
    """

    ATOMIC_INIT = "Dummy"
    BS_KPOINT_LIST = "Band structure k-point list"
    BS_KPOINT_MP_GRID = "Band structure Monkhorst-Pack grid"
    BS_KPOINT_MP_OFFSET = "Band structure Monkhorst-Pack grid offset"
    BS_KPOINT_MP_SPACING = "Band structure Monkurst-Pack grid density"
    BS_KPOINT_PATH = "Band structure path"
    BS_KPOINT_PATH_SPACING = "Band structure path spacing"
    BS_KPOINTS_LIST = "Alias for BS_KPOINT_LIST"
    BS_KPOINTS_MP_GRID = "Alias for BS_KPOINT_MP_GRID"
    BS_KPOINTS_MP_OFFSET = "Alias for BS_KPOINT_MP_OFFSET"
    BS_KPOINTS_MP_SPACING = "Alias for BS_KPOINT_MP_SPACING"
    BS_KPOINTS_PATH = "Alias for BS_KPOINT_PATH"
    BS_KPOINTS_PATH_SPACING = "Alias for BS_KPOINT_PATH_SPACING"
    CELL_CONSTRAINTS = "Constrains on unit cell parameters"
    CELL_DEVEL_CODE = "A devel_code for use in cell only"
    CELL_NOISE = "Noise added onto unit cell parameters"
    CHEMICAL_POTENTIAL = "The chemical potential of each species"
    ELNES_KPOINT_LIST = "k-point list for ELNES (core level spectroscopy) calculations"
    ELNES_KPOINT_MP_GRID = "The Monkhorst-Pack grid for ELNES (core level spectroscopy) k-points"
    ELNES_KPOINT_MP_OFFSET = "Origin offset of the ELNES (core level spectroscopy) MP grid"
    ELNES_KPOINT_MP_SPACING = "The spacing of points on the fine MP set for ELNES (core level spectroscop"
    EP_KPOINT_PAIRS = "A list of pairs of k-points from which phonons scatter from/to"
    EXTERNAL_BFIELD = "External applied magnetic field"
    EXTERNAL_EFIELD = "External applied electric field"
    EXTERNAL_PRESSURE = "External pressure"
    FIX_ALL_CELL = "Fix all lattice parameters"
    FIX_ALL_IONS = "Fix all ionic positions"
    FIX_COM = "Fix centre of mass"
    FIX_VOL = "Fix volume of cell"
    HUBBARD_ALPHA = "The Hubbard alpha for specific ion and orbital"
    HUBBARD_U = "The Hubbard U for each species and orbital"
    IONIC_CONSTRAINTS = "Constrains on ionic position"
    IONIC_VELOCITIES = "Initial ionic velocities"
    JCOUPLING_SITE = "The perturbing site for a magres J-coupling calculation"
    KPOINT_LIST = "Alias for KPOINTS_LIST"
    KPOINT_MP_GRID = "Alias for KPOINTS_MP_GRID"
    KPOINT_MP_OFFSET = "Alias for KPOINTS_MP_OFFSET"
    KPOINT_MP_SPACING = "Alias for KPOINTS_MP_SPACING"
    KPOINTS_LIST = "SCF k-points"
    KPOINTS_MP_GRID = "SCF Monkhorst-Pack grid"
    KPOINTS_MP_OFFSET = "SCF Monkhorst Pack grid offset"
    KPOINTS_MP_SPACING = "SCF Monkhorst-Pack grid density"
    LATTICE_ABC = "Lattice vectors - ABC"
    LATTICE_CART = "Lattice vectors - Cartesian"
    MAGRES_KPOINT_LIST = "k-point list for magnetic resonance calculations"
    MAGRES_KPOINT_MP_GRID = "The Monkhorst-Pack grid for magnetic resonance k-points"
    MAGRES_KPOINT_MP_OFFSET = "Origin offset of the magnetic resonance MP grid"
    MAGRES_KPOINT_MP_SPACING = "The spacing of points on the fine MP set for magnetic resonance calculatio"
    MAGRES_KPOINT_PATH = "Path of k-points at which magnetic resonance is calculated"
    MAGRES_KPOINT_PATH_SPACING = "The magnetic resonance k-point path spacing"
    NONLINEAR_CONSTRAINTS = "Constrains on bonds, angles and torsions"
    OPTICS_KPOINT_LIST = "Alias for OPTICS_KPOINTS_LIST"
    OPTICS_KPOINT_MP_GRID = "Alias for OPTICS_KPOINTS_MP_GRID"
    OPTICS_KPOINT_MP_OFFSET = "Alias for OPTICS_KPOINTS_MP_OFFSET"
    OPTICS_KPOINT_MP_SPACING = "Alias for OPTICS_KPOINTS_MP_SPACING"
    OPTICS_KPOINTS_LIST = "List of optics k-points"
    OPTICS_KPOINTS_MP_GRID = "Monkhorst-Pack grid for optics"
    OPTICS_KPOINTS_MP_OFFSET = "Optics Monkhorst-Pack grid offset"
    OPTICS_KPOINTS_MP_SPACING = "Optics Monhurst-Pack grid density of points"
    PHONON_FINE_KPOINT_LIST = "List of phonon wavevectors on the fine grid"
    PHONON_FINE_KPOINT_MP_GRID = "Fine MP-grid of phonon wavevectors"
    PHONON_FINE_KPOINT_MP_OFFSET = "Origin offset of the fine phonon MP grid"
    PHONON_FINE_KPOINT_MP_SPACING = "The spacing of points on the fine MP set for phonons"
    PHONON_FINE_KPOINT_PATH = "Path of phonon wavevectors on a fine scale"
    PHONON_FINE_KPOINT_PATH_SPACING = "The fine spacing of points on a path at which phonons are calculated"
    PHONON_GAMMA_DIRECTIONS = "Phonon gamma-point LO/TO splitting"
    PHONON_KPOINT_LIST = "List of phonon k-points"
    PHONON_KPOINT_MP_GRID = "Phonon wavevector Monkhorst-Pack grid"
    PHONON_KPOINT_MP_OFFSET = "Phonon wavevector Monkhorst Pack grid offset"
    PHONON_KPOINT_MP_SPACING = "Phonon wavevector Monkhorst-Pack grid density"
    PHONON_KPOINT_PATH = "Phonon dispersion k-point path"
    PHONON_KPOINT_PATH_SPACING = "Phonon dispersion path spacing"
    PHONON_KPOINTS_LIST = "Alias for PHONON_KPOINT_LIST"
    PHONON_KPOINTS_PATH = "Alias for PHONON_KPOINT_PATH"
    PHONON_KPOINTS_PATH_SPACING = "Alias for PHONON_KPOINT_PATH_SPACING"
    PHONON_SUPERCELL_MATRIX = "Supercell matrix for finite difference phonon calculations"
    POSITIONS_ABS = "Atomic positions"
    POSITIONS_ABS_INTERMEDIATE = "Transition state search intermediate state"
    POSITIONS_ABS_PRODUCT = "Transiation state search product"
    POSITIONS_FRAC = "Atomic positions"
    POSITIONS_FRAC_INTERMEDIATE = "Transition state search intermediate state"
    POSITIONS_FRAC_PRODUCT = "Transition state search product"
    POSITIONS_NOISE = "Noise added onto atomic positions"
    QUANTISATION_AXIS = "quantisation (magnetization) axis in fractional coordinates"
    QUANTIZATION_AXIS = "quantisation (magnetization) axis in fractional coordinates"
    SEDC_CUSTOM_PARAMS = "Customized parameters for semi-empirical dispersion correction schemes"
    SNAP_TO_SYMMETRY = "Force supplied lattice parameters and positions to obey given symmetries"
    SPECIES_GAMMA = "Gyromagnetic radius for each species"
    SPECIES_LCAO_STATES = "States for Linear combination of atomic orbitals"
    SPECIES_MASS = "Atomic mass"
    SPECIES_POT = "Specification of the pseudopotentials to be used"
    SPECIES_Q = "Electric quadrupole moment for each species"
    SPECTRAL_KPOINT_LIST = "Spectral properties k-point list"
    SPECTRAL_KPOINT_MP_GRID = "Spectral properties Monkhorst-Pack grid"
    SPECTRAL_KPOINT_MP_OFFSET = "Spectral properties Monkhorst-Pack grid offset"
    SPECTRAL_KPOINT_MP_SPACING = "Spectral properties Monkurst-Pack grid density"
    SPECTRAL_KPOINT_PATH = "Spectral properties k-point path"
    SPECTRAL_KPOINT_PATH_SPACING = "Spectral properties k-point path spacing"
    SPECTRAL_KPOINTS_LIST = "Alias for SPECTRAL_KPOINT_LIST"
    SPECTRAL_KPOINTS_MP_GRID = "Alias for SPECTRAL_KPOINT_MP_GRID"
    SPECTRAL_KPOINTS_MP_OFFSET = "Alias for SPECTRAL_KPOINT_MP_OFFSET"
    SPECTRAL_KPOINTS_MP_SPACING = "Alias for SPECTRAL_KPOINT_MP_SPACING"
    SPECTRAL_KPOINTS_PATH = "Alias for SPECTRAL_KPOINT_PATH"
    SPECTRAL_KPOINTS_PATH_SPACING = "Alias for SPECTRAL_KPOINT_PATH_SPACING"
    SUPERCELL_KPOINT_LIST = "Alias for SUPERCELL_KPOINTS_LIST"
    SUPERCELL_KPOINT_MP_GRID = "Alias for SUPERCELL_KPOINTS_MP_GRID"
    SUPERCELL_KPOINT_MP_OFFSET = "Alias for SUPERCELL_KPOINTS_MP_OFFSET"
    SUPERCELL_KPOINT_MP_SPACING = "Alias for SUPERCELL_KPOINTS_MP_SPACING"
    SUPERCELL_KPOINTS_LIST = "SCF k-points for FD phonon supercell"
    SUPERCELL_KPOINTS_MP_GRID = "SCF Monkhorst-Pack grid for FD phonon supercell calculation"
    SUPERCELL_KPOINTS_MP_OFFSET = "SCF Monkhorst Pack grid offset for a FD phonon supercell calculation"
    SUPERCELL_KPOINTS_MP_SPACING = "SCF Monkhorst-Pack grid density for FD phonon calculations"
    SUPERCELL_MATRIX = "Supercell matrix for creating supercell"
    SYMMETRY_GENERATE = "Generate crystal symmetry operations"
    SYMMETRY_OPS = "Crystal symmetry operations"
    SYMMETRY_TOL = "Symmetry Tolerance"
    UNIT_CELL = "Use one of the standard unit cells"


class ParamKeyword(Enum):
    """
    Enum defining valid keywords for CASTEP .param files.
    """

    BACKUP_INTERVAL = "seconds between backups"
    BASIS_DE_DLOGE = "d(Etot)/d(log(Ecut))"
    BASIS_PRECISION = "accuracy of basis set"
    BFIELD_UNIT = "unit of magnetic field in output"
    BORN_CHARGE_SUM_RULE = "enforce Born charge sum rule"
    BOUNDARY_TYPE = "boundary conditions in electrostatics"
    BS_EIGENVALUE_TOL = "band convergence tolerance"
    BS_MAX_CG_STEPS = "maximum CG steps in band structure calculation"
    BS_MAX_ITER = "maximum iterations in band structure calculation"
    BS_NBANDS = "number of bands/k-point in band structure calculation"
    BS_NEXTRA_BANDS = "number of extra bandstructure bands"
    BS_PERC_EXTRA_BANDS = "percentage of extra bandstructure bands"
    BS_RE_EST_K_SCRN = "re-estimate k-screening length before BS run"
    BS_WRITE_EIGENVALUES = "turn additional eigenvalue output on/off"
    BS_XC_DEFINITION = "BS exchange-correlation functional"
    BS_XC_FUNCTIONAL = "BS exchange-correlation functional"
    CALC_FULL_EX_POT = "OBSOLETE"
    CALC_MOLECULAR_DIPOLE = "electric dipole on/off"
    CALCULATE_BERRY_PHASE = "Polarisation analysis on/off"
    CALCULATE_BORN_CHARGES = "calculate Born effective charges"
    CALCULATE_DELTASCF = "calculate Molecular Orbital projected DOS?"
    CALCULATE_DENSDIFF = "calculate density difference based on atoms"
    CALCULATE_ELF = "ELF on/off"
    CALCULATE_HIRSHFELD = "Hirshfeld on/off"
    CALCULATE_MODOS = "calculate Molecular Orbital projected DOS?"
    CALCULATE_POLARISATION = "Polarisation analysis on/off"
    CALCULATE_POLARIZATION = "Polarisation analysis on/off"
    CALCULATE_RAMAN = "calculate Raman intensities"
    CALCULATE_STRESS = "stress on/off"
    CHARGE = "net charge"
    CHARGE_UNIT = "unit of charge in output"
    CHECKPOINT = "checkpoint filename"
    CML_FILENAME = "Withdrawn"
    CML_OUTPUT = "CML output on/off"
    COMMENT = "comment string"
    CONTINUATION = "continuation filename"
    CUT_OFF_ENERGY = "maximum energy of planewaves in basis set"
    DATA_DISTRIBUTION = "data distribution"
    DELTASCF_CHECKPOINT = "checkfile of precomputed subystem for excitation reference"
    DELTASCF_CONSTRAINTS = "list of states of constrained states"
    DELTASCF_DFTU_CHECKPOINT = "checkfile of precomputed subystem for DFT+U(MO) reference"
    DELTASCF_EXCITE = "enforce excitaion constraint on top of DFT+U(MO)?"
    DELTASCF_METHOD = "type of deltaSCF calculation"
    DELTASCF_MODE = "type of deltaSCF calculation"
    DELTASCF_NET_SPIN_1 = "enforce given spin in channel=1 for SIMPLE deltaSCF"
    DELTASCF_NET_SPIN_2 = "enforce given spin in channel=2 for SIMPLE deltaSCF"
    DELTASCF_OVERLAP_CUTOFF = "cutoff for LINEAR EXPANSION deltaSCF resonance to be ignored"
    DELTASCF_SMEARING = "occupation smearing for SIMPLE deltaSCF"
    DEVEL_CODE = "developers code"
    DIELEC_EMB_BULK_PERMITTIVITY = "bulk permittivity in electrostatics"
    DIELEC_EMB_CAVITY_TYPE = "type of cavity in electrostatics"
    DIELEC_EMB_FUNC_METHOD = "type of dielectric function in electrostatics"
    DIELEC_EMB_PARAM_SET = "set of parameters in electrostatics"
    DIPOLE_CORRECTION = "periodic dipole correction"
    DIPOLE_DIR = "periodic dipole direction"
    DIPOLE_UNIT = "unit of electric dipole in output"
    EFERMI_TOL = "Fermi-energy convergence tolerance"
    EFIELD_CALC_ION_PERMITTIVITY = "calculate zero-frequency permittivity"
    EFIELD_CALCULATE_NONLINEAR = "Calculate non-linear optical property"
    EFIELD_CHI2_UNIT = "unit of Efield chi2 in output"
    EFIELD_CONVERGENCE_WIN = "convergence tolerance window in EFIELD"
    EFIELD_DFPT_METHOD = "EFIELD DFPT solver method"
    EFIELD_ENERGY_TOL = "E(2) convergence tolerance in EFIELD"
    EFIELD_FREQ_SPACING = "Spacing of frequencies in permittivity calc"
    EFIELD_IGNORE_MOLEC_MODES = "Ignore lowest modes in permittivity calc"
    EFIELD_MAX_CG_STEPS = "max. number of cg steps in EFIELD"
    EFIELD_MAX_CYCLES = "maximum cycles in EFIELD"
    EFIELD_OSCILLATOR_Q = "Q-factor for line-shape broadening"
    EFIELD_UNIT = "unit of electric field in output"
    ELEC_CONVERGENCE_WIN = "convergence tolerance window"
    ELEC_DUMP_FILE = "wavefunction/density etc dump filename"
    ELEC_EIGENVALUE_TOL = "eigenvalue convergence tolerance"
    ELEC_ENERGY_TOL = "total energy per atom convergence tolerance"
    ELEC_FORCE_TOL = "max force per atom convergence tolerance"
    ELEC_METHOD = "treatment of metals or finite temperature insulator"
    ELEC_RESTORE_FILE = "wavefunction etc restore filename on reuse/continuation"
    ELEC_TEMP = "electron temperatures"
    ELECTRONIC_MINIMIZER = "electronic minimization method"
    ELNES_EIGENVALUE_TOL = "band convergence tolerance"
    ELNES_NBANDS = "number of bands in elnes calculation"
    ELNES_NEXTRA_BANDS = "number of extra elnes bands"
    ELNES_PERC_EXTRA_BANDS = "percentage of extra bandstructure bands"
    ELNES_XC_DEFINITION = "elnes exchange-correlation functional"
    ELNES_XC_FUNCTIONAL = "elnes exchange-correlation functional"
    ENERGY_UNIT = "unit of energy in output"
    ENTROPY_UNIT = "unit of entropy in output"
    EXCHANGE_REFLECT_KPTS = "OBSOLETE"
    EXCITED_STATE_SCISSORS = "scissors operator band-gap correction"
    FFT_MAX_PRIME_FACTOR = "largest prime factor in FFT"
    FINE_CUT_OFF_ENERGY = "maximum energy component of charge density"
    FINE_GMAX = "maximum |g| in fine grid"
    FINE_GRID_SCALE = "fine grid size"
    FINITE_BASIS_CORR = "finite basis set correction"
    FINITE_BASIS_NPOINTS = "Number of points used in automatic basis correction"
    FINITE_BASIS_SPACING = "finite cut-off energy spacing in automatic basis correction"
    FIX_OCCUPANCY = "treat system as an insulator"
    FIXED_NPW = "use fixed PW (T) or fixed Ecut (F)"
    FORCE_CONSTANT_UNIT = "unit of force constant in output"
    FORCE_UNIT = "unit of force in output"
    FREQUENCY_UNIT = "unit of frequency in output"
    GA_BULK_SLICE = "GA bulk or surface slice"
    GA_FIXED_N = "GA fixed number of atoms"
    GA_MAX_GENS = "GA max. number of generations"
    GA_MUTATE_AMP = "GA mutation amplitude"
    GA_MUTATE_RATE = "GA mutation rate (probability)"
    GA_POP_SIZE = "GA population size"
    GA_SPIN_MUTATE_AMP = "GA spin mutation amplitude"
    GA_SPIN_MUTATE_RATE = "GA spin mutation rate (probability)"
    GEOM_CONVERGENCE_WIN = "geometry optimization convergence tolerance window"
    GEOM_DISP_TOL = "geometry optimization displacement convergence tolerance"
    GEOM_ENERGY_TOL = "geometry optimization energy convergence tolerance"
    GEOM_FORCE_TOL = "geometry optimization force convergence tolerance"
    GEOM_FREQUENCY_EST = "estimated <frequency> at gamma point"
    GEOM_LBFGS_MAX_UPDATES = "max number of LBFGS updates stored"
    GEOM_LINMIN_TOL = "line minimizer tolerance"
    GEOM_MAX_ITER = "maximum number of geometry optimization iterations"
    GEOM_METHOD = "geometry optimization method"
    GEOM_MODULUS_EST = "estimated bulk modulus"
    GEOM_PRECON_EXP_A = "A value of EXP preconditioner"
    GEOM_PRECON_EXP_C_STAB = "stabilization constant of EXP preconditioner"
    GEOM_PRECON_EXP_MU = "mu value for EXP preconditioner"
    GEOM_PRECON_EXP_R_CUT = "cutoff distance for EXP preconditioner"
    GEOM_PRECON_EXP_R_NN = "nearest neighbor distance for EXP preconditioner"
    GEOM_PRECON_FF_C_STAB = "stabilization constant of FF preconditioner"
    GEOM_PRECON_FF_R_CUT = "cutoff distance for FF preconditioner"
    GEOM_PRECON_SCALE_CELL = "scaling cell on/off"
    GEOM_PRECONDITIONER = "type of preconditioner"
    GEOM_SPIN_FIX = "number of fixed spin geometry optimization iterations"
    GEOM_STRESS_TOL = "geometry optimization stress convergence tolerance"
    GEOM_TPSD_INIT_STEPSIZE = "initial 2-point SD stepsize"
    GEOM_TPSD_ITERCHANGE = "max number of TPSD updates before BFGS"
    GEOM_USE_LINMIN = "line minimiser on/off"
    GRID_SCALE = "standard grid size"
    IMPLICIT_SOLVENT_APOLAR_FACTOR = "scaling factor for apolar term in implicit solvent"
    IMPLICIT_SOLVENT_APOLAR_TERM = "apolar term in implicit solvent on/off"
    IMPLICIT_SOLVENT_RESCALE_APOLAR = "rescale apolar term in implicit solvent?"
    IMPLICIT_SOLVENT_SURFACE_TENSION = "surface tension in implicit solvent"
    IMPOSE_TRS = "OBSOLETE"
    INV_LENGTH_UNIT = "unit of inverse length in output"
    IPRINT = "verbosity control"
    IR_INTENSITY_UNIT = "unit of IR intensity in output"
    K_SCRN_AVERAGING_SCHEME = "OBSOLETE"
    K_SCRN_DEN_FUNCTION = "OBSOLETE"
    LENGTH_UNIT = "unit of length in output"
    MAGRES_CONV_TOL = "energy convergence tolerance in magres calc"
    MAGRES_CONVERGENCE_WIN = "convergence tolerance window in magres calc"
    MAGRES_JCOUPLING_TASK = "JCOUPLING run type"
    MAGRES_MAX_CG_STEPS = "max. number of cg steps in MAGRES"
    MAGRES_MAX_SC_CYCLES = "max. number of sc cycles in MAGRES"
    MAGRES_METHOD = "crystal or molecular position operator"
    MAGRES_TASK = "MAGRES run type"
    MAGRES_WRITE_RESPONSE = "Write current to file"
    MAGRES_XC_DEFINITION = "magres exchange-correlation functional"
    MAGRES_XC_FUNCTIONAL = "magres exchange-correlation functional"
    MASS_UNIT = "unit of mass in output"
    MAX_CG_STEPS = "max. number of conjugate gradient steps"
    MAX_DIIS_STEPS = "max. number of RMM/DIIS steps"
    MAX_SCF_CYCLES = "maximum SCF cycles"
    MAX_SD_STEPS = "max. number of steepest descent steps"
    MD_BAROSTAT = "MD barostat"
    MD_CELL_DAMP_RINGING = "Damp cell ringing mode"
    MD_CELL_T = "MD characteristic cell time"
    MD_DAMPING_RESET = "damped molecular dynamics reset frequency"
    MD_DAMPING_SCHEME = "damped MD scheme for geometry optimization"
    MD_DELTA_T = "MD timestep"
    MD_ELEC_CONVERGENCE_WIN = "MD convergence tolerance window"
    MD_ELEC_EIGENVALUE_TOL = "MD eigenvalue convergence tolerance"
    MD_ELEC_ENERGY_TOL = "MD total energy per atom convergence tolerance"
    MD_ELEC_FORCE_TOL = "max force per atom convergence tolerance"
    MD_ENSEMBLE = "MD ensemble"
    MD_EQM_CELL_T = "MD equilibration time for cell"
    MD_EQM_ION_T = "MD equilibration time for ions"
    MD_EQM_METHOD = "MD enhanced equilibration method"
    MD_EQM_T = "MD equilibration time"
    MD_EXTRAP = "MD wavefunction extrapolation scheme"
    MD_EXTRAP_FIT = "MD extrapolation parameters scheme"
    MD_HUG_COMPRESSION = "Hugoniostat compression ratio"
    MD_HUG_DIR = "Hugoniostat compression direction"
    MD_HUG_METHOD = "Hugoniostat method"
    MD_HUG_T = "Hugoniostat coupling constant"
    MD_ION_T = "MD characteristic ionic time"
    MD_LANGEVIN_T = "OBSOLETE"
    MD_NHC_LENGTH = "Nose-Hoover chain length"
    MD_NOSE_T = "OBSOLETE"
    MD_NUM_BEADS = "PIMD number of beads"
    MD_NUM_ITER = "number of MD steps"
    MD_OPT_DAMPED_DELTA_T = "optimal time step for damped MD"
    MD_PATHINT_INIT = "PIMD initialisation method"
    MD_PATHINT_NUM_STAGES = "PIMD number of stages"
    MD_PATHINT_STAGING = "PIMD staging modes on/off"
    MD_SAMPLE_ITER = "MD property sampling interval"
    MD_TEMPERATURE = "MD temperature"
    MD_THERMOSTAT = "MD thermostat"
    MD_USE_PATHINT = "PIMD on/off"
    MD_USE_PLUMED = "Use PLUMED metadynamics"
    MD_XLBOMD = "XL-BOMD on/off"
    MD_XLBOMD_HISTORY = "XL-BOMD history length"
    MESSAGE_SIZE = "max alltoallv message size"
    METALS_METHOD = "treatment of metals or finite temperature insulator"
    MG_FD_ORDER = "multi-grid finite difference order"
    MG_PADDING = "multi-grid padding"
    MIX_CHARGE_AMP = "charge density mixing amplitude"
    MIX_CHARGE_GMAX = "maximum G-vector in charge mixing scheme"
    MIX_CUT_OFF_ENERGY = "density mixing cut off energy"
    MIX_HISTORY_LENGTH = "number of densities in mixing scheme"
    MIX_KED_CHARGE_AMP = "KED charge mixing amplitude"
    MIX_KED_CHARGE_GMAX = "maximum G-vector in KED charge mixing scheme"
    MIX_KED_SPIN_AMP = "KED spin mixing amplitude"
    MIX_KED_SPIN_GMAX = "maximum G-vector in KED spin mixing scheme"
    MIX_METRIC_Q = "density mixing metric coefficient"
    MIX_SPIN_AMP = "spin density mixing amplitude"
    MIX_SPIN_GMAX = "maximum G-vector in spin mixing scheme"
    MIXING_SCHEME = "density mixing scheme"
    MODOS_CHECKPOINT = "checkfile of precomputed subystem for MODOS"
    MODOS_STATES = "list of states for MODOS"
    NBANDS = "number of bands"
    NDOWN = "number of down spins"
    NELECTRONS = "number of electrons"
    NEXTRA_BANDS = "number of extra bands"
    NLXC_CALC_FULL_EX_POT = "calculate full exchange potential matrix"
    NLXC_DIV_CORR_NPTS_STEP = "step in npts for testing convergence"
    NLXC_DIV_CORR_ON = "OBSOLETE"
    NLXC_DIV_CORR_S_WIDTH = "width of envelope function"
    NLXC_DIV_CORR_TOL = "convergence tolerance"
    NLXC_EXCHANGE_FRACTION = "OBSOLETE"
    NLXC_EXCHANGE_REFLECT_KPTS = "assume time reversal symmetry when calculating Vxc"
    NLXC_EXCHANGE_SCREENING = "OBSOLETE"
    NLXC_IMPOSE_TRS = "impose time reversal symmetry"
    NLXC_K_SCRN_AVERAGING_SCHEME = "averaging scheme for k-screening length"
    NLXC_K_SCRN_DEN_FUNCTION = "OBSOLETE"
    NLXC_PAGE_EX_POT = "page exchange potentials to disk"
    NLXC_PPD_INTEGRAL = "OBSOLETE"
    NLXC_PPD_SIZE_X = "x-size of parallelepiped"
    NLXC_PPD_SIZE_Y = "y-size of parallelepiped"
    NLXC_PPD_SIZE_Z = "z-size of parallelepiped"
    NLXC_RE_EST_K_SCRN = "update k-screening length?"
    NSPINS = "number of spin channels"
    NUM_BACKUP_ITER = "md/geom iterations between backups"
    NUM_DUMP_CYCLES = "frequency of wavefunction dumps"
    NUM_FARMS = "number of task farms"
    NUM_OCC_CYCLES = "number of occupancy minimization cycles"
    NUM_PROC_IN_SMP = "number of processors in SMP node"
    NUM_PROC_IN_SMP_FINE = "number of processors in SMP node"
    NUP = "number of up spins"
    OPT_STRATEGY = "optimization strategy"
    OPT_STRATEGY_BIAS = "optimization strategy bias"
    OPTICS_NBANDS = "number of bands in optics calculation"
    OPTICS_NEXTRA_BANDS = "number of extra optics bands"
    OPTICS_PERC_EXTRA_BANDS = "percentage of extra bandstructure bands"
    OPTICS_XC_DEFINITION = "optics exchange-correlation functional"
    OPTICS_XC_FUNCTIONAL = "optics exchange-correlation functional"
    PAGE_EX_POT = "OBSOLETE"
    PAGE_WVFNS = "page wavefunctions to disk"
    PDOS_CALCULATE_WEIGHTS = "partial DOS analysis on/off"
    PERC_EXTRA_BANDS = "percentage of extra bands"
    PHONON_CALC_LO_TO_SPLITTING = "gamma-point phonon LO/TO correction"
    PHONON_CALCULATE_DOS = "density of states calculation"
    PHONON_CONST_BASIS = "Withdrawn"
    PHONON_CONVERGENCE_WIN = "convergence tolerance window in LR"
    PHONON_DFPT_METHOD = "phonon DFPT solver method"
    PHONON_DOS_LIMIT = "density of states upper limit"
    PHONON_DOS_SPACING = "density of states resolution"
    PHONON_ENERGY_TOL = "E(2) convergence tolerance in LR"
    PHONON_FINE_CUTOFF_METHOD = "non-periodic force extraction"
    PHONON_FINE_METHOD = "fine phonon calculation method"
    PHONON_FINITE_DISP = "finite displacement amplitude"
    PHONON_FORCE_CONSTANT_CUT_SCALE = "scale factor for CUMULANT PHONON_FINE_CUTOFF_METHOD"
    PHONON_FORCE_CONSTANT_CUTOFF = "Cutoff for force constant matrix"
    PHONON_FORCE_CONSTANT_ELLIPSOID = "alias for PHONON_FORCE_CONSTANT_CUT_SCALE"
    PHONON_MAX_CG_STEPS = "max. number of cg steps in LR"
    PHONON_MAX_CYCLES = "maximum cycles in LR"
    PHONON_METHOD = "phonon calculation method"
    PHONON_PRECONDITIONER = "scheme to use in LR"
    PHONON_SUM_RULE = "enforce phonon sum rule - DEPRECATED"
    PHONON_SUM_RULE_METHOD = "select method to enforce phonon sum rule"
    PHONON_USE_KPOINT_SYMMETRY = "reduced or full kpoint set in LR"
    PHONON_WRITE_DYNAMICAL = "Write out reciprocal space dynamical matrix"
    PHONON_WRITE_FORCE_CONSTANTS = "Write out real-space force constant matrix"
    POPN_BOND_CUTOFF = "population analysis bond cutoff"
    POPN_CALCULATE = "population analysis on/off"
    POPN_WRITE = "population analysis output"
    PPD_INTEGRAL = "OBSOLETE"
    PPD_SIZE_X = "OBSOLETE"
    PPD_SIZE_Y = "OBSOLETE"
    PPD_SIZE_Z = "OBSOLETE"
    PRESSURE_UNIT = "unit of pressure in output"
    PRINT_CLOCK = "clock on/off"
    PRINT_MEMORY_USAGE = "memory on/off"
    PSPOT_BETA_PHI_TYPE = "<beta|phi> representation"
    PSPOT_NONLOCAL_TYPE = "pseudopotential representation"
    RAMAN_METHOD = "Raman tensor calculation method"
    RAMAN_RANGE_HIGH = "stop frequency for Raman"
    RAMAN_RANGE_LOW = "start frequency for Raman"
    RAND_SEED = "seed for random numbers"
    RE_EST_K_SCRN = "OBSOLETE"
    RELATIVISTIC_TREATMENT = "level of relativity theory"
    REUSE = "reuse filename"
    RUN_TIME = "maximum duration of job"
    SECONDD_METHOD = "OBSOLETE"
    SEDC_A1_XDM = "A1 value for XDM semi-empirical dispersion correction scheme"
    SEDC_A2_XDM = "A2 value for XDM semi-empirical dispersion correction scheme"
    SEDC_APPLY = "turn on/off semi-empirical dispersion correction scheme"
    SEDC_C9_XDM = "Whether three-body dispersion coefficients are computed with XDM"
    SEDC_D_G06 = "d value for G06 semi-empirical dispersion correction scheme"
    SEDC_D_JCHS = "d value for JCHS semi-empirical dispersion correction scheme"
    SEDC_D_TS = "d value for TS semi-empirical dispersion correction scheme"
    SEDC_LAMBDA_OBS = "lambda value for OBS semi-empirical dispersion scheme"
    SEDC_N_OBS = "n value for OBS semi-empirical dispersion correction scheme"
    SEDC_S6_G06 = "S6 value for G06 semi-empirical dispersion correction scheme"
    SEDC_S6_JCHS = "S6 value for JCHS semi-empirical dispersion correction scheme"
    SEDC_SC_XDM = "SC value for XDM semi-empirical dispersion correction scheme"
    SEDC_SCHEME = "semi-empirical dispersion correction scheme"
    SEDC_SR_JCHS = "SR value for JCHS semi-empirical dispersion correction scheme"
    SEDC_SR_TS = "SR value for TS semi-empirical dispersion correction scheme"
    SMEARING_SCHEME = "metal smearing scheme"
    SMEARING_WIDTH = "width of metal smearing"
    SPECTRAL_EIGENVALUE_TOL = "spectral convergence tolerance"
    SPECTRAL_MAX_ITER = "maximum iterations in band structure calculation"
    SPECTRAL_MAX_STEPS_PER_ITER = "maximum steps per iter in spectral calculation"
    SPECTRAL_NBANDS = "number of bands/k-point in spectral calculation"
    SPECTRAL_NEXTRA_BANDS = "number of extra spectral bands"
    SPECTRAL_PERC_EXTRA_BANDS = "percentage of extra spectral bands"
    SPECTRAL_RE_EST_K_SCRN = "re-estimate k-screening length before spectral run"
    SPECTRAL_TASK = "type of spectrum to calculate"
    SPECTRAL_THEORY = "theory level in spectral calc"
    SPECTRAL_WRITE_EIGENVALUES = "turn additional eigenvalue output on/off"
    SPECTRAL_XC_DEFINITION = "spectral exchange-correlation functional"
    SPECTRAL_XC_FUNCTIONAL = "spectral exchange-correlation functional"
    SPIN = "net spin"
    SPIN_FIX = "max number of fixed spin SCF cycles"
    SPIN_ORBIT_COUPLING = "use spin-orbit coupling (T) or not (F)"
    SPIN_POLARISED = "spin polarised"
    SPIN_POLARIZED = "spin polarized"
    SPIN_TREATMENT = "electronic spin treatment"
    SPIN_UNIT = "unit of spin in output"
    STOP = "abort run"
    TASK = "type of calculation"
    TDDFT_APPROXIMATION = "select Tamm-Dancoff approximation in TDDFT"
    TDDFT_CONVERGENCE_WIN = "convergence tolerance window in TDDFT calc"
    TDDFT_EIGENVALUE_METHOD = "TDDFT matrix solution method"
    TDDFT_EIGENVALUE_TOL = "state convergence tolerance"
    TDDFT_MAX_ITER = "maximum number of iterations in TDDFT calculation"
    TDDFT_METHOD = "Method used to approach TDDFT"
    TDDFT_NEXTRA_STATES = "number of extra TDDFT states"
    TDDFT_NUM_STATES = "number of TDDFT states"
    TDDFT_POSITION_METHOD = "select position operator method in TDDFT"
    TDDFT_SELECTED_STATE = "TDDFT state to use in geometry/MD"
    TDDFT_XC_DEFINITION = "tddft exchange-correlation functional"
    TDDFT_XC_FUNCTIONAL = "TDDFT exchange correlation kernel"
    THERMO_CALCULATE_HELMHOLTZ = "Calculate Helmholtz free energy"
    THERMO_T_NPOINTS = "Number of points in temperature interval"
    THERMO_T_SPACING = "Temperature spacing"
    THERMO_T_START = "Starting temperature"
    THERMO_T_STOP = "Final temperature"
    TIME_UNIT = "unit of time in output"
    TSSEARCH_CG_MAX_ITER = "max CG steps in QST search"
    TSSEARCH_DISP_TOL = "displacement convergence tolerance in QST search"
    TSSEARCH_ENERGY_TOL = "energy convergence tolerance in NEB search"
    TSSEARCH_FORCE_TOL = "force convergence tolerance in QST search"
    TSSEARCH_LSTQST_PROTOCOL = "LST/QST search protocol"
    TSSEARCH_MAX_PATH_POINTS = "max number of path points in NEB  search"
    TSSEARCH_METHOD = "TS search method"
    TSSEARCH_QST_MAX_ITER = "max iters in QST search"
    USE_SMEARED_IONS = "Use smeared ions in electrostatics"
    VELOCITY_UNIT = "unit of velocity in output"
    VERBOSITY = "verbosity control"
    VOLUME_UNIT = "unit of volume in output"
    WANNIER_ION_CMOMENTS = "Compute ion multipole moments from Wannier functions"
    WANNIER_ION_CUT = "Compute ion multipole moments from truncated integration"
    WANNIER_ION_CUT_FRACTION = "Ion density fraction for truncated integration"
    WANNIER_ION_CUT_TOL = "Tolerance in wannier_ion_cut_fraction"
    WANNIER_ION_MOMENTS = "Compute ion multipole moments from Wannier functions"
    WANNIER_ION_RMAX = "Ion radius for Wannier function assignment"
    WANNIER_MAX_SD_STEPS = "max. number of sd steps in WANNIER"
    WANNIER_MIN_ALGOR = "Spread minimisation algorithm"
    WANNIER_PRINT_CUBE = "Number of Wannier function to print out"
    WANNIER_RESTART = "Options for restart"
    WANNIER_SD_STEP = "Wannier steepest descent step length"
    WANNIER_SPREAD_TOL = "Wannier convergence tolerance in LAMBDA"
    WANNIER_SPREAD_TYPE = "Spread functional definition"
    WRITE_BANDS = "output bands file"
    WRITE_BIB = "output BibTeX references"
    WRITE_CELL_STRUCTURE = "output final structure in CELL format"
    WRITE_CHECKPOINT = "control output checkpoint file"
    WRITE_CIF_STRUCTURE = "output final structure in CIF format"
    WRITE_CST_ESP = "output cst_esp file"
    WRITE_FORMATTED_DENSITY = "formatted density on/off"
    WRITE_FORMATTED_DIELEC_PERM = "formatted dielectric function on/off"
    WRITE_FORMATTED_ELF = "formatted ELF on/off"
    WRITE_FORMATTED_POTENTIAL = "formatted potential on/off"
    WRITE_GEOM = "output geom file"
    WRITE_MD = "output MD file"
    WRITE_NONE = "write extra files on/off"
    WRITE_ORBITALS = "unformatted orbitals file on/off"
    WRITE_OTFG = "output OTFG files"
    XC_DEFINITION = "exchange-correlation functional"
    XC_FUNCTIONAL = "exchange-correlation functional"
    XC_VXC_DERIV_EPSILON = "OBSOLETE"


class OTFPseudopotentialLibrary(Enum):
    """
    An Enum specifying allowed values for the built-in pseudopotential
    libraries in CASTEP, defined by the SPECIES_POT block.
    """

    UNKNOWN = 0
    QC5 = 1  # QC5 pseudopotentials (delta=1.7 meV, 0.8 meV excluding N, O, Cr, Mn)
    HARD = 2  # "Ultimate" set of HARD pseudopotentials
    MS = 3  # Default settings from Materials Studio
    C7 = 7  # OTFG definitions as of CASTEP 7.0
    C8 = 8  # OTFG definitions as of CASTEP 8.0
    C9 = 9  # OTFG definitions as of CASTEP 9.0/16.0 (delta=0.5 meV)
    NCP9 = 10  # Norm-conserving pseudopotentials as of CASTEP 9.0/16.0 (delta=1.1 meV)
    C17 = 11  # OTFG definitions as of CASTEP 17.0
    NCP17 = 12  # Recommended set of norm-conserving pseudopotentials as of CASTEP 17.0
    C18 = 13  # OTFG definitions as of CASTEP 18.0
    NCP18 = 14  # Recommended set of norm-conserving pseudopotentials as of CASTEP 18.0
    C19 = 15  # OTFG definitions as of CASTEP 19.0 (delta=0.442 meV)
    NCP19 = 16  # Recommended set of norm-conserving pseudopotentials as of CASTEP 19.0 (delta=1.098 meV)
    SOC19 = 17
