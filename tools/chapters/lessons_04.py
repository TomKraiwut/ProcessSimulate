# -*- coding: utf-8 -*-
"""Lesson 04: Robot and Gripper -- from the Training/Basic step-by-step deck (Process Simulate 2502)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "สร้างกลไกของ CNC และ Gripper ด้วย Kinematics Editor, Joint Dependency และ Pose (OPEN / CLOSE)",
    "ใส่หุ่น HP20D ด้วย Insert Component, Placement แล้วติด Gripper ด้วย Mount Tool",
    "สร้างงานโหลดเข้า-ออก: Compound, Object Flow, Device Operation, Generic Robotic Operation และ Pick and Place",
    "ดูและแก้ Motion Type / Speed / OLP Commands ใน Path Editor และ Teach Pendant",
    "สร้าง Collision Set ตั้ง Collision Options แล้วเล่นทั้งชุด (36.27 วินาที ไม่ชน)",
]

BODY = f'''
<p class="lead" style="max-width:46em;">เซลล์ที่มีเครื่อง <strong>CNC</strong>, <strong>Gripper</strong> และหุ่น <strong>HP20D</strong> — ทำทีละขั้น รวม 29 ขั้น ตั้งแต่สร้างกลไก ใส่หุ่นและติด Gripper สั่งหุ่นหยิบชิ้นงานเข้า-ออกเครื่อง CNC ไปจนถึงตรวจชน</p>

<h2>ภาพรวม: 9 หัวข้อจากกลไกถึงตรวจชน</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Kinematics</td><td>link + joint ให้ CNC และ Gripper</td></tr>
<tr><td>02</td><td>Pose</td><td>OPEN / CLOSE ของประตูและปากจับ</td></tr>
<tr><td>03</td><td>ใส่หุ่น + Mount Tool</td><td>HP20D ที่ X 1000 Rz 180 ติด Gripper</td></tr>
<tr><td>04</td><td>Object Flow / Device Op</td><td>Bank วิ่งบนสายพาน ประตูปิด-เปิด</td></tr>
<tr><td>05</td><td>Link</td><td>เรียงลำดับใน Sequence Editor</td></tr>
<tr><td>06</td><td>Robotic Operation</td><td>RB_Load_In 9 จุด + Grip / Release</td></tr>
<tr><td>07</td><td>Pick and Place</td><td>RB_Load_Out จาก CNC ไป Work_Table</td></tr>
<tr><td>08</td><td>Path Editor</td><td>PTP / LIN, Speed, OLP Commands</td></tr>
<tr><td>09</td><td>Collision</td><td>Collision Set + Collision Mode</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate 2502 · โฟลเดอร์ <code>04_ROBOT_AND_GRIPPER</code> · <code>Library\\</code> (.cojt 7 ชิ้น) · <code>1_</code> ถึง <code>7_</code> <code>.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>กลไก</td><td>Kinematics Editor, Joint Dependency, Pose Editor</td><td>1_CNC_and_Gripper</td></tr>
<tr><td>02</td><td>Robot</td><td>Insert Component, Placement, Mount Tool</td><td>2_Insert_Robot</td></tr>
<tr><td>03</td><td>Flow</td><td>Compound, Object Flow, Device Op, Link</td><td>3_Object_Flow</td></tr>
<tr><td>04</td><td>หยิบเข้า</td><td>Generic Robotic Op, Path Editor, OLP</td><td>4_Robot_Load_In</td></tr>
<tr><td>05</td><td>หยิบออก</td><td>Pick and Place, Start / End, Link</td><td>5_Robot_Load_Out</td></tr>
<tr><td>06</td><td>ตรวจชน</td><td>Collision Set, Options, Collision Mode</td><td>6_Collision_Check</td></tr>
</table>

<p class="lead" style="max-width:46em;">เซลล์ที่มีเครื่อง <strong>CNC</strong>, <strong>Gripper</strong> และหุ่น <strong>HP20D</strong> — ทำทีละขั้น รวม 29 ขั้น ตั้งแต่สร้างกลไก ใส่หุ่นและติด Gripper สั่งหุ่นหยิบชิ้นงานเข้า-ออกเครื่อง CNC ไปจนถึงตรวจชน</p>

<h2>ภาพรวม: 9 หัวข้อจากกลไกถึงตรวจชน</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Kinematics</td><td>link + joint ให้ CNC และ Gripper</td></tr>
<tr><td>02</td><td>Pose</td><td>OPEN / CLOSE ของประตูและปากจับ</td></tr>
<tr><td>03</td><td>ใส่หุ่น + Mount Tool</td><td>HP20D ที่ X 1000 Rz 180 ติด Gripper</td></tr>
<tr><td>04</td><td>Object Flow / Device Op</td><td>Bank วิ่งบนสายพาน ประตูปิด-เปิด</td></tr>
<tr><td>05</td><td>Link</td><td>เรียงลำดับใน Sequence Editor</td></tr>
<tr><td>06</td><td>Robotic Operation</td><td>RB_Load_In 9 จุด + Grip / Release</td></tr>
<tr><td>07</td><td>Pick and Place</td><td>RB_Load_Out จาก CNC ไป Work_Table</td></tr>
<tr><td>08</td><td>Path Editor</td><td>PTP / LIN, Speed, OLP Commands</td></tr>
<tr><td>09</td><td>Collision</td><td>Collision Set + Collision Mode</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>04_ROBOT_AND_GRIPPER</code> · <code>Library\\</code> (.cojt 7 ชิ้น) · <code>1_</code> ถึง <code>7_</code> <code>.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>กลไก</td><td>Kinematics Editor, Joint Dependency, Pose Editor</td><td>1_CNC_and_Gripper</td></tr>
<tr><td>02</td><td>Robot</td><td>Insert Component, Placement, Mount Tool</td><td>2_Insert_Robot</td></tr>
<tr><td>03</td><td>Flow</td><td>Compound, Object Flow, Device Op, Link</td><td>3_Object_Flow</td></tr>
<tr><td>04</td><td>หยิบเข้า</td><td>Generic Robotic Op, Path Editor, OLP</td><td>4_Robot_Load_In</td></tr>
<tr><td>05</td><td>หยิบออก</td><td>Pick and Place, Start / End, Link</td><td>5_Robot_Load_Out</td></tr>
<tr><td>06</td><td>ตรวจชน</td><td>Collision Set, Options, Collision Mode</td><td>6_Collision_Check</td></tr>
</table>

<h2>ขั้นที่ 1: ตั้ง System Root แล้วเปิด 1_CNC_and_Gripper</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-01.jpg", "ขั้นที่ 1: ตั้ง System Root แล้วเปิด 1_CNC_and_Gripper"),
    step_list([
        'File',
        'Disconnected Study',
        'Open in Standard Mode',
        'เลือก 1_CNC_and_Gripper',
        'Open',
        'System Root บนหน้า Welcome ต้องเป็น ...\\04_ROBOT_AND_GRIPPER\\Library',
    ])
)}

<h2>ขั้นที่ 2: ไฟล์ 1 ยังไม่มีกลไก Pose Editor จึงเป็นสีเทา</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-02.jpg", "ขั้นที่ 2: ไฟล์ 1 ยังไม่มีกลไก Pose Editor จึงเป็นสีเทา"),
    step_list([
        'mGripper และ mCNC ใน Resources (ไฟล์ 1)',
        'Kinematics Editor กดได้',
        'Pose Editor สีเทา = ยังไม่มี joint ให้ตั้งท่า',
        'เป้าหมาย (ไฟล์ 2): lnk1',
        'lnk2 ต่อด้วย joint j1',
    ])
)}

<h2>ขั้นที่ 3: Set Modeling Scope ที่ mCNC แล้วดูชิ้นส่วนข้างใน</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-03.jpg", "ขั้นที่ 3: Set Modeling Scope ที่ mCNC แล้วดูชิ้นส่วนข้างใน"),
    step_list([
        'เลือก mCNC &gt; Set Modeling Scope',
        'ช่อง Scope = mCNC',
        'CNC ตัวเครื่อง',
        'DoorL ประตูซ้าย',
        'DoorR ประตูขวา',
        'คลิก DoorL ใน tree ชิ้นนั้นจะสว่างในหน้าจอ 3D',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> Modeling Scope เปิดชิ้นส่วนให้แก้ไขได้ทีละชิ้น ต้องอยู่ใน Scope ก่อน Kinematics Editor ถึงจะสร้าง link ได้</div>

<h2>ขั้นที่ 4: Kinematics Editor &gt; Create Link ทั้ง 3 link</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-04.jpg", "ขั้นที่ 4: Kinematics Editor &gt; Create Link ทั้ง 3 link"),
    step_list([
        'Create Link (ปุ่มแรกในหน้าต่าง)',
        'Name = lnk1 (ขึ้นเอง)',
        'แถวสีเขียว Link Elements แล้วคลิก CNC ใน tree',
        'OK',
        'lnk1 = CNC',
        'lnk2 = DoorL',
        'lnk3 = DoorR',
    ])
)}
<div class="tip"><strong>ทำซ้ำ:</strong> กด Create Link อีก 2 ครั้ง ครั้งที่ 2 คลิก DoorL ครั้งที่ 3 คลิก DoorR สี link ในกราฟตรงกับสีในหน้าจอ 3D</div>

<h2>ขั้นที่ 5: ลาก lnk1 ไป lnk2 สร้าง j1 แบบ Prismatic แกน -Y</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-05.jpg", "ขั้นที่ 5: ลาก lnk1 ไป lnk2 สร้าง j1 แบบ Prismatic แกน -Y"),
    step_list([
        'กดค้างที่ lnk1 ลากไปปล่อยที่ lnk2 ได้ joint j1',
        'แกน From 0,0,0 To 0, -100, 0 (ทิศ -Y)',
        'Joint type = Prismatic (เลื่อน)',
        'Limits = No limits',
        'OK',
        'j1 lnk1 &gt; lnk2',
        'j2 lnk1 &gt; lnk3 แกน To 0, 100, 0 (ทิศ+Y)',
    ])
)}

<h2>ขั้นที่ 6: Joint Dependency ให้ j2 ขยับตาม j1</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-06.jpg", "ขั้นที่ 6: Joint Dependency ให้ j2 ขยับตาม j1"),
    step_list([
        'เลือกเส้น j2 ในกราฟ &gt; ปุ่ม Joint Dependency &gt; เลือก Joint Function',
        'ลูกศรข้าง Joint Name &gt; คลิก j1',
        'คลิกปุ่ม j1 เพื่อใส่ลงสูตร',
        'สูตรขึ้นเป็น (D(j1)) = ระยะเลื่อนของ j1',
        'Apply แล้ว Close',
    ])
)}

<h2>ขั้นที่ 7: Pose Editor ของ CNC: OPEN j1 = 400, CLOSE j1 = 0</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-07.jpg", "ขั้นที่ 7: Pose Editor ของ CNC: OPEN j1 = 400, CLOSE j1 = 0"),
    step_list([
        'Pose Editor &gt; New... &gt; พิมพ์ 400 แล้วกด Tab',
        'Pose name ลบชื่อเดิมแล้วพิมพ์ OPEN',
        'OK',
        'OPEN',
        'CLOSE = 0 (ทำซ้ำข้อ 1-3)',
        'Jump ทดสอบทีละท่า',
    ])
)}

<h2>ขั้นที่ 8: Gripper: link 2 ตัวและ j1 แบบ Prismatic แกน -X</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-08.jpg", "ขั้นที่ 8: Gripper: link 2 ตัวและ j1 แบบ Prismatic แกน -X"),
    step_list([
        'Gripper_Clamp',
        'Gripper_Base',
        'lnk1 = Gripper_Base',
        'lnk2 = Gripper_Clamp',
        'To -100, 0, 0 (ทิศ -X)',
        'Prismatic แล้ว OK',
    ])
)}

<h2>ขั้นที่ 9: Pose ของ Gripper: OPEN j1 = 20, CLOSE j1 = 0</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-09.jpg", "ขั้นที่ 9: Pose ของ Gripper: OPEN j1 = 20, CLOSE j1 = 0"),
    step_list([
        'New... &gt; 20 แล้ว Tab',
        'ชื่อ OPEN &gt; OK',
        'OPEN',
        'CLOSE = 0',
        'Jump OPEN: Clamp เลื่อนออก 20 mm',
    ])
)}

<h2>ขั้นที่ 10: End Modeling และการไม่บันทึกทับ (อธิบาย)</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-10.jpg", "ขั้นที่ 10: End Modeling และการไม่บันทึกทับ (อธิบาย)"),
    step_list([
        'End Modeling = ปิดโหมดแก้ไขของชิ้นที่อยู่ใน Scope',
        'ช่อง Scope บอกว่ากำลังแก้ชิ้นไหน',
        'เปิดไฟล์ถัดไป PS ถามว่าจะ Save ไหม: ตอบ No ไฟล์สอนไม่เปลี่ยน',
    ])
)}
<div class="tip"><strong>บทถัดไป:</strong> เปิด 2_Insert_Robot_and_Layout ซึ่งมี CNC และ Gripper ที่มีกลไกและ Pose ครบ แล้วทุกคนเริ่มบท 2 จากจุดเดียวกัน</div>

<h2>ขั้นที่ 11: Insert Component ใส่หุ่น HP20D จาก Library</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-11.jpg", "ขั้นที่ 11: Insert Component ใส่หุ่น HP20D จาก Library"),
    step_list([
        'Modeling &gt; Insert Component ไปที่ Library',
        'HP20D.cojt',
        'Preview เป็นหุ่นยนต์',
        'Open',
        'HP20D ขึ้นใน Resources (วางที่จุด 0)',
    ])
)}

<h2>ขั้นที่ 12: Placement วาง HP20D ที่ X 1000 หมุน Rz 180</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-12.jpg", "ขั้นที่ 12: Placement วาง HP20D ที่ X 1000 หมุน Rz 180"),
    step_list([
        'เลือก HP20D &gt; Placement Manipulator กดลูกศรขยาย',
        'พิมพ์ Rz = 180 ก่อน',
        'แล้ว X = 1000',
        'Close',
    ])
)}

<h2>ขั้นที่ 13: Mount Tool ติด Gripper ที่ปลายแขน HP20D</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-13.jpg", "ขั้นที่ 13: Mount Tool ติด Gripper ที่ปลายแขน HP20D"),
    step_list([
        'เลือก HP20D &gt; Robot &gt; Mount Tool แล้วคลิก Gripper ใน tree',
        'Frame ของ Gripper = Base Frame (ขึ้นเอง)',
        'Mount on = HP20D',
        'Frame = TOOLFRAME',
        'Apply แล้ว Close',
        'Gripper ย้ายไปติดหน้าแปลนหุ่น ขยับตามแขน',
    ])
)}

<h2>ขั้นที่ 14: New Compound Operation (CompOp)</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-14.jpg", "ขั้นที่ 14: New Compound Operation (CompOp)"),
    step_list([
        'แท็บ Operation ลูกศรใต้ New Operation',
        'New Compound Operation',
        'Name = CompOp',
        'Scope = Operation Root',
        'OK',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> เมนู New Operation รวมทุกชนิด: Object Flow, Device, Pick and Place, Generic Robotic ใช้ซ้ำในบท 4-5 ไฟล์ 4-7 ชื่อ compound ว่า Operation = กล่องเดียวกับ CompOp</div>

<h2>ขั้นที่ 15: New Object Flow Operation ให้ Bank (Bank_In)</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-15.jpg", "ขั้นที่ 15: New Object Flow Operation ให้ Bank (Bank_In)"),
    step_list([
        'Name = Bank_In',
        'Object = Bank (เลือก Bank ก่อนเปิดคำสั่ง)',
        'Start Point = ตำแหน่งปัจจุบัน',
        'End Point คลิกช่องเขียวแล้วคลิกปลายสายพาน',
        'Duration = 5',
        'OK',
        'ต้นสายพาน loc1 (600, 2559.8, 830)',
        'ปลายสายพาน loc (600, 759.8, 830)',
    ])
)}

<h2>ขั้นที่ 16: New Device Operation ประตู CNC (CNC_CLOSE / CNC_OPEN)</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-16.jpg", "ขั้นที่ 16: New Device Operation ประตู CNC (CNC_CLOSE / CNC_OPEN)"),
    step_list([
        'Name = CNC_CLOSE',
        'Device = CNC (เลือกก่อนเปิดคำสั่ง)',
        'From pose = OPEN',
        'To pose = CLOSE',
        'Duration = 3',
        'OK',
    ])
)}
<div class="tip"><strong>ทำซ้ำ:</strong> CNC_OPEN: From CLOSE &gt; To OPEN 3 วินาที CNC จะเป็นสีฟ้าตอนถูกเลือก ค่าเริ่มต้นของ Duration คือ 5 ต้องแก้เป็น 3</div>

<h2>ขั้นที่ 17: Set Current Operation, Link แล้วเล่นได้ 11 วินาที</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-17.jpg", "ขั้นที่ 17: Set Current Operation, Link แล้วเล่นได้ 11 วินาที"),
    step_list([
        'ก่อน: Bank_In เริ่มพร้อม CNC_CLOSE (ยังไม่ Link)',
        'หลัง: Bank_In 0-5 &gt; CLOSE 5-8 &gt; OPEN 8-11',
        'คลิกขวา CompOp &gt; Set Current Operation',
        'เลือก Bank_In แล้ว Ctrl+คลิก CNC_CLOSE &gt; ปุ่ม Link',
        'เล่นจบ 11.00 วินาที',
    ])
)}

<h2>ขั้นที่ 18: New Generic Robotic Operation (RB_Load_In)</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-18.jpg", "ขั้นที่ 18: New Generic Robotic Operation (RB_Load_In)"),
    step_list([
        'Robot = HP20D (เลือกหุ่นก่อน)',
        'Tool = Gripper (ขึ้นเอง)',
        'Scope = CompOp',
        'OK',
        '1 Name = RB_Load_In',
        'ไฟล์ 4: 9 จุด Start &gt; BeforePick &gt; Pick &gt; AfterPick &gt; via &gt; BeforePlace &gt; Place &gt; AfterPlace &gt; End',
    ])
)}

<h2>ขั้นที่ 19: เพิ่มจุดแล้ว Manipulate Location ยก Z +100</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-19.jpg", "ขั้นที่ 19: เพิ่มจุดแล้ว Manipulate Location ยก Z +100"),
    step_list([
        'Add Location Before เพิ่มจุดก่อนจุดที่เลือก',
        'Add Location After',
        'Add Current Location = ท่าหุ่นตอนนี้ (Start / End ท่า Home)',
        'Add Location By Pick คลิกจุดในหน้าจอ 3D (Pick / Place)',
        'Manipulate Location เลื่อนจุดที่เลือก',
        'แกน Z',
        'พิมพ์ 100',
        'Close',
    ])
)}

<h2>ขั้นที่ 20: Path Editor ดู Motion Type, Speed, OLP ของ RB_Load_In</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-20.jpg", "ขั้นที่ 20: Path Editor ดู Motion Type, Speed, OLP ของ RB_Load_In"),
    step_list([
        'เลือก RB_Load_In &gt; แท็บ Path Editor &gt; Add Operations to Editor',
        'ระยะเวลารวม 9.75 วินาที',
        'PTP 100 % = Start, BeforePick, via, BeforePlace, End',
        'LIN 500 mm/s = Pick, AfterPick, Place, AfterPlace',
        'OLP Commands ที่ Pick / Place (5 คำสั่ง)',
    ])
)}

<h2>ขั้นที่ 21: Teach Pendant ดู OLP Commands ที่ Pick (Grip)</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-21.jpg", "ขั้นที่ 21: Teach Pendant ดู OLP Commands ที่ Pick (Grip)"),
    step_list([
        'LIN / 500 mm/s / zone fine',
        'OLP ที่ Pick: Drive CLOSE &gt; WaitDevice CLOSE &gt; Grip',
        'Add &gt; Standard Commands เพิ่มคำสั่ง',
        'Part Handling &gt; Grip จับชิ้นงาน',
        'Release ปล่อย (ใช้ที่ Place)',
        'Tool Handling &gt; DriveDevice สั่ง Gripper ไป Pose',
        'WaitDevice รอจนถึง Pose',
    ])
)}

<h2>ขั้นที่ 22: เล่นทั้ง compound: หยิบเข้า CNC แล้วรอ 5 วินาที</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-22.jpg", "ขั้นที่ 22: เล่นทั้ง compound: หยิบเข้า CNC แล้วรอ 5 วินาที"),
    step_list([
        'Bank_In 0-5',
        'RB_Load_In ต่อจาก Bank_In',
        'CNC_CLOSE 3 วินาที',
        'เส้น Link ยาว = รอ 5 วินาทีก่อน CNC_OPEN (เวลาเครื่องทำงาน)',
        'หุ่นหยิบ Bank บนสายพาน',
        'หุ่นวาง Bank ใน CNC',
    ])
)}

<h2>ขั้นที่ 23: New Pick and Place Operation (RB_Load_Out)</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-23.jpg", "ขั้นที่ 23: New Pick and Place Operation (RB_Load_Out)"),
    step_list([
        'Name = RB_Load_Out',
        'Robot = HP20D (เลือกหุ่นก่อน)',
        'Gripper',
        'Scope = compound (คลิกในต้นไม้ Operations)',
        'ท่าหยิบ CLOSE',
        'ท่าวาง OPEN',
        'Pick จุดหยิบ',
        'Place จุดวาง',
        'ลูกศรข้างช่อง',
        'Frame by 6 values',
    ])
)}

<h2>ขั้นที่ 24: พิมพ์จุด Pick / Place แล้วกด OK</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-24.jpg", "ขั้นที่ 24: พิมพ์จุด Pick / Place แล้วกด OK"),
    step_list([
        'Pick: X -449.8 Y -0.2',
        'Z 810 มุมหมุน 0',
        'OK',
        'Place: พิมพ์ Rz 90 ก่อน',
        'แล้ว 600, -900, 860',
        'OK',
        'RB_Load_Out',
        'Scope = Operation',
        'OK (ทดสอบแล้ว PS ไม่ปิดตัว)',
    ])
)}

<h2>ขั้นที่ 25: เพิ่ม Start / End ที่ท่า Home แล้วเรียงจุด</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-25.jpg", "ขั้นที่ 25: เพิ่ม Start / End ที่ท่า Home แล้วเรียงจุด"),
    step_list([
        'OK ได้ RB_Load_Out มี pick และ place ให้อัตโนมัติ',
        'เลือก HP20D &gt; Robot &gt; Home แล้วเลือกจุดสุดท้าย &gt; Add Current Location 2 ครั้ง ตั้งชื่อ F2 = End / Start',
        'Path Editor: เลือก Start',
        'Move Up จน Start อยู่บนสุด',
    ])
)}
<div class="note"><strong>ระวัง:</strong> Add Location Before จะคัดลอกจุดที่เลือก (ไม่ใช่ท่า Home) และเปิด Robot Jog ให้เลื่อนเอง ถ้าจะได้ท่า Home ให้ใช้ Add Current Location แล้วเลื่อนลำดับใน Path Editor</div>

<h2>ขั้นที่ 26: Link ต่อจาก CNC_OPEN แล้วเล่น: Bank ไปวางบนโต๊ะ</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-26.jpg", "ขั้นที่ 26: Link ต่อจาก CNC_OPEN แล้วเล่น: Bank ไปวางบนโต๊ะ"),
    step_list([
        'CNC_OPEN เลือกก่อน',
        'Ctrl+คลิก RB_Load_Out &gt; Link',
        'จบ 33.73 วินาที',
        'หุ่นหยิบ Bank ใน CNC',
        'Bank วางบน Work_Table',
    ])
)}

<h2>ขั้นที่ 27: Collision Viewer &gt; Edit Collision Set</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-27.jpg", "ขั้นที่ 27: Collision Viewer &gt; Edit Collision Set"),
    step_list([
        'New Collision Set',
        'Edit Collision Set',
        'new_collision_set',
        'แท็บ Collision Viewer',
        'Check: HP20D, Gripper',
        'With: CNC',
        'OK',
    ])
)}

<h2>ขั้นที่ 28: Collision Options และ Collision Mode</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-28.jpg", "ขั้นที่ 28: Collision Options และ Collision Mode"),
    step_list([
        'ปุ่ม Collision Options ใน Collision Viewer &gt; หน้า Collision',
        'Check for Collision Near-Miss + ระยะ (mm) เตือนก่อนชน',
        'Stop Simulation when a Collision is Detected',
        'OK',
        'แท็บ Home &gt; Collision Mode (สีฟ้า = เปิด)',
    ])
)}

<h2>ขั้นที่ 29: เล่นทั้งชุด 36.27 วินาที ผล: ไม่ชน</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-29.jpg", "ขั้นที่ 29: เล่นทั้งชุด 36.27 วินาที ผล: ไม่ชน"),
    step_list([
        'No pairs to display = ไม่มีคู่ที่ชน',
        'หุ่นเข้า-ออก CNC ไม่เฉียดประตู',
        'จบ 36.27 วินาที',
        'RB_Load_Out 9 จุด 10.52 วินาที (เพิ่ม Before / After / via จากขั้น 19)',
    ])
)}

<h2>ไฟล์ในบทเรียนและสิ่งที่อยู่ในแต่ละไฟล์</h2>
<table>
<tr><th>ไฟล์ (เปิดตอนเริ่มบท)</th><th>สิ่งที่มี</th><th>เวลา compound</th></tr>
<tr><td>1_CNC_and_Gripper.psz</td><td>mCNC, mGripper, Bank (ยังไม่มีกลไก)</td><td>-</td></tr>
<tr><td>2_Insert_Robot_and_Layout.psz</td><td>CNC / Gripper มี Pose + Conveyer, Work_Table, FG</td><td>-</td></tr>
<tr><td>3_Object_Flow_and_Device_Operation.psz</td><td>+ HP20D, CompOp: Bank_In, CNC_CLOSE, CNC_OPEN</td><td>6.00 (11.00 หลัง Link)</td></tr>
<tr><td>4_Robot_Load_In.psz</td><td>+ RB_Load_In 9 จุด (compound ชื่อ Operation)</td><td>25.75</td></tr>
<tr><td>5_Robot_Load_Out.psz</td><td>เหมือนผลบท 4 ยังไม่มี RB_Load_Out (ไฟล์เริ่ม)</td><td>25.75</td></tr>
<tr><td>6_Collision_Check.psz</td><td>+ RB_Load_Out 9 จุด + new_collision_set</td><td>36.27</td></tr>
<tr><td>7_Completed_Backup.psz</td><td>เฉลยงานครบเหมือนไฟล์ 6</td><td>36.27</td></tr>
</table>

<h2>เช็กลิสต์: ผู้เรียนทำได้ครบหรือยัง</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th><th>ตรวจด้วย</th></tr>
<tr><td>1</td><td>สร้าง link / joint แบบ Prismatic + Joint Dependency</td><td>ประตู 2 บานเปิดพร้อมกัน</td></tr>
<tr><td>2</td><td>สร้าง Pose OPEN / CLOSE แล้ว Jump</td><td>CNC 400 / 0, Gripper 20 / 0</td></tr>
<tr><td>3</td><td>Insert Component + Placement + Mount Tool</td><td>Gripper ติดปลายแขน HP20D</td></tr>
<tr><td>4</td><td>Object Flow, Device Operation, Link</td><td>เล่นจบ 11.00 วินาที</td></tr>
<tr><td>5</td><td>Generic Robotic Op + จุด + OLP Grip / Release</td><td>Bank ไปอยู่ใน CNC</td></tr>
<tr><td>6</td><td>Pick and Place + Start / End</td><td>Bank ไปอยู่บน Work_Table</td></tr>
<tr><td>7</td><td>อ่าน Path Editor: PTP / LIN, Speed</td><td>บอกได้ว่าจุดไหนใช้ LIN</td></tr>
<tr><td>8</td><td>Collision Set + Collision Mode</td><td>No pairs to display</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>Pose Editor สีเทา</td><td>ชิ้นนั้นยังไม่มี joint: Set Modeling Scope แล้วสร้าง link / joint ก่อน</td></tr>
<tr><td>พิมพ์ค่า j1 แล้วกด Enter ได้ท่า pos1</td><td>ใช้ Tab แทน Enter แล้วตั้งชื่อ ถ้าได้ pos1 แล้วใช้ Edit... เปลี่ยนชื่อ</td></tr>
<tr><td>ชื่อ Pose ต่อท้ายกัน (pos1OPEN)</td><td>ในช่อง Pose name กด End แล้ว Shift+Home, Delete ก่อนพิมพ์</td></tr>
<tr><td>Joint Dependency สูตรผิด (cos)</td><td>กด C ล้างสูตร เปิดรายการ Joint Name เลือก j1 แล้วกดปุ่ม j1</td></tr>
<tr><td>เวลาเล่นมากกว่าในไฟล์</td><td>หุ่นไม่ได้อยู่ท่า Home: Robot &gt; Home แล้ว Jump Simulation to Start</td></tr>
<tr><td>Add Location Before ไม่ได้ท่า Home</td><td>ใช้ Add Current Location แล้ว Move Up ใน Path Editor</td></tr>
<tr><td>ไดอะล็อก Open มีรายการเด้งทับ</td><td>คลิกชื่อไฟล์ในรายการอีกครั้งแล้วกด Open</td></tr>
<tr><td>ปิดไฟล์แล้วถาม Save</td><td>No = ไม่เก็บสิ่งที่ลอง ถ้าจะเก็บใช้ Save As ชื่อใหม่</td></tr>
</table>
'''
