# -*- coding: utf-8 -*-
"""Draft a chapter from a Step-by-Step slide deck exported as PDF (PowerPoint: File > Save As > PDF).

  python -X utf8 pdf_to_chapter.py <deck.pdf> <chapter-number> [--section lessons]

* slides titled "ขั้นที่ ..." (and any other slide with a screenshot): the screenshot area (pictures + red number
  callouts) is cropped to assets/images/<section>/<NN>-<seq>.jpg, the numbered legend becomes step_list(), and
  labelled notes (หมายเหตุ / ข้อควรจำ / ...) become note/tip boxes
* slides titled ไฟล์ในบทเรียน / เช็กลิสต์ / ปัญหาที่พบบ่อย: rebuilt as <table>
* overview / workflow slides: text is dumped as "# TODO" comments -- write the intro by hand
Writes tools/chapters/<section>_<NN>.py (or ..._draft.py if that file exists). Needs a human pass: objectives, intro,
before/after slides, wording.
"""
import argparse
import io
import os
import re

import pymupdf
from PIL import Image, ImageDraw

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SCALE = 2.6          # render scale (pt -> px)
MAX_W = 1600
PAD = 8              # pt of margin around the screenshot area
NOTE_START = re.compile(r"^(หมายเหตุ|บทถัดไป|ในไฟล์ตัวอย่าง|ข้อควรจำ|ข้อคิด|สรุป|ระวัง|อ่านค่า|ทำซ้ำ|ทำไมย้าย|ใช้กับลูกค้า|วิธีเปิด|ผลลัพธ์|ตอนทำภาพ|ทำไมแยก|ใช้ทำอะไร|วิธีหา|ข้อต่าง)")
THAI = "฀-๿"
SKIP_TITLES = ("Thank you",)
OVERVIEW_TITLES = ("ภาพรวม", "Workflow", "Work flow", "Simulation Workflow")
TABLE_TITLES = ("เครื่องมือวิเคราะห์ทั้งหมด", "ไฟล์ในบทเรียน", "ไฟล์ที่ได้", "เช็กลิสต์", "ปัญหาที่พบบ่อย")
SKIP_BLOCK = ("©", "Confidential", "Step by Step |")


