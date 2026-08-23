#!/usr/bin/env python3
# TAKANE-SHIKI Japanese Sentence Patterns 80 — page generator
import html as H, subprocess, os
from levels import badges

CSS = """
  @page { size: A4 portrait; margin: 0; }
  :root{ --maroon:#7B1E3B; --gold:#C8A24A; --ink:#1A1A1A; --grey:#6B6B6B;
         --line:#D8D2CC; --tint:#FBF4F5; --tint2:#FAF6EE; }
  *{ box-sizing:border-box; margin:0; padding:0; }
  html,body{ background:#EDEDED; }
  body{ font-family:"Noto Sans CJK JP","Noto Sans Sinhala","Meiryo",sans-serif;
        color:var(--ink); -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  .page{ width:210mm; height:297mm; background:#fff; margin:0 auto;
         padding:9mm 10mm 12mm 10mm; position:relative; overflow:hidden; }
  @media print{ html,body{background:#fff;} .page{margin:0;} }

  ruby rt{ font-size:.5em; font-weight:400; letter-spacing:0; }
  .si{ font-family:"Noto Sans Sinhala",sans-serif; }
  .rom{ font-family:"Helvetica Neue",Arial,sans-serif; color:var(--maroon); letter-spacing:.01em; }
  .en{ font-family:"Helvetica Neue",Arial,sans-serif; }

  .top{ display:flex; justify-content:space-between; align-items:flex-end;
        border-bottom:1.6pt solid var(--maroon); padding-bottom:1.5mm; }
  .brand{ font:600 6.6pt/1 "Helvetica Neue",Arial,sans-serif; letter-spacing:.16em;
          color:var(--grey); text-transform:uppercase; }
  .lvl{ font:700 6.6pt/1 "Helvetica Neue",Arial,sans-serif; color:var(--maroon);
        border:.8pt solid var(--maroon); border-radius:1mm; padding:.9mm 1.7mm; }
  .bdg{ display:flex; align-items:center; gap:1.4mm; }
  .jft{ font:700 6.6pt/1 "Helvetica Neue",Arial,sans-serif; color:#fff; letter-spacing:.04em;
        background:var(--gold); border-radius:1mm; padding:.9mm 1.7mm; }

  .head{ display:flex; align-items:center; gap:4mm; margin-top:2.4mm; }
  .num{ width:13mm; height:13mm; flex:0 0 13mm; background:var(--maroon); color:#fff;
        border-radius:2mm; display:flex; align-items:center; justify-content:center;
        font:700 13pt/1 "Helvetica Neue",Arial,sans-serif; }
  .ttl{ flex:1; }
  .tag{ display:inline-block; font-size:7.6pt; font-weight:700; color:#fff;
        background:var(--gold); border-radius:1mm; padding:.7mm 2mm; margin-bottom:1.2mm; }
  .ttl .jp{ font-size:18pt; font-weight:700; letter-spacing:.02em; line-height:1.2; }
  .ttl .ro{ font-size:11pt; font-weight:600; margin-top:.8mm; }

  .lab{ display:flex; align-items:center; gap:2mm; margin:2.2mm 0 1.4mm; }
  .lab span{ font-size:9.6pt; font-weight:700; color:var(--maroon); white-space:nowrap; }
  .lab .sub{ font:600 6.6pt/1 "Helvetica Neue",Arial,sans-serif; color:var(--grey); font-weight:500; }
  .lab:after{ content:""; flex:1; height:.6pt; background:var(--line); }

  .basic{ background:var(--tint); border:.8pt solid #EBD9DE; border-radius:2mm; padding:2.8mm 4mm; }
  .basic .jp{ font-size:15.5pt; font-weight:700; line-height:1.5; }
  .basic .ro{ font-size:10.5pt; font-weight:600; margin-top:1mm; }
  .basic .en{ font-size:10pt; margin-top:1.6mm; }
  .basic .sn{ font-size:10.5pt; margin-top:.6mm; }

  .use{ border-left:2.4pt solid var(--gold); padding:.4mm 0 .4mm 3mm; }
  .use p{ font-size:9.2pt; line-height:1.45; }
  .use p+p{ margin-top:1.1mm; }
  .use .en,.use .si{ color:#3A3A3A; }
  .use .si{ font-size:9.8pt; }

  .pat{ background:var(--tint2); border:.8pt solid #E7DCC4; border-radius:2mm; padding:2.4mm 4mm; }
  .patrow{ display:flex; align-items:center; gap:2.5mm; }
  .patrow+.patrow{ margin-top:2mm; }
  .cell{ background:#fff; border:1pt solid var(--maroon); border-radius:1.2mm;
         padding:1.4mm 3mm; text-align:center; min-width:17mm; }
  .cell.hi{ background:var(--maroon); }
  .cell.hi .j{ color:#fff; } .cell.hi .r{ color:#F3DDC6; }
  .cell .j{ font-size:13pt; font-weight:700; line-height:1.15; }
  .cell .r{ font-size:8pt; font-weight:600; color:var(--maroon); }
  .blank{ background:#fff; border:1pt dashed #A79070; border-radius:1.2mm; flex:1; height:8.5mm; }
  .plus{ font:700 11pt/1 Arial,sans-serif; color:var(--gold); }
  .to{ font:700 12pt/1 Arial,sans-serif; color:var(--maroon); padding:0 1mm; }
  .pnote{ font-size:7.6pt; font-weight:700; color:var(--maroon); margin:1.6mm 0 .8mm; }
  .patrow+.pnote{ margin-top:2.4mm; }
  .arrow{ text-align:center; font:700 10pt/1 Arial,sans-serif; color:var(--maroon); margin:1.2mm 0; }

  table{ width:100%; border-collapse:collapse; }
  td{ vertical-align:top; padding:__ROWPAD__mm 0; border-bottom:.6pt dotted var(--line); }
  tr:last-child td{ border-bottom:none; }
  td.no{ width:7mm; }
  .dot{ width:5.4mm; height:5.4mm; border-radius:50%; background:var(--maroon); color:#fff;
        font:700 7.4pt/5.4mm "Helvetica Neue",Arial,sans-serif; text-align:center; }
  td.ja{ width:52%; padding-right:4mm; }
  td.ja .j{ font-size:12.5pt; font-weight:700; line-height:1.45; }
  td.ja .r{ font-size:9pt; font-weight:600; margin-top:.4mm; }
  td.tr .e{ font-size:9.2pt; line-height:1.35; }
  td.tr .s{ font-size:10pt; line-height:1.45; margin-top:.5mm; color:#2E2E2E; }
  tr.qrow td{ border-bottom:none; padding-bottom:.8mm; }
  tr.arow td{ padding-top:0; }
  .dot.ab{ background:var(--gold); }
  tr.arow td.ja .j, tr.arow td.tr{ padding-left:0; }

  .ans{ display:grid; grid-template-columns:1fr 1fr; gap:1.6mm 3mm; margin-top:2.4mm;
        border:.8pt solid var(--line); border-radius:2mm; padding:2.2mm 3.5mm; }
  .anshead{ grid-column:1/-1; display:flex; align-items:center; gap:2mm; }
  .anshead b{ font-size:9.6pt; color:var(--maroon); }
  .anshead span{ font:500 6.6pt/1 "Helvetica Neue",Arial,sans-serif; color:var(--grey); }
  .ans{ padding:2.2mm 3.5mm; }
  .ans .a .j{ font-size:12pt; font-weight:700; line-height:1.3; display:inline; }
  .ans .a .r{ font-size:8.6pt; font-weight:600; display:inline; margin-left:1.5mm; }
  .ans .a .t{ font-size:9pt; margin-top:.6mm; }
  .ans .a .t .si{ font-size:9.6pt; }

  .endmark{ font-size:1pt; color:#fff; height:1pt; }
  .foot{ position:absolute; left:10mm; right:10mm; bottom:5mm;
         display:flex; justify-content:space-between; align-items:center;
         border-top:.6pt solid var(--line); padding-top:1.4mm;
         font:6.6pt/1 "Helvetica Neue",Arial,sans-serif; color:#9A9A9A; }
  .foot b{ color:var(--maroon); font-size:7.4pt; }
"""

