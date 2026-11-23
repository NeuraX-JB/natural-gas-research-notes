# Check the frozen research evidence

The notes cite canonical evidence revision `ba3b94ba3a97c3262099da73a25a3a33f06c34ee`. Their standalone packaging revision is recorded separately in [SOURCE_SNAPSHOT.json](../../SOURCE_SNAPSHOT.json). Keep those roles distinct: packaging does not create a new empirical result.

## Reproduce the displayed arithmetic

Requirements: Git and Python 3.10 or later, standard library only. From this notes repository, clone the public archive into a separate directory and check out the exact cited revision:

```sh
git clone https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter.git ../henry-hub-evidence
git -C ../henry-hub-evidence checkout --detach ba3b94ba3a97c3262099da73a25a3a33f06c34ee
python lab/research/check_evidence.py --storage-csv ../henry-hub-evidence/lab/storage/backtest.csv --curve-html ../henry-hub-evidence/index.html
```

Use an unused destination directory. The checkout command affects only the newly cloned archive. The check reads the supplied files and prints whether the original annual storage table and nine matched-contract price differences agree. It does not fetch new observations, write a forecast, alter the archive, or refit a model.

The storage check compares all 10 table rows, including the pooled sample, using the saved replay's rounded predictions. It verifies sample dates, uniqueness, finite values, MAE, relative reduction and inclusive interval coverage. The curve check reads the embedded snapshot data, intersects delivery months, and uses decimal subtraction to check every displayed difference.

## Refit or extend the model separately

An arithmetic check cannot establish that the model originally used only information available at the time. To inspect the method, read the [frozen model](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/storage/model.py), [stored state](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/storage/state.json), [source manifest](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/data/manifest.json) and [complete lab instructions](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/lab/README.md).

A refresh can change source vintages and sample coverage. Treat any refreshed replay as a new experiment, record its inputs, and do not silently substitute its output into these dated notes. A prospective forecast test additionally needs frozen issue times, available weather vintages and later outcomes.

## Rebuild the reading pages

Markdown is the publication source. Generate the static, script-free reading pages with `python lab/research/render_notes.py`; check that they are current with `python lab/research/render_notes.py --check`. The renderer supports the small Markdown subset used in these notes and fails on unsupported block syntax. The repository's [validation guide](../../VALIDATION.md) covers local links and source integrity.
