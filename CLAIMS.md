# Claims and computational coverage

Locations refer to the 30-page JFAA submission after the four pre-arXiv edits.
Equation numbers are read from that source, not older drafts. Figure numbering
follows the paper: Figure 3 is the collision window and Figure 4 is the repair
fraction. Every `Cxx` script prints the claimed/computed values and tolerance,
and exits nonzero on failure. `CLAIMS_REPORT.md` records each subcheck.

“Exact identity” describes the mathematical statement, not a claim that a
floating-point test proves it. “PASS” is limited to the specified test cases.
Exact symbolic and rational checks are identified separately. No historical
private data or external manuscript checkout is needed at runtime.

| Paper location (number, page) | Statement in words | Type | Method | Script | Status |
|---|---|---|---|---|---|
| Prop. 1; (4)-(5), p.4 | Node and weight variations equal centered finite differences of G | exact identity | floating point; centered step 2e-6, tolerance 2e-8 | [checks/C01_first_variation.py](checks/C01_first_variation.py) | PASS for listed cases |
| §2.3; (10), pp.5-6 | Weighted metric normalization of Q_red; q = epsilon^T Q_red epsilon / S | exact identity | independent dense projection and block sum; tolerance 1e-10 + 1e-11 relative | [checks/C02_fourier_blocks.py](checks/C02_fourier_blocks.py) | PASS for listed cases |
| Thm. 5; (16)-(18), pp.8-9 | F Q_red F^-1 is the direct sum of C_r for Figure 1 and seeded 1D/2D configurations | exact identity | real constrained least squares versus complex character conjugation | [checks/C02_fourier_blocks.py](checks/C02_fourier_blocks.py) | PASS for listed cases |
| Fig. 1; (14),(16), p.9 | Class (3,0): representatives (3,0),(-2,0), multiplicities 3,6 and mass 9 | numerical value | exact integer arithmetic | [checks/C03_alias_geometry.py](checks/C03_alias_geometry.py) | PASS for listed cases |
| Fig. 1, p.9 | Class center (-1/3,0), covariance diag(50,0), alias gap (5,0) | numerical value | exact rational arithmetic | [checks/C03_alias_geometry.py](checks/C03_alias_geometry.py) | PASS for listed cases |
| Fig. 1(b), p.9 | Unit polarization has defect 50 cos^2(theta) | exact identity | floating point over 361 angles; tolerance 2e-14 | [checks/C03_alias_geometry.py](checks/C03_alias_geometry.py) | PASS for listed cases |
| Remark 9, pp.12-13 | 35 differences meet all 25 classes, with at most two representatives per class | numerical value | integer enumeration and augmented affine ranks | [checks/C04_manifold_example.py](checks/C04_manifold_example.py) | PASS for listed cases |
| Remark 9; Thm. 8, pp.12-13 | Dense reduced rank 10, kernel dimension 40, unique weight (Y rank 24) | numerical value | dense SVD rank threshold 1e-9; does not prove local manifold existence | [checks/C04_manifold_example.py](checks/C04_manifold_example.py) | PASS for listed cases |
| Thm. 7, pp.10-11 | Difference-set injectivity is equivalent to zero reduced form on four examples | exact identity | integer classes versus dense projection; zero threshold 1e-9 | [checks/C05_exact_persistence.py](checks/C05_exact_persistence.py) | PASS for listed cases |
| (22), pp.10-11 | Right-inverse weights are normalized, positive and restore G=I in small perturbed injective examples | exact identity | floating point; residual <=3e-14, perturbation scale 1e-3 | [checks/C05_exact_persistence.py](checks/C05_exact_persistence.py) | PASS for listed cases |
| (40)-(48); Thm. 13, pp.18-19 | Deficit law equals dense Q_red for m=4,8,16 and every m<=s<=2m-1 | exact identity | full Fourier conjugation; maximum absolute tolerance 3e-10 | [checks/C06_deficit_law.py](checks/C06_deficit_law.py) | PASS for listed cases |
| Fig. 3(a); (43), p.19 | m=8,s=10: centers 4/3,2/3,0,-2/3,-4/3 and collided pairs (3,-7) through (7,-3) | numerical value | rational class data and figure assertions | [checks/C06_deficit_law.py](checks/C06_deficit_law.py) | PASS for listed cases |
| Fig. 3(b); (48), p.19 | Covariances 250/3,400/3,150,400/3,250/3 | numerical value | dense operator comparison plus rational class construction | [checks/C06_deficit_law.py](checks/C06_deficit_law.py) | PASS for listed cases |
| Cor. 14; (49), p.20 | Kernel dimension 2(s-m)+1, with protected signed band abs(n)<=s-m | exact identity | integer enumeration for m=4,8,16, all admissible s, including Nyquist cases | [checks/C07_protected_band.py](checks/C07_protected_band.py) | PASS for listed cases |
| Cor. 16; (53), p.21 | E q = sigma^2 s(delta^2-1)/6 | exact identity | SymPy summation symbolic in delta,s; unit variance Monte Carlo | [checks/C08_iid_jitter.py](checks/C08_iid_jitter.py) | PASS for listed cases |
| Cor. 16; (53), p.21 | E fixed energy = sigma^2 m^2(m^2-1)/(6s) | exact identity | SymPy summation symbolic in m,s; unit variance Monte Carlo | [checks/C08_iid_jitter.py](checks/C08_iid_jitter.py) | PASS for listed cases |
| (54), p.21 | Expected-energy ratio s^2(delta^2-1)/(m^2(m^2-1)) | exact identity | SymPy exact simplification; ratios of expectations, not mean sample ratios | [checks/C08_iid_jitter.py](checks/C08_iid_jitter.py) | PASS for listed cases |
| (55), p.21 | Proportional limit rho -> kappa^2(2-kappa)^2 | exact identity | SymPy symbolic limit | [checks/C08_iid_jitter.py](checks/C08_iid_jitter.py) | PASS for listed cases |
| Cor. 16 endpoint; Fig. 4, pp.21-22 | s=2m-1 has delta=1, no collisions, E q=0 and complete first-order repair | numerical value | empty sum and exact rational formulas; included in C06,C07 and figure checks | [checks/C08_iid_jitter.py](checks/C08_iid_jitter.py) | PASS for listed cases |
| Cor. 16, p.21 | Mean energies for m=16 at s=16,24,31 | numerical value | 60000 seeded Gaussian draws per grid; six estimated standard errors; ratio tolerance .015 | [checks/C08_iid_jitter.py](checks/C08_iid_jitter.py) | PASS for listed cases |
| (56)-(57), p.22 | Voronoi finite differences have symbol -i s sin(2pi r/s)/(2pi) | exact identity | finite differences at step 1e-6; tolerance 2e-9 | [checks/C09_voronoi.py](checks/C09_voronoi.py) | PASS for listed cases |
| (58), p.22 | Prescribed Voronoi excess is N_r abs(a_r-p_bar_r)^2 | exact identity | raw representative sum versus centered covariance; tolerance 1e-10 + 1e-12 relative | [checks/C09_voronoi.py](checks/C09_voronoi.py) | PASS for listed cases |
| (59), p.22 | Closed collided-class Voronoi excess | exact identity | independent representative sum and closed deficit formula | [checks/C09_voronoi.py](checks/C09_voronoi.py) | PASS for listed cases |
| Fig. 4, p.22 | Entire m=16 Voronoi curve agrees with dense expected energies | numerical value | all s=16..31, dense trace versus class sum | [checks/C09_voronoi.py](checks/C09_voronoi.py) | PASS for listed cases |
| §6.5, pp.22-23 | Critical Voronoi repair fraction is negative; zero symbol only at rigid and even-grid Nyquist modes | numerical value | explicit symbol and dense energy checks | [checks/C09_voronoi.py](checks/C09_voronoi.py) | PASS for listed cases |
| §6.5, p.23 | Low-mode Voronoi symbol agrees to first order | exact identity | SymPy sine Taylor series | [checks/C09_voronoi.py](checks/C09_voronoi.py) | PASS for listed cases |
| Prop. 17; (60)-(63), pp.23-24 | Exact square rules have P_Y X=0 | exact identity | seeded translated/permuted 1D exact rules and an exactly sheared 4x4 tensor DFT | [checks/C10_square_orthogonality.py](checks/C10_square_orthogonality.py) | PASS for listed cases |
| Prop. 19; (66)-(67), pp.24-25 | Node-space and spectral square-DFT energies agree | exact identity | independent pair sum versus Fourier transform for every s=2..64 | [checks/C11_square_energy.py](checks/C11_square_energy.py) | PASS for listed cases |
| Prop. 19 proof, p.24 | Fejer sum equals r(s-r) | exact identity | exact SymPy algebraic-number reduction for s=2..8; floating point for all s<=64 | [checks/C11_square_energy.py](checks/C11_square_energy.py) | PASS for listed cases |
| (68)-(69), pp.24-25 | H^(1/2) limit for cos(x)+0.4 sin(3x), with its exact finite-s correction | exact identity | floating point at s=16,32,64,128,256; target .74, finite correction 1.22/s | [checks/C11_square_energy.py](checks/C11_square_energy.py) | PASS for listed cases |
| §7.2, p.25 | Circular log-Vandermonde Hessian equals reduced energy and has spectrum r(s-r) | exact identity | independent analytic pair Hessian at s=6 versus dense Q_red/S | [checks/C11_square_energy.py](checks/C11_square_energy.py) | PASS for listed cases |
| Props. 11-12; (32),(37), pp.14-17 | Mixed shears are q-null and minimized second-order residual factors as E_s1(g) E_s2(f) | exact identity | direct least squares over all real xi and zero-sum omega for seeded 4x4 and 3x5 examples | [checks/C12_second_order.py](checks/C12_second_order.py) | PASS for listed cases |
| (38); Fig. 2(a), pp.16-17 | Cosine-family optimal coefficient is 36 alpha^2 beta^2, with E_4(cos)=6 | numerical value | direct second-order minimization and independent 1D spectral energies | [checks/C12_second_order.py](checks/C12_second_order.py) | PASS for listed cases |
| Fig. 2(b), p.17 | Straight mixed paths approach levels 6,3,1.5; pure shears remain exact | numerical value | direct finite-t Gram matrices; mixed-limit tolerance 1e-5, pure residual <1e-13 | [checks/C12_second_order.py](checks/C12_second_order.py) | PASS for listed cases |
| Thm. 20; (74), p.26 | Tensor class mass factors across coordinates | exact identity | integer class enumeration on m=(3,2,2), s=(4,4,3) | [checks/C13_tensor_box.py](checks/C13_tensor_box.py) | PASS for listed cases |
| Thm. 20; (75)-(76), p.26 | Tensor center and diagonal covariance factor coordinatewise, including empty classes | exact identity | direct multi-dimensional differences versus per-coordinate statistics | [checks/C13_tensor_box.py](checks/C13_tensor_box.py) | PASS for listed cases |
| Thm. 20; (77)-(78), p.26 | 3D factored blocks give the dense reduced operator and its zero coordinates | exact identity | dense real projection versus full character conjugation | [checks/C13_tensor_box.py](checks/C13_tensor_box.py) | PASS for listed cases |
| §8.2; (79)-(80), p.27 | Rank-1 example: M=17, 23 distinct-node characters, 69 differences | numerical value | integer enumeration; exact Gram residual check | [checks/C14_rank1_lattice.py](checks/C14_rank1_lattice.py) | PASS for listed cases |
| §8.2, p.27 | Covariance rank histogram (1,2,20) for ranks (0,1,2) | numerical value | matrix ranks with explicit threshold 1e-9 | [checks/C14_rank1_lattice.py](checks/C14_rank1_lattice.py) | PASS for listed cases |
| (81)-(82), p.27 | Class r=2 has four specified representatives, multiplicities 4,2,2,7, center (0,2/5) and affine rank 3 | numerical value | integer enumeration and weighted class statistics | [checks/C14_rank1_lattice.py](checks/C14_rank1_lattice.py) | PASS for listed cases |
| §8.2, p.27 | Dense reduced defect agrees with block formula to relative error below 1e-14 | numerical value | five seeded tangents, direct real constrained least squares | [checks/C14_rank1_lattice.py](checks/C14_rank1_lattice.py) | PASS for listed cases |
| §8.3; (83), p.28 | Characteristic polynomial (lambda^2-lambda-1)(lambda^2+lambda-1) and eigenvalues ±(1±sqrt(5))/2 | exact identity | SymPy exact complex DFT matrix and characteristic polynomial; numerical eigenspectrum | [checks/C15_spectral_objective.py](checks/C15_spectral_objective.py) | PASS for listed cases |
| (84), p.28 | Alternative tangent satisfies (H+Y zeta)^2=2I | exact identity | SymPy exact arithmetic | [checks/C15_spectral_objective.py](checks/C15_spectral_objective.py) | PASS for listed cases |
| §8.3, p.28 | Squared Frobenius norms 6 and 8; spectral half-spreads golden ratio and sqrt(2) | numerical value | exact traces and numerical Hermitian eigenvalues | [checks/C15_spectral_objective.py](checks/C15_spectral_objective.py) | PASS for listed cases |
| Prop. 15; (50), pp.20-21 | Positive-exponent stationary spectral covariance equals S^-1 sum_h K(h) exp(ir.h) | exact identity | finite covariance propagation for a seeded vector moving-average field | [checks/C16_stationary_jitter.py](checks/C16_stationary_jitter.py) | PASS for listed cases |
| (51), p.20 | D_r=C_r+N_r p_bar_r p_bar_r^T | exact identity | independent uncentered and centered class moments | [checks/C16_stationary_jitter.py](checks/C16_stationary_jitter.py) | PASS for listed cases |
| Prop. 15, p.21 | Stationary expected reduced and fixed energies are spectral traces; 0<=rho_stat<=1 | exact identity | dense covariance trace versus spectral sum | [checks/C16_stationary_jitter.py](checks/C16_stationary_jitter.py) | PASS for listed cases |
| §6.4, p.21 | Stationary jitter in a protected band has zero reduced energy | exact identity | sampled trigonometric covariance supported on the protected band | [checks/C16_stationary_jitter.py](checks/C16_stationary_jitter.py) | PASS for listed cases |
| Prop. 2, pp.5-6 | Fixed-node optimum has the stated first-order weight derivative and t^2 q leading energy | exact identity | direct constrained least squares at two small t values | [checks/C17_local_optimum.py](checks/C17_local_optimum.py) | PASS for listed cases |
| Cor. 3, p.6 | Other positive normalized weights cannot beat the fixed-node minimum | exact identity | seeded finite examples only; arbitrary-path liminf is proved in paper | [checks/C17_local_optimum.py](checks/C17_local_optimum.py) | PASS for listed cases |
| Remark 18; (64), p.24 | Square log determinant separates into node and weight contributions | exact identity | independent complex determinants for both signs of a perturbation | [checks/C18_determinant.py](checks/C18_determinant.py) | PASS for listed cases |
| Remark 18; (65), p.24 | Log determinant Hessian is -norm(H)^2 and node/weight mixed term vanishes | exact identity | centered second difference tolerance 2e-6; direct inner product | [checks/C18_determinant.py](checks/C18_determinant.py) | PASS for listed cases |
| (7), p.5 | Frame-potential excess equals squared Gram defect | exact identity | independent pairwise frame potential and Gram matrix | [checks/C19_frame_and_reconstruction.py](checks/C19_frame_and_reconstruction.py) | PASS for listed cases |
| (8), p.5 | Isotropic mean reconstruction error equals sigma_c^2 norm(G-I)^2 | exact identity | exact finite distribution with covariance I/M | [checks/C19_frame_and_reconstruction.py](checks/C19_frame_and_reconstruction.py) | PASS for listed cases |
| (9), p.5 | Optimally compensated q-null paths have vanishing first-order spectral and condition-number errors | exact identity | two finite steps on an injective example; asymptotic theorem remains in paper | [checks/C19_frame_and_reconstruction.py](checks/C19_frame_and_reconstruction.py) | PASS for listed cases |
| Prop. 10; (26),(28)-(29), p.13 | Affine relations cancel constant/linear terms but detect a mixed-shear quadratic obstruction | exact identity | explicit null relation and second-moment Fourier coefficient | [checks/C20_affine_obstruction.py](checks/C20_affine_obstruction.py) | PASS for listed cases |
| (30), p.14 | Square tensor covariance S diag(r1(s1-r1),r2(s2-r2)) | exact identity | direct class enumeration for 4x4 and 3x5 | [checks/C20_affine_obstruction.py](checks/C20_affine_obstruction.py) | PASS for listed cases |
| Prop. 6; (19)-(20), pp.9-10 | General admissible prescribed weight symbol has optimum-plus-excess decomposition | exact identity | random vector displacement, direct Gram tangent versus class statistics | [checks/C21_prescribed_symbol.py](checks/C21_prescribed_symbol.py) | PASS for listed cases |
| (15),(21), pp.8,10 | Optimal class-center symbol equals dense minimizer; singleton symbol uses raw frequency | exact identity | dense zero-sum least squares and integer singleton comparison | [checks/C21_prescribed_symbol.py](checks/C21_prescribed_symbol.py) | PASS for listed cases |
| (23)-(25), p.11 | Changing positive exact reference weights reparametrizes X and q without creating a new obstruction | exact identity | nonuniform exact weights in injective and colliding 2D examples | [checks/C22_reference_weights.py](checks/C22_reference_weights.py) | PASS for listed cases |
| Figure 1, p.9 | Alias geometry | figure | recomputed from src/aliasgeom, assertions before export | [figures/figure1.py](figures/figure1.py) | PASS; figures/out/Figure1.pdf |
| Figure 2, p.17 | Tensor obstruction and straight paths | figure | recomputed from src/aliasgeom, assertions before export | [figures/figure2.py](figures/figure2.py) | PASS; figures/out/Figure2.pdf |
| Figure 3, p.19 | One-dimensional collision window | figure | recomputed from src/aliasgeom, assertions before export | [figures/figure3.py](figures/figure3.py) | PASS; figures/out/Figure3.pdf |
| Figure 4, p.22 | Optimal and Voronoi repair fractions | figure | recomputed from src/aliasgeom, assertions before export | [figures/figure4.py](figures/figure4.py) | PASS; figures/out/Figure4.pdf |

