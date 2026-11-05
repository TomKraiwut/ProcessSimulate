# -*- coding: utf-8 -*-
"""Lesson 05: BIW Spot Welding -- from the Training/Basic step-by-step deck (Process Simulate 2502)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "สร้างจุดเชื่อมด้วย Weld Point (Preserve จาก SPOT_CD) และฉายจุดลงผิวชิ้นงานด้วย Project",
    "สร้าง Weld Operation (Weld_Op 10 จุด) และใช้ Gun Search เลือกปืนที่เชื่อมได้ครบจาก 14 รุ่น",
    "ติด Fixture และหุ่น S040R03 พร้อมปืนด้วย Mount Tool",
    "ใช้ Pie Chart / WDC ปรับมุมเข้าอัตโนมัติ และตั้ง Start / via ก่อน-หลังจุดเชื่อม",
    "ตรวจ Collision แล้วเพิ่ม via หลบ จากนั้น Mirror ให้หุ่นตัวที่ 2 เชื่อมอีกฝั่ง",
]

BODY = f'''
<p class="lead" style="max-width:46em;">งานเชื่อมจุดตัวถังรถ (BIW) ทีละขั้น รวม 25 ขั้น — ตั้งแต่สร้างจุดเชื่อมและเลือกปืน วางจิ๊กและหุ่น ปรับมุมเข้า-ออก ตรวจชน ไปจนถึง Mirror ให้หุ่นอีกตัวเชื่อมอีกฝั่งพร้อมกัน</p>

<h2>ภาพรวม: จากจุดเชื่อมถึงหุ่น 2 ตัว</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Weld Point</td><td>Preserve จุดจาก SPOT_CD แล้วสร้างจุดเชื่อม</td></tr>
<tr><td>02</td><td>Project</td><td>ฉายจุดลงผิว PartC ได้ทิศของจุด</td></tr>
<tr><td>03</td><td>Weld Operation</td><td>Weld_Op รวม 10 จุด</td></tr>
<tr><td>04</td><td>Gun Search</td><td>ปืน 14 รุ่น รุ่นไหนเชื่อมได้ครบ</td></tr>
<tr><td>05</td><td>Fixture + Robot</td><td>จิ๊กจับชิ้นงาน หุ่น S040R03 ติดปืน</td></tr>
<tr><td>06</td><td>Pie Chart / WDC</td><td>มุมที่ปืนเข้าได้ ปรับมุมอัตโนมัติ</td></tr>
<tr><td>07</td><td>Approach / Depart</td><td>Start และ via ก่อน-หลังจุดเชื่อม</td></tr>
<tr><td>08</td><td>Collision</td><td>หาจุดชนแล้วเพิ่ม via หลบ</td></tr>
<tr><td>09</td><td>Mirror</td><td>หุ่นตัวที่ 2 เชื่อมอีกฝั่ง</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate 2502 · โฟลเดอร์ <code>05_BIW_SPOT_WELDING</code> · <code>Library\\</code> (Part, Resource) · <code>1_</code> ถึง <code>8_</code> <code>.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>1-2: จุดเชื่อม + ปืน</td><td>Weld Point, Project, Weld Op, Gun Search</td><td>1_ / 2_</td></tr>
<tr><td>02</td><td>3-4: เซลล์</td><td>Fixture, Robot, Mount Tool</td><td>3_ / 4_</td></tr>
<tr><td>03</td><td>5: WDC</td><td>Pie Chart, Automatic Approach Angle</td><td>ต่อจากบท 4</td></tr>
<tr><td>04</td><td>6: เข้า-ออก</td><td>Start, via ก่อน-หลังจุด</td><td>5_WDC</td></tr>
<tr><td>05</td><td>7: ตรวจชน</td><td>Collision Set, Collision Mode</td><td>6_Approach</td></tr>
<tr><td>06</td><td>8: Mirror</td><td>Mirror, Compound Operation</td><td>7_Collision</td></tr>
</table>
<p>งานครบในไฟล์ 8: หุ่น 2 ตัวเชื่อมฝั่งละ 10 จุดพร้อมกัน = <strong>62.53 วินาที</strong> (อ่านจาก Sequence Editor)</p>

<p class="lead" style="max-width:46em;">งานเชื่อมจุดตัวถังรถ (BIW) ทีละขั้น รวม 25 ขั้น — ตั้งแต่สร้างจุดเชื่อมและเลือกปืน วางจิ๊กและหุ่น ปรับมุมเข้า-ออก ตรวจชน ไปจนถึง Mirror ให้หุ่นอีกตัวเชื่อมอีกฝั่งพร้อมกัน</p>

<h2>ภาพรวม: จากจุดเชื่อมถึงหุ่น 2 ตัว</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Weld Point</td><td>Preserve จุดจาก SPOT_CD แล้วสร้างจุดเชื่อม</td></tr>
<tr><td>02</td><td>Project</td><td>ฉายจุดลงผิว PartC ได้ทิศของจุด</td></tr>
<tr><td>03</td><td>Weld Operation</td><td>Weld_Op รวม 10 จุด</td></tr>
<tr><td>04</td><td>Gun Search</td><td>ปืน 14 รุ่น รุ่นไหนเชื่อมได้ครบ</td></tr>
<tr><td>05</td><td>Fixture + Robot</td><td>จิ๊กจับชิ้นงาน หุ่น S040R03 ติดปืน</td></tr>
<tr><td>06</td><td>Pie Chart / WDC</td><td>มุมที่ปืนเข้าได้ ปรับมุมอัตโนมัติ</td></tr>
<tr><td>07</td><td>Approach / Depart</td><td>Start และ via ก่อน-หลังจุดเชื่อม</td></tr>
<tr><td>08</td><td>Collision</td><td>หาจุดชนแล้วเพิ่ม via หลบ</td></tr>
<tr><td>09</td><td>Mirror</td><td>หุ่นตัวที่ 2 เชื่อมอีกฝั่ง</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>05_BIW_SPOT_WELDING</code> · <code>Library\\</code> (Part, Resource) · <code>1_</code> ถึง <code>8_</code> <code>.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>1-2: จุดเชื่อม + ปืน</td><td>Weld Point, Project, Weld Op, Gun Search</td><td>1_ / 2_</td></tr>
<tr><td>02</td><td>3-4: เซลล์</td><td>Fixture, Robot, Mount Tool</td><td>3_ / 4_</td></tr>
<tr><td>03</td><td>5: WDC</td><td>Pie Chart, Automatic Approach Angle</td><td>ต่อจากบท 4</td></tr>
<tr><td>04</td><td>6: เข้า-ออก</td><td>Start, via ก่อน-หลังจุด</td><td>5_WDC</td></tr>
<tr><td>05</td><td>7: ตรวจชน</td><td>Collision Set, Collision Mode</td><td>6_Approach</td></tr>
<tr><td>06</td><td>8: Mirror</td><td>Mirror, Compound Operation</td><td>7_Collision</td></tr>
</table>
<p>งานครบในไฟล์ 8: หุ่น 2 ตัวเชื่อมฝั่งละ 10 จุด พร้อมกัน = <strong>62.53 วินาที</strong> (อ่านจาก Sequence Editor)</p>

<h2>ขั้นที่ 1: ตั้ง System Root แล้วเปิด 1_Weld_Point</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-01.jpg", "ขั้นที่ 1: ตั้ง System Root แล้วเปิด 1_Weld_Point"),
    step_list([
        'File',
        'Disconnected Study',
        'Open in Standard Mode',
        'เลือก 1_Weld_Point &gt; Open',
    ])
)}

<h2>ขั้นที่ 2: ไฟล์ 1 มี PartC, PartD และ SPOT_CD (จุดอ้างอิง)</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-02.jpg", "ขั้นที่ 2: ไฟล์ 1 มี PartC, PartD และ SPOT_CD (จุดอ้างอิง)"),
    step_list([
        'Set Modeling Scope',
        'ช่อง Scope = SPOT_CD',
        'SPOT_CD ชิ้นอ้างอิงจากงานต้นฉบับ',
        'Weld_10p จุด point1-10 ที่ใช้',
    ])
)}

<h2>ขั้นที่ 3: Set as Preserved Objects ให้จุด point1-10</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-03.jpg", "ขั้นที่ 3: Set as Preserved Objects ให้จุด point1-10"),
    step_list([
        'Shift+คลิก point10 (เลือก 10 จุด)',
        'Set as Preserved Objects (แท็บ Modeling กลุ่ม Geometry)',
        '1 คลิก point1',
        'ไอคอนจุดเปลี่ยนเป็นสีเขียว = Preserved',
    ])
)}

<h2>ขั้นที่ 4: Create Weld Points แล้วคลิกจุดสีแดงบนชิ้นงาน</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-04.jpg", "ขั้นที่ 4: Create Weld Points แล้วคลิกจุดสีแดงบนชิ้นงาน"),
    step_list([
        'แท็บ Process &gt; ปุ่ม Create Weld Points (ไอคอนจุดสีฟ้า)',
        'คลิกจุดแดงในหน้าจอ 3D ทีละจุด',
        'Home &gt; Mfgs ได้ wp, wp1, ...',
        'ตอนทำภาพได้ 9 จุด (ไฟล์ 2 มี 10 จุด)',
    ])
)}

<h2>ขั้นที่ 5: Project Weld Points ฉายจุดลงผิว PartC</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-05.jpg", "ขั้นที่ 5: Project Weld Points ฉายจุดลงผิว PartC"),
    step_list([
        'Project weld points on a customized list of parts',
        'ช่องเขียว Parts',
        'Obtain Parts แล้วลบ SPOT_CD ให้เหลือ PartC',
        'Project',
        'ฉายแบบแม่นไม่ผ่าน: ตอบ Yes (ฉายแบบประมาณ)',
        'ได้ลูกศรทิศของจุดบนผิว',
    ])
)}

<h2>ขั้นที่ 6: New Weld Operation (Weld_Op) ใส่จุดเชื่อม</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-06.jpg", "ขั้นที่ 6: New Weld Operation (Weld_Op) ใส่จุดเชื่อม"),
    step_list([
        'Robot / Gun ว่างไว้ก่อน (บท 2, 4)',
        'Weld List คลิกช่องเขียวแล้วเลือก wp ทั้งหมด',
        'OK',
        '1 Name = Weld_Op',
        'Weld_Op มีจุดเชื่อมเรียงตามลำดับ',
    ])
)}
<div class="note"><strong>ระวัง:</strong> เลือก Operations (ต้นไม้ล่างซ้าย) ก่อนเปิด Operation &gt; New Operation &gt; New Weld Operation ถ้าเลือก Part เมนูจะเป็นสีเทา ใน Weld List ให้เลือก wp จากต้นไม้ Operations (เลือกจาก Mfgs ขึ้น Invalid Location)</div>

<h2>ขั้นที่ 7: Insert Component ปืน 15 รุ่นจาก SPOT_GUN</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-07.jpg", "ขั้นที่ 7: Insert Component ปืน 15 รุ่นจาก SPOT_GUN"),
    step_list([
        'Ctrl+คลิกเลือกปืนหลายรุ่น',
        'Open',
        '1 Modeling &gt; Insert Component &gt; Resource\\SPOT_GUN',
        'ปืนขึ้นใน Resources',
    ])
)}

<h2>ขั้นที่ 8: Weld_Op &gt; Operation Properties ตั้ง Gun แล้ว Set Current</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-08.jpg", "ขั้นที่ 8: Weld_Op &gt; Operation Properties ตั้ง Gun แล้ว Set Current"),
    step_list([
        'คลิกขวา Weld_Op &gt; Operation Properties &gt; แท็บ Process',
        'Gun คลิกช่องแล้วคลิก SPOT_GUN_MAA32963S ใน Objects',
        'OK',
        'คลิกขวา Weld_Op &gt; Set Current Operation (ต้องมีก่อน Gun Search)',
    ])
)}

<h2>ขั้นที่ 9: Geometric Gun Search เลือกจุดและปืน</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-09.jpg", "ขั้นที่ 9: Geometric Gun Search เลือกจุดและปืน"),
    step_list([
        'Process &gt; Geometric Gun Search &gt; Next: จุดของ Weld_Op ขึ้นเอง',
        'Select guns from Study &gt; Shift เลือกทุกปืน',
        'ปุ่ม &gt;',
        'ปืนที่จะทดสอบ',
    ])
)}

<h2>ขั้นที่ 10: ตั้งการตรวจชนแล้ว Search</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-10.jpg", "ขั้นที่ 10: ตั้งการตรวจชนแล้ว Search"),
    step_list([
        'All objects in Study (ชนกับทุกอย่าง)',
        'Gun States: Closed + Open',
        'Gun Rotation หมุนปืนหาท่า 180° / 90 สเต็ป',
        'Next &gt; Search',
    ])
)}

<h2>ขั้นที่ 11: ผล Gun Search: ปืนไหนเชื่อมได้ครบ 10 จุด</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-11.jpg", "ขั้นที่ 11: ผล Gun Search: ปืนไหนเชื่อมได้ครบ 10 จุด"),
    step_list([
        'C_GUN 0 % ชนตั้งแต่ wp',
        '100 % = เครื่องหมายถูกทุกจุด',
        'tmx_140 0 % / X_GUN 40 %',
    ])
)}

<h2>ขั้นที่ 12: Insert Fixture (MAA28354S + PALLET)</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-12.jpg", "ขั้นที่ 12: Insert Fixture (MAA28354S + PALLET)"),
    step_list([
        'Insert Component &gt; Resource\\LINE_CD เลือก MAA28354S_BASE ถึง TRANSFER',
        'Ctrl+คลิก PALLET',
        'Open',
        'Fixture ขึ้นที่พื้น (Z 0) ใต้ชิ้นงาน',
    ])
)}

<h2>ขั้นที่ 13: Placement ยก Fixture ขึ้น Z 1267 ให้รับชิ้นงาน</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-13.jpg", "ขั้นที่ 13: Placement ยก Fixture ขึ้น Z 1267 ให้รับชิ้นงาน"),
    step_list([
        'เลือกชิ้น Fixture ทั้ง 17 (Shift) &gt; Placement Manipulator &gt; แกน Z',
        'พิมพ์ 1267 Enter',
        'Close',
    ])
)}

<h2>ขั้นที่ 14: ไฟล์ 4 มี compound Gun, Fixture แล้วใส่หุ่น</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-14.jpg", "ขั้นที่ 14: ไฟล์ 4 มี compound Gun, Fixture แล้วใส่หุ่น"),
    step_list([
        'Gun frame + SPOT_GUN',
        'Fixture 17 ชิ้น',
        'Gripper / Base จากงานเต็ม (ไม่ใช้)',
        'ROBOT_MODEL\\irb6650_320',
        'Open',
    ])
)}

<h2>ขั้นที่ 15: Placement วาง S040R03 ที่ (2800, -2900, 0) Rz 90</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-15.jpg", "ขั้นที่ 15: Placement วาง S040R03 ที่ (2800, -2900, 0) Rz 90"),
    step_list([
        'Placement Manipulator &gt; ลูกศรขยาย',
        'Rz = 90 ก่อน',
        'X = 2800',
        'Y = -2900',
        'ก่อน: จุด 0 ซ้อนใน Fixture',
        'หลัง: หันเข้าหาชิ้นงาน',
    ])
)}

<h2>ขั้นที่ 16: Mount Tool ติด SPOT_GUN แล้วตั้ง Robot ให้ Weld_Op</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-16.jpg", "ขั้นที่ 16: Mount Tool ติด SPOT_GUN แล้วตั้ง Robot ให้ Weld_Op"),
    step_list([
        'S040R03 &gt; Robot &gt; Mount Tool &gt; Tool = SPOT_GUN_MAA32963S',
        'Frame = Base Frame',
        'Mount on = S040R03',
        'TOOLFRAME',
        'Apply',
        'Weld_Op &gt; Operation Properties &gt; Process &gt; Robot = S040R03',
    ])
)}

<h2>ขั้นที่ 17: Pie Chart ดูช่วงมุมที่ปืนเข้าเชื่อมได้</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-17.jpg", "ขั้นที่ 17: Pie Chart ดูช่วงมุมที่ปืนเข้าเชื่อมได้"),
    step_list([
        'แดง = หุ่นเอื้อมไม่ถึง',
        'น้ำเงิน = เข้าได้ (All OK)',
    ])
)}

<h2>ขั้นที่ 18: Automatic Approach Angle ปรับมุมทุกจุดอัตโนมัติ</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-18.jpg", "ขั้นที่ 18: Automatic Approach Angle ปรับมุมทุกจุดอัตโนมัติ"),
    step_list([
        'Robot = S040R03',
        'Tool = SPOT_GUN',
        'Optimal zone',
        'ทุกจุดได้ถูก',
        'Execute',
        'Weld Distribution Center: 30.75 วินาที',
        'Assign (10)',
    ])
)}

<h2>ขั้นที่ 19: Add Location Before ได้ via แล้วถอย Z -100</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-19.jpg", "ขั้นที่ 19: Add Location Before ได้ via แล้วถอย Z -100"),
    step_list([
        'เลือก wp (ต้นไม้ Operations) &gt; Operation &gt; Add Location Before ได้ via',
        'Robot Jog เปิดเอง: แกน Z ของ TCPF',
        'กดลูกศรถอยจน -100',
        'Close',
    ])
)}
<div class="tip"><strong>ทำซ้ำ:</strong> เลือก wp &gt; Add Location After ได้ via1 แล้วถอย -100 เหมือนกันทุกจุด จุดเชื่อมได้คู่ via ก่อน-หลัง (ไฟล์ 6 มี 32 จุด)</div>

<h2>ขั้นที่ 20: Start ที่ท่า Home แล้วเรียงให้อยู่หน้าสุด</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-20.jpg", "ขั้นที่ 20: Start ที่ท่า Home แล้วเรียงให้อยู่หน้าสุด"),
    step_list([
        'S040R03 &gt; Robot &gt; Home &gt; Add Current Location &gt; F2 = Start',
        'Path Editor: Move Up ให้ Start อยู่บนสุด',
        'ไฟล์ 5 = 30.75 วินาที',
        'เล่นได้ 47.23 วินาที',
    ])
)}

<h2>ขั้นที่ 21: Collision Set: ปืนกับชิ้นงาน + Fixture</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-21.jpg", "ขั้นที่ 21: Collision Set: ปืนกับชิ้นงาน + Fixture"),
    step_list([
        'Check = SPOT_GUN_MAA32963S',
        'With = SPOT_CD',
        'Fixture',
        'OK',
        'New Collision Set',
        'Edit Collision Set',
        'ไฟล์ 6 มี new_collision_set แล้ว',
    ])
)}

<h2>ขั้นที่ 22: Collision Mode แล้วเล่น: ไฟล์ 6 ปืนชนชิ้นงาน</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-22.jpg", "ขั้นที่ 22: Collision Mode แล้วเล่น: ไฟล์ 6 ปืนชนชิ้นงาน"),
    step_list([
        'ชิ้นที่ชนเป็นสีแดงในหน้าจอ 3D',
        'Collision: SPOT_GUN, C, SPOT_CD',
        'Home &gt; Collision Mode (สีฟ้า = เปิด)',
    ])
)}
<div class="note"><strong>ระวัง:</strong> เปิดไฟล์ใหม่แล้ว Collision Mode จะปิดเอง ต้องกดเปิดอีกครั้งก่อนเล่น ไม่งั้นรายการว่างเหมือนไม่ชน</div>

<h2>ขั้นที่ 23: เพิ่ม via หลบ: ไฟล์ 7 ไม่ชนแล้ว (62.39 วินาที)</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-23.jpg", "ขั้นที่ 23: เพิ่ม via หลบ: ไฟล์ 7 ไม่ชนแล้ว (62.39 วินาที)"),
    step_list([
        'No pairs to display = ไม่มีคู่ที่ชน',
        'ไฟล์ 7 เพิ่ม via20-via31 (47 จุด) ระหว่างจุดที่ชน',
        'Weld_Op 62.39 วินาที',
    ])
)}

<h2>ขั้นที่ 24: Mirror Operation ได้หุ่นและงานอีกฝั่ง</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-24.jpg", "ขั้นที่ 24: Mirror Operation ได้หุ่นและงานอีกฝั่ง"),
    step_list([
        'เลือก Weld_Op &gt; Operation &gt; Mirror',
        'Weld_Op_mirrored',
        'Apply',
        'ระนาบกระจก (แกน XZ)',
        'ได้ Weld_Op_mirrored',
    ])
)}

<h2>ขั้นที่ 25: Compound Operation: หุ่น 2 ตัวเชื่อมพร้อมกัน 62.53 วินาที</h2>
{side_by_side(
    screenshot("assets/images/lessons/05-25.jpg", "ขั้นที่ 25: Compound Operation: หุ่น 2 ตัวเชื่อมพร้อมกัน 62.53 วินาที"),
    step_list([
        'CompOp = Weld_Op + Weld_Op_mirrored (ไม่ Link)',
        'จบ 62.53 เท่าตัวที่นานสุด',
    ])
)}
<div class="tip"><strong>สรุป:</strong> New Compound Operation &gt; ลาก Weld_Op และ Weld_Op_mirrored เข้า &gt; Set Current Operation &gt; เล่น สองงานไม่ได้ Link กัน จึงทำพร้อมกัน เวลาไม่บวกกัน</div>

<h2>ไฟล์ในบทเรียนและสิ่งที่อยู่ในแต่ละไฟล์</h2>
<table>
<tr><th>ไฟล์</th><th>สิ่งที่มี</th><th>Weld_Op</th></tr>
<tr><td>1_Weld_Point.psz</td><td>PartC, PartD, SPOT_CD (ยังไม่มีจุดเชื่อม)</td><td>-</td></tr>
<tr><td>2_Weld_Gun.psz</td><td>+ จุดเชื่อม 10 จุด + Weld_Op</td><td>20.00</td></tr>
<tr><td>3_Fixture.psz</td><td>+ ปืน 15 รุ่น · Gun = SPOT_GUN_MAA32963S</td><td>30.75</td></tr>
<tr><td>4_Robot.psz</td><td>+ compound Gun / Fixture / Gripper / Base</td><td>30.75</td></tr>
<tr><td>5_WDC.psz</td><td>+ S040R03 ติดปืน · มุมจุดปรับแล้ว</td><td>30.75</td></tr>
<tr><td>6_Approach_Aeparture_Angle.psz</td><td>+ Start / via ก่อน-หลัง (32 จุด)</td><td>46.50</td></tr>
<tr><td>7_Collision_Check.psz</td><td>+ via หลบชน (47 จุด)</td><td>62.40</td></tr>
<tr><td>8_Mirror_Operation.psz</td><td>+ หุ่น/งาน mirrored + CompOp</td><td>62.53</td></tr>
</table>

<h2>เช็กลิสต์: ผู้เรียนทำได้ครบหรือยัง</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th><th>ตรวจด้วย</th></tr>
<tr><td>1</td><td>Preserve จุด, Create Weld Points, Project</td><td>จุดมีลูกศรทิศบนผิว PartC</td></tr>
<tr><td>2</td><td>New Weld Operation</td><td>Weld_Op มี 10 จุด</td></tr>
<tr><td>3</td><td>Gun Search และอ่านผล</td><td>บอกได้ว่าปืนไหน 100 %</td></tr>
<tr><td>4</td><td>Insert Fixture / Robot + Placement + Mount Tool</td><td>ปืนติดหุ่น S040R03</td></tr>
<tr><td>5</td><td>Pie Chart / Automatic Approach Angle</td><td>ทุกจุดเป็นเครื่องหมายถูก</td></tr>
<tr><td>6</td><td>via ก่อน-หลัง + Start</td><td>เล่น Weld_Op ได้ครบ</td></tr>
<tr><td>7</td><td>Collision Set + Collision Mode</td><td>No pairs to display</td></tr>
<tr><td>8</td><td>Mirror + Compound</td><td>หุ่น 2 ตัวเชื่อมพร้อมกัน</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>Set as Preserved Objects สีเทา</td><td>Set Modeling Scope ที่ SPOT_CD ก่อนและเลือกจุดแต่ละตัว (ไม่ใช่ Weld_10p)</td></tr>
<tr><td>Projection on exact part geometry failed</td><td>ตอบ Yes ให้ฉายแบบประมาณ</td></tr>
<tr><td>New Weld Operation สีเทา</td><td>เลือก Operations ในต้นไม้ล่างซ้ายก่อน</td></tr>
<tr><td>Weld List ขึ้น Invalid Location</td><td>เลือก wp จากต้นไม้ Operations ไม่ใช่ Mfgs</td></tr>
<tr><td>Gun Search ไม่มีจุดให้เลือก</td><td>ตั้ง Gun แล้ว Set Current Operation ก่อน</td></tr>
<tr><td>Robot Jog พิมพ์ค่าแล้วไม่ขยับ</td><td>กดลูกศรตาม Step Size แทน</td></tr>
<tr><td>เล่นแล้วไม่มีผลการชน</td><td>เปิด Collision Mode ใหม่ทุกครั้งที่เปิดไฟล์</td></tr>
<tr><td>Mirror เตือน Missing the assigned robot</td><td>กด OK แล้วใส่หุ่นตัวที่ 2 ให้ Weld_Op_mirrored</td></tr>
</table>
'''