def fix_text(s):
    """The PDF text layer drops spaces around Thai/Latin boundaries and splits SARA AM from its consonant."""
    s = re.sub(r"\s+", " ", s.replace("\n", " ")).strip()
    s = re.sub(r" ([ัำ-ฺ็-๎])", r"\1", s)          # "ต ำ" -> "ตำ", "ซ ้ำ" -> "ซ้ำ"
    s = re.sub(rf"([{THAI}])([A-Za-z0-9])", r"\1 \2", s)
    s = re.sub(rf"([A-Za-z0-9%)])([{THAI}])", r"\1 \2", s)
    s = re.sub(rf"([{THAI}])([(=])", r"\1 \2", s)                    # "ที่(3500" -> "ที่ (3500", "แถวบน=" -> "แถวบน ="
    s = re.sub(rf"(\))([{THAI}])", r"\1 \2", s)
    s = re.sub(rf"([{THAI}])/ ", chr(92) + "1/", s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def note_label(text):
    m = NOTE_START.match(text)
    if not m:
        return None, text
    return m.group(1), text[len(m.group(1)):].lstrip()


def analyse(page):
    """-> dict(title, items[(n,text)], extras[text], crop Rect|None, white[Rect])"""
    title, items, notes, extras, callouts, white, extra_rects = None, [], [], [], [], [], []
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, txt = b[:5]
        t = txt.strip()
        if not t or t.startswith(SKIP_BLOCK):
            continue
        if re.fullmatch(r"\d+", t) and len(t) <= 2:
            if y0 > 495:      # page number in the footer
                continue
            callouts.append(pymupdf.Rect(x0, y0, x1, y1))
            continue
        if re.fullmatch(r"(\d+\n)+\d+", t):        # several callouts in one block ("1\n2")
            callouts.append(pymupdf.Rect(x0, y0, x1, y1))
            continue
        if y0 < 80 and title is None:
            title = fix_text(t)
            continue
        if re.match(r"^\d+\n.+", t, re.S):
            cur = None
            white.append(pymupdf.Rect(x0 - 30, y0 - 4, x1 + 8, y1 + 4))
            for ln in t.split("\n"):
                ln = ln.strip()
                if re.fullmatch(r"\d+", ln) and (cur is None or int(ln) == cur[0] + 1):
                    cur = [int(ln), []]
                    items.append(cur)
                elif cur is not None and ln:
                    cur[1].append(ln)
            continue
        ft = fix_text(t)
        if note_label(ft)[0]:
            notes.append(pymupdf.Rect(x0, y0, x1, y1))
        else:
            extra_rects.append(pymupdf.Rect(x0, y0, x1, y1))
        extras.append((y0, ft))
    items = sorted((n, fix_text(" ".join(ls))) for n, ls in items)
    imgs = [pymupdf.Rect(r["bbox"]) for r in page.get_image_info() if r["bbox"][3] - r["bbox"][1] > 40]
    imgs = [r for r in imgs if not any(r.contains(pymupdf.Point((n.x0 + n.x1) / 2, (n.y0 + n.y1) / 2)) for n in notes)]
    for n in notes:                       # the gray box behind a note is a vector shape: blank it and the text
        c = pymupdf.Point((n.x0 + n.x1) / 2, (n.y0 + n.y1) / 2)
        white.append(n + (-4, -4, 4, 4))
        for dr in page.get_drawings():
            r = dr["rect"]
            if r.contains(c) and r.height < 160 and r.width > n.width:
                white.append(r)
    crop = None
    keep = imgs + extra_rects            # slide text that is not a labelled note stays inside the picture
    if keep:
        crop = keep[0]
        for r in keep[1:] + callouts:
            crop |= r
        crop = pymupdf.Rect(max(crop.x0 - PAD, 0), max(crop.y0 - PAD, 84), min(crop.x1 + PAD, page.rect.x1),
                            min(crop.y1 + PAD, 495))
    extras.sort()
    return dict(title=title, items=items, extras=[t for _, t in extras if note_label(t)[0]], crop=crop, white=white)


def save_crop(page, rect, path, white=()):
    pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=rect)
    im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
    dr = ImageDraw.Draw(im)
    for w in white:                      # blank the legend / note boxes that sit inside the crop
        w = w & rect
        if not w.is_empty:
            dr.rectangle([(w.x0 - rect.x0) * SCALE, (w.y0 - rect.y0) * SCALE,
                          (w.x1 - rect.x0) * SCALE, (w.y1 - rect.y0) * SCALE], fill="white")
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, "JPEG", quality=84, optimize=True)


