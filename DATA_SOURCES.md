# Sources and attribution for the research notes

This repository contains research text and a figure. Source observations, models and application archives remain in the cited canonical revision; they are not bundled under local data or API paths.

| Source | Use in these notes | Frozen evidence |
| :--- | :--- | :--- |
| U.S. Energy Information Administration | Lower 48 working gas stock changes in note 001 | [Source definitions](lab/data/README.md), [source manifest](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/data/manifest.json), [replay CSV](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/storage/backtest.csv) |
| NOAA Climate Prediction Center | Observed population-weighted CONUS HDD/CDD, base 65°F, in note 001 | [Weather definitions](lab/data/README.md), [manifest and raw-source records](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/data/manifest.json) |
| SEC filings recorded by the canonical application | Two reconstructed futures curve snapshots in note 002 | [Matched contracts and filing links](lab/research/curve-repricing.md), [frozen application](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/index.html) |

The observed-weather replay uses current-vintage files and may contain historical revisions. It does not reconstruct all first-release timestamps. SEC-derived curve dates are snapshot labels, not evidence of when the extracted values first became available.

The broader canonical repository also includes spot observations, forecast-weather research and geographic assets. Those projects are outside this notes package. EIA attributes its underlying spot data to Refinitiv, an LSEG business; that attribution is retained in the reference source definitions, without implying that the storage replay uses spot prices.

No repository-wide license is declared. Public access to filings or data does not by itself establish unrestricted reuse. This document grants no new rights to research text, figures, code or third-party material. See [reproduction instructions](lab/research/REPRODUCE.md) and the [snapshot record](SOURCE_SNAPSHOT.json) for evidence lineage.
