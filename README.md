# ProcessSimulate

เว็บไซต์สอนการใช้งาน Siemens Tecnomatix Process Simulate แบบ Step by Step (ภาษาไทย) — เผยแพร่ผ่าน GitHub Pages
เนื้อหามาจากชุดสอน `Training\Basic` (ไฟล์ `.pptx` ของแต่ละบท) โครงเว็บและ generator ใช้แบบเดียวกับ PlantSimulation

## โครงสร้างเว็บ

- [index.html](index.html) — หน้าแรก (การ์ดของทุกบท)
- **Step by Step 00–09** ([lessons/](lessons/index.html)) — แต่ละบทเป็นเมนูหลักของตัวเอง `lessons/00.html` .. `04.html`
  - 00 CAD Import · 01 Part Assembly · 02 Kinematics · 03 Basic Process · 04 Robot and Gripper · 05 BIW Spot Welding · 06 Robot Painting · 07 Robot Press Line · 08 AGV · 09 Human Basic
- [assets/style.css](assets/style.css) / [assets/main.js](assets/main.js) — สไตล์ (แดง / เทา / ขาว ตามสไลด์) และเมนู off-canvas ที่ใช้ร่วมกันทุกหน้า

## สร้าง/แก้ไขหน้าเว็บด้วยสคริปต์ (ไม่แก้ไฟล์ .html ตรงๆ)

หน้าเว็บทั้งหมดถูก generate จาก Python ในโฟลเดอร์ [tools/](tools/) — ไฟล์ `.html` จะถูกเขียนทับเมื่อรัน generator ใหม่

- [tools/gen_site.py](tools/gen_site.py) — โครงเมนู (`SECTIONS`), คำอธิบายการ์ด (`HUB_CARD_DESC`), เทมเพลต และ helper (`screenshot`, `step_list`, `side_by_side`, `youtube_embed`)
- [tools/chapters/](tools/chapters/) — เนื้อหาบทละไฟล์ `lessons_NN.py` มี `OBJECTIVES` และ `BODY` (f-string; ปีกกาจริงต้องเป็น `{{` `}}`, backslash ต้องเป็น `\`)
- [tools/gen_chapters.py](tools/gen_chapters.py), [tools/gen_index.py](tools/gen_index.py) — สร้างหน้าบท / หน้ารวม / หน้าแรก

```bash
cd tools
python gen_site.py
python gen_chapters.py
python gen_index.py
```

ทดสอบก่อน push: `python -m http.server 8000` จากโฟลเดอร์นี้ แล้วเปิด `http://localhost:8000/`

## ทำบทใหม่จากสไลด์ (`pdf_to_chapter.py`)

1. เปิด `.pptx` ใน PowerPoint แล้ว **Save As → PDF** (หรือสั่งผ่าน COM)
2. `python -X utf8 tools/pdf_to_chapter.py <deck.pdf> <เลขบท>`
   - ตัดภาพหน้าจอ (พร้อมเลขวงกลมแดง) ของทุกสไลด์ไปที่ `assets/images/lessons/<NN>-<ลำดับ>.jpg`
   - อ่านคำอธิบายเลขกำกับเป็น `step_list()`, กล่อง หมายเหตุ/ข้อควรจำ เป็น note/tip, สไลด์ตาราง (ไฟล์ในบทเรียน / เช็กลิสต์ / ปัญหาที่พบบ่อย) เป็น `<table>`
   - สไลด์ภาพรวม/Workflow จะถูกทิ้งเป็นคอมเมนต์ `# TODO` ให้เขียนเอง
3. แก้ไฟล์ `tools/chapters/lessons_NN.py` — ใส่ OBJECTIVES, ย่อหน้านำ, ตารางภาพรวม และตรวจคำผิด (ข้อความจาก PDF มักมีช่องว่างเพี้ยนระหว่างไทย/อังกฤษ)

เพิ่มบทใหม่: เพิ่มชื่อใน `SECTIONS["lessons"]["chapters"]` และ `"ids"`, เพิ่ม `HUB_CARD_DESC`, แล้วสร้างไฟล์บท

## วิธีเปิดใช้งานเป็นเว็บไซต์ (GitHub Pages)

Settings → Pages → Source: **Deploy from a branch** → branch `main`, โฟลเดอร์ `/ (root)` → Save
ผลลัพธ์อยู่ที่ `https://tomkraiwut.github.io/ProcessSimulate/`
