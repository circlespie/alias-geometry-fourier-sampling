# Alias geometry and Fourier sampling

The paper *Alias Geometry and Density Compensation in Perturbed Fourier Sampling*
studies which node perturbations can be repaired by diagonal reweighting near an
exact Fourier rule. Alias-class covariances describe the remaining first-order
Gram error, with further results on exact persistence, tensor shears and jitter.

With Python 3.11 or newer, the one-command quick start is:

```sh
python -m pip install -r requirements.txt && python run_all.py
```

After installation, `make all` (or `python run_all.py`) runs every check,
regenerates Figures 1-4 in `figures/out/`, and writes `CLAIMS_REPORT.md`.
`make test` runs the same checks through pytest. The measured reference runtime
is recorded in the report; the suite is designed to take well under ten minutes
on a laptop. Random checks use fixed seeds and one BLAS thread.

[CLAIMS.md](CLAIMS.md) maps statements, equation numbers and pages in the
30-page JFAA submission to independent computations and stated tolerances.
The report includes claimed and computed values, errors and PASS/FAIL results.
Numerical checks are illustrations, not proofs of general theorems.
All figure computations use `src/aliasgeom`; no manuscript, private data, or
external files are needed. PDFs have timestamp metadata suppressed; floating-point
roundoff and PDF byte output can vary across platforms and dependency versions.

Use [CITATION.cff](CITATION.cff) to cite this companion. Paper: [arXiv](ARXIV_URL).
Repository: https://github.com/circlespie/alias-geometry-fourier-sampling. The arXiv link will be filled after submission;
see [PUBLISH_STEPS.md](PUBLISH_STEPS.md).