## What is proved, not computed

All general mathematical assertions are proved in the paper, not by this repository.
In particular:

- Proposition 1 is a general differentiation statement; C01 tests selected rules.
- Proposition 2 and Corollary 3 concern smooth optima and all admissible weight
  paths, including nondifferentiable paths. C17 illustrates their finite limits.
- Theorem 5 is a decomposition for arbitrary finite sampling subgroups, not only
  the finite grids tested in C02. Its general rank/kernel result is a proof.
- Theorem 7 establishes exact positive persistence in a neighborhood of every
  eligible rule. C05 checks formula (22) at finitely many small perturbations;
  its displayed identity G=I is evaluated to a stated floating-point tolerance.
- Theorem 8 proves a smooth exactness manifold and identifies its tangent space.
  C04 checks the example's ranks and hypotheses; it does not construct or prove
  that manifold.
- Proposition 10 gives an obstruction for arbitrary admissible exact paths.
  C20 checks one affine relation and pure/mixed tensor tangents.
- Proposition 11 identifies a tangent cone; Proposition 12 equates an infimum
  over all admissible paths with a finite second-order minimization. C12 checks
  the latter minimization and factorization, not the unrestricted path argument.
- Theorem 13 and Corollary 14 hold throughout their stated integer ranges.
  C06-C07 enumerate selected m values, not an infinite family.
