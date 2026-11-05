# -*- coding: utf-8 -*-
"""Lesson 01: Part Assembly -- from the Training/Basic step-by-step deck (Process Simulate 2502)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "ตั้ง System Root แล้ววางชิ้นส่วนด้วย Placement Manipulator (ลาก / พิมพ์ค่า) และ Relocate (Frame by 6 values)",
    "สร้าง Compound Operation และ Object Flow Operation แล้วเพิ่มจุดด้วย Add Location Before ใน Path Editor",
    "ต่อ operation ด้วย Link ใน Sequence Editor แล้วเล่นผลด้วย Set Current Operation (3 ชิ้น = 15 วินาที)",
    "แยกชิ้นส่วน PLC ด้วย Automatic Disassembly และใช้ Display Event ให้ชิ้นส่วนโผล่ตามลำดับประกอบ (6 ชิ้น = 30 วินาที)",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ประกอบชิ้นส่วน 2 ชุดทีละขั้น รวม 20 ขั้น — ชุด <strong>BASIC</strong> (3 ชิ้นลงบน BASE) ฝึกวางและสร้าง operation และชุด <strong>PLC</strong> (6 ชิ้น) ฝึกแยกชิ้นอัตโนมัติและแสดงลำดับประกอบ</p>

<h2>ภาพรวม: ประกอบชิ้นส่วนชุด BASIC และชุด PLC</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>System Root + เปิดไฟล์</td><td>ชี้ Library แล้วเปิด BASIC_0</td></tr>
<tr><td>02</td><td>Placement</td><td>CYLENDER ลาก X 150 / CUBOID พิมพ์ค่า</td></tr>
<tr><td>03</td><td>Relocate</td><td>TRIANGURA ไปที่ frame จาก 6 ค่า</td></tr>
<tr><td>04</td><td>Compound Operation</td><td>กล่อง CompOp รวมงานประกอบ</td></tr>
<tr><td>05</td><td>Object Flow</td><td>CYLENDER_Op จากด้านบนลงหลุม</td></tr>
<tr><td>06</td><td>Path Editor</td><td>Add Location Before เพิ่มจุด</td></tr>
<tr><td>07</td><td>เล่นผลงาน BASIC_2</td><td>3 operation ต่อกันครบ 15 วินาที</td></tr>
<tr><td>08</td><td>Disassembly</td><td>Automatic Disassembly ใน PLC_1 แยก 6 ชิ้นอัตโนมัติ</td></tr>
<tr><td>09</td><td>Display Event</td><td>PLC_2: ชิ้นส่วนโผล่ขึ้นตามลำดับ 30 วินาที</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate 2502 · โฟลเดอร์ <code>01_PART_ASSEMBLY</code> · <code>Library\\</code> (ไฟล์ชิ้นส่วน .cojt) · <code>BASIC_0 / 1 / 2 .psz</code> · <code>PLC_1 / PLC_2 .psz</code>
</div>
<h2>Workflow: 5 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>บท 0: วางชิ้นส่วน</td><td>Placement Manipulator และ Relocate วาง 3 ชิ้นเข้าที่</td><td>BASIC_0 &rarr; 1</td></tr>
<tr><td>02</td><td>บท 1: สร้าง operation</td><td>Compound, Object Flow, Path Editor, Add Location Before, Link</td><td>BASIC_1 &rarr; 2</td></tr>
<tr><td>03</td><td>บท 2: ดูผลงาน</td><td>Set Current Operation แล้วเล่นลำดับประกอบ</td><td>BASIC_2</td></tr>
<tr><td>04</td><td>บท 3: PLC แยกชิ้น</td><td>Automatic Disassembly สร้างทางเดินให้ 6 ชิ้น</td><td>PLC_1</td></tr>
<tr><td>05</td><td>บท 4: PLC ลำดับ</td><td>6 operation ต่อกัน + Display Event</td><td>PLC_2</td></tr>
</table>
<p>ตัวเลขจากไฟล์ตัวอย่าง (อ่านจาก PS 2502): ชิ้นส่วน BASIC 3 ชิ้น = <strong>15 วินาที</strong> (BASIC_2) · ชิ้นส่วน PLC 6 ชิ้น = <strong>30 วินาที</strong> (PLC_2) · operation ละ 5 วินาที (Sequence Editor)</p>

<p class="lead" style="max-width:46em;">ประกอบชิ้นส่วน 2 ชุดทีละขั้น รวม 20 ขั้น — ชุด <strong>BASIC</strong> (3 ชิ้นลงบน BASE) ฝึกวางและสร้าง operation และชุด <strong>PLC</strong> (6 ชิ้น) ฝึกแยกชิ้นอัตโนมัติและแสดงลำดับประกอบ</p>

<h2>ภาพรวม: ประกอบชิ้นส่วนชุด BASIC และชุด PLC</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>System Root + เปิดไฟล์</td><td>ชี้ Library แล้วเปิด BASIC_0</td></tr>
<tr><td>02</td><td>Placement</td><td>CYLENDER ลาก X 150 / CUBOID พิมพ์ค่า</td></tr>
<tr><td>03</td><td>Relocate</td><td>TRIANGURA ไปที่ frame จาก 6 ค่า</td></tr>
<tr><td>04</td><td>Compound Operation</td><td>กล่อง CompOp รวมงานประกอบ</td></tr>
<tr><td>05</td><td>Object Flow</td><td>CYLENDER_Op จากด้านบนลงหลุม</td></tr>
<tr><td>06</td><td>Path Editor</td><td>Add Location Before เพิ่มจุด</td></tr>
<tr><td>07</td><td>เล่นผลงาน BASIC_2</td><td>3 operation ต่อกันครบ 15 วินาที</td></tr>
<tr><td>08</td><td>Disassembly</td><td>Automatic Disassembly ใน PLC_1 แยก 6 ชิ้นอัตโนมัติ</td></tr>
<tr><td>09</td><td>Display Event</td><td>PLC_2: ชิ้นส่วนโผล่ขึ้นตามลำดับ 30 วินาที</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>01_PART_ASSEMBLY</code> · <code>Library\\</code> (ไฟล์ชิ้นส่วน .cojt) · <code>BASIC_0 / 1 / 2 .psz</code> · <code>PLC_1 / PLC_2 .psz</code>
</div>
<h2>Workflow: 5 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>บท 0: วางชิ้นส่วน</td><td>Placement Manipulator และ Relocate วาง 3 ชิ้นเข้าที่</td><td>BASIC_0 &rarr; 1</td></tr>
<tr><td>02</td><td>บท 1: สร้าง operation</td><td>Compound, Object Flow, Path Editor, Add Location Before, Link</td><td>BASIC_1 &rarr; 2</td></tr>
<tr><td>03</td><td>บท 2: ดูผลงาน</td><td>Set Current Operation แล้วเล่นลำดับประกอบ</td><td>BASIC_2</td></tr>
<tr><td>04</td><td>บท 3: PLC แยกชิ้น</td><td>Automatic Disassembly สร้างทางเดินให้ 6 ชิ้น</td><td>PLC_1</td></tr>
<tr><td>05</td><td>บท 4: PLC ลำดับ</td><td>6 operation ต่อกัน + Display Event</td><td>PLC_2</td></tr>
</table>
<p>ตัวเลขจากไฟล์ตัวอย่าง (อ่านจากไฟล์ตัวอย่าง): ชิ้นส่วน BASIC 3 ชิ้น = <strong>15 วินาที</strong> (BASIC_2) · ชิ้นส่วน PLC 6 ชิ้น = <strong>30 วินาที</strong> (PLC_2) · operation ละ 5 วินาที (Sequence Editor)</p>

<h2>ขั้นที่ 1: ตั้ง System Root ให้ชี้ไปที่โฟลเดอร์ Library</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-01.jpg", "ขั้นที่ 1: ตั้ง System Root ให้ชี้ไปที่โฟลเดอร์ Library"),
    step_list([
        'เมนู File เลือก Options',
        'เลือกหน้า Disconnected',
        'Client System Root กดปุ่ม... เลือกโฟลเดอร์ Library ของบทเรียน (ในภาพคือ <code>...\\01_PART_ASSEMBLY\\Library</code>)',
        'กด OK',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> ค่าใหม่มีผลตอนเปิดไฟล์ครั้งถัดไปและใช้ร่วมกับโปรแกรม Tecnomatix อื่นในเครื่อง ถ้าชี้ผิดที่ PS จะหาไฟล์ชิ้นส่วน .cojt ไม่เจอ</div>

<h2>ขั้นที่ 2: เปิดไฟล์ BASIC_0_ASSEMBLY.psz</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-02.jpg", "ขั้นที่ 2: เปิดไฟล์ BASIC_0_ASSEMBLY.psz"),
    step_list([
        'เมนู File &gt; Disconnected Study',
        'Open in Standard Mode',
        'เลือก BASIC_0_ASSEMBLY',
        'กด Open',
    ])
)}
<div class="note"><strong>ระวัง:</strong> ถ้ามีไฟล์เปิดอยู่ PS จะถามว่าจะ Save ไฟล์เดิมไหม ตอบ No ถ้าไม่ต้องการเก็บสิ่งที่ลองทำ</div>

<h2>เป้าหมายบท 0: วางชิ้นส่วน 3 ชิ้นเข้าที่บน BASE</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-03.jpg", "เป้าหมายบท 0: วางชิ้นส่วน 3 ชิ้นเข้าที่บน BASE"),
    step_list([
        'CYLENDER ใช้ Placement Manipulator (ขั้นที่ 3)',
        'CUBOID ใช้ Placement พิมพ์ตัวเลข (ขั้นที่ 4)',
        'TRIANGURA ใช้ Relocate (ขั้นที่ 5)',
    ])
)}

<h2>ขั้นที่ 3: Placement Manipulator เลื่อน CYLENDER ลงหลุม</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-04.jpg", "ขั้นที่ 3: Placement Manipulator เลื่อน CYLENDER ลงหลุม"),
    step_list([
        'เลือก CYLENDER ใน Objects แล้วกด Placement Manipulator บน toolbar ของหน้าจอ 3D',
        'เลือกแกน X',
        'พิมพ์ 150 แล้วกด Enter',
        'Frame of Reference = Self (ค่าเริ่มต้น)',
        'กด Close',
        'CYLENDER ลงหลุมพอดี',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ลากลูกศรในหน้าจอ 3D ก็เลื่อนได้ แต่พิมพ์ตัวเลขจะได้ตำแหน่งตรงกับไฟล์เฉลย</div>

<h2>ขั้นที่ 4: Placement พิมพ์ตัวเลขวาง CUBOID ลงช่องเอียง</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-05.jpg", "ขั้นที่ 4: Placement พิมพ์ตัวเลขวาง CUBOID ลงช่องเอียง"),
    step_list([
        'เลือก CUBOID เปิด Placement Manipulator แล้วกดลูกศรมุมล่างซ้ายเพื่อขยาย',
        'แถวล่าง = มุมหมุน Rx Ry Rz พิมพ์ Rx = 45 ก่อน',
        'แถวบน = ตำแหน่ง X Y Z พิมพ์ -150, 12.28, 46.20',
        'CUBOID เข้าช่องพอดี แล้วกด Close',
    ])
)}
<div class="note"><strong>ระวัง:</strong> พิมพ์มุมหมุนก่อน แล้วค่อยพิมพ์ตำแหน่ง และลบค่าเดิมในช่องให้หมดก่อนพิมพ์ (ถ้ามีเครื่องหมาย - ค้างในช่อง Z จะได้ -46.20 ต้องพิมพ์ใหม่)</div>

<h2>ขั้นที่ 5: Relocate ย้าย TRIANGURA ไปที่ frame จาก 6 ค่า</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-06.jpg", "ขั้นที่ 5: Relocate ย้าย TRIANGURA ไปที่ frame จาก 6 ค่า"),
    step_list([
        'From frame = Self',
        'To frame กดลูกศรข้างช่อง',
        'Frame by 6 values',
        'แถวล่าง Rx = 60',
        'แถวบน 0, -8.53, -170.71',
        'กด OK',
    ])
)}

<h2>ขั้นที่ 5 (ต่อ): กด Apply แล้ว TRIANGURA เข้าร่อง</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-07.jpg", "ขั้นที่ 5 (ต่อ): กด Apply แล้ว TRIANGURA เข้าร่อง"),
    step_list([
        'กด Apply',
        'กด Close',
        'TRIANGURA เข้าร่องบน BASE ครบ 3 ชิ้น',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> ถ้าจะเก็บงานใช้ File &gt; Disconnected Study &gt; Save As ชื่อใหม่ อย่าบันทึกทับไฟล์ตัวอย่าง</div>

<h2>ขั้นที่ 6: สร้าง Compound Operation ชื่อ CompOp</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-08.jpg", "ขั้นที่ 6: สร้าง Compound Operation ชื่อ CompOp"),
    step_list([
        'เปิดไฟล์ BASIC_1 แท็บ Operation กดลูกศรใต้ New Operation',
        'New Compound Operation',
        'Name = CompOp',
        'Scope = Operation Root',
        'กด OK',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> Compound Operation คือกล่องรวม operation ย่อย ใช้เป็นตัวที่ Set Current แล้วเล่นงานประกอบทั้งชุดในครั้งเดียว</div>

<h2>ขั้นที่ 7: New Object Flow Operation ให้ CYLENDER</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-09.jpg", "ขั้นที่ 7: New Object Flow Operation ให้ CYLENDER"),
    step_list([
        'เลือก CYLENDER แล้ว New Operation &gt; New Object Flow Operation',
        'Name ตั้งให้เป็น CYLENDER_Op',
        'Object = CYLENDER',
        'Scope คลิกช่องให้เป็นสีเขียวแล้วคลิก CompOp ใน Operation Tree',
        'Start Point = จุดเหนือหลุม (ขั้นที่ 8)',
        'End Point = จุดประกอบ 0, 0.02, 60',
        'กด OK',
    ])
)}

<h2>ขั้นที่ 8: Start Point เหนือหลุม 150 mm ได้ทางเดินแนวตั้ง</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-10.jpg", "ขั้นที่ 8: Start Point เหนือหลุม 150 mm ได้ทางเดินแนวตั้ง"),
    step_list([
        'Start Point ลูกศร &gt; Frame by 6 values',
        'พิมพ์ 0, 0.02, 210 แล้ว OK',
        'กด OK ที่หน้าต่าง Object Flow',
        'จุดเริ่ม: เหนือหลุม 150 mm',
        'จุดจบ: ในหลุม',
    ])
)}
<div class="note"><strong>ระวัง:</strong> ช่อง Start Point เริ่มต้นเป็น Current Location (ตำแหน่งที่ประกอบแล้ว) ถ้าไม่เปลี่ยน ชิ้นงานจะไม่ลอยขึ้นมาก่อน</div>

<h2>ขั้นที่ 9: เปิด CYLENDER_Op ใน Path Editor</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-11.jpg", "ขั้นที่ 9: เปิด CYLENDER_Op ใน Path Editor"),
    step_list([
        'เลือก CYLENDER_Op ใน Operation Tree',
        'แท็บ Path Editor กด Add Operations to Editor (ปุ่มซ้ายสุด)',
        'loc = จุดเริ่ม loc1 = จุดจบ',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> ถ้าเลือก CompOp แล้วกด Add จะเห็นทุก operation ในกล่องพร้อมกัน (ดูได้ในไฟล์ BASIC_2)</div>

<h2>ขั้นที่ 10: คลิกขวาที่ loc1 แล้ว Add Location Before</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-12.jpg", "ขั้นที่ 10: คลิกขวาที่ loc1 แล้ว Add Location Before"),
    step_list([
        'ใน Path Editor คลิกขวาที่ loc1 (จุดจบ)',
        'Add Location Before',
        'ได้ loc2 แทรกระหว่าง loc กับ loc1 ที่ตำแหน่งเดียวกับ loc1',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> หน้าต่าง Placement Manipulator ของ loc2 เปิดขึ้นเองทันที ใช้เลื่อนจุดใหม่ในขั้นถัดไป</div>

<h2>ขั้นที่ 11: ยก loc2 ขึ้น 30 mm เป็นจุดชะลอก่อนลงหลุม</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-13.jpg", "ขั้นที่ 11: ยก loc2 ขึ้น 30 mm เป็นจุดชะลอก่อนลงหลุม"),
    step_list([
        'เลือกแกน Z',
        'พิมพ์ 30 แล้วกด Enter',
        'ช่อง Z ของตำแหน่งเปลี่ยนจาก 60 เป็น 90',
        'กด Close',
        'ทางเดินเป็น 3 จุด: บน &gt; จุดชะลอ &gt; ในหลุม',
    ])
)}

<h2>ขั้นที่ 12: Set Current Operation แล้วเล่น simulation</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-14.jpg", "ขั้นที่ 12: Set Current Operation แล้วเล่น simulation"),
    step_list([
        'เลือก CompOp',
        'แท็บ Operation กด Set Current Operation',
        'Jump Simulation to Start',
        'Play Simulation Forward',
        'CYLENDER เลื่อนลง loc &gt; loc2 &gt; loc1',
    ])
)}
<div class="note"><strong>ระวัง:</strong> ถ้าขึ้น Previous simulation is not reset ให้ตอบ Yes ก่อน ไม่อย่างนั้นกด Play แล้วชิ้นงานจะค้างอยู่ที่เดิม</div>

<h2>ขั้นที่ 13: ทำซ้ำกับ CUBOID, TRIANGURA แล้ว Link ใน Sequence Editor</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-15.jpg", "ขั้นที่ 13: ทำซ้ำกับ CUBOID, TRIANGURA แล้ว Link ใน Sequence Editor"),
    step_list([
        'Object Flow ให้ CUBOID และ TRIANGURA แบบเดียวกัน (Scope = CompOp)',
        'Sequence Editor เลือก operation 2 ตัวตามลำดับแล้วกด Link',
        'ผล: ต่อกัน 0-5, 5-10, 10-15 วินาที',
    ])
)}

<h2>ขั้นที่ 14: เปิด BASIC_2 ดูลำดับประกอบครบ 15 วินาที</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-16.jpg", "ขั้นที่ 14: เปิด BASIC_2 ดูลำดับประกอบครบ 15 วินาที"),
    step_list([
        'CYLENDER 0-5 วินาที',
        'CUBOID 5-10 วินาที',
        'TRIANGURA 10-15 วินาที',
        'เวลารวม 15.00 วินาที',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> เปิดไฟล์แล้วเลือก CompOp &gt; Set Current Operation &gt; Jump to Start ก่อนกด Play ทุกครั้ง</div>

<h2>ขั้นที่ 15: เลือกชิ้นส่วน PLC 6 ชิ้นแล้วกด Automatic Disassembly</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-17.jpg", "ขั้นที่ 15: เลือกชิ้นส่วน PLC 6 ชิ้นแล้วกด Automatic Disassembly"),
    step_list([
        'เปิด PLC_1_ASSEMBLY.psz แล้วคลิก PLC_Body',
        'กด Shift ค้างแล้วคลิก PLC_PCB (เลือกครบ 6 ชิ้น)',
        'แท็บ Process กลุ่ม Assembly กด Automatic Disassembly',
    ])
)}
<div class="note"><strong>ระวัง:</strong> ถ้าเลือกแค่โฟลเดอร์ Parts ปุ่มจะยังเป็นสีเทา ต้องเลือกตัวชิ้นส่วน</div>

<h2>ขั้นที่ 16: ตั้งค่า 3 แท็บในหน้าต่าง Automatic Disassembly</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-18.jpg", "ขั้นที่ 16: ตั้งค่า 3 แท็บในหน้าต่าง Automatic Disassembly"),
    step_list([
        'Objects ติ๊กชิ้นที่จะแยก (ครบ 6)',
        'Explosion Distance = Automatic',
        'Explosion Direction = 2D Horizontal',
        'Sequence Name = Assembly',
        'Sequence Type ติ๊ก Assembly และ Disassembly',
        'Operation Linkage = Parallel',
        'กด Explode',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ทุกค่าในภาพเป็นค่าเริ่มต้นของ PS ไม่ได้เปลี่ยน</div>

<h2>ขั้นที่ 17: ผลลัพธ์ชิ้นส่วนแยกออกและได้ Assembly_out / Assembly_in</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-19.jpg", "ขั้นที่ 17: ผลลัพธ์ชิ้นส่วนแยกออกและได้ Assembly_out / Assembly_in"),
    step_list([
        'ชิ้นส่วน 6 ชิ้นถูกแยกออกไปตามแนวนอน',
        'เส้นทางพากลับเข้าตำแหน่งประกอบเดิม',
        'Assembly_out สร้างจาก Disassembly',
        'Assembly_in ทุกชิ้นเคลื่อนเข้าพร้อมกัน (Parallel) 5 วินาที',
    ])
)}

<h2>ขั้นที่ 18: เปิด PLC_2 ดูลำดับประกอบ 6 ชิ้นทีละชิ้น</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-20.jpg", "ขั้นที่ 18: เปิด PLC_2 ดูลำดับประกอบ 6 ชิ้นทีละชิ้น"),
    step_list([
        'Assembly_0_in มี 6 operation ต่อกันด้วย Link ตัวละ 5 วินาที',
        'จุดแดงที่ต้นแถบ = Event ที่ทำให้ชิ้นส่วนโผล่ขึ้นมา (ขั้นที่ 20)',
        'จบที่ 30 วินาที',
    ])
)}

<h2>ขั้นที่ 19: คลิกขวาที่แถบ operation แล้ว Display Event</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-21.jpg", "ขั้นที่ 19: คลิกขวาที่แถบ operation แล้ว Display Event"),
    step_list([
        'คลิกขวาที่แถบ PLC_PCB_in ใน Sequence Editor',
        'Display Event (Ctrl+D)',
        'คลิกชิ้นส่วนใน Objects (PLC_PCB) ให้ขึ้นในรายการ',
        'Start Time = 0',
        'After Start of Task',
        'กด OK',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> Start Time เริ่มต้นเป็นตำแหน่งที่คลิกขวาบนแถบ (ในภาพเดิมขึ้น 2.45) ตอนทำภาพกด Cancel เพราะ PLC_2 มี Event อยู่แล้ว ใช้ Blank Event (Ctrl+B) เมื่อต้องการซ่อนชิ้นส่วน</div>

<h2>ขั้นที่ 20: เล่น simulation ชิ้นส่วนโผล่ขึ้นตามลำดับ</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-22.jpg", "ขั้นที่ 20: เล่น simulation ชิ้นส่วนโผล่ขึ้นตามลำดับ"),
    step_list([
        'ช่องขาว = ชิ้นที่ยังถูกซ่อน',
        'ช่องดำ = ชิ้นที่แสดงอยู่',
    ])
)}

<h2>ไฟล์ในบทเรียนและสิ่งที่อยู่ในแต่ละไฟล์</h2>
<table>
<tr><th>ไฟล์</th><th>สถานะชิ้นส่วน</th><th>Operation</th></tr>
<tr><td>BASIC_0_ASSEMBLY.psz</td><td>ชิ้นส่วน 3 ชิ้นวางแยกจาก BASE</td><td>ไม่มี</td></tr>
<tr><td>BASIC_1_ASSEMBLY_Placement.psz</td><td>3 ชิ้นเข้าที่: CYLENDER X 150, CUBOID Rx 45, TRIANGURA Rx 60</td><td>ไม่มี</td></tr>
<tr><td>BASIC_2_ASSEMBLY_Operation.psz</td><td>ชิ้นส่วนเข้าที่ + มีทางเดินประกอบ</td><td>CompOp: CYLENDER_Op, CUBOID_Op, TRIANGURA_Op ตัวละ 2 location 5 วินาที</td></tr>
<tr><td>PLC_1_ASSEMBLY.psz</td><td>PLC 6 ชิ้นประกอบอยู่</td><td>ไม่มี (ใช้ฝึก Automatic Disassembly)</td></tr>
<tr><td>PLC_2_ASSEMBLY_SOP.psz</td><td>PLC 6 ชิ้น + ทางเดินประกอบ</td><td>Assembly_in &gt; Assembly_0_in: 6 operation ตัวละ 5 วินาที + Event</td></tr>
<tr><td>Library\\</td><td>ไฟล์ชิ้นส่วน .cojt (BASE, Part1-3, PLC_*)</td><td>ใช้เป็น System Root</td></tr>
</table>

<h2>เช็กลิสต์: ผู้เรียนทำได้ครบหรือยัง</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th><th>ตรวจด้วย</th></tr>
<tr><td>1</td><td>ตั้ง System Root แล้วเปิด .psz เห็นชิ้นส่วนครบ</td><td>Objects &gt; Parts มี BASE, CUBOID, CYLENDER, TRIANGURA</td></tr>
<tr><td>2</td><td>เลื่อนชิ้นงานด้วย Placement Manipulator</td><td>CYLENDER อยู่ในหลุม</td></tr>
<tr><td>3</td><td>วางชิ้นงานด้วยการพิมพ์ตำแหน่งและมุม</td><td>CUBOID อยู่ในช่องเอียง</td></tr>
<tr><td>4</td><td>ย้ายชิ้นงานด้วย Relocate และ Frame by 6 values</td><td>TRIANGURA อยู่ในร่อง</td></tr>
<tr><td>5</td><td>สร้าง Compound และ Object Flow Operation</td><td>CompOp &gt; CYLENDER_Op มี loc, loc1</td></tr>
<tr><td>6</td><td>เพิ่มจุดด้วย Add Location Before แล้วเลื่อนจุด</td><td>Path Editor มี loc2 ระหว่าง loc กับ loc1</td></tr>
<tr><td>7</td><td>Set Current Operation แล้วเล่น simulation</td><td>ชิ้นงานเคลื่อนจากบนลงหลุม</td></tr>
<tr><td>8</td><td>แยกชิ้นส่วนด้วย Automatic Disassembly</td><td>PLC_1 มี Assembly_out และ Assembly_in</td></tr>
<tr><td>9</td><td>เพิ่ม Display Event ให้ operation</td><td>ชิ้นส่วนโผล่ขึ้นเมื่อ operation เริ่ม</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>เปิด .psz แล้วชิ้นส่วนไม่ขึ้น</td><td>ตั้ง System Root ให้ชี้โฟลเดอร์ Library แล้วเปิดไฟล์ใหม่ (ขั้นที่ 1)</td></tr>
<tr><td>พิมพ์ค่าแล้วได้เลขติดลบ/ตำแหน่งผิด</td><td>ลบค่าเดิมในช่องให้หมดก่อนพิมพ์ และพิมพ์มุมหมุนก่อนตำแหน่ง</td></tr>
<tr><td>คลิกชิ้นงานแล้วช่อง End Point ไม่ขึ้น</td><td>ชิ้นงานที่กำลังจะเคลื่อนที่ใช้เป็นจุดไม่ได้ ให้ใช้ Frame by 6 values (ขึ้นค่าจุดที่คลิกไว้)</td></tr>
<tr><td>Scope ไม่มี CompOp ให้เลือก</td><td>คลิกช่อง Scope ให้เป็นสีเขียวแล้วคลิก CompOp ใน Operation Tree</td></tr>
<tr><td>ทางเดินพุ่งผิดทิศ</td><td>จุดใช้ frame ผิด เลือก operation กด Delete &gt; Yes แล้วสร้างใหม่ (Ctrl+Z ไม่ได้ลบ operation ในการทดสอบนี้)</td></tr>
<tr><td>กด Play แล้วชิ้นงานไม่ขยับ</td><td>ตอบ Yes ที่ Previous simulation is not reset แล้ว Set Current Operation และ Jump to Start</td></tr>
<tr><td>Automatic Disassembly เป็นสีเทา</td><td>เลือกตัวชิ้นส่วน (คลิก + Shift คลิก) ไม่ใช่โฟลเดอร์ Parts</td></tr>
<tr><td>ปิดไฟล์แล้วถาม Save</td><td>No = ไม่เก็บสิ่งที่ลอง ถ้าจะเก็บใช้ Save As ชื่อใหม่ ไม่ทับไฟล์ตัวอย่าง</td></tr>
</table>
'''
