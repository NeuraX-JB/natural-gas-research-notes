#!/usr/bin/env python3
"""Render the repository's small Markdown publication subset without runtime JavaScript."""
import argparse
import html
import re
from pathlib import Path
from urllib.parse import urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAGES = {"storage-weather.md": "storage-weather.html", "curve-repricing.md": "curve-repricing.html", "REPRODUCE.md": "reproduce.html"}


def inline(text):
    pattern = r"(!?\[[^\]\n]*\]\([^\)\n]+\)|\*\*[^*\n]+\*\*|`[^`\n]+`)"
    result = []
    for token in re.split(pattern, text):
        link = re.fullmatch(r"(!?)\[([^\]]*)\]\(([^\)]+)\)", token)
        if link:
            image, label, url = link.groups()
            if urlsplit(url).scheme not in ("", "https", "http"):
                raise ValueError("Unsupported link scheme")
            url = PAGES.get(url, url)
            attr = html.escape(url, quote=True)
            result.append(f'<img src="{attr}" alt="{html.escape(label, quote=True)}" loading="lazy">' if image else f'<a href="{attr}">{html.escape(label)}</a>')
        elif token.startswith("**") and token.endswith("**"):
            result.append("<strong>" + html.escape(token[2:-2]) + "</strong>")
        elif token.startswith("`") and token.endswith("`"):
            result.append("<code>" + html.escape(token[1:-1]) + "</code>")
        else:
            result.append(html.escape(token))
    return "".join(result)


