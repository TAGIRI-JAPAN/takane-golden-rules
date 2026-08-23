#!/usr/bin/env python3
"""Reference / explanation page generator (tables, kana charts).
Shares the look of build.py but lays out grids instead of sentence patterns."""
import html as H, os
from build import CSS as BASE_CSS, _pdf
from levels import badges

EXTRA = """
  .rt{ width:100%; border-collapse:collapse; margin-top:1.2mm; }
  .rt th{ background:var(--maroon); color:#fff; font-size:8.4pt; font-weight:700;
          padding:__TP__mm 1.4mm; text-align:center; border:.6pt solid var(--maroon);
          white-space:nowrap; }
  .rt td{ border:.6pt solid var(--line); padding:__TP__mm 1.4mm; text-align:center;
          font-size:10.5pt; font-weight:600; vertical-align:middle; }
  .rt td.hd{ background:var(--tint2); color:var(--maroon); font-size:9pt; font-weight:700;
             white-space:nowrap; }
  .rt td.l{ text-align:left; }
  .rt td small{ display:block; font:600 7.2pt/1.15 "Helvetica Neue",Arial,sans-serif;
                color:var(--maroon); margin-top:.3mm; letter-spacing:.01em; }
  .rt td em{ font-style:normal; color:#9A9A9A; }
  .rt td.hi{ background:var(--tint); }
  .rt td.hi small{ color:#A8123B; }
  .rt tr.grp td.hd{ background:var(--maroon); color:#fff; }
  .rt td .si{ font-size:10pt; font-weight:500; }
  .rt.sm td{ font-size:8.4pt; padding:__TP__mm .5mm; font-weight:600; }
  .rt.sm th{ font-size:7.6pt; padding:__TP__mm .5mm; }
  .rt.sm td.hd{ font-size:8.4pt; }
  .kn td{ font-size:__KFS__pt; padding:__TP__mm 0; line-height:1.15; }
  .kn td small{ display:inline; margin:0 0 0 1.2mm; font-size:7.4pt;
                vertical-align:.6mm; }
  .rnote{ font-size:8.6pt; line-height:1.45; margin-top:1.4mm;
          border-left:2.4pt solid var(--gold); padding-left:2.6mm; }
  .rnote b{ color:var(--maroon); }
  .rnote .si{ font-size:9.4pt; }
  .cols2{ display:grid; grid-template-columns:1fr 1fr; gap:0 5mm; }
  .cols3{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:0 4mm; }
  .lab.tight{ margin:2.0mm 0 .6mm; }
"""

def lab(jp, sub):
    return f'<div class="lab tight"><span>{jp}</span><span class="sub">{sub}</span></div>'

def _cell(v):
    """'かき|kaki'  -> cell with romaji;  '*' prefix highlights;  '-' -> em dash"""
    cls = ""
    if isinstance(v, str) and v.startswith("*"):
        cls, v = " class=\"hi\"", v[1:]
    if v == "-":
        return f'<td{cls or ""}><em>—</em></td>'
    if "|" in v:
        j, r = v.split("|", 1)
        return f'<td{cls}>{j}<small>{r}</small></td>'
    return f'<td{cls}>{v}</td>'

def tbl(headers, rows, kana=False, firstcol_hd=True, small=False):
    cls = "rt kn" if kana else ("rt sm" if small else "rt")
    h = ""
    if headers:
        h = "<tr>" + "".join(f"<th>{x}</th>" for x in headers) + "</tr>"
    body = []
    for r in rows:
        if r == "GRP":
            continue
        tds = []
        for i, v in enumerate(r):
            if i == 0 and firstcol_hd:
                tds.append(f'<td class="hd">{v}</td>')
            else:
                tds.append(_cell(v))
        body.append("<tr>" + "".join(tds) + "</tr>")
    return f'<table class="{cls}">{h}{"".join(body)}</table>'

def exs(items, start=1):
    """example rows: (jp, romaji, en, sinhala) — same look as the pattern pages"""
    rows = []
    for i, (j, r, e, si) in enumerate(items, start):
        rows.append(f'<tr><td class="no"><div class="dot">{i}</div></td>'
                    f'<td class="ja"><div class="j">{j}</div>'
                    f'<div class="r rom">{r}</div></td>'
                    f'<td class="tr"><div class="e en">{H.escape(e)}</div>'
                    f'<div class="s si">{si}</div></td></tr>')
    return "<table>" + "".join(rows) + "</table>"

def note(html):
    return f'<div class="rnote">{html}</div>'

def build(p):
    body = []
    if p.get("intro"):
        body.append('<div class="lab tight"><span>この ページは</span>'
                    '<span class="sub">ABOUT THIS PAGE / මේ පිටුව</span></div>')
        body.append(f'<div class="use"><p>{p["intro"][0]}</p>'
                    f'<p class="en">{p["intro"][1]}</p>'
                    f'<p class="si">{p["intro"][2]}</p></div>')
    body.extend(p["blocks"])
    return f"""<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8">
<title>{p['no']} {p['title_jp']}</title><style>{BASE_CSS}{EXTRA}</style></head><body>
<div class="page">
  <div class="top">
    <div class="brand">TAKANE-SHIKI &nbsp;GOLDEN RULES</div>
    <div class="bdg">{badges(p['no'])}</div>
  </div>
  <div class="head">
    <div class="num">{p['no']}</div>
    <div class="ttl">
      <div class="jp">{p['title_jp']}</div>
      <div class="ro rom">{p['title_ro']}</div>
    </div>
  </div>
  {''.join(body)}
  <div class="endmark">ENDMARK</div>
  <div class="foot">
    <div>Unit <b>{p['no']}</b> / 124 &nbsp;・&nbsp; {p['foot']}</div>
    <div>日本語 × English × සිංහල</div>
  </div>
</div></body></html>"""

def render(p, stem):
    import pymupdf
    combos = [(tp, fs) for fs in (13.5, 12.6, 11.8, 11.0, 10.2)
                       for tp in (1.5, 1.2, 0.9, 0.7, 0.5, 0.3)]
    for tp, fs in combos:
        html = (build(p).replace("__TP__", str(tp)).replace("__KFS__", str(fs))
                        .replace("__ROWPAD__", "2.0"))
        open(f"{stem}.html", "w").write(html)
        _pdf(stem)
        pg = pymupdf.open(f"{stem}.pdf")[0]
        end = [w for w in pg.get_text("words") if "ENDMARK" in w[4]]
        if end and end[0][3] < 814:
            print(f"{stem}: pad {tp}mm / kana {fs}pt, bottom {end[0][3]:.0f}pt")
            return tp
    print(f"{stem}: WARNING did not fit")
    return None
