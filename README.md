# E-commerce landing page A/B test

**Question:** should a business replace its existing landing page to increase conversion?

[Visual case study](https://tola-adelase.github.io/ab-testing-case-study.html) · [Original notebook](Project%203%20-%20Analyze%20A_B%20Test%20Results.ipynb) · [Saved HTML](Project%203%20-%20Analyze%20A_B%20Test%20Results.html)

Academic project for the **Udacity Data Analyst Nanodegree**. Original course prompts and attribution are preserved. This is not an employer experiment.

## Results

| Group | Users | Conversions | Conversion rate |
|---|---:|---:|---:|
| Old page / control | 145,274 | 17,489 | 12.0386% |
| New page / treatment | 145,310 | 17,264 | 11.8808% |

New minus old: **−0.1578 percentage points**, with a descriptive 95% normal-approximation interval of **[−0.3938, +0.0781] percentage points**. Pooled one-sided z-test for positive uplift: **p ≈ 0.9051**. If launch requires demonstrated conversion improvement, retain the existing page. This does not establish equivalence, harm, revenue impact or savings.

## Reproduce the main comparison

Python 3.9+, no third-party packages. From the repository root:

```bash
python3 scripts/verify_ab_results.py
```

The companion was executed against the bundled CSV on 22 October 2026. See [verified-results.json](verified-results.json). It checks sample counts and conversions and calculates rates, effect, interval and the pooled z-test. It does not modify or execute the historical notebook or repeat its simulation and country/logistic-regression extensions.

Preparation: read 294,478 records; exclude 3,893 assignment/page mismatches; remove the second occurrence of one duplicated user in original row order; analyse 290,584 users. The null-hypothesis test uses a pooled standard error; the interval uses an unpooled standard error. The alternative is new-page conversion greater than old-page conversion.

## Historical notebook environment

The repository includes `ab_data.csv` and `countries.csv`. A starting environment uses JupyterLab, pandas, NumPy, matplotlib, statsmodels and SciPy:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install jupyterlab pandas numpy matplotlib statsmodels scipy
jupyter lab
```

Open the notebook from this repository root. Exact historical dependency versions were not retained. This environment and a complete notebook rerun have **not been validated**; API updates may be required. The saved HTML is readable without installation.

## Limitations

- Excluding assignment/page mismatches changes the analysed population and may bias causal interpretation; this is not a clean intent-to-treat estimate.
- The historical simulation seeds Python `random`, but not NumPy's generator. The analytical companion is deterministic.
- No prospective power plan, minimum detectable effect, equivalence margin or product guardrail framework is documented.
- Failure to establish uplift is not proof that the variants are equal.