def markdown(source):
    lines = source.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Publication must start with its title")
    title, out, headings, i = lines[0][2:], [], [], 1
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            code, i = [], i+1
            while i < len(lines) and lines[i] != "```":
                code.append(lines[i]); i += 1
            if i == len(lines):
                raise ValueError("Unclosed code fence")
            out.append('<pre tabindex="0" aria-label="Reproduction commands"><code>' + html.escape("\n".join(code)) + '</code></pre>')
            i += 1
            continue
        heading = re.fullmatch(r"(#{2,3}) (.+)", line)
        if heading:
            level, text = len(heading[1]), heading[2]
            anchor = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
            if level == 2:
                headings.append((anchor, text))
            out.append(f'<h{level} id="{anchor}">{inline(text)}</h{level}>')
            i += 1
            continue
        if line.startswith("| "):
            cells = lambda value: [part.strip() for part in value.strip().strip("|").split("|")]
            header = cells(line)
            if i+1 >= len(lines) or not all(re.fullmatch(r":?-+:?", part) for part in cells(lines[i+1])):
                raise ValueError("Table needs a Markdown delimiter row")
            caption = "Retrospective storage replay: annual and pooled results" if header[0] == "Calendar year" else "Same delivery contracts in the two stored curve snapshots"
            table = ['<div class="table-scroll" role="region" tabindex="0" aria-label="' + caption + '"><table><caption>' + caption + '</caption><thead><tr>']
            table.extend('<th scope="col">' + inline(cell) + '</th>' for cell in header)
            table.append('</tr></thead><tbody>')
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                row = cells(lines[i])
                if len(row) != len(header):
                    raise ValueError("Table cell count mismatch")
                table.append('<tr><th scope="row">' + inline(row[0]) + '</th>' + ''.join('<td>' + inline(cell) + '</td>' for cell in row[1:]) + '</tr>')
                i += 1
            table.append('</tbody></table></div>')
            out.append(''.join(table))
            continue
        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append('<li>' + inline(lines[i][2:]) + '</li>'); i += 1
            out.append('<ul>' + ''.join(items) + '</ul>')
            continue
        if re.match(r"^(?:>|#|\s{4}|\d+\. )", line):
            raise ValueError("Unsupported Markdown block: " + line[:60])
        paragraph = [line]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(?:#|\||- |```)", lines[i]):
            paragraph.append(lines[i]); i += 1
        out.append('<p>' + inline(" ".join(paragraph)) + '</p>')
    return title, '\n'.join(out), headings


def document(title, description, content, root_prefix):
    return f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · John Barreto</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<link rel="stylesheet" href="{root_prefix}lab/assets/research.css"></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="mast"><div class="wrap"><a href="{root_prefix}">John Barreto · Research notes</a><nav aria-label="Publication"><a href="{root_prefix}">All notes</a><a href="{root_prefix}lab/research/reproduce.html">Reproduce evidence</a><a href="https://github.com/NeuraX-JB/natural-gas-research-notes">Source repository</a></nav></div></header>
{content}
<footer class="wrap"><p>John Barreto · Independent natural gas research. Research and educational use.</p><p><a href="{root_prefix}DATA_SOURCES.md">Sources and attribution</a> · <a href="{root_prefix}SOURCE_SNAPSHOT.json">Source edition</a> · <a href="{root_prefix}VALIDATION.md">Validation</a></p></footer>
</body></html>
'''


def outputs():
    result = {}
    for source, target in PAGES.items():
        title, content, headings = markdown((HERE / source).read_text(encoding="utf-8"))
        toc = '<nav class="toc" aria-label="In this publication"><strong>In this publication</strong><ul>' + ''.join(f'<li><a href="#{anchor}">{html.escape(label)}</a></li>' for anchor, label in headings) + '</ul></nav>'
        body = '<main class="reading" id="main"><article><h1>' + html.escape(title) + '</h1>' + toc + content + f'<p class="source-link"><a href="{source}">Read the Markdown source</a> · <a href="#main">Back to top</a></p></article></main>'
        result[HERE / target] = document(title, title + ' — methods, frozen evidence and limitations.', body, '../../')
    body = '''<main id="main"><section class="hero"><div class="wrap"><div class="eyebrow">Independent natural gas research</div><h1>Weather, storage and the Henry Hub futures curve</h1><p>Two studies by John Barreto examine the size of a weekly storage miss and the change in a winter gas premium. Each study links its calculations to the underlying observations.</p></div></section>
<div class="wrap"><p class="caveat"><strong>Evidence edition · 23 November 2026.</strong> The storage study is a retrospective replay using observed weather and current-vintage data. Its frozen live ledger had no completed scored forecasts. The curve study is a descriptive comparison of two archived snapshots.</p>
<section class="grid" aria-label="Publications"><article class="card"><h2>Natural Gas Field Studies</h2><p>Ten books on physical delivery, industrial demand, power generation and Henry Hub prices. Each volume includes its research files.</p><a class="button" href="field-studies/">Browse the ten books</a></article><article class="card"><span class="tag">Note 001 · Retrospective nowcast</span><h2>Does observed weather improve weekly storage estimates?</h2><p>Across 463 weeks, adding observed weather cut the average storage miss from 30.50 to 20.50 billion cubic feet. The seasonal median was still closer on 197 weeks.</p><p class="note-meta"><time datetime="2026-11-23">23 November 2026</time> · 2026 results are partial</p><a class="button" href="lab/research/storage-weather.html">Read storage and weather</a></article>
<article class="card"><span class="tag">Note 002 · Descriptive curve comparison</span><h2>One benchmark, different delivery months.</h2><p>All nine matched contracts fell between 30 June and 30 September 2026. January 2027 fell $0.639 per million Btu and July 2027 fell $0.160. Follow the change in the January premium back to the filings.</p><p class="note-meta"><time datetime="2026-11-23">23 November 2026</time> · Two archived observations</p><a class="button" href="lab/research/curve-repricing.html">Read curve repricing</a></article></section>
<figure class="figure"><img src="lab/assets/storage-replay.svg" width="820" height="540" alt="Retrospective storage replay: model MAE is lower than the seasonal benchmark in each year from 2018 through partial 2026. All annual values are provided in the storage note."><figcaption>Recorded replay results, not verified live performance. <a href="lab/research/storage-weather.html#question-and-result">Read the complete results table and its qualifications.</a></figcaption></figure>
<section class="card"><h2>Reproduce the reported arithmetic</h2><p>The evidence checker recalculates the annual storage errors, the two weekly examples and the nine matched contract changes from the archived files.</p><a href="lab/research/reproduce.html">Open the reproduction guide</a></section></div></main>'''
    result[ROOT / 'index.html'] = document('Natural Gas Research Notes', 'Dated natural gas research by John Barreto: observed weather and storage estimates, matched futures contracts, methods, evidence and limitations.', body, './')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if checked-in HTML differs; write nothing')
    args = parser.parse_args()
    changed = []
    for path, rendered in outputs().items():
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != rendered:
                changed.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(rendered, encoding='utf-8')
    if changed:
        raise SystemExit('Stale reading pages; run render_notes.py: ' + ', '.join(changed))
    print('Four static reading pages are current.' if args.check else 'Rendered four static reading pages.')