def cells(spec):
    out = []
    for i, it in enumerate(spec):
        if it == "TO":
            out.append('<div class="to">&#8594;</div>'); continue
        if i and spec[i-1] != "TO": out.append('<div class="plus">+</div>')
        if it == "BLANK":
            out.append('<div class="blank"></div>')
        else:
            j, r = it[0], it[1]
            hi = ' hi' if len(it) > 2 and it[2] else ''
            out.append(f'<div class="cell{hi}"><div class="j">{j}</div><div class="r rom">{r}</div></div>')
    return '<div class="patrow">' + ''.join(out) + '</div>'

def build(p):
    def cellpair(x):
        return (f'<td class="ja"><div class="j">{x[0]}</div><div class="r rom">{x[1]}</div></td>'
                f'<td class="tr"><div class="e en">{H.escape(x[2])}</div>'
                f'<div class="s si">{x[3]}</div></td>')

    off = p.get("start", 0)
    parts = []
    for i0, e in enumerate(p["examples"]):
        i = i0 + off
        if e[0] == "QA":
            parts.append(f'<tr class="qrow"><td class="no"><div class="dot">{i+1}</div></td>'
                         + cellpair(e[1]) + '</tr>')
            parts.append('<tr class="arow"><td class="no"><div class="dot ab">A</div></td>'
                         + cellpair(e[2]) + '</tr>')
        else:
            parts.append(f'<tr><td class="no"><div class="dot">{i+1}</div></td>'
                         + cellpair(e) + '</tr>')
    rows = ''.join(parts)

    pat = []
    for blk in p["pattern"]:
        if blk == "ARROW": pat.append('<div class="arrow">&#9660;</div>')
        elif isinstance(blk, str) and blk.startswith("NOTE:"):
            pat.append(f'<div class="pnote">{blk[5:]}</div>')
        else: pat.append(cells(blk))

    ans = ''
    if p.get("answers"):
        items = ''.join(
            f'<div class="a"><div class="j">{a[0]}</div><div class="r rom">{a[1]}</div>'
            f'<div class="e en">{H.escape(a[2])}</div><div class="s si">{a[3]}</div></div>'
            for a in p["answers"])
        cols = p.get("answers_cols", 2)
        ans = (f'<div class="ans" style="grid-template-columns:repeat({cols},1fr)">'
               f'<div class="anshead"><b>{p["answers_label"][0]}</b>'
               f'<span>{p["answers_label"][1]}</span></div>{items}</div>')

    tag = f'<div class="tag">{p["tag"]}</div>' if p.get("tag") else ''
    skip = set(p.get("skip", ()))
    say = p.get("say_label", ("言ってみよう！", "LET'S SAY IT / අපි කියමු"))

    sec_basic = "" if "basic" in skip else (
        '<div class="lab"><span>基本フレーズ</span>'
        '<span class="sub">BASIC PHRASE / මූලික වාක්‍ය ඛණ්ඩය</span></div>'
        f'<div class="basic"><div class="jp">{p["basic"][0]}</div>'
        f'<div class="ro rom">{p["basic"][1]}</div>'
        f'<div class="en">{H.escape(p["basic"][2])}</div>'
        f'<div class="sn si">{p["basic"][3]}</div></div>')

    sec_use = "" if "use" in skip else (
        '<div class="lab"><span>つかいかた</span>'
        '<span class="sub">HOW TO USE / භාවිතය</span></div>'
        f'<div class="use"><p>{p["use"][0]}</p>'
        f'<p class="en">{p["use"][1]}</p>'
        f'<p class="si">{p["use"][2]}</p></div>')

    sec_pat = "" if "pattern" in skip else (
        '<div class="lab"><span>基本パターン</span>'
        '<span class="sub">BASIC PATTERN / මූලික ව්‍යුහය</span></div>'
        f'<div class="pat">{"".join(pat)}</div>')

    return f"""<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8">
<title>{p['no']} {p['title_jp']}</title><style>{CSS}</style></head><body>
<div class="page">
  <div class="top">
    <div class="brand">TAKANE-SHIKI &nbsp;GOLDEN RULES</div>
    <div class="bdg">{badges(p['no'])}</div>
  </div>
  <div class="head">
    <div class="num">{p['no']}</div>
    <div class="ttl">{tag}
      <div class="jp">{p['title_jp']}</div>
      <div class="ro rom">{p['title_ro']}</div>
    </div>
  </div>
  {sec_basic}
  {sec_use}
  {sec_pat}
  <div class="lab"><span>{say[0]}</span><span class="sub">{say[1]}</span></div>
  <table>{rows}</table>
  {ans}
  <div class="endmark">ENDMARK</div>
  <div class="foot">
    <div>Unit <b>{p['no']}</b> / 124 &nbsp;・&nbsp; {p['foot']}</div>
    <div>日本語 × English × සිංහල</div>
  </div>
</div></body></html>"""

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

def _pdf(stem):
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={stem}.pdf",
                    f"file://{os.path.abspath(stem)}.html"], capture_output=True)

def render(p, stem):
    """Auto-fit: shrink example-row padding until everything fits above the footer."""
    import pymupdf
    for pad in (2.9, 2.6, 2.3, 2.0, 1.7, 1.4, 1.1):
        open(f"{stem}.html", "w").write(build(p).replace("__ROWPAD__", str(pad)))
        _pdf(stem)
        pg = pymupdf.open(f"{stem}.pdf")[0]
        end = [w for w in pg.get_text("words") if "ENDMARK" in w[4]]
        if end and end[0][3] < 814:
            print(f"{stem}: rowpad {pad}mm, content bottom {end[0][3]:.0f}pt")
            return pad
    print(f"{stem}: WARNING did not fit")
    return None
