# -*- coding: utf-8 -*-
"""Lesson 03: Basic Process -- from 03_BASIC_PROCESS/BASIC_PROCESS_StepByStep.pdf (Process Simulate)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "จัดวางชิ้นส่วนในเซลล์ด้วย Placement Manipulator และ Relocate แล้วติด Gripper เข้ากับหุ่นยนต์ด้วย Mount Tool",
    "สร้าง Operation (Compound, Object Flow, Pick and Place) ตั้ง Current Operation และเล่น simulation",
    "ตรวจ Reach Test ปรับ Motion Type/Speed ใน Path Editor แล้วเทียบเวลา และตรวจ Collision",
    "ต่อลำดับงานด้วย Link อ่าน cycle time จาก Gantt และสั่งรถยกด้วย Device Operation + Attach Event",
    "ส่งงานด้วย Movie Recorder (.mp4) และ Export to Web (.html)",
]

BODY = f'''
<p class="lead" style="max-width:46em;">เซลล์ตัวอย่างที่มี Machine สายพาน หุ่น UR20 พาเลท และรถยก — ทำทีละขั้นรวม 28 ขั้น ตั้งแต่จัดวาง ติดเครื่องมือ
สร้างงานหยิบ-วาง ตรวจเอื้อมถึงและตรวจชน ไปจนถึงต่อลำดับ 2 กล่อง อ่าน cycle time <strong>14.17 วินาที</strong> สั่งรถยก และส่งงาน</p>

<h2>ภาพรวม: 9 หัวข้อ</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Placement / Relocate</td><td>วาง Pallet, Box, UR20 เข้าที่</td></tr>
<tr><td>02</td><td>Mount Tool</td><td>ติด Vacuum_Gripper เข้า UR20</td></tr>
<tr><td>03</td><td>Object Flow</td><td>Box_Op เลื่อนกล่องบนสายพาน</td></tr>
<tr><td>04</td><td>Pick and Place</td><td>RB1 หุ่นหยิบกล่องวางบนพาเลท</td></tr>
<tr><td>05</td><td>Reach Test</td><td>หุ่นเอื้อมถึงทุก location ไหม</td></tr>
<tr><td>06</td><td>Path Editor</td><td>Motion Type + Speed แล้วเทียบเวลา</td></tr>
<tr><td>07</td><td>Collision</td><td>หัวจับชน Machine ไหม</td></tr>
<tr><td>08</td><td>SOP / Gantt</td><td>กล่องที่ 2 และ cycle time 14.17 วินาที</td></tr>
<tr><td>09</td><td>Forklift</td><td>Device Operation + Attach Event</td></tr>
</table>

<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>03_BASIC_PROCESS</code> ที่มี <code>Library\\</code> (ไฟล์ <code>.cojt</code> 7 ชิ้น)
และไฟล์ <code>0_</code> ถึง <code>3_Basic_Process</code> <code>.psz</code>
</div>

<h2>Workflow: 5 ช่วง 4 ไฟล์</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>Layout</td><td>Placement, Relocate, Mount Tool</td><td><code>0_Layout</code></td></tr>
<tr><td>02</td><td>Operation</td><td>Object Flow, Pick and Place, Reach, Path Editor, Collision</td><td><code>1_Operation</code></td></tr>
<tr><td>03</td><td>SOP</td><td>กล่องที่ 2 + อ่าน cycle time จาก Gantt</td><td><code>2_SOP</code></td></tr>
<tr><td>04</td><td>Forklift</td><td>Pose, Device Operation, Attach Event</td><td><code>3_Forklift</code></td></tr>
<tr><td>05</td><td>ส่งงาน</td><td>Movie Recorder และ Export to Web</td><td>ทุกไฟล์</td></tr>
</table>
<h2>ขั้นที่ 1: ตั้ง System Root แล้วเปิด 0_Basic_Process_Layout</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-01.jpg", "ขั้นที่ 1: ตั้ง System Root แล้วเปิด 0_Basic_Process_Layout"),
    step_list([
        'File',
        'Disconnected Study',
        'Open in Standard Mode',
        'เลือก 0_Basic_Process_Layout',
        'Open',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> System Root บนหน้า Welcome ต้องเป็น <code>...\\03_BASIC_PROCESS\\Library</code> ก่อนเปิดไฟล์ ไม่เช่นนั้นชิ้นส่วนจะไม่ขึ้น</div>

<h2>ขั้นที่ 2: เป้าหมายจัดของในเซลล์ให้เข้าที่</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-02.jpg", "ขั้นที่ 2: เป้าหมายจัดของในเซลล์ให้เข้าที่"),
    step_list([
        'Machine วางไว้แล้วที่ x -3400',
        'Pallet, UR20, Box ซ้อนกันที่จุด 0',
        'Pallet y -1200 (ขั้น 3)',
        'UR20 ขึ้นขาตั้ง z 750 (ขั้น 5)',
        'Box ปลายสายพาน (ขั้น 4)',
    ])
)}
<p><strong>ก่อน:</strong> ไฟล์ 0 &nbsp;·&nbsp; <strong>หลัง:</strong> เท่ากับไฟล์ 1 (รูปซ้าย = ก่อน, รูปขวา = หลัง)</p>

<h2>ขั้นที่ 3: Placement Manipulator เลื่อน Pallet ไป Y -1200</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-03.jpg", "ขั้นที่ 3: Placement Manipulator เลื่อน Pallet ไป Y -1200"),
    step_list([
        'เลือก Pallet แล้วกด Placement Manipulator เลือกแกน Y',
        'พิมพ์ -1200 กด Enter',
        'Close',
        'Pallet เลื่อนออกมาข้างหุ่น',
        'ป้ายบอก Y: -1200.00',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ช่องตัวเลขคือระยะที่เลื่อนจากตำแหน่งเดิม (ไม่ใช่ตำแหน่งสุดท้าย) ลากลูกศรในหน้าจอ 3D ก็ได้ แต่พิมพ์ตัวเลขจะได้ค่าตรงกับไฟล์เฉลย</div>

<h2>ขั้นที่ 4: Placement พิมพ์ตำแหน่ง X Y Z ให้ Box</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-04.jpg", "ขั้นที่ 4: Placement พิมพ์ตำแหน่ง X Y Z ให้ Box"),
    step_list([
        'เลือก Box เปิด Placement Manipulator แล้วกดลูกศรล่างซ้ายเพื่อขยาย',
        'แถวบน = ตำแหน่ง: X = -5400',
        'Z = 800',
        'แถวล่าง = มุมหมุน Rx Ry Rz (ไม่เปลี่ยน)',
        'Close',
        'Box อยู่ปลายสายพานของ Machine',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> ถ้าต้องหมุนด้วย ให้พิมพ์มุมหมุน (แถวล่าง) ก่อน แล้วค่อยพิมพ์ตำแหน่ง (เหมือนการวางรถยกในขั้นที่ 21)</div>

<h2>ขั้นที่ 5: Relocate ยก UR20 ขึ้นขาตั้งด้วย Frame by 6 values</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-05.jpg", "ขั้นที่ 5: Relocate ยก UR20 ขึ้นขาตั้งด้วย Frame by 6 values"),
    step_list([
        'เลือก UR20 กด Relocate From frame = Self',
        'To frame กดลูกศรข้างช่อง',
        'Frame by 6 values',
        'พิมพ์ Z = 750 (0, 0, 750)',
        'OK',
        'Apply แล้ว Close',
        'UR20 อยู่บนขาตั้ง',
    ])
)}

<h2>ขั้นที่ 6: Mount Tool ติด Vacuum_Gripper เข้ากับ UR20</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-06.jpg", "ขั้นที่ 6: Mount Tool ติด Vacuum_Gripper เข้ากับ UR20"),
    step_list([
        'เลือก UR20 &gt; แท็บ Robot &gt; Mount Tool แล้วคลิก Vacuum_Gripper ใน Objects',
        'Frame ของกริปเปอร์ = Base Frame (ขึ้นเอง)',
        'Mount on = UR20',
        'Frame ของหุ่น = TOOLFRAME',
        'Apply แล้ว Close',
        'กริปเปอร์ติดที่ปลายแขนหุ่นและจะเคลื่อนตามแขน',
    ])
)}

<h2>ขั้นที่ 7: ก่อนปิดหรือเปิดไฟล์ถัดไป ตอบ No (หรือ Save As)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-07.jpg", "ขั้นที่ 7: ก่อนปิดหรือเปิดไฟล์ถัดไป ตอบ No (หรือ Save As)"),
    step_list([
        'ตอบ No = ไม่เก็บสิ่งที่ลอง ไฟล์ตัวอย่างไม่เปลี่ยน',
        'ถ้าจะเก็บงานใช้ File &gt; Disconnected Study &gt; Save As ชื่อใหม่',
    ])
)}
<div class="tip"><strong>บทถัดไป:</strong> เปิด 1_Basic_Process_Operation (เฉลยของบท 0) ทุกคนจะเริ่มบท 1 จากจุดเดียวกัน</div>

<h2>ขั้นที่ 8: New Compound Operation (กล่อง CompOp)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-08.jpg", "ขั้นที่ 8: New Compound Operation (กล่อง CompOp)"),
    step_list([
        'แท็บ Operation ลูกศรใต้ New Operation',
        'New Compound Operation',
        'Name (ไฟล์ตัวอย่าง = CompOp)',
        'Scope = Operation Root',
        'OK',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> Compound Operation คือกล่องรวม operation ย่อย ใช้ตั้งเป็น Current Operation แล้วเล่นทั้งชุด</div>

<h2>ขั้นที่ 9: New Object Flow Operation ให้ Box (Box_Op)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-09.jpg", "ขั้นที่ 9: New Object Flow Operation ให้ Box (Box_Op)"),
    step_list([
        'Name = Box_Op',
        'Object = Box (เลือก Box ก่อนเปิดคำสั่ง)',
        'Start Point = ตำแหน่งปัจจุบัน',
        'End Point คลิกช่องเขียวแล้วคลิกจุดปลายทาง',
        'Duration = 5 วินาที',
        'OK',
        'Box เลื่อนตามสายพานมาถึงหุ่น',
    ])
)}
<div class="tip"><strong>ในไฟล์ตัวอย่าง:</strong> Box_Op มี 2 จุด loc1 &gt; loc และใช้เวลา 5 วินาที (0-5 ใน Sequence Editor)</div>

<h2>ขั้นที่ 10: New Pick and Place Operation ให้ UR20 (RB1)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-10.jpg", "ขั้นที่ 10: New Pick and Place Operation ให้ UR20 (RB1)"),
    step_list([
        'Name',
        'Robot = UR20 (เลือกหุ่นก่อน)',
        'Gripper = Vacuum_Gripper',
        'ท่าหยิบ CLOSE',
        'ท่าวาง OPEN',
        'Pick คลิกจุดหยิบ (บน Box)',
        'Place คลิกจุดวาง (บน Pallet)',
        'OK',
        'ผล: RB1 มี 9 location: bPick &gt; pick &gt; aPick &gt; via &gt; bPlace &gt; place &gt; aPlace &gt; via &gt; bPick',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ภาพในบทนี้กด Cancel แล้วใช้ RB1 ที่มีอยู่ในไฟล์ (ผู้จัดทำยังไม่เคยทดสอบปุ่ม OK ของคำสั่งนี้)</div>

<h2>ขั้นที่ 11: Set Current Operation แล้วเล่นได้ 9.65 วินาที</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-11.jpg", "ขั้นที่ 11: Set Current Operation แล้วเล่นได้ 9.65 วินาที"),
    step_list([
        'เลือก CompOp &gt; Set Current Operation',
        'Box_Op 0-5 วินาที',
        'RB1 5-9.65 วินาที (4.65)',
        'จบ 9.65',
        'เริ่ม: Box ที่ปลายสายพาน',
        'จบ: Box บน Pallet',
    ])
)}
<p>แกนเวลาเริ่มที่ 0.00 วินาที และจบที่ <strong>9.65 วินาที</strong></p>

<h2>ขั้นที่ 12: Reach Test หุ่นเอื้อมถึงทุก location ไหม</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-12.jpg", "ขั้นที่ 12: Reach Test หุ่นเอื้อมถึงทุก location ไหม"),
    step_list([
        'เลือก RB1 แท็บ Robot &gt; Reach Test (Robot = UR20 ขึ้นเอง)',
        'ทุก location มีเครื่องหมายถูกสีเขียว = เอื้อมถึงครบ 9 จุด',
        'Close',
    ])
)}
<div class="tip"><strong>ทำไมย้ายมาบทนี้:</strong> Reach Test ทดสอบกับ location เท่านั้น ไฟล์ 0 ยังไม่มี operation รายการจึงว่าง ใช้ตรวจ layout ก่อนส่งงานลูกค้า ถ้าขึ้นกากบาทให้ย้ายหุ่นหรือชิ้นงานแล้วทดสอบใหม่</div>

<h2>ขั้นที่ 13: Path Editor ดู Motion Type, Speed, Zone ของ RB1</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-13.jpg", "ขั้นที่ 13: Path Editor ดู Motion Type, Speed, Zone ของ RB1"),
    step_list([
        'เลือก RB1 แท็บ Path Editor กด Add Operations to Editor',
        'ระยะเวลารวม RB1 = 4.65 วินาที',
        'Motion Type ทุกจุด = PTP (Joint)',
        'Speed = 100 %',
        'Zone = fine (หยุดตรงจุด)',
        'OLP Commands ที่ pick / place = คำสั่งจับ / ปล่อย',
    ])
)}
<div class="tip"><strong>อ่านค่า:</strong> ค่าทุกจุดเป็นค่าเริ่มต้นที่ PS สร้างให้ ขั้นถัดไปจะเปลี่ยนช่วงหยิบ-วางเป็นเส้นตรง (LIN) แล้วเทียบเวลา</div>

<h2>ขั้นที่ 14: Teach Pendant เปลี่ยน pick เป็น LIN 300 mm/s</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-14.jpg", "ขั้นที่ 14: Teach Pendant เปลี่ยน pick เป็น LIN 300 mm/s"),
    step_list([
        'เลือก pick ใน Path Editor แท็บ Robot &gt; Teach Pendant',
        'Motion Type คลิกช่องค่าให้ขึ้นรายการ',
        'กล่อง OLP Commands: Drive CLOSE, WaitDevice CLOSE, Grip TCPF',
        'เลือก LIN (Speed เปลี่ยนเป็น 1000 mm/s)',
        'Speed = 300 mm/s',
    ])
)}
<div class="tip"><strong>ทำซ้ำ:</strong> กดลูกศร &gt; (Next) บน Teach Pendant ไปที่ aPick, place, aPlace แล้วตั้ง LIN 300 mm/s เหมือนกัน · ก่อนพิมพ์ Speed ให้ลบค่าเดิมให้หมด (ถ้าไม่ลบจะได้ค่า 99999)</div>

<h2>ขั้นที่ 15: เล่นใหม่แล้วเทียบเวลาก่อน/หลัง</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-15.jpg", "ขั้นที่ 15: เล่นใหม่แล้วเทียบเวลาก่อน/หลัง"),
    step_list([
        'ก่อน 4.65',
        'หลัง 7.11',
        'แถวที่เปลี่ยนแสดง LIN / 300 mm/s',
    ])
)}
<p>รูปซ้าย = ก่อน (PTP ทุกจุด) · รูปขวา = หลัง (LIN 300 mm/s 4 จุด)</p>
<table>
<tr><th>รายการ</th><th>ก่อน</th><th>หลัง</th></tr>
<tr><td>RB1</td><td>4.65 วินาที</td><td>7.11 วินาที</td></tr>
<tr><td>pick / aPick / place / aPlace</td><td>0.31-0.40 วินาทีต่อจุด</td><td>0.97 วินาทีต่อจุด</td></tr>
<tr><td>CompOp (จบ simulation)</td><td>9.65 วินาที</td><td>12.11 วินาที</td></tr>
</table>
<div class="tip"><strong>สรุป:</strong> LIN 300 mm/s ช้ากว่า PTP 100 % แต่เดินตรงปลอดภัยกว่าตอนเข้าใกล้ชิ้นงาน ต้องเลือกให้สมดุลระหว่างเวลากับความปลอดภัย</div>

<h2>ขั้นที่ 16: Collision Viewer สร้างชุดตรวจชน</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-16.jpg", "ขั้นที่ 16: Collision Viewer สร้างชุดตรวจชน"),
    step_list([
        'New Collision Set (ปุ่มแรก)',
        'แท็บ Collision Viewer ใต้หน้าจอ',
        'Check: Vacuum_Gripper, Box',
        'With: Machine',
        'OK',
        'ได้ new_collision_set',
    ])
)}

<h2>ขั้นที่ 17: เปิด Collision Mode แล้วเล่นผล: ไม่ชน</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-17.jpg", "ขั้นที่ 17: เปิด Collision Mode แล้วเล่นผล: ไม่ชน"),
    step_list([
        'แท็บ Home &gt; Collision Mode (ปุ่มเป็นสีฟ้า = เปิด)',
        'เล่น CompOp ตลอด 12 วินาที Collision Viewer ขึ้น No pairs to display (ไม่ชน)',
        'ถ้าชน ชิ้นที่ชนจะเป็นสีแดงและขึ้นคู่ที่ชนในรายการ',
    ])
)}
<div class="tip"><strong>ใช้กับลูกค้า:</strong> ตรวจชนทุกครั้งหลังแก้ทางเดิน (เช่น เปลี่ยนเป็น LIN ในขั้น 14) เพราะทางเดินใหม่อาจเฉียดเครื่อง</div>

<h2>ขั้นที่ 18: Insert Component ใส่ Box ใบที่ 2 จาก Library</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-18.jpg", "ขั้นที่ 18: Insert Component ใส่ Box ใบที่ 2 จาก Library"),
    step_list([
        'แท็บ Modeling &gt; Insert Component ไปที่โฟลเดอร์ Library',
        'Box.cojt',
        'Preview แสดงชิ้นงาน',
        'Open',
        'Box ใหม่ขึ้นใน Parts (ไฟล์ 2 ตั้งชื่อ Box_1)',
    ])
)}

<h2>ขั้นที่ 19: ไฟล์ 2 เรียงลำดับ 4 operation ด้วย Link</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-19.jpg", "ขั้นที่ 19: ไฟล์ 2 เรียงลำดับ 4 operation ด้วย Link"),
    step_list([
        'Box_Op 0-5 วินาที',
        'RB1 5-9.72 วินาที',
        'Box_1_Op 5-10 วินาที เริ่มพร้อม RB1 (ขนานกัน)',
        'RB2 10-14.17 วินาที',
        'จบ 14.17 วินาที',
    ])
)}
<div class="tip"><strong>Link:</strong> เลือก 2 operation ใน Sequence Editor ตามลำดับ แล้วกดปุ่ม Link — ตัวที่ 2 จะเริ่มเมื่อตัวแรกจบ (ลูกศรสีดำ)</div>

<h2>ขั้นที่ 20: อ่าน cycle time ทำไมไม่ใช่ผลบวกตรงๆ</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-20.jpg", "ขั้นที่ 20: อ่าน cycle time ทำไมไม่ใช่ผลบวกตรงๆ"),
    step_list([
        '9.70: กล่องแรกวางแล้วกล่องที่ 2 มาถึงปลายสายพานพอดี',
        '14.17: กล่อง 2 ใบซ้อนบน Pallet',
    ])
)}
<table>
<tr><th>วิธีคิด</th><th>ผล</th></tr>
<tr><td>ผลบวกตรงๆ: 5 + 4.72 + 5 + 4.17</td><td>18.89 วินาที</td></tr>
<tr><td>เวลาจริงจาก Gantt</td><td><strong>14.17 วินาที</strong> (เร็วกว่า 4.72 วินาที)</td></tr>
</table>
<div class="tip"><strong>ข้อคิด:</strong> Box_1_Op วิ่งระหว่างที่หุ่นทำ RB1 (ทำงานขนานกัน) cycle time จึงสั้นกว่าผลบวก การจัดลำดับให้งานทับกันได้คือวิธีลดเวลาโดยไม่ต้องเร่งหุ่น</div>

<h2>ขั้นที่ 21: ใส่ Forklift แล้ววางที่ (3500, -1200, 0) หมุน Rz 180</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-21.jpg", "ขั้นที่ 21: ใส่ Forklift แล้ววางที่ (3500, -1200, 0) หมุน Rz 180"),
    step_list([
        'Insert Component &gt; Forklift.cojt &gt; Open',
        'Preview รถยก',
        'Placement ขยายแล้วพิมพ์ Rz = 180 ก่อน',
        'แล้ว X = 3500',
        'Y = -1200',
        'รถยกหันงาเข้าหา Pallet',
    ])
)}

<h2>ขั้นที่ 22: Object Flow ของรถยกวิ่งไปที่ Pallet (Forklift_Op)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-22.jpg", "ขั้นที่ 22: Object Flow ของรถยกวิ่งไปที่ Pallet (Forklift_Op)"),
    step_list([
        'Name = Forklift_Op',
        'Object = Forklift',
        'End Point คลิกช่องเขียวแล้วคลิก Pallet ในหน้าจอ 3D',
        'Duration 5 วินาที',
        'รถยกที่จุดเริ่ม',
        'ปลายทาง: Pallet',
    ])
)}
<div class="note"><strong>ระวัง:</strong> ถ้า Objects tree ถูกหน้าต่างบัง ให้คลิก Pallet ในหน้าจอ 3D แทน (คลิกใน tree ไม่ติด)</div>

<h2>ขั้นที่ 23: Pose Editor ของรถยก HOME และ UP (j1 = 500)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-23.jpg", "ขั้นที่ 23: Pose Editor ของรถยก HOME และ UP (j1 = 500)"),
    step_list([
        'เลือก Forklift &gt; Modeling &gt; Pose Editor: HOME, UP',
        'เลือก UP กด Jump',
        'กด New ดู Joint Jog: ท่าปัจจุบัน UP',
        'j1 = 500 mm (ยกงาขึ้น)',
        'ช่วงที่ยกได้ 0-1500',
        'งายกขึ้นในหน้าจอ 3D',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> Edit เป็นสีเทาเพราะ pose มาจาก Library (แก้ได้ใน Modeling Scope แบบบท Kinematics) ภาพนี้กด Cancel แล้ว Jump กลับ HOME</div>

<h2>ขั้นที่ 24: New Device Operation สั่งรถยกยกงา (Forklift_UP)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-24.jpg", "ขั้นที่ 24: New Device Operation สั่งรถยกยกงา (Forklift_UP)"),
    step_list([
        'Name (ไฟล์ตัวอย่าง = Forklift_UP)',
        'Device = Forklift (เลือกก่อนเปิดคำสั่ง)',
        'From pose = ท่าปัจจุบัน',
        'To pose = UP',
        'Duration = 5 วินาที',
        'OK',
        'ในไฟล์ 3: Forklift_UP ต่อจาก Forklift_Op จบที่ 24.17 วินาที',
    ])
)}

<h2>ขั้นที่ 25: Attach Event ติด Pallet + Box + Box_1 กับงารถยก (lnk2)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-25.jpg", "ขั้นที่ 25: Attach Event ติด Pallet + Box + Box_1 กับงารถยก (lnk2)"),
    step_list([
        'Pallet',
        'Box',
        'Box_1',
        'To Object = lnk2 (link ของงา: กด + หน้า Forklift ใน Objects)',
        'Start Time = 0',
        'After Start of Task',
        'Forklift มีชิ้นย่อย (lnk) ให้เลือก',
    ])
)}
<div class="tip"><strong>วิธีเปิดหน้าต่างนี้:</strong> คลิกแถบ <code>Forklift_UP</code> ใน Sequence Editor &gt; Operation &gt; New Event &gt; Attach Event
(ภาพนี้คือ Edit Event ของ event ในไฟล์เฉลย)</div>

<h2>ขั้นที่ 26: ข้อควรระวัง — ติดแค่ Pallet กล่องจะไม่ยกตาม</h2>
{screenshot("assets/images/lessons/03-26.jpg", "ขั้นที่ 26: เทียบการ Attach ที่ถูกกับที่ผิด")}
<table>
<tr><th></th><th>ติด Pallet + Box + Box_1 (ถูก)</th><th>ติดแค่ Pallet (ผิด)</th></tr>
<tr><td>ที่ 20.20 วินาที</td><td>กล่องยกขึ้นพร้อมพาเลท</td><td>พาเลทยกขึ้น แต่กล่องค้างที่ระดับเดิม</td></tr>
<tr><td>จบที่ 24.17 วินาที</td><td>กล่องอยู่บนพาเลท</td><td>กล่องจมทะลุพาเลทและหายไปใต้พาเลท</td></tr>
</table>

<h2>ขั้นที่ 27: Movie Recorder อัดวิดีโอ .mp4</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-27.jpg", "ขั้นที่ 27: Movie Recorder อัดวิดีโอ .mp4"),
    step_list([
        'แท็บ Operation &gt; Movie Recorder แล้วกดเฟือง (Settings)',
        'ปุ่มแดง = Record แล้วกด Play',
        'Stop เมื่อเล่นจบ',
        'ป้าย REC ขึ้นในหน้าจอ 3D ระหว่างอัด',
        'Destination โฟลเดอร์เก็บไฟล์',
        'Format MPEG-4 (.mp4)',
        'ความละเอียด FullHD',
        'OK',
    ])
)}

<h2>ขั้นที่ 28: Export to Web ส่งงานให้คนที่ไม่มี Process Simulate</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-28.jpg", "ขั้นที่ 28: Export to Web ส่งงานให้คนที่ไม่มี Process Simulate"),
    step_list([
        'File &gt; Import / Export &gt; Export to Web แล้วตั้ง File name .html',
        'Launch in browser เปิดไฟล์ทันทีหลังสร้าง',
        'Level of details Low = ไฟล์เล็ก',
        'ติ๊ก Include simulation',
        'Operation คลิกช่องเขียวแล้วคลิก CompOp',
        'OK',
    ])
)}
<div class="tip"><strong>ผลลัพธ์:</strong> ได้ไฟล์ HTML ไฟล์เดียว เปิดด้วย browser หมุนดูโมเดลและเล่น simulation ได้ (ตัวอย่างไฟล์จริง: <code>02_KINEMATICS\\KINEMATICS_WebView.html</code>)</div>

<h2>ไฟล์ในบทเรียนและสิ่งที่อยู่ในแต่ละไฟล์</h2>
<table>
<tr><th>ไฟล์</th><th>สถานะ layout</th><th>Operation</th></tr>
<tr><td><code>0_Basic_Process_Layout.psz</code></td><td>Machine x -3400 / Pallet, UR20, Box ที่จุด 0</td><td>ไม่มี</td></tr>
<tr><td><code>1_Basic_Process_Operation.psz</code></td><td>Pallet y -1200, UR20 z 750 + Gripper, Box (-5400, 0, 800)</td><td>CompOp: Box_Op + RB1 = 9.65 วินาที</td></tr>
<tr><td><code>2_Basic_Process_SOP.psz</code></td><td>+ Box_1 ที่ตำแหน่งเดียวกับ Box</td><td>+ Box_1_Op + RB2 = 14.17 วินาที</td></tr>
<tr><td><code>3_Basic_Process_Forklift.psz</code></td><td>+ Forklift (3500, -1200, 0, Rz 180) pose HOME / UP</td><td>+ Forklift_Op + Forklift_UP = 24.17 วินาที</td></tr>
<tr><td><code>Library\\</code></td><td colspan="2">Box, Cobot_Stand, Forklift, Machine, Pallet, Vacuum_Gripper, Robots\\UR20 — ใช้เป็น System Root</td></tr>
</table>

<h2>เช็กลิสต์: ทำได้ครบหรือยัง</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th><th>ตรวจด้วย</th></tr>
<tr><td>1</td><td>วางของด้วย Placement (แกน / พิมพ์ค่า) และ Relocate</td><td>ตำแหน่งตรงกับไฟล์ 1</td></tr>
<tr><td>2</td><td>Mount Tool</td><td>กริปเปอร์ติดปลายแขน UR20</td></tr>
<tr><td>3</td><td>สร้าง Compound, Object Flow, Pick and Place</td><td>CompOp &gt; Box_Op, RB1</td></tr>
<tr><td>4</td><td>Reach Test</td><td>ทุก location เป็นเครื่องหมายถูกสีเขียว</td></tr>
<tr><td>5</td><td>เปลี่ยน Motion Type / Speed แล้วเทียบเวลา</td><td>RB1 4.65 &rarr; 7.11 วินาที</td></tr>
<tr><td>6</td><td>สร้าง Collision Set และอ่านผล</td><td>No pairs to display</td></tr>
<tr><td>7</td><td>อ่าน cycle time จาก Gantt</td><td>อธิบายได้ว่าทำไม 14.17 ไม่ใช่ 18.89</td></tr>
<tr><td>8</td><td>Device Operation + Attach Event ให้รถยก</td><td>พาเลทและกล่องยกขึ้นพร้อมกัน</td></tr>
<tr><td>9</td><td>อัดวิดีโอ / Export to Web</td><td>ได้ไฟล์ .mp4 / .html</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>เปิด .psz แล้วชิ้นส่วนไม่ขึ้น</td><td>System Root ต้องชี้ <code>03_BASIC_PROCESS\\Library</code> แล้วเปิดไฟล์ใหม่</td></tr>
<tr><td>เมนูลูกศร To frame ปิดก่อนคลิก</td><td>กดลูกศรใหม่ แล้วคลิก Frame by 6 values ทันที</td></tr>
<tr><td>Reach Test รายการว่าง</td><td>ต้องมี operation / location ก่อน (ทดสอบในไฟล์ 1)</td></tr>
<tr><td>แก้ค่าในตาราง Path Editor ไม่ได้</td><td>เลือก location แล้วใช้ Teach Pendant</td></tr>
<tr><td>พิมพ์ Speed แล้วได้ 99999</td><td>ลบค่าเดิมในช่องให้หมดก่อนพิมพ์</td></tr>
<tr><td>End Point ของ Object Flow ไม่ขึ้น</td><td>tree ถูกหน้าต่างบัง ให้คลิกชิ้นงานในหน้าจอ 3D แทน</td></tr>
<tr><td>รถยกยกพาเลทแต่กล่องค้าง</td><td>ใส่ Box, Box_1 ใน Attach ด้วย และ To Object = lnk2</td></tr>
<tr><td>ปิดไฟล์แล้วถาม Save</td><td>No = ไม่เก็บสิ่งที่ลอง ถ้าจะเก็บใช้ Save As ชื่อใหม่</td></tr>
</table>
'''
