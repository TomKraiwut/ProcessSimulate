# -*- coding: utf-8 -*-
"""Lesson 09: Human Basic -- from the Training/Basic step-by-step deck (Process Simulate 2502)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "ตั้ง System Root, Convert and Insert CAD (JT) แล้วสร้างคนด้วย Create Human (Jack / Jill, Database, Quick Create)",
    "ตั้งท่าด้วย Human Posturing (Posture Library, Adjust Joint) และดู Work Zones / Vision Window",
    "สร้างงานด้วย Task Simulation Builder (TSB): Set Active, Go / Get / Put (เดินหยิบวาง 6.77 วินาที)",
    "ใช้ Position / Pose / Regrasp แล้วเทียบการวาง 3 ระดับชั้น (ล่าง 7.98 / กลาง 9.01 / บน 9.74 วินาที)",
    "วิเคราะห์ Ergonomics ด้วย RULA และ Analysis Tools ครบ 19 ตัว (RULA แขนซ้ายจากชั้นล่างไปชั้นบน 4 &rarr; 7)",
]

BODY = f'''
<p class="lead" style="max-width:46em;">จำลองคนทำงานด้วย Process Simulate Human ทีละขั้น รวม 35 ขั้น — สร้างคน (Jack / Jill) ตั้งท่า สร้างงานเดินหยิบวางด้วย TSB เทียบการวาง 3 ระดับความสูง แล้ววิเคราะห์ท่าทางด้วย RULA และ Analysis Tools</p>

<h2>ภาพรวม: จากการสร้างคนถึงการวิเคราะห์ Ergonomics</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Insert CAD</td><td>JT ใน _JT_Store เป็น .cojt</td></tr>
<tr><td>02</td><td>Create Human</td><td>Jack / Jill, ANSUR, percentile</td></tr>
<tr><td>03</td><td>Human Posturing</td><td>Posture Library, Adjust Joint</td></tr>
<tr><td>04</td><td>Work Zones / Vision</td><td>ระยะเอื้อมและมุมมองของคน</td></tr>
<tr><td>05</td><td>TSB</td><td>Task Simulation Builder, Set Active</td></tr>
<tr><td>06</td><td>Go / Get / Put</td><td>เดินหยิบวาง 6.77 วินาที</td></tr>
<tr><td>07</td><td>Position / Regrasp</td><td>ยกกล่องตั้งท่า เปลี่ยนมือจับ</td></tr>
<tr><td>08</td><td>เทียบ 3 ระดับชั้น</td><td>ล่าง 7.98 / กลาง 9.01 / บน 9.74 วินาที</td></tr>
<tr><td>09</td><td>Ergonomics</td><td>RULA + Analysis Tools ครบ 19 ตัว</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate 2502 · โฟลเดอร์ <code>09_HUMAN_BASIC</code> · Process Simulate <strong>2512</strong> (บทนี้ใช้เวอร์ชันนี้) · <code>Library\\</code> (Box, Conveyor, Rack, Jack) · <code>PSH_1</code> ถึง <code>PSH_5</code> <code>.psz</code>
</div>
<h2>Workflow: 7 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>บท 1: เปิดไฟล์ + CAD</td><td>System Root, Open, Convert and Insert CAD</td><td>PSH_1</td></tr>
<tr><td>02</td><td>บท 2: สร้างคน</td><td>Create Human, Database, Quick Create</td><td>PSH_1</td></tr>
<tr><td>03</td><td>บท 3: ท่าทาง</td><td>Posturing, Work Zones, Vision</td><td>PSH_2</td></tr>
<tr><td>04</td><td>บท 4: TSB พื้นฐาน</td><td>Set Active, Go / Get / Put, Play</td><td>PSH_1</td></tr>
<tr><td>05</td><td>บท 5: ชั้นกลาง</td><td>Position, Pose, มือแยก</td><td>PSH_3</td></tr>
<tr><td>06</td><td>บท 6: ล่าง vs บน</td><td>Regrasp, เทียบเวลา 3 ระดับ</td><td>PSH_4 / 5</td></tr>
<tr><td>07</td><td>บท 7: Ergonomics</td><td>RULA 3 ระดับ + Analysis Tools 19 ตัว</td><td>PSH_3 / 4 / 5</td></tr>
</table>

<p class="lead" style="max-width:46em;">จำลองคนทำงานด้วย Process Simulate Human ทีละขั้น รวม 35 ขั้น — สร้างคน (Jack / Jill) ตั้งท่า สร้างงานเดินหยิบวางด้วย TSB เทียบการวาง 3 ระดับความสูง แล้ววิเคราะห์ท่าทางด้วย RULA และ Analysis Tools</p>

<h2>ภาพรวม: จากการสร้างคนถึงการวิเคราะห์ Ergonomics</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Insert CAD</td><td>JT ใน _JT_Store เป็น .cojt</td></tr>
<tr><td>02</td><td>Create Human</td><td>Jack / Jill, ANSUR, percentile</td></tr>
<tr><td>03</td><td>Human Posturing</td><td>Posture Library, Adjust Joint</td></tr>
<tr><td>04</td><td>Work Zones / Vision</td><td>ระยะเอื้อมและมุมมองของคน</td></tr>
<tr><td>05</td><td>TSB</td><td>Task Simulation Builder, Set Active</td></tr>
<tr><td>06</td><td>Go / Get / Put</td><td>เดินหยิบวาง 6.77 วินาที</td></tr>
<tr><td>07</td><td>Position / Regrasp</td><td>ยกกล่องตั้งท่า เปลี่ยนมือจับ</td></tr>
<tr><td>08</td><td>เทียบ 3 ระดับชั้น</td><td>ล่าง 7.98 / กลาง 9.01 / บน 9.74 วินาที</td></tr>
<tr><td>09</td><td>Ergonomics</td><td>RULA + Analysis Tools ครบ 19 ตัว</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>09_HUMAN_BASIC</code> · <code>Library\\</code> (Box, Conveyor, Rack, Jack) · <code>PSH_1</code> ถึง <code>PSH_5</code> <code>.psz</code>
</div>
<h2>Workflow: 7 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>บท 1: เปิดไฟล์ + CAD</td><td>System Root, Open, Convert and Insert CAD</td><td>PSH_1</td></tr>
<tr><td>02</td><td>บท 2: สร้างคน</td><td>Create Human, Database, Quick Create</td><td>PSH_1</td></tr>
<tr><td>03</td><td>บท 3: ท่าทาง</td><td>Posturing, Work Zones, Vision</td><td>PSH_2</td></tr>
<tr><td>04</td><td>บท 4: TSB พื้นฐาน</td><td>Set Active, Go / Get / Put, Play</td><td>PSH_1</td></tr>
<tr><td>05</td><td>บท 5: ชั้นกลาง</td><td>Position, Pose, มือแยก</td><td>PSH_3</td></tr>
<tr><td>06</td><td>บท 6: ล่าง vs บน</td><td>Regrasp, เทียบเวลา 3 ระดับ</td><td>PSH_4 / 5</td></tr>
<tr><td>07</td><td>บท 7: Ergonomics</td><td>RULA 3 ระดับ + Analysis Tools 19 ตัว</td><td>PSH_3 / 4 / 5</td></tr>
</table>

<h2>ขั้นที่ 1: ตั้ง System Root แล้วเปิด PSH_1_Basic_Human</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-01.jpg", "ขั้นที่ 1: ตั้ง System Root แล้วเปิด PSH_1_Basic_Human"),
    step_list([
        'File',
        'Disconnected Study',
        'Open in Standard Mode',
        'PSH_1_Basic_Human',
        'Open',
    ])
)}

<h2>ขั้นที่ 2: ของใน study: Box, Conveyor, Rack และคน Jack</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-02.jpg", "ขั้นที่ 2: ของใน study: Box, Conveyor, Rack และคน Jack"),
    step_list([
        'Box (Part) ชิ้นงานที่ยก',
        'Conveyor ต้นทาง',
        'Rack ชั้นวาง 4 ชั้น',
        'Jack คน (Library\\HUMAN_MODELS)',
        'TSB_Simulation_1 งานของคน',
        'Jack ยืนหน้า Rack',
        'Box อยู่ต้น Conveyor',
    ])
)}

<h2>ขั้นที่ 3: File &gt; Import / Export &gt; Convert and Insert CAD Files</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-03.jpg", "ขั้นที่ 3: File &gt; Import / Export &gt; Convert and Insert CAD Files"),
    step_list([
        'Import / Export',
        'Convert and Insert CAD Files',
        'Add... เลือกไฟล์ JT',
        'Import (หลังตั้งค่าครบ)',
        'Close',
    ])
)}

<h2>ขั้นที่ 4: Add Box.jt แล้วดู File Import Settings</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-04.jpg", "ขั้นที่ 4: Add Box.jt แล้วดู File Import Settings"),
    step_list([
        'Look in = _JT_Store',
        'Box.jt',
        'Open',
        'Target Folder = Library',
        'Base class = Part',
        'Prototype = PmPartPrototype',
        'OK',
    ])
)}

<h2>ขั้นที่ 5: แท็บ Human &gt; Create Human</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-05.jpg", "ขั้นที่ 5: แท็บ Human &gt; Create Human"),
    step_list([
        'แท็บ Human &gt; Create Human',
        'Gender = Male / Female',
        'Database = ANSUR',
        'Height 50% = 1750 mm',
        'Weight 50% = 79 kg',
        'Create (ตอนทำภาพกด Close)',
    ])
)}

<h2>ขั้นที่ 6: Database และ Quick Create</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-06.jpg", "ขั้นที่ 6: Database และ Quick Create"),
    step_list([
        'Database เปิดรายการ',
        'มีหลายประเทศ เช่น ASIAN_INDIAN, CHINESE, JAPANESE, KOREAN',
        'ลูกศรใต้ Create Human',
        'Create Default Female',
        'Create Default Male เลือกให้ตรงกับคนงานจริง งานในไทยใช้ฐานข้อมูลเอเชียได้ ถ้าไม่มีให้ใช้ ANSUR แล้วปรับ Height / Weight เอง',
    ])
)}

<h2>ขั้นที่ 7: เปิด PSH_2: มี Jack และ Jill</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-07.jpg", "ขั้นที่ 7: เปิด PSH_2: มี Jack และ Jill"),
    step_list([
        'Jack ยืนหน้า Rack',
        'Jill ย่อตัวที่ Conveyor',
        'กรวยสีเหลือง = Vision Envelope มุมมองของคน',
        'Jack ใน Resources',
        'Jill ใน Resources',
    ])
)}

<h2>ขั้นที่ 8: เลือก Jill &gt; Human Posturing แท็บ Control</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-08.jpg", "ขั้นที่ 8: เลือก Jill &gt; Human Posturing แท็บ Control"),
    step_list([
        'เลือก Jill &gt; แท็บ Human &gt; Human Posturing &gt; แท็บ Control',
        'Posture Mode = Standing / Seated',
        'Lock ล็อกเท้าไว้กับพื้น (Left / Right foot)',
        'คลิกขวาที่ส่วนของร่างกายในรูปเพื่อเลือกส่วนที่จะขยับ',
        'Create Operation เก็บท่าเป็น operation',
        'Close',
    ])
)}

<h2>ขั้นที่ 9: Posture Library และ Adjust Joint</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-09.jpg", "ขั้นที่ 9: Posture Library และ Adjust Joint"),
    step_list([
        'Posture Library',
        'เลือกท่า เช่น Kneel one knee',
        'Apply',
        'Adjust Joint',
        'เลือกส่วน เช่น Torso',
        'Flexion = 34.02 deg (ค่าในไฟล์)',
    ])
)}

<h2>ขั้นที่ 10: Work Zones และ Vision Window</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-10.jpg", "ขั้นที่ 10: Work Zones และ Vision Window"),
    step_list([
        'Work Zones แนวตั้ง: Primary 889-1321 mm',
        'แนวนอน: Primary 305 mm',
        'ด้านข้าง: Primary 254 mm',
        'OK แสดงกล่องโซนใน 3D',
        'สีแดง = นอกโซนที่ทำงานสบาย',
        'Vision Window = Mid eye',
        'OK เปิดหน้าต่างมุมมองของคน',
    ])
)}
<div class="tip"><strong>ใช้ทำอะไร:</strong> Work Zones ตรวจว่าชิ้นงานอยู่ในระยะเอื้อมสบายไหม Vision Window เห็นภาพจากตาของคน ใช้ตรวจว่ามองเห็นจุดทำงานไหม</div>

<h2>ขั้นที่ 11: เปิด Task Simulation Builder (TSB)</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-11.jpg", "ขั้นที่ 11: เปิด Task Simulation Builder (TSB)"),
    step_list([
        'แท็บ Human &gt; Task Simulation Builder ขึ้น No Active Simulation',
        'ปุ่มงาน Go, Get, Put, Position, Pose, Regrasp ...',
        'ยังเป็นสีเทาจนกว่าจะมี simulation',
        'เมนู Simulation',
        'Create Simulation (งานใหม่)',
        'Set Active Simulation (งานที่มีแล้ว)',
        'Analysis Tools (บท 7)',
    ])
)}

<h2>ขั้นที่ 12: Set Active Simulation = TSB_Simulation_1</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-12.jpg", "ขั้นที่ 12: Set Active Simulation = TSB_Simulation_1"),
    step_list([
        'เปิดรายการเลือก TSB_Simulation_1',
        'OK',
        'หัวหน้าต่างเปลี่ยนเป็น TSB_Simulation_1 ปุ่มงานกดได้',
        'Go_to_target_Jack 0-1.58 s',
        'Get_Box_Jack 1.58-3.14 s',
        'Put_Box_Jack 3.14-6.77 s',
        'จบ 6.77 วินาที',
    ])
)}

<h2>ขั้นที่ 13: งาน Go: Jack เดินไปที่ Conveyor</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-13.jpg", "ขั้นที่ 13: งาน Go: Jack เดินไปที่ Conveyor"),
    step_list([
        'Who = Jack',
        'Where ช่องเขียว: คลิกจุดในหน้าจอ 3D',
        'Name ตั้งให้อัตโนมัติ',
        'Occurs after งานก่อนหน้า',
        'Next แล้ว Finish',
        'ตัวจับตำแหน่งปลายทางของการเดิน',
    ])
)}

<h2>ขั้นที่ 14: งาน Get (หยิบ) และ Put (วาง)</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-14.jpg", "ขั้นที่ 14: งาน Get (หยิบ) และ Put (วาง)"),
    step_list([
        'Get: Right / Left hand จุดจับแต่ละมือ',
        'หรือ Object = Box ให้หาที่จับเอง',
        'Hand(s) = Both (สองมือ)',
        'Put: Placement Manipulator ย้าย Box ไปที่วาง',
        'Close แล้ว Next',
    ])
)}

<h2>ขั้นที่ 15: เล่น simulation: Jack ยกกล่องไปวางบน Rack</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-15.jpg", "ขั้นที่ 15: เล่น simulation: Jack ยกกล่องไปวางบน Rack"),
    step_list([
        '1 Jump to start',
        'Play (แถบเล่นของ TSB)',
    ])
)}

<h2>ขั้นที่ 16: PSH_3 ชั้นกลาง: Get &gt; Position &gt; Put &gt; Pose</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-16.jpg", "ขั้นที่ 16: PSH_3 ชั้นกลาง: Get &gt; Position &gt; Put &gt; Pose"),
    step_list([
        'Get_Box_Jack 0-3.04 s',
        'Position_Box_Jack 3.04-4.60 s ยกกล่องขึ้นถือ',
        'Put_Box_Jack 4.60-8.01 s',
        'Pose_Jack 8.01-9.01 s กลับท่ายืน',
        'จบ 9.01 วินาที',
        'Human Disembodied Hand Root มือแยก (Male right / left hand) มือแยกคืออะไร มือที่ไม่ติดกับตัวคน ใช้กำหนดท่าจับชิ้นงานให้ละเอียด ไฟล์ 3-5 มีมือแยกคู่นี้ (ยังไม่ได้ลองสร้างเอง ปุ่ม Create Hands อยู่แท็บ Human)',
    ])
)}

<h2>ขั้นที่ 17: งาน Position (ยกถือ) และ Pose (ตั้งท่า)</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-17.jpg", "ขั้นที่ 17: งาน Position (ยกถือ) และ Pose (ตั้งท่า)"),
    step_list([
        'Position What = ชิ้นงานที่ถืออยู่ แล้วย้ายด้วย Placement',
        'Link to ผูกกับชิ้นอื่น (ไม่บังคับ)',
        'Pose: Set Posture ตั้งท่าที่ต้องการ',
        'Duration = 1.0 s',
    ])
)}

<h2>ขั้นที่ 18: เล่น PSH_3 แล้วหมุนกล้องไปด้านข้าง</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-18.jpg", "ขั้นที่ 18: เล่น PSH_3 แล้วหมุนกล้องไปด้านข้าง"),
    step_list([
        'ด้านข้าง: วางกล่องบนชั้นกลางพอดีระดับอก',
        'View Cube คลิก Front',
        'คลิกขอบ Front | Right ได้มุมด้านข้าง',
    ])
)}

<h2>ขั้นที่ 19: PSH_4 ชั้นล่าง: ต้องย่อตัววาง 7.98 วินาที</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-19.jpg", "ขั้นที่ 19: PSH_4 ชั้นล่าง: ต้องย่อตัววาง 7.98 วินาที"),
    step_list([
        'Get &gt; Position &gt; Put จบ 7.98 วินาที (ไม่มี Pose)',
        'Put_Box_Jack 3.39 s = Walk 1.34 + Bend and reach 1.98 + Release 0.07',
        'ตอนจบ Jack ยังย่อตัวอยู่ที่ชั้นล่าง',
    ])
)}

<h2>ขั้นที่ 20: PSH_5 ชั้นบน: เดินเพิ่มและ Regrasp 9.74 วินาที</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-20.jpg", "ขั้นที่ 20: PSH_5 ชั้นบน: เดินเพิ่มและ Regrasp 9.74 วินาที"),
    step_list([
        'Go_to_target_Jack เดินเพิ่ม 2.72 s',
        'Regrasp_Box_Jack 0.20 s เปลี่ยนท่ามือจับก่อนยกสูง',
        'จบ 9.74 วินาที ยกกล่องเหนือศีรษะ',
        'Define Regrasp Posture ตั้งท่ามือใหม่',
    ])
)}

<h2>ขั้นที่ 21: เทียบการวาง 3 ระดับความสูง</h2>
{screenshot("assets/images/lessons/09-21.jpg", "ขั้นที่ 21: เทียบการวาง 3 ระดับความสูง")}
<div class="tip"><strong>สรุป:</strong> ชั้นล่างเร็วสุดแต่ต้องย่อตัว ชั้นบนช้าสุดและต้องยกแขนสูง เวลาอย่างเดียวบอกความเสี่ยงไม่ได้ ต้องดูท่าทางด้วย RULA (บท 7)</div>

<h2>ขั้นที่ 22: Analysis Tools &gt; ติ๊ก RULA &gt; Analyze</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-22.jpg", "ขั้นที่ 22: Analysis Tools &gt; ติ๊ก RULA &gt; Analyze"),
    step_list([
        'เล่น TSB ไปจังหวะที่จะประเมิน แล้วแท็บ Human &gt; Analysis Tools',
        'Human = Jack',
        'ติ๊ก RULA (กลุ่ม Posture Analysis)',
        'Analyze (ไม่ใช่ OK) RULA คืออะไร Rapid Upper Limb Assessment ให้คะแนนท่าแขน คอ ลำตัว ขา 1-7: 1-2 ยอมรับได้ 3-4 ควรตรวจเพิ่ม 5-6 ควรแก้เร็ว 7 ต้องแก้ทันที',
    ])
)}

<h2>ขั้นที่ 23: Create Report: ข้อมูลงานแล้วกด OK</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-23.jpg", "ขั้นที่ 23: Create Report: ข้อมูลงานแล้วกด OK"),
    step_list([
        'Name ชื่อรายงาน (RULA)',
        'Snapshots: Cell view + Vision view',
        'ติ๊ก Once created, open in the Report Viewer',
        'Trunk = Standing',
        'Force Use = Intermittent',
        'OK',
    ])
)}

<h2>ขั้นที่ 24: Report Viewer: อ่านคะแนนทีละส่วน</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-24.jpg", "ขั้นที่ 24: Report Viewer: อ่านคะแนนทีละส่วน"),
    step_list([
        'รายงาน RULA ในรายการซ้าย',
        'หัวรายงาน: Jack, male, 1750 mm, 79 kg, ANSUR',
        'แขนขวา Upper Arm 131° = more than 90 ได้ 4 ขยายหน้าต่าง กดขยาย Report Viewer แล้วเลื่อนลงดูทีละขั้น (Step 1-15) และตาราง A / B / C',
    ])
)}

<h2>ขั้นที่ 25: ผล RULA 3 ระดับ: ชั้นบนเสี่ยงที่สุด</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-25.jpg", "ขั้นที่ 25: ผล RULA 3 ระดับ: ชั้นบนเสี่ยงที่สุด"),
    step_list([
        'Table C = คะแนนสุดท้ายจาก Final A กับ Final B',
        'สีแดง/ส้ม = เสี่ยงสูง สีเขียว = ยอมรับได้',
    ])
)}

<h2>ขั้นที่ 26: Analysis Tools มี 2 แบบ: Static (ท่าเดียว) และ Dynamic (ทั้งงาน)</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-26.jpg", "ขั้นที่ 26: Analysis Tools มี 2 แบบ: Static (ท่าเดียว) และ Dynamic (ทั้งงาน)"),
    step_list([
        '',
        '1 ช่อง Simulation ว่าง = Static ประเมินท่าที่หยุดอยู่ (เช่น วางกล่อง 9.74 s)',
        'คลิกช่อง Simulation แล้วคลิก TSB_Simulation_1 ใน Operations tree = Dynamic ประเมินตลอดงาน',
    ])
)}

<h2>ขั้นที่ 27: Dynamic: ติ๊กทุกตัว &gt; Analyze แล้วตอบหน้าต่างทีละตัว</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-27.jpg", "ขั้นที่ 27: Dynamic: ติ๊กทุกตัว &gt; Analyze แล้วตอบหน้าต่างทีละตัว"),
    step_list([
        'ติ๊ก 14 ตัว &gt; Analyze',
        'หน้าต่างตั้งค่า เช่น NIOSH Details (กะ ≤ 8 ชม., ยก 1 ครั้ง/นาที) &gt; OK',
        'Create Report ของแต่ละตัว &gt; OK (ติ๊ก Once created, open in the Report Viewer)',
        'บางตัวถาม Save (EAWS .eaws3, Ergonomic Metrics .csv) หรือเปิด Excel',
    ])
)}

<h2>ขั้นที่ 28: Posture: OWAS และ Posture Monitor</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-28.jpg", "ขั้นที่ 28: Posture: OWAS และ Posture Monitor"),
    step_list([
        'Action Category 3 (ส้ม) ตอนวางชั้นบน 8.93 s',
        'Category 2 (เหลือง) ตอนก้มหยิบและยืดตัว',
        'Posture Monitor มุมข้อต่อระหว่างเล่น เขียว = ไม่เกินเกณฑ์',
    ])
)}

<h2>ขั้นที่ 29: Ergonomic Metrics: % ของรอบงานในแต่ละท่า</h2>
{screenshot("assets/images/lessons/09-29.jpg", "ขั้นที่ 29: Ergonomic Metrics: % ของรอบงานในแต่ละท่า")}

<h2>ขั้นที่ 30: Strength: Static Strength Prediction และ Force Solver</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-30.jpg", "ขั้นที่ 30: Strength: Static Strength Prediction และ Force Solver"),
    step_list([
        'Static Strength (Dynamic): ลำตัวไม่ผ่าน 3 จังหวะ ก้มหยิบ 1.36 s, Grasp 2.97 s, ยืดตัว 3.04 s',
        'Force Solver (Static 9.74 s): % Capable 96-100 % ทุกข้อต่อที่แรง 0 N',
        'L4/L5 Compression 1,318 N',
    ])
)}

<h2>ขั้นที่ 31: Hand: Strain Index ของมือขวา = 0.6</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-31.jpg", "ขั้นที่ 31: Hand: Strain Index ของมือขวา = 0.6"),
    step_list([
        'เลือกมือ Left / Right Hand',
        '1 Composite Strain Index = 0.6 (เขียว)',
        'Hours/day 8, Duty Cycle 9 %',
    ])
)}
<div class="tip"><strong>อ่านค่า:</strong> Strain Index ดูความเสี่ยงที่มือและข้อมือ งานย่อยได้ 0.1-0.2 รวมทั้งงาน 0.6 ถือว่าต่ำ Effort (%MVC) = แรงเทียบแรงสูงสุดของคน นั้นใช้ได้กับงาน TSB เท่านั้น</div>

<h2>ขั้นที่ 32: Low Back: Low Back Analysis, NIOSH, Cumulative Loading</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-32.jpg", "ขั้นที่ 32: Low Back: Low Back Analysis, NIOSH, Cumulative Loading"),
    step_list([
        'Low Back L4/L5 สูงสุด ≈ 2,050 N ที่ 2.9 s (เกณฑ์ 3,400 N)',
        'NIOSH RWL 4.1 kg ที่ชั้นบน (5.45 kg ที่ Conveyor)',
        'CBL ทั้งกะ 14.43 MNs (เกณฑ์ 22.5) ผ่าน',
    ])
)}

<h2>ขั้นที่ 33: Fatigue และ Energy Expenditure</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-33.jpg", "ขั้นที่ 33: Fatigue และ Energy Expenditure"),
    step_list([
        'Fatigue: มีเวลาพักพอ ไม่เกิดความล้าที่ข้อต่อ',
        'Energy Expenditure (TSB) 3.288 kcal/min ต่ำกว่าเกณฑ์ 5 รวม 0.534 kcal ต่อรอบ',
        'Energy (Manual): ใส่งานเอง Category / Detail / Load',
        'ยังไม่ใส่งาน: 0.861 kcal/min (ยืนอย่างเดียว)',
    ])
)}

<h2>ขั้นที่ 34: Static ที่ 9.74 s: REBA และ EAWS</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-34.jpg", "ขั้นที่ 34: Static ที่ 9.74 s: REBA และ EAWS"),
    step_list([
        'REBA ถามท่าเพิ่ม (ยกไหล่, น้ำหนักที่มือ, การจับ) &gt; OK',
        'ซ้าย 6',
        'ขวา 7 = Medium ต้องแก้ใกล้ RULA 6 / 7',
    ])
)}

<h2>ขั้นที่ 35: Timing: Timing Report, Walk Analysis และ MTMmotion</h2>
{side_by_side(
    screenshot("assets/images/lessons/09-35.jpg", "ขั้นที่ 35: Timing: Timing Report, Walk Analysis และ MTMmotion"),
    step_list([
        'Timing Report แยกเวลาเป็นรหัส MTM-1 (W4FT = เดิน, B = ก้มตัว, G1A = จับ)',
        'MTMmotion (Beta) &gt; Results &gt; Generate Analysis',
        'MTMmotion ได้ 6.48 s (UAS) เทียบ TSB 9.74 s ภาพซ้าย = Walk Analysis เส้นทางเดิน',
    ])
)}

<h2>สรุป: Analysis Tools 19 ตัวใช้ตอบคำถามอะไร (Jack วางชั้นบน)</h2>
{screenshot("assets/images/lessons/09-36.jpg", "สรุป: Analysis Tools 19 ตัวใช้ตอบคำถามอะไร (Jack วางชั้นบน)")}

<h2>เครื่องมือวิเคราะห์ทั้งหมด (1/2): Posture และ Strength</h2>
<table>
<tr><th>เครื่องมือ (S = Static, D = Dynamic)</th><th>คืออะไร</th><th>ใช้เพื่ออะไร</th></tr>
<tr><td>Posture Monitor (S, D)</td><td>ตารางมุมข้อต่อแบบสดเทียบกับเกณฑ์มุม</td><td>ดูขณะเล่นว่าข้อต่อไหนงอหรือบิดเกิน</td></tr>
<tr><td>Ergonomic Metrics (D)</td><td>รายงานรวม: % ของรอบในแต่ละท่า เดิน ยืน เอื้อม ระยะมือ</td><td>ดูว่าท่าไม่ดีเกิดนานแค่ไหนในหนึ่งรอบ</td></tr>
<tr><td>OWAS (S, D)</td><td>ให้รหัสท่าหลัง/แขน/ขา/น้ำหนักแล้วจัดเป็น Action Category 1-4</td><td>จัดลำดับท่าทั้งตัวที่ต้องแก้ก่อน</td></tr>
<tr><td>REBA (S)</td><td>Rapid Entire Body Assessment คะแนนทั้งตัว 1-15</td><td>ประเมินความเสี่ยงกล้ามเนื้อและกระดูกของท่าหนึ่ง</td></tr>
<tr><td>RULA (S)</td><td>Rapid Upper Limb Assessment คะแนน 1-7 เน้นแขน คอ ลำตัว</td><td>ตัดสินว่างานแขนและไหล่ต้องปรับหรือไม่</td></tr>
<tr><td>Static Strength Prediction (S, D)</td><td>% ของคนในฐานข้อมูลที่มีแรงพอ แยกทีละข้อต่อ</td><td>ตรวจว่าคนส่วนใหญ่ทำงานนี้ไหว</td></tr>
<tr><td>Force Solver (S)</td><td>เพิ่มแรงที่มือทีละขั้นจนคนรับไม่ไหว</td><td>หาน้ำหนักหรือแรงสูงสุดที่ท่านั้นรับได้</td></tr>
<tr><td>Arm Strength Evaluation (S)</td><td>แรงสูงสุดที่แขนออกได้ขณะถือของ (ต้องใส่น้ำหนักที่มือ)</td><td>ตรวจงานดัน ดึง ถือเครื่องมือ</td></tr>
</table>

<h2>เครื่องมือวิเคราะห์ทั้งหมด (2/2): Hand, Low Back, Fatigue, Timing</h2>
<table>
<tr><th>เครื่องมือ (S = Static, D = Dynamic)</th><th>คืออะไร</th><th>ใช้เพื่ออะไร</th></tr>
<tr><td>Strain Index (D, TSB)</td><td>ดัชนีความเสี่ยงมือและข้อมือจากแรง เวลา ความถี่ ท่าข้อมือ</td><td>งานใช้มือซ้ำ เช่น ประกอบขันน็อต</td></tr>
<tr><td>Low Back Analysis (S, D)</td><td>แรงอัดและแรงเฉือนที่หลัง L4/L5 เทียบเกณฑ์ 3,400 N</td><td>ตรวจว่าหลังรับแรงเกินตอนก้มหรือยก</td></tr>
<tr><td>NIOSH (D)</td><td>สมการยกของ NIOSH ให้ RWL (น้ำหนักที่แนะนำ) และ Lifting Index</td><td>กำหนดน้ำหนักของที่ยกได้ปลอดภัย</td></tr>
<tr><td>Cumulative Loading (D)</td><td>แรงที่หลังสะสมตลอดกะ (MNs)</td><td>ดูผลของงานซ้ำทั้งวัน ไม่ใช่ครั้งเดียว</td></tr>
<tr><td>Fatigue (D)</td><td>เทียบเวลาออกแรงกับเวลาพักในหนึ่งรอบ</td><td>ดูว่ามีเวลาพักพอ ไม่ให้กล้ามเนื้อล้า</td></tr>
<tr><td>Energy Expenditure (D, TSB)</td><td>พลังงานที่ใช้ kcal/min จากงาน TSB เทียบเกณฑ์ 5</td><td>ดูว่างานหนักหรือเหนื่อยเกินไหม</td></tr>
<tr><td>Energy Expenditure Manual (S)</td><td>พิมพ์งานเองทีละข้อ (ยก ถือ เดิน) คิดตามข้อมูลของ Garg</td><td>ประเมินงานที่ยังไม่มี simulation</td></tr>
<tr><td>EAWS (S, D)</td><td>แบบประเมินมาตรฐาน MTM รวมท่า แรง น้ำหนัก แขน (ส่งออก .eaws3)</td><td>คะแนนความเสี่ยงรวมตามมาตรฐาน EAWS</td></tr>
<tr><td>Walk Analysis (D, TSB)</td><td>ภาพเส้นทางเดินมุมบนของแต่ละคน</td><td>หาทางเดินที่ยาวหรือซ้อนกันเพื่อลดการเดิน</td></tr>
<tr><td>Timing Report (D)</td><td>แยกเวลาแต่ละงานย่อยเป็นรหัส MTM-1</td><td>ตรวจเวลามาตรฐานของแต่ละท่า</td></tr>
<tr><td>MTMmotion (D, Beta)</td><td>วิเคราะห์เวลาแบบ MTM (UAS) จากข้อมูล simulation</td><td>เทียบเวลาทำงานกับมาตรฐาน MTM</td></tr>
</table>

<h2>ไฟล์ในบทเรียนและสิ่งที่อยู่ในแต่ละไฟล์</h2>
<table>
<tr><th>ไฟล์</th><th>สิ่งที่มี</th><th>เวลา TSB</th></tr>
<tr><td>PSH_1_Basic_Human.psz</td><td>Box, Conveyor, Rack, Jack + Go &gt; Get &gt; Put</td><td>6.77 s</td></tr>
<tr><td>PSH_2_Human Posturing.psz</td><td>เหมือนไฟล์ 1 + Jill ตั้งท่าก้ม + Vision Envelope</td><td>6.77 s</td></tr>
<tr><td>PSH_3_..._Center.psz</td><td>วางชั้นกลาง + Position + Pose + มือแยก</td><td>9.01 s</td></tr>
<tr><td>PSH_4_..._Under.psz</td><td>วางชั้นล่าง (ย่อตัว)</td><td>7.98 s</td></tr>
<tr><td>PSH_5_..._Over.psz</td><td>วางชั้นบน + Go + Regrasp</td><td>9.74 s</td></tr>
<tr><td>Library\\ / _JT_Store\\</td><td>Box, Conveyor, Rack (.cojt / .jt), HUMAN_MODELS\\Jack.cojt</td><td>-</td></tr>
</table>

<h2>เช็กลิสต์: ผู้เรียนทำได้ครบหรือยัง</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th><th>ตรวจด้วย</th></tr>
<tr><td>1</td><td>ตั้ง System Root แล้วเปิด PSH_1</td><td>เห็น Jack, Rack, Conveyor, Box</td></tr>
<tr><td>2</td><td>รู้ทางเข้า Convert and Insert CAD</td><td>File &gt; Import / Export</td></tr>
<tr><td>3</td><td>สร้างคนด้วย Create Human / Quick Create</td><td>คนใหม่ใน Resources</td></tr>
<tr><td>4</td><td>ตั้งท่าด้วย Posture Library / Adjust Joint</td><td>ท่าคนเปลี่ยนใน 3D</td></tr>
<tr><td>5</td><td>Set Active Simulation แล้วเล่น TSB</td><td>Jack วางกล่องบน Rack 6.77 s</td></tr>
<tr><td>6</td><td>บอกหน้าที่ Go / Get / Put / Position / Pose / Regrasp</td><td>อธิบาย Gantt ของ PSH_5 ได้</td></tr>
<tr><td>7</td><td>เทียบเวลา 3 ระดับชั้น</td><td>7.98 / 9.01 / 9.74 s</td></tr>
<tr><td>8</td><td>สร้างรายงาน RULA แล้วอ่านคะแนน</td><td>ชั้นบน 6 / 7</td></tr>
<tr><td>9</td><td>แยก Static / Dynamic แล้วรัน Analysis Tools ทุกกลุ่ม</td><td>Report Viewer + Excel + CSV</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>คลิกเมนู File แล้วไม่เกิดอะไร</td><td>หน้า Welcome ยังเปิดอยู่: ปิดก่อนหรือกด Open ที่หน้า Welcome</td></tr>
<tr><td>ปุ่มใน TSB เป็นสีเทา</td><td>Simulation &gt; Set Active Simulation เลือก TSB_Simulation_1</td></tr>
<tr><td>เลือกในรายการ Set Active ไม่ติด</td><td>คลิกลูกศรเปิดรายการแล้วคลิกชื่อทันทีถ้าไม่ติดให้ทำซ้ำ</td></tr>
<tr><td>เล่นจบแล้วไม่เห็นคน</td><td>Rack บังอยู่: View Cube &gt; Front แล้วคลิกขอบ Front | Right</td></tr>
<tr><td>Analysis Tools กด OK ไม่มีรายงาน</td><td>ติ๊ก RULA แล้วกด Analyze</td></tr>
<tr><td>Report Viewer เต็มจอ</td><td>ปุ่มปิดมุมขวาบนของ Report Viewer (ระวังกดโดนปุ่มปิด PS)</td></tr>
<tr><td>มีโฟลเดอร์ LibraryHuman เพิ่ม</td><td>PS สร้างเองตอนเปิด Work Zones (รอยเท้า) ลบได้ถ้าไม่ใช้</td></tr>
<tr><td>ปิดไฟล์แล้วถาม Save</td><td>No = ไม่เก็บสิ่งที่ลอง ถ้าจะเก็บใช้ Save As ชื่อใหม่</td></tr>
<tr><td>Analysis Tools ครึ่งหนึ่งเป็นสีเทา</td><td>ใส่หรือล้างช่อง Simulation (Static / Dynamic ขั้นที่ 26)</td></tr>
<tr><td>Excel ขึ้น error ซ้ำและว่าง</td><td>macro ปิดอยู่: อ่าน CSV ใน%APPDATA%\\Tecnomatix\\Reports</td></tr>
<tr><td>คลิกปุ่ม PS ไม่ติดหลังทำรายงาน</td><td>ปิด Report Viewer ที่ย่ออยู่มุมล่างซ้ายก่อน</td></tr>
</table>
'''