def table_html(page):
    """Rebuild a table slide. Each table row is one (or a few) text boxes whose lines are the cells; wrapped cells
    continue on the next line, so lines are assigned to columns by their left edge (columns = the header row's lines)."""
    blocks = []
    for blk in page.get_text("dict")["blocks"]:
        if blk.get("type") != 0:
            continue
        x0, y0, x1, y1 = blk["bbox"]
        lines = [(l["bbox"][0], "".join(s["text"] for s in l["spans"]).strip()) for l in blk["lines"]]
        lines = [(x, s) for x, s in lines if s]
        txt = " ".join(s for _, s in lines)
        if not lines or txt.startswith(SKIP_BLOCK) or y0 < 80 or y0 > 495:
            continue
        blocks.append(((y0 + y1) / 2, lines))
    blocks.sort(key=lambda b: b[0])
    rows = []
    for cy, lines in blocks:
        if rows and abs(rows[-1][0] - cy) <= 9:
            rows[-1][1].extend(lines)
        else:
            rows.append([cy, list(lines)])
    if not rows:
        return "<table></table>"
    cols = sorted({round(x) for x, _ in rows[0][1]})
    out = ["<table>"]
    for i, (_, lines) in enumerate(rows):
        cells = {}
        for x, s in lines:
            c = max((k for k in range(len(cols)) if cols[k] <= x + 6), default=0)
            cells.setdefault(c, []).append(s)
        tag = "th" if i == 0 else "td"
        out.append("<tr>" + "".join(f"<{tag}>{fix_text(' '.join(cells.get(k, [])))}</{tag}>" for k in range(len(cols))) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def page_text_lines(page):
    return [fix_text(b[4]) for b in page.get_text("blocks")
            if 80 <= b[1] <= 495 and b[4].strip() and not b[4].startswith(SKIP_BLOCK)]


def py_str(s):
    """Escape for a '...' string inside an f-string body (backslashes are doubled once, for the whole body, in main)."""
    return s.replace("'", "&#39;").replace('"', "&quot;").replace("{", "{{").replace("}", "}}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("chapter", type=int)
    ap.add_argument("--section", default="lessons")
    a = ap.parse_args()
    doc = pymupdf.open(a.pdf)
    nn = f"{a.chapter:02d}"
    parts, seq, todos = [], 0, []
    for pno, page in enumerate(doc, start=1):
        info = analyse(page)
        t = info["title"] or ""
        if pno == 1 or t.startswith(SKIP_TITLES):
            continue
        if t.startswith(OVERVIEW_TITLES):      # cards / workflow strips: write by hand, text dumped as a reminder
            todos.append(f"# TODO slide {pno} ({t}): " + " | ".join(page_text_lines(page)))
            continue
        if t.startswith(TABLE_TITLES):
            parts.append(f"<!-- slide {pno} -->\n<h2>{t}</h2>\n" + table_html(page).replace("{", "{{").replace("}", "}}"))
            continue
        heading = re.sub(r"^ขั้นที่\s*(\d+):?\s*", r"ขั้นที่ \1: ", t)
        block = [f"<h2>{heading}</h2>"]
        shot = ""
        if info["crop"] is not None:
            seq += 1
            rel = f"assets/images/{a.section}/{nn}-{seq:02d}.jpg"
            save_crop(page, info["crop"], os.path.join(ROOT, *rel.split("/")), info["white"])
            shot = f'screenshot("{rel}", "{py_str(re.sub("<.*?>", "", heading))}")'
        legend = [txt for _, txt in info["items"]]
        notes = []
        for ex in info["extras"]:
            lab, rest = note_label(ex)
            if lab:
                notes.append((lab, rest))
            else:
                todos.append(f"# TODO slide {pno}: extra text -> {ex[:120]}")
        if shot and legend:
            steps = ",\n        ".join("'" + py_str(x) + "'" for x in legend)
            block.append("{side_by_side(\n    " + shot + ",\n    step_list([\n        " + steps + ",\n    ])\n)}")
        elif shot:
            block.append("{" + shot + "}")
        for lab, rest in notes:
            cls = "note" if lab in ("ข้อควรจำ", "ระวัง", "หมายเหตุ") else "tip"
            block.append(f'<div class="{cls}"><strong>{lab}:</strong> {py_str(rest)}</div>')
        parts.append(f"<!-- slide {pno} -->\n" + "\n".join(block))
    body = "\n\n".join(parts).replace(chr(92), chr(92) * 2)
    out = os.path.join(ROOT, "tools", "chapters", f"{a.section}_{nn}.py")
    if os.path.exists(out):
        out = out.replace(".py", "_draft.py")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write('# -*- coding: utf-8 -*-\n"""DRAFT generated by pdf_to_chapter.py -- edit by hand."""\n')
        f.write("from gen_site import screenshot, step_list, side_by_side\n\n"
                + "\n".join(todos).replace(chr(92), "/") + "\n\nOBJECTIVES = [\n    # TODO\n]\n\n")
        f.write("BODY = f'''\n" + body + "\n'''\n")
    print("wrote", out, "-", seq, "screenshots")


if __name__ == "__main__":
    main()
