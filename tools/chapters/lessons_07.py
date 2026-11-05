# -*- coding: utf-8 -*-
"""Lesson 07: Robot Press Line -- from the Training/Basic step-by-step deck (Process Simulate 2502)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "เปิดไฟล์แล้ว Save As ทำสำเนาก่อนลอง และเลือกหุ่น Robot_1 ที่อยู่หน้าเครื่อง Press_500T_1",
    "ตั้งค่า Smart Place: Locations (pick / place) และ Search Area ตาราง 9 × 9 จุดรอบหุ่น",
    "กด Start แล้วอ่านสีของแต่ละจุด (ถึงทั้ง pick และ place / ถึงแต่ชน)",
    "ย้ายหุ่นไปจุดที่เหมาะสมด้วย Place แล้วคืนหุ่นด้วย Reset",
]

BODY = f'''
<p class="lead" style="max-width:46em;">หาตำแหน่งวางหุ่นที่เอื้อมถึงทุกจุดด้วย <strong>Smart Place</strong> ในไลน์ปั๊ม — ทีละขั้น รวม 9 ขั้น ให้ PS ทดสอบทุกจุดรอบหุ่นแล้วเลือกจุดที่ใช้ได้</p>

<h2>ภาพรวม: หาตำแหน่งวางหุ่นที่เอื้อมถึงทุกจุด</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Save As</td><td>ทำสำเนาไฟล์ก่อนลอง</td></tr>
<tr><td>02</td><td>เลือกหุ่น</td><td>Robot_1 หน้าเครื่อง Press_500T_1</td></tr>
<tr><td>03</td><td>Smart Place</td><td>แท็บ Robot กลุ่ม Reach</td></tr>
<tr><td>04</td><td>Locations</td><td>pick และ place ของ Robot_1</td></tr>
<tr><td>05</td><td>Search Area</td><td>ตาราง 9 × 9 จุดรอบหุ่น</td></tr>
<tr><td>06</td><td>Start</td><td>อ่านสีของแต่ละจุด</td></tr>
<tr><td>07</td><td>Place</td><td>ย้ายหุ่นไปจุดสีน้ำเงิน</td></tr>
<tr><td>08</td><td>Reset</td><td>คืนหุ่นกลับที่เดิม</td></tr>
<tr><td>09</td><td>Collision</td><td>สีส้ม = ถึงแต่ชน</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate 2502 · โฟลเดอร์ <code>07_ROBOT_PRESS_LINE</code> · <code>Library\\</code> (Resource, part) · <code>Robot_Press_Line_Completed.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>เปิด + Save As</td><td>เปิดไฟล์ Completed แล้ว Save As เป็น 1_Smart_Place</td><td>File</td></tr>
<tr><td>02</td><td>เลือกหุ่น</td><td>Objects &gt; Step1 &gt; Robot_1</td><td>Objects</td></tr>
<tr><td>03</td><td>ตั้งค่า</td><td>Robot Placement, pick + place, Search Area</td><td>Smart Place</td></tr>
<tr><td>04</td><td>Start</td><td>PS ทดสอบทุกจุดในตาราง</td><td>Smart Place</td></tr>
<tr><td>05</td><td>Place</td><td>คลิกจุดน้ำเงินแล้วย้ายหุ่น</td><td>Smart Place</td></tr>
<tr><td>06</td><td>Reset</td><td>หุ่นกลับขึ้นฐานแล้ว Close</td><td>Smart Place</td></tr>
</table>
<p>ผลในตัวอย่าง: จาก 81 จุดที่ทดสอบ มี <strong>28 จุด</strong> ที่ Robot_1 ยืนแล้วเอื้อมถึงทั้ง pick และ place</p>

<p class="lead" style="max-width:46em;">หาตำแหน่งวางหุ่นที่เอื้อมถึงทุกจุดด้วย <strong>Smart Place</strong> ในไลน์ปั๊ม — ทีละขั้น รวม 9 ขั้น ให้ PS ทดสอบทุกจุดรอบหุ่นแล้วเลือกจุดที่ใช้ได้</p>

<h2>ภาพรวม: หาตำแหน่งวางหุ่นที่เอื้อมถึงทุกจุด</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Save As</td><td>ทำสำเนาไฟล์ก่อนลอง</td></tr>
<tr><td>02</td><td>เลือกหุ่น</td><td>Robot_1 หน้าเครื่อง Press_500T_1</td></tr>
<tr><td>03</td><td>Smart Place</td><td>แท็บ Robot กลุ่ม Reach</td></tr>
<tr><td>04</td><td>Locations</td><td>pick และ place ของ Robot_1</td></tr>
<tr><td>05</td><td>Search Area</td><td>ตาราง 9 × 9 จุดรอบหุ่น</td></tr>
<tr><td>06</td><td>Start</td><td>อ่านสีของแต่ละจุด</td></tr>
<tr><td>07</td><td>Place</td><td>ย้ายหุ่นไปจุดสีน้ำเงิน</td></tr>
<tr><td>08</td><td>Reset</td><td>คืนหุ่นกลับที่เดิม</td></tr>
<tr><td>09</td><td>Collision</td><td>สีส้ม = ถึงแต่ชน</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>07_ROBOT_PRESS_LINE</code> · <code>Library\\</code> (Resource, part) · <code>Robot_Press_Line_Completed.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>เปิด + Save As</td><td>เปิดไฟล์ Completed แล้ว Save As เป็น 1_Smart_Place</td><td>File</td></tr>
<tr><td>02</td><td>เลือกหุ่น</td><td>Objects &gt; Step1 &gt; Robot_1</td><td>Objects</td></tr>
<tr><td>03</td><td>ตั้งค่า</td><td>Robot Placement, pick + place, Search Area</td><td>Smart Place</td></tr>
<tr><td>04</td><td>Start</td><td>PS ทดสอบทุกจุดในตาราง</td><td>Smart Place</td></tr>
<tr><td>05</td><td>Place</td><td>คลิกจุดน้ำเงินแล้วย้ายหุ่น</td><td>Smart Place</td></tr>
<tr><td>06</td><td>Reset</td><td>หุ่นกลับขึ้นฐานแล้ว Close</td><td>Smart Place</td></tr>
</table>
<p>ผลในตัวอย่าง: จาก 81 จุดที่ทดสอบ มี <strong>28 จุด</strong> ที่ Robot_1 ยืนแล้วเอื้อมถึงทั้ง pick และ place</p>

<h2>ขั้นที่ 1: Save As เป็นไฟล์ใหม่ 1_Smart_Place</h2>
{side_by_side(
    screenshot("assets/images/lessons/07-01.jpg", "ขั้นที่ 1: Save As เป็นไฟล์ใหม่ 1_Smart_Place"),
    step_list([
        'File',
        'Disconnected Study',
        'Save As...',
        'โฟลเดอร์ 07_ROBOT_PRESS_LINE',
        'File name = 1_Smart_Place',
        'Save',
    ])
)}

<h2>ขั้นที่ 2: เลือก Robot_1 แล้วเปิด Robot &gt; Smart Place</h2>
{side_by_side(
    screenshot("assets/images/lessons/07-02.jpg", "ขั้นที่ 2: เลือก Robot_1 แล้วเปิด Robot &gt; Smart Place"),
    step_list([
        'Objects &gt; Resources &gt; Step1',
        'คลิก Robot_1',
        'แท็บ Robot',
        'กลุ่ม Reach &gt; Smart Place',
    ])
)}

<h2>ขั้นที่ 3: หน้าต่าง Smart Place แบบ Robot Placement</h2>
{side_by_side(
    screenshot("assets/images/lessons/07-03.jpg", "ขั้นที่ 3: หน้าต่าง Smart Place แบบ Robot Placement"),
    step_list([
        'Robot Placement (หาที่วางหุ่น)',
        'Robot = Robot_1 ขึ้นให้เอง',
        'ช่อง Locations สีเขียว = รอให้คลิกจุด',
        'Search Area พื้นที่ที่จะลองวางหุ่น',
        'Start ยังกดไม่ได้จนกว่าจะมี Location',
    ])
)}

<h2>ขั้นที่ 4: ใส่ pick และ place ของ Robot_1 ลง Locations</h2>
{side_by_side(
    screenshot("assets/images/lessons/07-04.jpg", "ขั้นที่ 4: ใส่ pick และ place ของ Robot_1 ลง Locations"),
    step_list([
        'Operations &gt; Simulation &gt; Robot &gt; กาง Robot_1',
        'คลิก pick',
        'คลิก place',
        'สองจุดขึ้นในรายการ Locations',
    ])
)}

<h2>ขั้นที่ 5: Search Area ค่าเริ่มต้น + ติ๊ก Partial Reach แล้ว Start</h2>
{side_by_side(
    screenshot("assets/images/lessons/07-05.jpg", "ขั้นที่ 5: Search Area ค่าเริ่มต้น + ติ๊ก Partial Reach แล้ว Start"),
    step_list([
        'Grid: 9 = 9 จุดต่อแกน (คลิกเพื่อแก้)',
        '-2000 ถึง',
        '2000 mm รอบตำแหน่งหุ่น (X และ Y)',
        'ติ๊ก Partial Reach',
        'ไม่ติ๊ก Collision (ดูขั้นที่ 9)',
        'Start ใช้เวลาไม่เกิน 20 วินาที',
    ])
)}

<h2>ขั้นที่ 6: อ่านผล: Solutions Found 28 จุด</h2>
{side_by_side(
    screenshot("assets/images/lessons/07-06.jpg", "ขั้นที่ 6: อ่านผล: Solutions Found 28 จุด"),
    step_list([
        'Solutions Found: 28 = จุดน้ำเงิน',
        'ช่องกลาง = ตำแหน่งเดิมของหุ่นเป็นสีน้ำเงิน',
    ])
)}
<div class="tip"><strong>สรุป:</strong> Robot_1 ยืนที่เดิมเอื้อมถึงทั้ง pick และ place และยังย้ายได้อีก 27 ตำแหน่ง ส่วนใหญ่ไปทางเครื่องปั๊ม (ขวา)</div>

<h2>ขั้นที่ 7: คลิกจุดน้ำเงินแล้ว Place หุ่นย้ายไปจุดนั้น</h2>
{side_by_side(
    screenshot("assets/images/lessons/07-07.jpg", "ขั้นที่ 7: คลิกจุดน้ำเงินแล้ว Place หุ่นย้ายไปจุดนั้น"),
    step_list([
        'คลิกจุดสีน้ำเงิน (ได้เครื่องหมาย X)',
        'Place At = ชื่อจุดเช่น point7-6-1',
        'Place',
        'หุ่นไปยืนที่จุดใหม่ ยังเอื้อมถึงเครื่องปั๊ม',
        'Base_Robot_1 ไม่ย้ายตาม (คนละชิ้น)',
    ])
)}

<h2>ขั้นที่ 8: Reset หุ่นกลับขึ้นฐานแล้ว Close</h2>
{side_by_side(
    screenshot("assets/images/lessons/07-08.jpg", "ขั้นที่ 8: Reset หุ่นกลับขึ้นฐานแล้ว Close"),
    step_list([
        'หุ่นกลับขึ้นยืนบน Base_Robot_1 ตามเดิม',
        'Reset คืนตำแหน่งตอนเปิดหน้าต่าง',
        'Close',
    ])
)}
<div class="note"><strong>ระวัง:</strong> ถ้าปิดโดยไม่ Reset หุ่นจะค้างที่จุดใหม่โดยไม่มีฐาน ถ้าเผลอบันทึกให้เปิดไฟล์ Completed แล้ว Save As ใหม่</div>

<h2>ขั้นที่ 9: ติ๊ก Collision แล้วได้ 0 จุด (ถึงแต่ชน)</h2>
{side_by_side(
    screenshot("assets/images/lessons/07-09.jpg", "ขั้นที่ 9: ติ๊ก Collision แล้วได้ 0 จุด (ถึงแต่ชน)"),
    step_list([
        'Solutions Found: 0',
        'จุดที่ถึงเป็นสีส้มทั้งหมด รวมตำแหน่งเดิม',
        'Collision Viewer มี new_collision_set เปิดอยู่',
    ])
)}

<h2>เช็กลิสต์: ผู้เรียนทำได้ครบหรือยัง</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th><th>ตรวจด้วย</th></tr>
<tr><td>1</td><td>Save As เป็นไฟล์ใหม่</td><td>แถบหัวขึ้น 1_Smart_Place.psz</td></tr>
<tr><td>2</td><td>เปิด Smart Place กับ Robot_1</td><td>ช่อง Robot = Robot_1</td></tr>
<tr><td>3</td><td>ใส่ pick และ place</td><td>Locations มี 2 รายการ</td></tr>
<tr><td>4</td><td>ตั้ง Search Area แล้ว Start</td><td>Solutions Found 28</td></tr>
<tr><td>5</td><td>อ่านสี 4 แบบ</td><td>บอกได้ว่าน้ำเงิน/ส้มคืออะไร</td></tr>
<tr><td>6</td><td>Place และ Reset</td><td>หุ่นกลับขึ้นฐานเดิม</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>Start กดไม่ได้</td><td>ใส่ Location อย่างน้อย 1 จุด (ช่องสีเขียว)</td></tr>
<tr><td>คลิกจุดใน Operations ไม่ได้</td><td>หน้าต่าง Smart Place บังอยู่ ลากไปด้านข้างก่อน</td></tr>
<tr><td>Solutions Found 0 ทุกจุดสีส้ม</td><td>เอาติ๊ก Collision ออก หรือดู collision set ใน Collision Viewer</td></tr>
<tr><td>มองไม่เห็นหุ่นย้าย</td><td>ลากหน้าต่างออกแล้วซูมที่ Step1</td></tr>
<tr><td>หุ่นลอยไม่มีฐานหลัง Place</td><td>ปกติฐานเป็นคนละชิ้น กด Reset</td></tr>
<tr><td>หาปุ่ม Smart Place ไม่เจอ</td><td>อยู่ที่แท็บ Robot กลุ่ม Reach (บางเวอร์ชันเรียกกลุ่ม Tools)</td></tr>
</table>
'''