- Proposition 15's zero-defect equivalence for all positive semidefinite spectral
  covariances follows from a matrix argument; C16 tests explicit covariances.
- Corollary 16's closed sums and limit are checked symbolically. The Monte Carlo
  comparison is a separate finite-sample illustration, not proof or an assurance
  for arbitrary probability laws.
- Proposition 17 holds for all positive exact square Fourier rules, not only
  the translated, permuted and sheared rules in C10.
- Proposition 19 includes the continuum limit for every H^sigma function with
  sigma>1/2. C11 verifies a trigonometric polynomial and finite identities;
  the approximation/density argument is not a computation.
- Theorem 20 is a general Cartesian factorization. C13 illustrates a 3D case,
  including aliased, oversampled and empty coordinate classes.

No further explicit numerical example or plotted curve in the paper was found
without a check. Literature attribution, general existence/uniqueness claims,
infinite-family statements and analytic limit arguments are not established by
finite tests. The public companion contains no manuscript, private notes,
conversation material, or imported historical verification reports.

## Scope and conventions

G is the weighted Gram matrix; the defect is G-I. The node transform has
positive exponent and normalization 1/S. The weighted node metric is (10), so
at a uniform rule the Euclidean quadratic matrix is Q_red/S. Real weights
are constrained by sum(zeta)=0 in all dense minimizations. Empty class centers
and covariances are zero. Fourier residues and raw differences are distinct.

All random checks have explicit seeds 4101-4122. Rank thresholds, absolute and
relative comparison tolerances, finite-difference steps and Monte Carlo sample
counts are in the scripts and report. The values 6 and 8 in Section 8.3 are
**squared** Frobenius norms. No experiment is described as a proof.
