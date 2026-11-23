# Natural Gas Research Notes

**John Barreto · Independent natural gas research**

Two dated natural gas studies with inspectable evidence, methods and limits.

**[Read this edition online](https://neurax-jb.github.io/natural-gas-research-notes/) · [Local reading page](index.html) · [GitHub portfolio](https://github.com/NeuraX-JB)**

**Methods and tools:** research methodology, chronological evaluation, statistical interpretation and technical writing.

## Publications

- [001 — Does observed weather improve weekly natural gas storage estimates?](lab/research/storage-weather.md) · 23 November 2026 · Retrospective nowcast replay.
- [002 — One benchmark, different delivery months](lab/research/curve-repricing.md) · 23 November 2026 · Two archived SEC-derived snapshots.

**The storage result is retrospective.** It uses observed weather and current-vintage data, not a verified live forecasting record. In the frozen edition, model MAE was 20.50 Bcf versus 30.50 Bcf for the seasonal benchmark across the same 463 weeks. The 2026 calendar-year group is partial; the live ledger had no completed scored forecasts at that snapshot date.

![Retrospective storage replay, 2018 to 13 November 2026: model MAE 20.50 Bcf versus seasonal median 30.50 Bcf; the note supplies all annual values and limitations](lab/assets/storage-replay.svg)

The curve note compares the same nine delivery months across two stored observations. Its price differences are descriptive and do not establish the causes of repricing.

## Read or reproduce locally

Run `python -m http.server 8000` from this root, then open `http://localhost:8000/`. Both publications and the reproduction guide have complete static HTML reading pages and work without JavaScript.

Use the [frozen evidence guide](lab/research/REPRODUCE.md) to verify the existing table arithmetic without refreshing data or producing new forecasts. Markdown is the publication source; run `python lab/research/render_notes.py` after editing a note, or `python lab/research/render_notes.py --check` to detect stale HTML.

See [source definitions](lab/data/README.md), [project-specific attribution](DATA_SOURCES.md), [validation commands](VALIDATION.md) and the [source snapshot record](SOURCE_SNAPSHOT.json).

## Source and publication

These notes were extracted from the [canonical research lab](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter). Their empirical evidence is pinned to revision `ba3b94ba3a97c3262099da73a25a3a33f06c34ee`; the standalone packaging provenance is recorded separately. Editorial clarifications do not replace the reported data or create a new experiment. The canonical website and forecast ledger remain separate.

No repository-wide license is declared and no new rights to third-party data are granted. Research and educational use; not investment advice.
