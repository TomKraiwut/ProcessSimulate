# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_site import (SECTIONS, QUIZ_PAGES, page_html, write, chapter_filename, chapter_numbers,
                      chapter_title, chapter_label, HUB_CARD_DESC)


def quiz_card(page, badge, desc):
    return f'''        <div class="card-grid">
          <a href="{page}" class="card">
            <div class="icon number">{badge}</div>
            <h3>{QUIZ_PAGES[page]["title"]}</h3>
            <p>{desc}</p>
          </a>
        </div>'''


def cards(section):
    out = []
    for n, i in enumerate(chapter_numbers(section)):
        out.append(f'''          <a href="{chapter_filename(section, i)}" class="card">
            <div class="icon number">{chapter_label(section, i)}</div>
            <h3>{chapter_title(section, i)}</h3>
            <p>{HUB_CARD_DESC[section][n]}</p>
          </a>''')
    return "\n".join(out)


BODY = f"""        <section id="banner">
          <h1>เรียนรู้ Siemens Tecnomatix Process Simulate</h1>
          <p class="tagline">ชุดสอน Step by Step บน Process Simulate ภาษาไทย</p>
          <p class="intro">
            ลงมือทำทีละบท ตั้งแต่นำเข้า CAD, ประกอบชิ้นส่วน, Kinematics, Basic Process
            ไปจนถึงหุ่นยนต์และ Gripper, งานเชื่อมจุดตัวถังรถ (BIW), งานพ่นสี, ไลน์ปั๊ม, AGV และคนจำลอง — ทุกบทมีภาพหน้าจอจริงพร้อมเลขกำกับ และตัวเลขที่วัดจริงใน Process Simulate
          </p>
        </section>

        <h2>เริ่มที่นี่</h2>
{quiz_card("pre-test.html", "ก่อน", "แบบทดสอบ 20 ข้อ และความคาดหวังต่อการเรียน ประมาณ 15 นาที — ใช้เทียบคะแนนกับหลังเรียน")}

        <h2>{SECTIONS["lessons"]["label"]}</h2>
        <p>แต่ละบทมีโฟลเดอร์ <code>Library</code> และไฟล์ <code>.psz</code> เรียงเลขตามขั้นตอน
        เปิดไฟล์ของขั้นไหนก็ได้เป็นจุดเริ่มต้น ไม่ต้องทำขั้นก่อนหน้าให้เสร็จ</p>
        <div class="card-grid">
{cards("lessons")}
        </div>

        <h2>เรียนจบแล้ว</h2>
{quiz_card("post-test.html", "หลัง", "แบบทดสอบ 20 ข้อชุดเดียวกับก่อนเรียน และประเมินการเรียน (Feedback) — ผลสอบส่งให้ทางอีเมล")}"""

if __name__ == "__main__":
    write("index.html", page_html("หน้าแรก", BODY, active_top="index"))
