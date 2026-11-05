# -*- coding: utf-8 -*-
"""Lesson 00: CAD Import -- from the Training/Basic step-by-step deck (Process Simulate 2502)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "สร้างโฟลเดอร์ <code>My_Project\\Library</code> ตั้ง System Root และเปิด New Study",
    "แปลงไฟล์ CAD (.jt) เป็นชิ้นส่วน .cojt แยกชิ้นด้วย New Part แล้วบันทึกด้วย End Modeling",
    "สร้าง Gripper: Frame (TCPF / BASEFRAME), Tool Definition และกลไก Crank (RRRR) พร้อม Pose OPEN / CLOSE",
    "สร้าง Device (XZ_Gantry, PS_CNC) และหุ่นยนต์ HP20D (7 link, 6 joint) แล้วติด Gripper ด้วย Mount Tool",
]

BODY = f'''
<p class="lead" style="max-width:46em;">นำไฟล์ CAD (JT) เข้า Process Simulate ทีละขั้น รวม 22 ขั้น — แปลงเป็นชิ้นส่วน .cojt แยกชิ้น สร้างเครื่องมือจับ (Gripper) อุปกรณ์ (Device) และหุ่นยนต์ HP20D พร้อม Kinematics ชิ้นส่วนที่ได้ถูกนำไปใช้ต่อในบท 01–04</p>

<h2>ภาพรวม: จากไฟล์ CAD สู่ชิ้นส่วนที่ใช้ใน simulation ได้</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>New Study</td><td>โฟลเดอร์ My_Project + System Root</td></tr>
<tr><td>02</td><td>Convert CAD</td><td>JT &gt; .cojt ใน Library</td></tr>
<tr><td>03</td><td>Part</td><td>แยกชิ้น + Compound Part</td></tr>
<tr><td>04</td><td>Vacuum Gripper</td><td>Frame + Tool Definition</td></tr>
<tr><td>05</td><td>Gripper 2F85</td><td>Crank RRRR + Pose + Tool Definition</td></tr>
<tr><td>06</td><td>Device</td><td>XZ_Gantry และ PS_CNC</td></tr>
<tr><td>07</td><td>Robot HP20D</td><td>7 link, 6 joint + limit</td></tr>
<tr><td>08</td><td>Robot Frame</td><td>BASEFRAME, TOOLFRAME, Mount Tool</td></tr>
<tr><td>09</td><td>Geometry + Save</td><td>Create Box + Save .psz</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate 2502 · โฟลเดอร์ <code>00_CAD_IMPORT</code> · ไฟล์ JT 6 ไฟล์ + <code>Robot\\HP20D.jt</code> · <code>Robot\\Specification.pdf</code> · <code>Robot\\HP0020D_A00.cojt</code> (เฉลย)
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ได้</th></tr>
<tr><td>01</td><td>Study</td><td>สร้างโฟลเดอร์ ตั้ง System Root และ New Study</td><td>My_Project</td></tr>
<tr><td>02</td><td>Part</td><td>Convert Part_Assembly, PLC แล้วแยกชิ้น</td><td>Part</td></tr>
<tr><td>03</td><td>Tool</td><td>Vacuum + 2F85 (Crank RRRR)</td><td>Gripper</td></tr>
<tr><td>04</td><td>Device</td><td>XZ_Gantry และ PS_CNC (.cojt ทำเอง)</td><td>Device</td></tr>
<tr><td>05</td><td>Robot</td><td>HP20D: link, joint, limit, frame</td><td>Robot</td></tr>
<tr><td>06</td><td>Save</td><td>Create Geometry แล้วบันทึก .psz</td><td>CAD_IMPORT.psz</td></tr>
</table>

<p class="lead" style="max-width:46em;">นำไฟล์ CAD (JT) เข้า Process Simulate ทีละขั้น รวม 22 ขั้น — แปลงเป็นชิ้นส่วน .cojt แยกชิ้น สร้างเครื่องมือจับ (Gripper) อุปกรณ์ (Device) และหุ่นยนต์ HP20D พร้อม Kinematics ชิ้นส่วนที่ได้ถูกนำไปใช้ต่อในบท 01–04</p>

<h2>ภาพรวม: จากไฟล์ CAD สู่ชิ้นส่วนที่ใช้ใน simulation ได้</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>New Study</td><td>โฟลเดอร์ My_Project + System Root</td></tr>
<tr><td>02</td><td>Convert CAD</td><td>JT &gt; .cojt ใน Library</td></tr>
<tr><td>03</td><td>Part</td><td>แยกชิ้น + Compound Part</td></tr>
<tr><td>04</td><td>Vacuum Gripper</td><td>Frame + Tool Definition</td></tr>
<tr><td>05</td><td>Gripper 2F85</td><td>Crank RRRR + Pose + Tool Definition</td></tr>
<tr><td>06</td><td>Device</td><td>XZ_Gantry และ PS_CNC</td></tr>
<tr><td>07</td><td>Robot HP20D</td><td>7 link, 6 joint + limit</td></tr>
<tr><td>08</td><td>Robot Frame</td><td>BASEFRAME, TOOLFRAME, Mount Tool</td></tr>
<tr><td>09</td><td>Geometry + Save</td><td>Create Box + Save .psz</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>00_CAD_IMPORT</code> · ไฟล์ JT 6 ไฟล์ + <code>Robot\\HP20D.jt</code> · <code>Robot\\Specification.pdf</code> · <code>Robot\\HP0020D_A00.cojt</code> (เฉลย)
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ได้</th></tr>
<tr><td>01</td><td>Study</td><td>สร้างโฟลเดอร์ ตั้ง System Root และ New Study</td><td>My_Project</td></tr>
<tr><td>02</td><td>Part</td><td>Convert Part_Assembly, PLC แล้วแยกชิ้น</td><td>Part</td></tr>
<tr><td>03</td><td>Tool</td><td>Vacuum + 2F85 (Crank RRRR)</td><td>Gripper</td></tr>
<tr><td>04</td><td>Device</td><td>XZ_Gantry และ PS_CNC (.cojt ทำเอง)</td><td>Device</td></tr>
<tr><td>05</td><td>Robot</td><td>HP20D: link, joint, limit, frame</td><td>Robot</td></tr>
<tr><td>06</td><td>Save</td><td>Create Geometry แล้วบันทึก .psz</td><td>CAD_IMPORT.psz</td></tr>
</table>

<h2>ขั้นที่ 1: สร้างโฟลเดอร์ My_Project\\Library และตั้ง System Root</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-01.jpg", "ขั้นที่ 1: สร้างโฟลเดอร์ My_Project\\Library และตั้ง System Root"),
    step_list([
        'หน้า Welcome ช่อง System Root = ...\\00_CAD_IMPORT\\My_Project\\Library',
        'คลิก New Study (RobcadStudy) แล้ว Create',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> System Root ใช้ร่วมทั้งเครื่อง ก่อนกลับไปเรียนบท 01-03 ต้องเปลี่ยนกลับเป็นโฟลเดอร์ Library ของบทนั้น ทุกไฟล์ที่ Convert / End Modeling จะไปอยู่ในโฟลเดอร์นี้</div>

<h2>ขั้นที่ 2: File &gt; Import / Export &gt; Convert and Insert CAD Files</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-02.jpg", "ขั้นที่ 2: File &gt; Import / Export &gt; Convert and Insert CAD Files"),
    step_list([
        'File &gt; Import / Export',
        'Convert and Insert CAD Files &gt; Add...',
        'เลือก Part_Assembly.jt',
        'Open',
    ])
)}

<h2>ขั้นที่ 3: File Import Settings ตั้งโฟลเดอร์ปลายทางและ Class</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-03.jpg", "ขั้นที่ 3: File Import Settings ตั้งโฟลเดอร์ปลายทางและ Class"),
    step_list([
        'Path = My_Project\\Library',
        'Base class = Part',
        'Compound class PmCompoundPart',
        'Prototype class PmPartPrototype',
        'Insert component ติ๊ก',
        'OK แล้วทำซ้ำกับ PLC.jt จากนั้น Import',
        'Conversion completed successfully',
    ])
)}

<h2>ขั้นที่ 4: Set Modeling Scope แล้ว New Part แยก BOLT / COVER</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-04.jpg", "ขั้นที่ 4: Set Modeling Scope แล้ว New Part แยก BOLT / COVER"),
    step_list([
        'เลือก Parts &gt; Modeling &gt; New Part &gt; PartPrototype &gt; OK',
        'ลาก BOLT (ชิ้นใน Part_Assembly) ไปวางใน PartPrototype ใหม่',
        'F2 เปลี่ยนชื่อ BOLT ทำซ้ำกับ COVER',
    ])
)}
<div class="tip"><strong>ทำไมแยก:</strong> แต่ละชิ้นต้องเป็น Part ของตัวเองจึงจะสร้าง Object Flow / ประกอบทีละชิ้นได้ (บท 01 Part Assembly)</div>

<h2>ขั้นที่ 5: End Modeling บันทึกแต่ละชิ้นเป็น .cojt</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-05.jpg", "ขั้นที่ 5: End Modeling บันทึกแต่ละชิ้นเป็น .cojt"),
    step_list([
        'เลือกชิ้น &gt; End Modeling &gt; ตั้งชื่อ &gt; Save ใน Library',
        'ได้ COVER.cojt, BOLT.cojt (BASE บันทึกกลับลง Part_Assembly.cojt)',
        'Create Compound Part ลาก BASE BOLT COVER เข้าไป ตั้งชื่อ PART_ASSEMBLY',
    ])
)}

<h2>ขั้นที่ 6: Convert Gripper เป็น Resource / Gripper</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-06.jpg", "ขั้นที่ 6: Convert Gripper เป็น Resource / Gripper"),
    step_list([
        'Base class = Resource',
        'Prototype class = Gripper',
        'เพิ่มทั้ง Gripper_Vacuum.jt และ Gripper_2F85.jt แล้ว Import',
    ])
)}

<h2>ขั้นที่ 7: Gripper_Vacuum สร้าง TCPF และ BASEFRAME</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-07.jpg", "ขั้นที่ 7: Gripper_Vacuum สร้าง TCPF และ BASEFRAME"),
    step_list([
        'Create Frame by 6 Values: TCPF = (0,0,0) Rx 180 ให้ Z ชี้ลงจากถ้วยดูด',
        'Frame at Circle Center คลิก 3 จุดบนขอบหน้าแปลน หา Z = 80.2 &gt; BASEFRAME (0,0,80.2)',
    ])
)}

<h2>ขั้นที่ 8: Tool Definition ของ Gripper_Vacuum</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-08.jpg", "ขั้นที่ 8: Tool Definition ของ Gripper_Vacuum"),
    step_list([
        'Tool Type = Gripper',
        'TCP Frame = TCPF',
        'Base Frame = BASEFRAME',
        'Gripping Objects = ถ้วยดูด 4 ชิ้น',
        'ถ้วยดูดเปลี่ยนเป็นสีส้ม = ชิ้นที่จับงาน',
    ])
)}

<h2>ขั้นที่ 9: Gripper_2F85 แบ่ง 11 ชิ้นเป็น link ของ Crank</h2>
{screenshot("assets/images/lessons/00-09.jpg", "ขั้นที่ 9: Gripper_2F85 แบ่ง 11 ชิ้นเป็น link ของ Crank")}
<div class="tip"><strong>วิธีหา:</strong> Set Modeling Scope แล้วคลิกทีละชิ้นใน tree ชิ้นที่เลือกเป็นสีฟ้า (มองจากด้านล่าง)</div>

<h2>ขั้นที่ 10: Kinematics Editor &gt; Create Crank (RRRR) ใส่จุดหมุน 4 จุด</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-10.jpg", "ขั้นที่ 10: Kinematics Editor &gt; Create Crank (RRRR) ใส่จุดหมุน 4 จุด"),
    step_list([
        'Create Crank (ปุ่มที่ 6 ใน Kinematics Editor) &gt; RRRR &gt; Next',
        'พิมพ์พิกัด 4 จุด (ข้างซ้าย z = 82.43)',
    ])
)}

<h2>ขั้นที่ 11: เลือกชิ้นส่วนให้แต่ละ link แล้ว Finish</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-11.jpg", "ขั้นที่ 11: เลือกชิ้นส่วนให้แต่ละ link แล้ว Finish"),
    step_list([
        'คลิก link ในแผนภาพแล้วคลิกชิ้นใน tree',
        'ข้างที่ 2: Fixed = Existing Link fixed_link',
        'ได้กราฟ fixed &gt; input &gt; coupler &gt; output &gt; dummy ทั้ง 2 ข้าง',
    ])
)}

<h2>ขั้นที่ 12: Joint Dependency ให้นิ้วสองข้างหุบพร้อมกัน</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-12.jpg", "ขั้นที่ 12: Joint Dependency ให้นิ้วสองข้างหุบพร้อมกัน"),
    step_list([
        'เลือกเส้น input_j2 &gt; Joint Dependency &gt; Joint Function',
        'Joint Name = input_j1 ได้ (T(input_j1)) &gt; Apply',
    ])
)}

<h2>ขั้นที่ 13: Pose OPEN / CLOSE และ Tool Definition ของ 2F85</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-13.jpg", "ขั้นที่ 13: Pose OPEN / CLOSE และ Tool Definition ของ 2F85"),
    step_list([
        'Gripper',
        'TCPF (0,140,91) ปลายนิ้ว',
        'BASEFRAME (0,0,91) หน้าแปลน',
        'Gripping Objects = pad 2550, 13097',
        'End Modeling &gt; Gripper_2F85.cojt',
    ])
)}

<h2>ขั้นที่ 14: Create Compound Resource รวม Gripper ทั้งสอง</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-14.jpg", "ขั้นที่ 14: Create Compound Resource รวม Gripper ทั้งสอง"),
    step_list([
        'เลือก Resources &gt; Modeling &gt; Create Compound Resource',
        'F2 ชื่อ GRIPPERS',
        'ลาก Gripper_Vacuum และ Gripper_2F85 เข้าไป',
    ])
)}
<div class="tip"><strong>ใช้ทำอะไร:</strong> จัดกลุ่ม resource ใน tree ให้หาง่าย ซ่อน/แสดงทั้งกลุ่มได้ในคลิกเดียว</div>

<h2>ขั้นที่ 15: XZ_Gantry นำเข้าเป็น Part แล้วสร้าง New Resource &gt; Device</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-15.jpg", "ขั้นที่ 15: XZ_Gantry นำเข้าเป็น Part แล้วสร้าง New Resource &gt; Device"),
    step_list([
        'Convert XZ_Gantry.jt (Part) &gt; Set Modeling Scope &gt; Resources &gt; New Resource &gt; Device',
        'ลาก Body, X, Z, Conveyor, TCPF เข้า Device ชื่อ XZ_GANTRY ส่วนกล่อง Part ที่เหลือชื่อ BOX',
        'End Modeling &gt; XZ_Gantry_Device.cojt (ต่อด้วยบท 02_KINEMATICS)',
    ])
)}

<h2>ขั้นที่ 16: PS_CNC ทำ .cojt เองแล้ว Insert Component</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-16.jpg", "ขั้นที่ 16: PS_CNC ทำ .cojt เองแล้ว Insert Component"),
    step_list([
        'สร้างโฟลเดอร์ PS_CNC.cojt ใน Library แล้วคัดลอก PS_CNC.jt เข้าไป &gt; Modeling &gt; Define Component Type = Device',
        'Insert Component &gt; PS_CNC.cojt ขึ้นเป็น Device ใน Resources',
    ])
)}

<h2>ขั้นที่ 17: ทฤษฎีหุ่นยนต์ใน PS ประกอบด้วยอะไร</h2>
{screenshot("assets/images/lessons/00-17.jpg", "ขั้นที่ 17: ทฤษฎีหุ่นยนต์ใน PS ประกอบด้วยอะไร")}

<h2>ขั้นที่ 18: Convert HP20D.jt เป็น Resource / Robot</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-18.jpg", "ขั้นที่ 18: Convert HP20D.jt เป็น Resource / Robot"),
    step_list([
        'Resource',
        'Robot',
    ])
)}

<h2>ขั้นที่ 19: Kinematics Editor สร้าง 7 link</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-19.jpg", "ขั้นที่ 19: Kinematics Editor สร้าง 7 link"),
    step_list([
        'Set Modeling Scope ที่ HP20D &gt; Kinematics Editor &gt; Create Link ทีละ link ตั้งชื่อตามเฉลย',
        'แต่ละ link มี 1 ชิ้น (ตามตารางขั้นที่ 18)',
    ])
)}

<h2>ขั้นที่ 20: สร้าง 6 joint จากค่าในเฉลย + Specification.pdf</h2>
{screenshot("assets/images/lessons/00-20.jpg", "ขั้นที่ 20: สร้าง 6 joint จากค่าในเฉลย + Specification.pdf")}
<div class="tip"><strong>ข้อต่าง:</strong> เฉลยใช้ Limit แบบ Variable ที่ U (ขึ้นกับ L, Upper Arm follow Lower Arm) ในงานนี้ตั้ง Constant -255/+165 ตาม PDF ส่วนแกน From/To อ่านจาก Joint Properties ของเฉลย</div>

<h2>ขั้นที่ 21: BASEFRAME, TOOLFRAME แล้วทดสอบ Joint Jog</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-21.jpg", "ขั้นที่ 21: BASEFRAME, TOOLFRAME แล้วทดสอบ Joint Jog"),
    step_list([
        'Set Baseframe (0,0,0)',
        'Create Toolframe (945,0,1305) Ry 180 ติด Twist',
        'End Modeling &gt; HP20D.cojt',
        'Robot &gt; Joint Jog ขยับ L 30 U 30 B -45',
    ])
)}

<h2>ขั้นที่ 22: Mount Tool ติด Gripper_2F85 ที่ TOOLFRAME</h2>
{side_by_side(
    screenshot("assets/images/lessons/00-22.jpg", "ขั้นที่ 22: Mount Tool ติด Gripper_2F85 ที่ TOOLFRAME"),
    step_list([
        'Tool = Gripper_2F85',
        'Frame = Base Frame (BASEFRAME)',
        'Mount on = HP20D',
        'TOOLFRAME',
        'Apply',
    ])
)}

<h2>ไฟล์ที่ได้ใน My_Project\\Library</h2>
<table>
<tr><th>ไฟล์ .cojt</th><th>ชนิด</th><th>ที่มา</th></tr>
<tr><td>Part_Assembly / BOLT / COVER</td><td>PartPrototype</td><td>Part_Assembly.jt แยก 3 ชิ้น</td></tr>
<tr><td>PLC</td><td>PartPrototype</td><td>PLC.jt</td></tr>
<tr><td>Gripper_Vacuum</td><td>Gripper</td><td>TCPF + BASEFRAME + ถ้วยดูด 4 ชิ้น</td></tr>
<tr><td>Gripper_2F85</td><td>Gripper</td><td>Crank RRRR 2 ข้าง, Pose OPEN/CLOSE</td></tr>
<tr><td>XZ_Gantry / XZ_Gantry_Device</td><td>Part / Device</td><td>แยกกล่อง BOX กับ gantry</td></tr>
<tr><td>PS_CNC</td><td>Device</td><td>.cojt ทำเอง + Define Component Type</td></tr>
<tr><td>HP20D</td><td>Robot</td><td>7 link 6 joint + frame</td></tr>
<tr><td>HP0020D_A00</td><td>Robot</td><td>เฉลย (คัดลอกจาก Robot\\)</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>System Root เป็นสีแดง</td><td>ชี้โฟลเดอร์ที่มีอยู่จริง (My_Project\\Library)</td></tr>
<tr><td>Path ต่อท้ายข้อความเดิม</td><td>ลบให้หมด (End, Shift+Home, Delete) ก่อนพิมพ์</td></tr>
<tr><td>Combo ไม่เปลี่ยนค่า</td><td>คลิกเปิดแล้วใช้ลูกศร/คลิกเลือกทันที</td></tr>
<tr><td>Frame ไม่อยู่ใน Gripper</td><td>Set Modeling Scope ที่ Gripper ก่อน Create Frame</td></tr>
<tr><td>Create Crank: Plane error</td><td>พิมพ์ค่าพิกัดซ้ำแล้วกด Enter</td></tr>
<tr><td>Link Entities: ชิ้นซ้ำ</td><td>Reedit แล้วลบชิ้นที่อยู่ link อื่น</td></tr>
<tr><td>Insert .cojt ทำเองขึ้น error</td><td>ต้อง Define Component Type ก่อน (มี TuneData.xml)</td></tr>
<tr><td>Ctrl+S ไม่บันทึก</td><td>File &gt; Disconnected Study &gt; Save</td></tr>
</table>
'''
