# Image naming convention

ภาพหน้าจอของบทเก็บที่ `assets/images/lessons/<NN>-<ลำดับ>.jpg` (เช่นภาพที่ 3 ของบท 04 คือ `04-03.jpg`)
ตัดจากสไลด์ Step by Step ด้วย `tools/pdf_to_chapter.py` (เฉพาะส่วนภาพหน้าจอพร้อมเลขกำกับสีแดง ไม่รวมหัวสไลด์/footer)
บีบเป็น JPG กว้างไม่เกิน 1600px ลำดับเลขในภาพตรงกับ `step_list()` ใต้ภาพ

ใช้ใน `tools/chapters/lessons_NN.py` ด้วย `screenshot("assets/images/lessons/04-01.jpg", "คำอธิบายภาพ")` —
เขียน path แบบ root-relative เสมอ `write()` ใน `gen_site.py` จะแปลงให้ตรงกับโฟลเดอร์ของหน้า

วิดีโอ: ห้าม commit `.mp4` ขึ้น repo ให้อัปโหลด YouTube แล้วฝังด้วย `youtube_embed(video_id, title)`
