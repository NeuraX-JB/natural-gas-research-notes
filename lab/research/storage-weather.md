# Does observed weather improve weekly natural gas storage estimates?

**Henry Hub Research · Research note 001 · 23 November 2026**

## Question and result

Can observed heating and cooling degree days improve an estimate of the EIA Lower 48 weekly net stock change relative to a simple seasonal benchmark?

In the checked-in chronological replay, the weather-adjusted model's mean absolute error (MAE) was 20.50 Bcf, compared with 30.50 Bcf for a five-year seasonal median, a relative reduction of 32.8%. Both methods are evaluated on the same 463 weekly dates, from 5 January 2018 through 13 November 2026. The model had lower MAE in each of the nine calendar-year groups; 2026 is incomplete.

![Mean absolute error by calendar year](../assets/storage-replay.svg)

| Calendar year | Weeks | Seasonal MAE (Bcf) | Model MAE (Bcf) | Relative reduction | Interval coverage |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 2018 | 52 | 28.81 | 23.67 | 17.9% | 57.7% |
| 2019 | 52 | 33.46 | 26.03 | 22.2% | 71.2% |
| 2020 | 52 | 27.42 | 23.07 | 15.9% | 82.7% |
| 2021 | 53 | 27.57 | 21.27 | 22.8% | 86.8% |
| 2022 | 52 | 32.31 | 19.12 | 40.8% | 80.8% |
| 2023 | 52 | 30.98 | 19.44 | 37.2% | 82.7% |
| 2024 | 52 | 34.27 | 20.41 | 40.4% | 76.9% |
| 2025 | 52 | 33.19 | 15.63 | 52.9% | 82.7% |
| 2026 (partial) | 46 | 26.07 | 15.25 | 41.5% | 82.6% |
| **All** | **463** | **30.50** | **20.50** | **32.8%** | **78.2%** |

MAE is the arithmetic mean of absolute errors in Bcf. Relative reduction is 100 × (1 − model MAE / baseline MAE). Coverage is the share of observations within the model's reported interval. Year groups are by the target week's Friday. Annual reductions should not be averaged to obtain the overall reduction.

## Method

The benchmark is the median of five previous seasonal analogs, using the Friday closest to the same month/day in each prior year. The model fits ordinary least squares to past deviations from that benchmark, with an intercept and two features: observed population-weighted HDD and CDD deviations from their respective five-year seasonal medians.

The rolling training window uses up to 156 previous eligible weeks, with a minimum of 104. The interval uses up to 104 earlier absolute replay errors, with a minimum of 52; the scored rows have an interval available. The target week's reported inventory change is not included in its training data. The target is the change in published working-gas stocks, which may differ from implied physical flow because of reclassifications.

Sources are the EIA Lower 48 working gas series and NOAA CPC observed, population-weighted CONUS degree days, base 65°F. Weather is aggregated Friday through Thursday, an approximation to the inventory reference interval.

## What the evidence does and does not show

The result supports the usefulness of observed temperature exposure in this historical model. It does not establish that weather alone determines gas inventories or that model performance would be identical with data vintages actually available before each historical release. The source files may include historical revisions, and original release timing is not established for all weather observations. The result is a retrospective **nowcast replay**, not a test of forecast-weather accuracy or a verified live performance record. At the snapshot date the live ledger had no completed scored forecasts.

The calendar-year breakdown is descriptive, not an independent holdout test or a winter-only analysis. Interval coverage of 78.2% is empirical, not a guarantee. Further research should evaluate frozen first-release forecasts, regional inputs and winter-specific performance, alongside alternative drivers such as production, LNG feedgas and industrial demand.

## Evidence and reproduction

- [Frozen replay CSV (463 weeks)](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/storage/backtest.csv)
- [Model source at the snapshot](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/storage/model.py)
- [Recorded model state at the snapshot](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/storage/state.json)
- [Data provenance and definitions](../data/README.md)
- [Live storage dashboard](https://neurax-jb.github.io/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/lab/storage/)
- [Rebuild instructions](../README.md)

This analysis is for research and education, not investment advice.
