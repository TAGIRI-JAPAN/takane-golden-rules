#!/usr/bin/env python3
"""Build every unit, merge the book, split per unit, and refresh units.json.

    python3 build_all.py            # render all 124 units, then package
    python3 build_all.py --merge    # skip rendering, just package what is there
"""
import importlib, json, os, re, shutil, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(os.path.dirname(HERE), "dist")
sys.path.insert(0, HERE)

from plan124 import ORDER
from levels import LEVEL
from scenes import S

CHAPTERS = {
    "01": "序章 文字", "04": "第1章 基本の文", "31": "第2章 きもちを つたえる",
    "42": "第3章 すき・くらべる", "56": "第4章 ようす・すいそく",
    "68": "第5章 時・文を つなぐ", "89": "第6章 動詞の かたち",
    "100": "第7章 する・させる・される", "103": "第8章 たのむ・きんし",
    "113": "第9章 すすめる・あいさつ", "117": "第10章 ていどの ことば",
    "122": "第11章 敬語", "124": "巻末",
}
DENY = re.compile(r'^(\{FUN\}|\{NEN\}|パーセント|%|％|分|年|;|ක|[〜–]8| minutes|点|問|字)')
MANUAL_PREREQ = {"01": [], "02": ["01"], "03": ["01", "02"], "25": ["24"],
                 "26": ["24", "25"], "27": ["25"], "124": []}


def stems_of(no):
    src = open(os.path.join(HERE, f"data_{no}.py"), encoding="utf-8").read()
    out, seen = [], set()
    for m in re.finditer(r'"([pu]\d+_[A-Za-z0-9_]+)"', src):
        s = m.group(1)
        if s not in seen:
            seen.add(s); out.append(s)
    return out, src


def render_all():
    os.chdir(HERE)
    t = time.time()
    for i, (no, kind, key, title, stem) in enumerate(ORDER, 1):
        print(f"[{i:>3}/124] {no} {title}", flush=True)
        subprocess.run([sys.executable, f"data_{no}.py"], check=True)
    print(f"rendered in {round(time.time()-t)}s")


def prereq_of(no, src):
    if no in MANUAL_PREREQ:
        return MANUAL_PREREQ[no]
    pre = set()
    for m in re.finditer(r'(?<![0-9])(\d{2,3})(?![0-9])', src):
        n, i, j = m.group(1), m.start(), m.end()
        if DENY.match(src[j:j + 10]):
            continue
        if i and (src[i - 1] == "#" or (src[i - 1].isalpha()
                  and not (src[i - 1] in "pu" and i >= 2 and src[i - 2] == '"'))):
            continue
        if n in LEVEL and int(n) < int(no):
            pre.add(n)
    return sorted(pre, key=int)


def package():
    import pymupdf
    os.chdir(HERE)
    os.makedirs(os.path.join(DIST, "units"), exist_ok=True)
    os.makedirs(os.path.join(DIST, "html"), exist_ok=True)

    doc, toc, units, page, chapter = pymupdf.open(), [], [], 1, None
    for no, kind, key, title, stem in ORDER:
        stems, src = stems_of(no)
        if no in CHAPTERS:
            chapter = CHAPTERS[no]
            toc.append((1, chapter, page))
        toc.append((2, f"{no}  {title}", page))
        for s in stems:
            doc.insert_pdf(pymupdf.open(f"{s}.pdf"))
        ro = re.search(r"title_ro='([^&]*)", src)
        lv, jft = LEVEL[no]
        units.append({
            "no": no, "order": int(no), "chapter": chapter, "title_jp": title,
            "title_ro": (ro.group(1).strip() if ro else "").replace("\\'", "'"),
            "level": lv, "jft_basic": jft, "scenes": S.get(no, []),
            "prereq": prereq_of(no, src),
            "pages": {"start": page, "count": len(stems)},
            "source": f"data_{no}.py", "stems": stems,
        })
        page += len(stems)

    doc.set_toc(toc)
    doc.set_metadata({"title": "TAKANE-SHIKI GOLDEN RULES — N5 / N4 (124 units)",
                      "subject": "日本語 × English × සිංහල"})
    doc.subset_fonts()
    master = os.path.join(DIST, "TAKANE_GOLDEN_RULES_124.pdf")
    doc.save(master, garbage=4, deflate=True, clean=True)
    print("merged:", master, doc.page_count, "pages")

    src_pdf = pymupdf.open(master)
    for u in units:
        a = u["pages"]["start"] - 1
        d = pymupdf.open()
        d.insert_pdf(src_pdf, from_page=a, to_page=a + u["pages"]["count"] - 1)
        try:
            d.subset_fonts()
        except Exception:
            pass
        d.set_metadata({"title": f"{u['no']} {u['title_jp']} — TAKANE-SHIKI GOLDEN RULES"})
        d.save(os.path.join(DIST, "units", f"unit_{u['no'].zfill(3)}.pdf"),
               garbage=4, deflate=True, clean=True)
        for i, s in enumerate(u["stems"], 1):
            suf = "" if len(u["stems"]) == 1 else f"_{i}"
            shutil.copy(f"{s}.html",
                        os.path.join(DIST, "html", f"unit_{u['no'].zfill(3)}{suf}.html"))
    print("split:", len(units), "units")

    out = {"title": "TAKANE-SHIKI GOLDEN RULES", "levels": ["N5", "N4"],
           "total_units": len(units), "total_pages": page - 1,
           "scene_tags": sorted({t for v in S.values() for t in v}), "units": units}
    with open(os.path.join(os.path.dirname(HERE), "units.json"), "w",
              encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("units.json refreshed")


if __name__ == "__main__":
    if "--merge" not in sys.argv:
        render_all()
    package()
