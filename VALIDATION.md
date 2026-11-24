# Validate the research notes

From the repository root, run the package check with Git and Python 3.10 or later. The checker and page renderer use the Python standard library. GitHub Actions runs this check under Python 3.12.

```sh
python scripts/validate.py
```

| Check | What it verifies |
| --- | --- |
| Package structure | Local HTML, Markdown and CSS link targets exist. Referenced HTML pages contain the linked section IDs when the URL includes a path and fragment. JSON files parse without duplicate keys or non-standard numbers. |
| Generated reading pages | The committed HTML matches the Markdown sources and the landing-page template. Run `python lab/research/render_notes.py` after editing either. |
| Published research arithmetic | A separate [frozen evidence check](lab/research/REPRODUCE.md) reads the original 463-row replay and embedded curve archive. It compares results with the published tables and worked examples. |

Use `python scripts/validate.py --static-only` for the structure checks alone. The [snapshot record](SOURCE_SNAPSHOT.json) identifies the evidence revision and the standalone packaging source. Its local data hash list is empty because the input data used by the notes live in the cited research archive. Running the package check alone confirms page consistency. Verifying the numeric results requires the separate evidence check.

The evidence check reads saved values. Historical release timing, live forecast performance and causes of repricing require other evidence.
