# One benchmark, different delivery months

**John Barreto · Research note 002 · 23 November 2026**

**Evidence status: two archived, SEC-derived curve snapshots.** This is a descriptive comparison of stored observations, not a forecast or a continuous exchange settlement history.

## Research question

When a natural gas futures curve changes, does the market reprice each delivery month by the same amount?

The portfolio's curve archive includes snapshots reconstructed from SEC filings for 30 June and 30 September 2026. In those snapshots January 2027 delivery moved from $4.391 to $3.752 per MMBtu, a decline of $0.639 per MMBtu. The other overlapping delivery months did not all change by the same amount.

[Open the matching-delivery-month comparison](https://neurax-jb.github.io/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/?data=strips&view=curve&a=2026-06-30&b=2026-09-30&align=delivery)

## Matched contracts and recorded provenance

Every row below uses the same delivery month in both snapshots. Prices are USD per MMBtu; change is **30 September minus 30 June**. The table reproduces the stored application values, rather than independently re-extracting the filings. Rounded prices support arithmetic comparisons, not sub-tick precision.

| Delivery month | 30 June 2026 | 30 September 2026 | Change (USD/MMBtu) |
| :--- | ---: | ---: | ---: |
| November 2026 | 3.393 | 3.026 | −0.367 |
| December 2026 | 3.980 | 3.370 | −0.610 |
| January 2027 | 4.391 | 3.752 | −0.639 |
| February 2027 | 3.959 | 3.428 | −0.531 |
| March 2027 | 3.155 | 2.763 | −0.392 |
| April 2027 | 2.942 | 2.664 | −0.278 |
| May 2027 | 2.917 | 2.693 | −0.224 |
| June 2027 | 3.046 | 2.852 | −0.194 |
| July 2027 | 3.255 | 3.095 | −0.160 |

The frozen app records these filing pointers:

- [United States 12 Month Natural Gas Fund — June 2026 report](https://www.sec.gov/Archives/edgar/data/1405513/000110465926092634/unl-20260630x10q.htm).
- [United States 12 Month Natural Gas Fund — September 2026 report](https://www.sec.gov/Archives/edgar/data/1405513/000110465926123997/unl-20260930x10q.htm).

The curve dates label the stored snapshot observations. They are not filing-publication timestamps or proof that the extracted values were available to a trader on those dates. Contracts present in only one snapshot are excluded from this matched comparison. The [evidence check](REPRODUCE.md) verifies all nine pairs and their displayed differences against the frozen app source.

## Interpretation

Comparing fixed delivery months rather than simply rolling front-month prices avoids mixing different delivery periods. The shape of the curve can be used to study how expectations for particular seasons and delivery months change, including winter premiums and calendar spreads.

The two snapshots establish price changes, not their causes. They cannot isolate the contributions of storage, weather, production or other market developments. The data are reconstructed snapshots and should not be treated as a continuous exchange settlement history. The explorer separately identifies the EIA four-contract historical archive and the SEC-derived longer snapshots, with distinct coverage.

## Evidence

- [Interactive curve explorer](https://neurax-jb.github.io/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/)
- [Application and embedded sources](https://github.com/NeuraX-JB/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/blob/ba3b94ba3a97c3262099da73a25a3a33f06c34ee/index.html)
- [Research portfolio](https://neurax-jb.github.io/Henry-Hub-Futures-Curve-Explorer-How-the-Natural-Gas-Market-prices-winter/lab/)

This analysis is for research and education, not investment advice.


## Citation and edition

Barreto, John. “One benchmark, different delivery months.” Research note 002, 23 November 2026. Evidence revision: `ba3b94ba3a97c3262099da73a25a3a33f06c34ee` in the canonical research repository. The table makes the original comparison inspectable; it adds no forecast or causal claim. Cite the note date and evidence revision together. See the [snapshot record](../../SOURCE_SNAPSHOT.json) for this standalone edition.
