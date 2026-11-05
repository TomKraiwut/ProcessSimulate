# -*- coding: utf-8 -*-
"""Lesson 02: Kinematics -- from the Training/Basic step-by-step deck (Process Simulate 2502)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "เปิด Device ให้แก้ไขได้ด้วย Set Modeling Scope แล้วสร้าง Link และ Joint ใน Kinematics Editor",
    "ตั้ง Pose (HOME, DOWN, UP, PLACE) ด้วย Pose Editor และจบงานด้วย End Modeling",
    "สั่ง Device Operation จาก pose ไป pose แล้วต่อ 6 operation ด้วย Link (รวม 32 วินาที)",
    "ใช้ Attach / Detach Event ให้ชิ้นงานติดไปกับหัวจับ แล้วอัดวิดีโอและ Export to Web",
]

BODY = f'''
<p class="lead" style="max-width:46em;">เปลี่ยนชิ้นส่วนที่นิ่งอยู่ให้เป็นเครื่องที่ขยับได้ — สร้างกลไก <strong>gantry</strong> แกน X / Z ทีละขั้น รวม 17 ขั้น แล้วสั่งให้หยิบ-วางกล่อง ตั้งแต่ Link, Joint, Pose ไปจนถึง Device Operation และ Event</p>

<h2>ภาพรวม: สร้างกลไก gantry แล้วสั่งหยิบ-วางชิ้นงาน</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Set Modeling Scope</td><td>เปิด Device ให้แก้ไขได้</td></tr>
<tr><td>02</td><td>Create Link</td><td>lnk1 ฐาน · lnk2 แกน X · lnk3 แกน Z</td></tr>
<tr><td>03</td><td>Create Joint</td><td>j1 เลื่อน 0-250 · j2 เลื่อน 0-95 mm</td></tr>
<tr><td>04</td><td>Pose Editor</td><td>HOME DOWN UP PLACE</td></tr>
<tr><td>05</td><td>End Modeling</td><td>ปิดโหมดแก้ไข (อธิบาย ไม่บันทึกทับ)</td></tr>
<tr><td>06</td><td>Device Operation</td><td>สั่ง Device จาก pose ไป pose</td></tr>
<tr><td>07</td><td>Sequence Editor</td><td>6 operation ต่อกันด้วย Link</td></tr>
<tr><td>08</td><td>Attach / Detach Event</td><td>ชิ้นงานติดไปกับหัวจับ</td></tr>
<tr><td>09</td><td>Video + Web</td><td>Movie Recorder · Export to Web</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate 2502 · โฟลเดอร์ <code>02_KINEMATICS</code> · <code>Library\\</code> (Device, Part .cojt) · <code>1_Modeling.psz</code> · <code>2_Device_Operation.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>เปิดแก้ไข</td><td>Set Modeling Scope ให้ Device</td><td>1_Modeling</td></tr>
<tr><td>02</td><td>Link + Joint</td><td>Kinematics Editor สร้าง 3 link 2 joint</td><td>1_Modeling</td></tr>
<tr><td>03</td><td>Pose</td><td>Pose Editor ตั้งท่า 4 ท่า แล้ว End Modeling</td><td>1_Modeling</td></tr>
<tr><td>04</td><td>Operation</td><td>Device Operation + Link ใน Sequence Editor</td><td>2_Device_Op</td></tr>
<tr><td>05</td><td>Event</td><td>Attach ตอนหยิบ Detach ตอนวาง</td><td>2_Device_Op</td></tr>
<tr><td>06</td><td>นำเสนอ</td><td>เล่น simulation อัดวิดีโอ ส่งออกเว็บ</td><td>2_Device_Op</td></tr>
</table>

<p class="lead" style="max-width:46em;">เปลี่ยนชิ้นส่วนที่นิ่งอยู่ให้เป็นเครื่องที่ขยับได้ — สร้างกลไก <strong>gantry</strong> แกน X / Z ทีละขั้น รวม 17 ขั้น แล้วสั่งให้หยิบ-วางกล่อง ตั้งแต่ Link, Joint, Pose ไปจนถึง Device Operation และ Event</p>

<h2>ภาพรวม: สร้างกลไก gantry แล้วสั่งหยิบ-วางชิ้นงาน</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Set Modeling Scope</td><td>เปิด Device ให้แก้ไขได้</td></tr>
<tr><td>02</td><td>Create Link</td><td>lnk1 ฐาน · lnk2 แกน X · lnk3 แกน Z</td></tr>
<tr><td>03</td><td>Create Joint</td><td>j1 เลื่อน 0-250 · j2 เลื่อน 0-95 mm</td></tr>
<tr><td>04</td><td>Pose Editor</td><td>HOME DOWN UP PLACE</td></tr>
<tr><td>05</td><td>End Modeling</td><td>ปิดโหมดแก้ไข (อธิบาย ไม่บันทึกทับ)</td></tr>
<tr><td>06</td><td>Device Operation</td><td>สั่ง Device จาก pose ไป pose</td></tr>
<tr><td>07</td><td>Sequence Editor</td><td>6 operation ต่อกันด้วย Link</td></tr>
<tr><td>08</td><td>Attach / Detach Event</td><td>ชิ้นงานติดไปกับหัวจับ</td></tr>
<tr><td>09</td><td>Video + Web</td><td>Movie Recorder · Export to Web</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>02_KINEMATICS</code> · <code>Library\\</code> (Device, Part .cojt) · <code>1_Modeling.psz</code> · <code>2_Device_Operation.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>เปิดแก้ไข</td><td>Set Modeling Scope ให้ Device</td><td>1_Modeling</td></tr>
<tr><td>02</td><td>Link + Joint</td><td>Kinematics Editor สร้าง 3 link 2 joint</td><td>1_Modeling</td></tr>
<tr><td>03</td><td>Pose</td><td>Pose Editor ตั้งท่า 4 ท่า แล้ว End Modeling</td><td>1_Modeling</td></tr>
<tr><td>04</td><td>Operation</td><td>Device Operation + Link ใน Sequence Editor</td><td>2_Device_Op</td></tr>
<tr><td>05</td><td>Event</td><td>Attach ตอนหยิบ Detach ตอนวาง</td><td>2_Device_Op</td></tr>
<tr><td>06</td><td>นำเสนอ</td><td>เล่น simulation อัดวิดีโอ ส่งออกเว็บ</td><td>2_Device_Op</td></tr>
</table>

<h2>ขั้นที่ 1: ตั้ง System Root แล้วเปิด 1_Modeling.psz</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-01.jpg", "ขั้นที่ 1: ตั้ง System Root แล้วเปิด 1_Modeling.psz"),
    step_list([
        'หน้า Welcome (Home &gt; Welcome Page) มีรายการ Recent Files',
        'คลิก 1_Modeling',
        'System Root ต้องชี้โฟลเดอร์ 02_KINEMATICS\\Library',
        'เปิดแล้วเห็น gantry และกล่องแดง (Part)',
    ])
)}

<h2>ขั้นที่ 2: เลือก Device แล้วกด Set Modeling Scope</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-02.jpg", "ขั้นที่ 2: เลือก Device แล้วกด Set Modeling Scope"),
    step_list([
        'แท็บ Modeling',
        'เลือก Device ใน Objects แล้วกด Set Modeling Scope',
        'Device มีชิ้นส่วน 5 ตัว: TCPF (frame), Conveyor, Z, X, Body',
        'ทุกชิ้นยังเป็นก้อนเดียวกัน ยังขยับไม่ได้',
        'ช่อง Scope เปลี่ยนเป็น Device ปุ่มสร้าง geometry ใช้ได้แล้ว',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> Modeling Scope คือการเปิด component ให้แก้ไขได้ ทำทีละ component เมื่อเสร็จต้อง End Modeling (ขั้นที่ 10)</div>

<h2>ขั้นที่ 3: เปิด Kinematics Editor แล้วกด Create Link</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-03.jpg", "ขั้นที่ 3: เปิด Kinematics Editor แล้วกด Create Link"),
    step_list([
        'Device ยังเลือกอยู่ กด Kinematics Editor',
        'ปุ่มแรกซ้ายบน = Create Link',
        'กล่อง lnk1 ขึ้นในกราฟ',
        'หน้าต่าง Link Properties ชื่อ lnk1 (เปลี่ยนชื่อได้)',
        'แถวสีเขียวใน Link Elements รอให้คลิกชิ้นส่วน (ขั้นที่ 4)',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ย้ายหน้าต่าง Kinematics Editor และ Link Properties ออกไปด้านขวา ไม่ให้บัง Objects tree</div>

<h2>ขั้นที่ 4: lnk1 = Body + Conveyor (ส่วนที่อยู่นิ่ง)</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-04.jpg", "ขั้นที่ 4: lnk1 = Body + Conveyor (ส่วนที่อยู่นิ่ง)"),
    step_list([
        'คลิก Body ใน Objects',
        'คลิก Conveyor',
        'ทั้ง 2 ชิ้นขึ้นในรายการ แถวเขียวเลื่อนลงรอชิ้นถัดไป',
        'กด OK',
    ])
)}
<div class="note"><strong>ระวัง:</strong> tree เลื่อนขึ้นลงหลังคลิกแต่ละครั้ง ดูชื่อก่อนคลิกชิ้นถัดไป ถ้าคลิกผิด (ในภาพเคยได้ TCPF) ให้คลิกชื่อนั้นในรายการแล้วกด Delete</div>

<h2>ขั้นที่ 5: lnk2 = X และ lnk3 = Z + TCPF</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-05.jpg", "ขั้นที่ 5: lnk2 = X และ lnk3 = Z + TCPF"),
    step_list([
        'lnk1 สีส้ม = ฐาน',
        'lnk2 สีเขียว = แคร่แกน X',
        'lnk3 สีเหลือง = หัวจับแกน Z',
        'สีในหน้าจอ 3D ตรงกับสีของ link',
    ])
)}

<h2>ขั้นที่ 6: ลากจาก lnk1 ไป lnk2 สร้าง joint j1 (แกน X)</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-06.jpg", "ขั้นที่ 6: ลากจาก lnk1 ไป lnk2 สร้าง joint j1 (แกน X)"),
    step_list([
        'กดค้างที่ lnk1',
        'ลากไปปล่อยที่ lnk2 หน้าต่าง Joint Properties เปิดขึ้น',
        'Name = j1',
        'แกน From 0,0,0 To = -100, 0, 0 (ทิศ -X)',
        'Joint type = Prismatic (เลื่อน)',
        'ลูกศรล่างซ้ายเปิดส่วน Limits แล้ว Limits type = Constant',
        'High limit = 250 Low limit = 0',
        'กด OK',
    ])
)}

<h2>ขั้นที่ 7: ลากจาก lnk2 ไป lnk3 สร้าง j2 (แกน Z ลง)</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-07.jpg", "ขั้นที่ 7: ลากจาก lnk2 ไป lnk3 สร้าง j2 (แกน Z ลง)"),
    step_list([
        'Parent = lnk2 Child = lnk3',
        'แกน To = 0, 0, -100 (ทิศลง -Z)',
        'Prismatic',
        'Constant 0 ถึง 95 แล้ว OK',
        'เส้น j1 lnk1 &gt; lnk2',
        'เส้น j2 lnk2 &gt; lnk3',
    ])
)}

<h2>ขั้นที่ 8: Pose Editor &gt; New ตั้งค่า joint แล้วตั้งชื่อ pose</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-08.jpg", "ขั้นที่ 8: Pose Editor &gt; New ตั้งค่า joint แล้วตั้งชื่อ pose"),
    step_list([
        'เลือก Device กด Pose Editor (มี HOME อยู่แล้ว)',
        'กด New หน้าต่าง Joint Jog เปิด',
        'พิมพ์ j2 = 95 (หรือลากแถบ)',
        'Lower / Upper Limit = ค่าที่ตั้งในขั้น 6-7',
        'Pose name = DOWN',
        'กด OK',
        'หัวจับลงถึงกล่องแดงพอดี = ทิศ j2 ถูก',
    ])
)}

<h2>ขั้นที่ 9: สร้างให้ครบ 4 pose แล้ว Jump กลับ HOME</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-09.jpg", "ขั้นที่ 9: สร้างให้ครบ 4 pose แล้ว Jump กลับ HOME"),
    step_list([
        'รายการมี HOME DOWN UP PLACE (HOME = j1 0, j2 0 มีมาตั้งแต่แรก)',
        'เลือก HOME กด Jump ให้เครื่องกลับท่าเริ่มแล้ว Close',
    ])
)}
<div class="note"><strong>ระวัง:</strong> ใช้ชื่อ pose ตามนี้ทุกตัวอักษร บท 1 อ้างชื่อเหล่านี้</div>

<h2>ขั้นที่ 10: End Modeling และการบันทึก (อธิบาย)</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-10.jpg", "ขั้นที่ 10: End Modeling และการบันทึก (อธิบาย)"),
    step_list([
        'End Modeling (แท็บ Modeling) = ปิดโหมดแก้ไขและเก็บกลไกลงไฟล์ชิ้นส่วน .cojt ใน Library',
        'คำถาม Save ไฟล์ .psz: ตอบ No ถ้าเป็นการฝึก หรือใช้ Save As ชื่อใหม่ ถ้าจะเก็บงาน',
    ])
)}
<div class="note"><strong>ระวัง:</strong> Library\\Device.cojt ใช้ร่วมกับ 2_Device_Operation (ไฟล์เฉลย) ถ้า End Modeling แล้วบันทึกทับไฟล์เฉลยจะเปลี่ยนตาม ในห้องเรียนให้คัดลอกโฟลเดอร์ 02_KINEMATICS ไว้ก่อน</div>

<h2>ขั้นที่ 11: เปิด 2_Device_Operation แล้ว New Device Operation</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-11.jpg", "ขั้นที่ 11: เปิด 2_Device_Operation แล้ว New Device Operation"),
    step_list([
        'เลือก Device แท็บ Operation &gt; ลูกศร New Operation',
        'New Device Operation',
        'Name ตั้งชื่อ (ไฟล์ตัวอย่างใช้ชื่อ pose ปลายทาง)',
        'Device = Device',
        'From pose = ท่าปัจจุบัน',
        'To pose = DOWN',
        'Duration = 5 วินาที (ลูกศรล่างซ้ายเปิดส่วนนี้)',
        'กด OK',
    ])
)}

<h2>ขั้นที่ 12: ได้ Device_Op 5 วินาที กด Play หัวจับลงหยิบ</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-12.jpg", "ขั้นที่ 12: ได้ Device_Op 5 วินาที กด Play หัวจับลงหยิบ"),
    step_list([
        'Device_Op ขึ้นใน Operation tree และถูกตั้งเป็น current operation ให้เอง',
        'แถบใน Sequence Editor ยาว 5 วินาที',
        'กด Play Simulation Forward',
        'ที่ 5.00 วินาที หัวจับอยู่ที่ DOWN (แต่ยังไม่จับกล่อง ต้องมี Attach Event)',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ตอนทำภาพลบ Device_Op ทิ้ง (เลือกแล้วกด Delete) เพราะไฟล์มีชุดเฉลยใน CompOp อยู่แล้ว</div>

<h2>ขั้นที่ 13: CompOp = 6 Device Operation ต่อกันด้วย Link รวม 32 วินาที</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-13.jpg", "ขั้นที่ 13: CompOp = 6 Device Operation ต่อกันด้วย Link รวม 32 วินาที"),
    step_list([
        'เลือก CompOp &gt; Set Current Operation ลำดับ DOWN &gt; HOME &gt; UP &gt; PLACE &gt; UP &gt; HOME',
        'ลูกศรดำ = Link (เลือก 2 operation ใน Sequence Editor แล้วกดปุ่ม Link)',
        'จุดแดง = Attach Event ตอนจบ DOWN',
        'จุดแดง = Detach Event ตอนเริ่ม UP ตัวที่ 2',
        'จบที่ 32 วินาที = 6 × 5 + รอ 1 วินาที 2 ครั้ง',
    ])
)}

<h2>ขั้นที่ 14: Attach Event ให้กล่องติดไปกับ lnk3</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-14.jpg", "ขั้นที่ 14: Attach Event ให้กล่องติดไปกับ lnk3"),
    step_list([
        'คลิกแถบ DOWN ใน Sequence Editor ก่อนแล้วกดลูกศร New Event',
        'Attach Event = หยิบ',
        'Detach Event = ปล่อย',
        'Objects to Attach คลิก Part',
        'To Object คลิกช่องแล้วคลิก lnk3',
        'Start Time = 0',
        'Before End of Task แล้ว OK Detach ทำแบบเดียวกันที่แถบ UP ตัวที่ 2: Detach Event, Objects = Part, After Start of Task 0 กล่องจะหลุดจากหัวจับตอนเริ่มยกขึ้น',
    ])
)}

<h2>ขั้นที่ 15: เล่น CompOp ดูหยิบ-วางครบรอบ</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-15.jpg", "ขั้นที่ 15: เล่น CompOp ดูหยิบ-วางครบรอบ"),
    step_list([
        'Jump Simulation to Start',
        'Play Simulation Forward',
        'ดูกล่องติดไปกับหัวจับหลัง DOWN และอยู่ที่แผ่นอีกฝั่งหลัง UP',
        'จบ 32.00 วินาที หัวจับกลับ HOME',
    ])
)}

<h2>ขั้นที่ 16: Record Video ด้วย Movie Recorder</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-16.jpg", "ขั้นที่ 16: Record Video ด้วย Movie Recorder"),
    step_list([
        'แท็บ Operation &gt; Movie Recorder แล้วกดเฟือง (Settings)',
        'ปุ่มแดง = Record แล้วกด Play ใน Sequence Editor',
        'Stop เมื่อเล่นจบ',
        'ป้าย REC ขึ้นในหน้าจอ 3D ระหว่างอัด',
        'Destination โฟลเดอร์ที่เก็บไฟล์',
        'Format MPEG-4 (.mp4)',
        'ความละเอียด FullHD',
        'OK',
    ])
)}

<h2>ขั้นที่ 17: Export to Web ส่งงานให้คนที่ไม่มี Process Simulate</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-17.jpg", "ขั้นที่ 17: Export to Web ส่งงานให้คนที่ไม่มี Process Simulate"),
    step_list([
        'File &gt; Import / Export',
        'Export to Web',
        'File name ตั้งชื่อ .html',
        'Launch in browser',
        'Level of details Low = ไฟล์เล็ก',
        'Include simulation Operation = CompOp',
        'OK',
    ])
)}
<div class="tip"><strong>ผลลัพธ์:</strong> KINEMATICS_WebView.html (9 MB) ในโฟลเดอร์คือไฟล์ที่ส่งออกไว้เปิดด้วย browser หมุนดูโมเดลและเล่น simulation ได้</div>

<h2>ไฟล์ในบทเรียนและสิ่งที่อยู่ในแต่ละไฟล์</h2>
<table>
<tr><th>ไฟล์</th><th>สถานะ Device</th><th>Operation</th></tr>
<tr><td>1_Modeling.psz</td><td>Device + Part ยังไม่มี link / joint</td><td>ไม่มี</td></tr>
<tr><td>2_Device_Operation.psz</td><td>Device มี lnk1-3, j1 (X 0-250), j2 (Z 0-95), pose HOME DOWN UP PLACE</td><td>CompOp: 6 Device Operation ตัวละ 5 วินาที + Attach / Detach รวม 32 วินาที</td></tr>
<tr><td>Library\\Device.cojt</td><td>ไฟล์ชิ้นส่วน gantry ที่มีกลไกแล้ว (เฉลย)</td><td>End Modeling บันทึกลงไฟล์นี้</td></tr>
<tr><td>Library\\Part.cojt</td><td>กล่องแดงที่ถูกหยิบ</td><td>-</td></tr>
<tr><td>KINEMATICS_WebView.html</td><td>ผลของ Export to Web</td><td>เปิดด้วย browser</td></tr>
</table>

<h2>เช็กลิสต์: ผู้เรียนทำได้ครบหรือยัง</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th><th>ตรวจด้วย</th></tr>
<tr><td>1</td><td>Set Modeling Scope ให้ Device</td><td>ช่อง Scope แสดง Device</td></tr>
<tr><td>2</td><td>สร้าง link 3 ตัวและแบ่งชิ้นส่วนถูก</td><td>Show colors: ฐานส้ม แกน X เขียว หัวจับเหลือง</td></tr>
<tr><td>3</td><td>สร้าง joint แบบ Prismatic พร้อมแกนและระยะ</td><td>j1 0-250, j2 0-95 ใน Joint Jog</td></tr>
<tr><td>4</td><td>สร้าง pose 4 ท่า</td><td>Pose Editor มี HOME DOWN UP PLACE</td></tr>
<tr><td>5</td><td>อธิบาย End Modeling และการไม่บันทึกทับ</td><td>ไฟล์ใน Library ไม่เปลี่ยน</td></tr>
<tr><td>6</td><td>สร้าง Device Operation จาก pose</td><td>แถบ 5 วินาทีใน Sequence Editor</td></tr>
<tr><td>7</td><td>Attach / Detach Event</td><td>กล่องย้ายไปแผ่นอีกฝั่ง</td></tr>
<tr><td>8</td><td>อัดวิดีโอและ Export to Web</td><td>ได้ไฟล์ .mp4 และ .html</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>Kinematics Editor เป็นสีเทา</td><td>ยังไม่ได้ Set Modeling Scope หรือไม่ได้เลือก Device</td></tr>
<tr><td>หน้าต่างบัง Objects tree</td><td>ลากหน้าต่าง Kinematics Editor / Link Properties ไปด้านขวาก่อนคลิกชิ้นส่วน</td></tr>
<tr><td>ได้ชิ้นส่วนผิดใน Link Elements</td><td>tree เลื่อนหลังคลิก คลิกชื่อผิดในรายการแล้วกด Delete</td></tr>
<tr><td>Joint type / Limits type ไม่เปลี่ยน</td><td>เปิดรายการแล้วคลิกที่ชื่อ (ลูกศรขึ้นลงบนคีย์บอร์ดไม่เลือกให้)</td></tr>
<tr><td>Joint Jog แล้วเลื่อนผิดทิศ</td><td>แก้แกน To ของ joint (เช่น -100 แทน 100) ใน Kinematics Editor</td></tr>
<tr><td>New Event / Attach Event เป็นสีเทา</td><td>คลิกแถบ operation ใน Sequence Editor ก่อน</td></tr>
<tr><td>เพิ่ม Event ผิดแล้ว Ctrl+Z ไม่หาย</td><td>เปิดไฟล์ใหม่ (Welcome &gt; Recent Files) แล้วตอบ No ที่คำถาม Save</td></tr>
<tr><td>ปิดไฟล์แล้วถาม Save</td><td>No = ไม่เก็บสิ่งที่ลอง ถ้าจะเก็บใช้ Save As ชื่อใหม่</td></tr>
</table>
'''
