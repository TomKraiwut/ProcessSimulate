# -*- coding: utf-8 -*-
"""Generates all chapter pages + regenerates basic.html hub for consistency.
Run after gen_site.py (reuses its templates by importing it)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_site import SECTIONS, SECTION_ORDER, page_html, chapter_filename, hub_page, write, HUB_INTRO, HUB_CARD_DESC, youtube_embed, screenshot, step_list, side_by_side

# ---------------------------------------------------------------------------
# Chapter objectives (2-3 goals per chapter, "เพื่อ..." style)
# ---------------------------------------------------------------------------
OBJECTIVES = {
    ("basic", 1): ["รู้ว่า Process Simulate ใช้แก้โจทย์อะไรได้บ้างในงานจริง",
                   "เข้าใจภาพรวมของทั้งคอร์ส 3 ระดับก่อนเริ่มเรียน"],
    ("basic", 2): ["จำตำแหน่งและหน้าที่ของส่วนประกอบหลักในโปรแกรมได้",
                   "เปิดโปรแกรม สร้าง Study ใหม่ และรู้จักหน้าจอหลักได้ด้วยตัวเอง"],
    ("basic", 3): ["จำ Object พื้นฐาน 6 ตัวที่ใช้บ่อยที่สุด และหน้าที่ของแต่ละตัวได้",
                   "รู้ว่า Object แต่ละตัวมี Attribute สำคัญอะไรที่ต้องตั้ง"],
    ("basic", 4): ["สร้างงานหยิบ-วางชิ้นงานด้วยหุ่นยนต์ (Pick and Place) ได้ด้วยตัวเอง",
                   "ใช้ Jog/Teach บันทึก Pose และเรียงลำดับด้วย PERT chart ได้"],
    ("basic", 5): ["รันและ Reset ซิมูเลชันได้อย่างถูกวิธี",
                   "อ่านและตีความ Collision Report, Cycle Time และ Reachability ได้"],
    ("basic", 6): ["บันทึกไฟล์ Study (.psz) และเปิดไฟล์เดิมกลับมาทำต่อได้",
                   "มีนิสัยสำรองไฟล์ที่ปลอดภัย ก่อนไฟล์เสียหรือหาย"],

    ("intermediate", 1): ["แยกความแตกต่างของ Device, Fixture, Gripper/Tool และ Conveyor ได้",
                          "เลือกใช้ Resource ที่เหมาะกับสถานการณ์ในเซลล์จริงได้"],
    ("intermediate", 2): ["เข้าใจว่า ExtTcp/Tool Center Point คืออะไร และทำไมต้องกำหนดให้ถูก",
                          "ใช้ Approach/Departure และ Via Point ควบคุมเส้นทางหุ่นยนต์ให้ปลอดภัยขึ้นได้"],
    ("intermediate", 3): ["แยกความแตกต่างของ Weld Point Operation และ Weld Line Operation ได้",
                          "สร้างจุดเชื่อมและจัดการ Weld Gun Tip ได้"],
    ("intermediate", 4): ["จัดลำดับ Operation แบบขนาน (Parallel) และต่อเนื่อง (Sequential) ใน PERT chart ได้",
                          "กำหนด Time Attribute และมองเห็นผลต่อ Cycle Time รวม"],
    ("intermediate", 5): ["รวมกลุ่มวัตถุเป็น Collision Set เพื่อตรวจสอบการชนอย่างมีระบบ",
                          "แยกความแตกต่างของ Static และ Dynamic Collision Detection ได้"],
    ("intermediate", 6): ["เก็บ Robot, Gripper, Fixture มาตรฐานไว้ใน Resource Library ได้",
                          "นำ Resource จาก Library กลับมาใช้ซ้ำข้าม Study ได้โดยไม่ต้องสร้างใหม่ทุกครั้ง"],

    ("advanced", 1): ["เข้าใจว่า Logic Block คืออะไร และผูก Signal เข้ากับอุปกรณ์ได้",
                      "ออกแบบเงื่อนไขการทำงานอย่างง่ายด้วย Logic Block โดยไม่ต้องเขียนโค้ด"],
    ("advanced", 2): ["เข้าใจโครงสร้างพื้นฐานของ Tecnomatix.Engineering .NET API",
                      "เขียนสคริปต์ไล่อ่านรายการ Operation ทั้งหมดใน Study ได้"],
    ("advanced", 3): ["เขียนสคริปต์สลับ Resource หลาย Scenario แล้วตรวจสอบการชนซ้ำอัตโนมัติได้",
                      "ประเมินได้ว่าเมื่อไหร่ควรใช้สคริปต์แทนการปรับ Layout ด้วยมือ"],
    ("advanced", 4): ["เข้าใจขั้นตอนของ Offline Programming (OLP) ตั้งแต่ต้นจนจบ",
                      "แปลง Pose/Path ที่ Teach ไว้เป็นโปรแกรมควบคุมหุ่นยนต์จริงได้"],
    ("advanced", 5): ["สร้าง Human ด้วย Quick Create/Human Library และเลือก Anthropometric Database ให้เหมาะกับกลุ่มผู้ปฏิบัติงานได้",
                      "ใช้เครื่องมือวิเคราะห์การยศาสตร์ (RULA, OWAS) ประเมินความเสี่ยงบาดเจ็บจากท่าทางเบื้องต้นได้"],
    ("advanced", 6): ["ออกแบบ Interlock ป้องกันหุ่นยนต์หลายตัวชนกันในพื้นที่ทำงานร่วมกันได้",
                      "เข้าใจแนวคิด Interlock ระหว่าง Resource มากกว่าหนึ่งตัว"],
    ("advanced", 7): ["ใช้ Study Manager บริหารเวอร์ชันไฟล์ Study เมื่อทำงานเป็นทีมได้",
                      "วางนโยบาย Check-in/Check-out ที่ลดปัญหาไฟล์ทับกันได้"],

    ("object-reference", 1): ["จำ Resource สายหลักที่ใช้บ่อยที่สุดและหน้าที่ของแต่ละตัวได้ไว",
                              "ทำตามสาธิตสั้นๆ ของแต่ละ Resource เพื่อเห็นพฤติกรรมจริงด้วยตาตัวเอง"],
    ("object-reference", 2): ["เข้าใจว่า Operation แต่ละประเภทมีไว้ทำอะไร",
                              "รู้ว่าจะไปดูรายละเอียดเชิงลึกของแต่ละตัวต่อได้จากบทไหน"],
    ("object-reference", 3): ["รู้จัก Object ประเภทตรรกะและเครื่องมือวิเคราะห์ที่มีให้ใช้",
                              "เลือกเครื่องมือที่เหมาะกับคำถามที่ต้องการตอบได้"],

    ("case-study", 1): ["เห็นตัวอย่างการประยุกต์ใช้ Process Simulate ในเซลล์เชื่อมตัวถังรถยนต์จริง",
                        "เชื่อมโยงความรู้จากหลายบทเข้าด้วยกันเป็นเซลล์เดียว"],
    ("case-study", 2): ["เห็นตัวอย่างการจำลองเซลล์หยิบ-วางและบรรจุภัณฑ์อัตโนมัติ",
                        "เข้าใจโจทย์เฉพาะของงาน Material Handling ที่ต้องคำนึงถึง Cycle Time และความเสียหายของชิ้นงาน"],
    ("case-study", 3): ["เห็นตัวอย่างการจำลองงานพ่นสีที่ต้องการความสม่ำเสมอของ Path",
                        "เข้าใจว่าทำไมงานพ่นสีให้ความสำคัญกับความเร็วและระยะห่างของปืนพ่นคงที่"],
    ("case-study", 4): ["เห็นตัวอย่างการจำลองงานประกอบอิเล็กทรอนิกส์ที่ต้องการความแม่นยำสูง",
                        "เข้าใจการนำ Collision Set และ Reachability มาใช้ร่วมกันในโจทย์ที่พื้นที่ทำงานแคบ"],

    ("tips-tricks", 1): ["รู้ทางลัดที่ช่วยให้ทำงานกับโปรแกรมเร็วขึ้นในชีวิตประจำวัน"],
    ("tips-tricks", 2): ["รู้ข้อผิดพลาดที่มือใหม่เจอบ่อย และวิธีเช็คให้ไวก่อนเสียเวลาไล่บั๊กผิดจุด"],
    ("tips-tricks", 3): ["รู้เทคนิคที่ช่วยให้เซลล์ขนาดใหญ่รันเร็วขึ้นโดยไม่กระทบผลลัพธ์"],
    ("tips-tricks", 4): ["รู้กับดัก .NET API และ Logic ที่พบบ่อยที่สุดเวลาเขียนสคริปต์ควบคุมเซลล์"],
}

# ---------------------------------------------------------------------------
# Chapter bodies (content sections, HTML)
# ---------------------------------------------------------------------------
BODY = {}

BODY[("basic", 1)] = '''
<h2>Process Simulate คืออะไร</h2>
<p>Process Simulate (Tecnomatix Process Simulate) เป็นซอฟต์แวร์จำลองกระบวนการผลิตของ Siemens ใช้วางแผน จำลอง และตรวจสอบ
(plan, simulate, validate) การทำงานของหุ่นยนต์และระบบอัตโนมัติหน้างานตลอดวงจรชีวิตของโครงการ ตั้งแต่ขั้น concept
ไปจนถึงเริ่มผลิตจริง มักใช้งานโดยแผนกวิศวกรรมการผลิต แผนกออกแบบไลน์หุ่นยนต์/อัตโนมัติ และแผนกจำลองกระบวนการ
ทั้งในบริษัทผู้ผลิตเองและผู้รับเหมาระบบ (System Integrator)</p>

<h2>Bill of Process (BOP): มองเซลล์การผลิตเป็น 4 ส่วน</h2>
<p>Process Simulate จัดโครงสร้างงานทุกชิ้นด้วยแนวคิด <strong>Bill of Process (BOP)</strong> แบ่งเป็น 4 ส่วนหลัก:</p>
<table>
<tr><th>ส่วนของ BOP</th><th>ความหมาย</th></tr>
<tr><td><strong>Part</strong></td><td>ชิ้นส่วนที่ประกอบกันเป็นผลิตภัณฑ์ (the pieces that make up the manufactured product)</td></tr>
<tr><td><strong>Resource</strong></td><td>สิ่งอำนวยงานในโรงงานที่ทำ Operation กับ Part เช่น สถานีงาน เซลล์ เครื่องมือ และ Fixture</td></tr>
<tr><td><strong>Manufacturing Feature</strong></td><td>ความสัมพันธ์พิเศษระหว่าง Part หลายชิ้น (เช่น จุดเชื่อมที่เชื่อมสอง Part เข้าด้วยกัน)</td></tr>
<tr><td><strong>Operation</strong></td><td>การกระทำที่ทำให้เกิดผลิตภัณฑ์ แบ่งเป็น Device Operation และ Robot Operation</td></tr>
</table>

<h2>สองโหมดการจำลอง: Time-based กับ Event-based</h2>
<table>
<tr><th>โหมด</th><th>ลักษณะการทำงาน</th></tr>
<tr><td><strong>Time-based Simulation</strong></td><td>ลำดับ Operation กำหนดตายตัวด้วย Gantt diagram ทำงานตามเส้นเวลาโดยตรง เหมาะกับตรวจสอบเบื้องต้นแบบเร็วและง่าย ไม่ต้องมี Sensor/Signal</td></tr>
<tr><td><strong>Event-based Simulation</strong></td><td>ลำดับควบคุมด้วย <strong>CEE (Cyclic Event Evaluator)</strong> — ตัวประมวลผลตรรกะในตัวของ Process Simulate เอง — ผ่าน Signal และเงื่อนไข เหมาะกับโมเดลที่มี Sensor/Logic/การเชื่อม PLC (Virtual Commissioning)</td></tr>
</table>

<div class="tip">
<strong>ทำไมไม่ทดลองกับหุ่นยนต์จริงเลย:</strong> การหยุดสายการผลิตจริงเพื่อทดสอบ Layout ใหม่มีต้นทุนสูงและเสี่ยงอุบัติเหตุ
Process Simulate ให้ทดลองวางตำแหน่ง ปรับ Path และเช็คการชนได้ไม่จำกัดรอบบนคอมพิวเตอร์ ก่อนค่อยส่งโปรแกรมไปหุ่นยนต์จริงครั้งเดียว
</div>

<h2>ภาพรวมคอร์สนี้</h2>
<p>คอร์สแบ่งเป็น 3 ระดับ: <strong>Basic</strong> รู้จักโปรแกรมและสร้างงาน Pick and Place แรก, <strong>Intermediate</strong>
ควบคุม Path/Resource ให้ละเอียดขึ้นและทำงานเชื่อม, <strong>Advanced</strong> ควบคุมเซลล์ด้วย Logic Block/CEE เขียน .NET API
และส่งออกโปรแกรมหุ่นยนต์จริงด้วย OLP</p>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ถ้าคุณต้องออกแบบเซลล์ใหม่ที่มีหุ่นยนต์ 3 ตัวทำงานใกล้กัน จะรู้ได้อย่างไรว่าหุ่นยนต์จะไม่ชนกัน
โดยไม่ต้องรอไปเจอหน้างานจริง?
</div>
<div class="tip"><strong>เฉลย:</strong> สร้างโมเดลทั้ง 3 หุ่นยนต์ใน Process Simulate ตาม Layout จริง แล้วรัน Collision Detection
(ดูบท Basic 5) — ถ้าพบว่าชนกัน ค่อยปรับ Path หรือใส่ตรรกะกันชนผ่าน CEE/Logic Block (ดูบท Advanced 6) ก่อนติดตั้งจริง</div>
'''

BODY[("basic", 2)] = '''
<h2>ส่วนประกอบหลักของโปรแกรม</h2>
<p>เมื่อเปิดโปรแกรมและสร้าง Study ใหม่ จะเจอส่วนหลักๆ ดังนี้</p>
<table>
<tr><th>ส่วนประกอบ</th><th>หน้าที่</th></tr>
<tr><td><strong>Object Tree / Study Tree</strong></td><td>โครงสร้างของ Study ทั้งหมด แบ่งเป็น Resources, Operations, Parts</td></tr>
<tr><td><strong>Graphic Viewer</strong></td><td>พื้นที่แสดงโมเดล 3 มิติของเซลล์การผลิต มี Graphic Viewer Toolbar และ Object Toolbars ลอยอยู่ในหน้าจอเดียวกัน</td></tr>
<tr><td><strong>Navigation Cube</strong></td><td>ลูกบาศก์มุมจอสำหรับหมุนมุมมอง (Rotate) และเดินดูรอบวัตถุ (Walk around object) แบบเร็วๆ</td></tr>
<tr><td><strong>Operation Tree / Sequence Editor</strong></td><td>แสดงลำดับ Operation แบบ PERT chart หรือ Gantt เพื่อกำหนดว่าอะไรทำงานก่อน-หลัง</td></tr>
<tr><td><strong>Jog/Teach Panel</strong></td><td>แผงควบคุมขยับหุ่นยนต์ทีละแกน (Jog) และบันทึกท่าทาง (Pose/Teach)</td></tr>
<tr><td><strong>Attribute Window</strong></td><td>เปิดจากดับเบิลคลิก Object — ตั้งค่าคุณสมบัติเฉพาะของ Object นั้น</td></tr>
</table>

<div class="tip">
<strong>Tip:</strong> คลิกขวาที่ Object เกือบทุกจุดในโปรแกรม (Object Tree, Graphic Viewer, Operation Tree) จะเจอ context menu
ที่รวมคำสั่งที่ใช้บ่อยที่สุดของ Object นั้นไว้ให้แล้ว เร็วกว่าไล่หาในเมนูบนสุดมาก
</div>

<h2>สร้าง Study ใหม่</h2>
{steps}

<div class="tip">
<strong>Tip:</strong> จัด Layout หน้าต่าง (Graphic Viewer, Object Tree, Operation Tree) ให้เห็นพร้อมกันตั้งแต่แรก
จะช่วยให้ไล่ดูว่ากำลังแก้ Object ไหนอยู่ได้ง่ายขึ้นมาก โดยเฉพาะเมื่อ Study เริ่มมี Operation หลายสิบตัว
</div>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ถ้าจัดวาง Resource ผิดตำแหน่งใน Graphic Viewer จะแก้ไขตำแหน่งได้จากส่วนไหนของโปรแกรม
โดยไม่ต้องลบแล้วสร้างใหม่?
</div>
<div class="tip"><strong>เฉลย:</strong> เลือก Resource ใน Object Tree หรือคลิกใน 3D Viewer แล้วแก้ค่าตำแหน่ง (Location) ได้จาก
Attribute Window หรือใช้ Manipulator ลากในหน้าจอ 3D โดยตรง</div>
'''.format(steps=step_list([
    "เปิดโปรแกรม Process Simulate แล้วเลือก Create New Study",
    "เลือกโฟลเดอร์ Library ของโปรเจกต์ (เช่น <code>My_Project/Library</code>) และตั้งชื่อ Study",
    "สังเกตหน้าจอเปล่า — Object Tree ด้านซ้าย, Graphic Viewer ตรงกลางพร้อม Navigation Cube มุมจอ",
    "ลองเปิด Operation Tree จากเมนู View เพื่อดูตำแหน่งของมัน",
]))

BODY[("basic", 3)] = '''
<h2>Object พื้นฐาน 6 ตัวที่ใช้บ่อย</h2>
<p>Object หลักในการสร้างเซลล์อ้างอิงจากแนวคิด Bill of Process (BOP) ที่แนะนำไว้ในบทที่แล้ว บวกกับ 2 Object เฉพาะของ Process Simulate
ที่ใช้ควบคุมการเคลื่อนที่และลำดับงาน:</p>
<table>
<tr><th>Object</th><th>ใช้ทำอะไร</th></tr>
<tr><td><strong>Study</strong></td><td>ไฟล์งานหลักที่รวม Resource, Operation, Part ของสถานการณ์จำลองหนึ่งชุด</td></tr>
<tr><td><strong>Resource</strong></td><td>ทรัพยากรจริงในเซลล์ (BOP: Resource) เช่น Robot, Fixture, Tool/Gripper, Device (สายพาน, ประตูนิรภัย)</td></tr>
<tr><td><strong>Part</strong></td><td>ชิ้นงานที่ถูกหยิบจับหรือแปรรูปในกระบวนการ (BOP: Part)</td></tr>
<tr><td><strong>Operation</strong></td><td>ขั้นตอนงานหนึ่งอย่าง (BOP: Operation) แบ่งเป็น Device Operation กับ Robot Operation เช่น Pick, Place, Weld Point</td></tr>
<tr><td><strong>PERT Chart</strong></td><td>แผนภาพแสดงลำดับก่อน-หลังของ Operation ทั้งหมดใน Study</td></tr>
<tr><td><strong>Pose</strong></td><td>ท่าทาง (มุมข้อต่อ) ของหุ่นยนต์ ณ จุดใดจุดหนึ่ง บันทึกด้วยการ Teach</td></tr>
</table>

<div class="note">
<strong>ข้อควรระวัง:</strong> Object แต่ละตัวมี Attribute เฉพาะของตัวเอง เช่น Robot มี Reach/Payload, Operation มี Time —
ก่อนเริ่มสร้างงานจริง ควรเปิด Attribute Window ของแต่ละ Object ดูก่อนว่ามีค่าอะไรให้ตั้งบ้าง จะช่วยลดเวลาย้อนกลับมาแก้ทีหลัง
</div>

<h2>ความสัมพันธ์ระหว่าง Object</h2>
<p>Study หนึ่งไฟล์ประกอบด้วย Resource และ Part หลายตัว โดย Operation คือสิ่งที่ผูก Resource เข้ากับ Part
(เช่น Robot หยิบ Part ด้วย Operation Pick) แล้ว PERT chart คือสิ่งที่เรียงลำดับว่า Operation ไหนเกิดก่อน-หลัง
ส่วน Pose คือรายละเอียดภายใน Operation ว่าหุ่นยนต์ต้องอยู่ท่าไหนในแต่ละจุด — ถ้ามี Part หลายชิ้นที่ต้องประกอบสัมพันธ์กัน
(เช่น จุดเชื่อมที่ยึดสอง Part เข้าด้วยกัน) ความสัมพันธ์นั้นถูกเก็บเป็น <strong>Manufacturing Feature</strong> ตาม BOP</p>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> ถ้าต้องการให้หุ่นยนต์ตัวเดียวหยิบชิ้นงาน 2 แบบสลับกัน ต้องสร้าง Part กี่ตัว และ Operation กี่ตัว?
</div>
<div class="tip"><strong>เฉลย:</strong> สร้าง Part 2 ตัว (แทนชิ้นงานแต่ละแบบ) และสร้าง Operation Pick แยกสำหรับแต่ละ Part
เพราะแต่ละ Part มักอยู่คนละตำแหน่งและต้องการ Pose หยิบที่ต่างกัน แม้ใช้ Robot และ Gripper ตัวเดียวกันก็ตาม</div>
'''

BODY[("basic", 4)] = f'''
<h2>สร้างงานแรก: หยิบ-วางชิ้นงานด้วยหุ่นยนต์ (Pick and Place)</h2>
<p>ทำตามขั้นตอนนี้เพื่อสร้างงานหยิบชิ้นงานจากจุด A ไปวางที่จุด B</p>

{step_list([
    "สร้าง Study ใหม่ แล้ว Import หุ่นยนต์ (Robot Resource) และชิ้นงาน (Part) เข้ามาในเซลล์",
    "จัดวางตำแหน่งหุ่นยนต์ ชิ้นงานต้นทาง และปลายทางในพื้นที่ทำงาน",
    "สร้าง <strong>Operation → Pick</strong> แล้วใช้ Jog/Teach เลื่อนหุ่นยนต์ไปยังตำแหน่งหยิบ บันทึกเป็น Pose",
    "สร้าง <strong>Operation → Place</strong> ทำแบบเดียวกันที่ตำแหน่งวาง",
    "เปิด <strong>PERT chart</strong> เรียงลำดับ Pick ก่อน Place",
    "กด <strong>Play</strong> ใน Sequence Editor / Simulation Player เพื่อรันและตรวจสอบการชน (Collision Check)",
])}

<div class="tip">
<strong>Tip:</strong> ก่อนรัน ให้ผูก Part เข้ากับปลายแขนหุ่นยนต์ด้วยคำสั่ง <strong>Attach</strong> ใน Operation Pick — ถ้าลืม
ชิ้นงานจะไม่เคลื่อนที่ตามหุ่นยนต์เวลารัน แม้ Pose จะถูกต้องแล้วก็ตาม
</div>

<h2>ตัวอย่าง: กระบวนการหยิบ-ป้อนชิ้นงานเข้าเครื่อง CNC</h2>
<p>ตัวอย่างคลาสสิกของงาน Pick and Place ในสายการผลิตจริงคือกระบวนการหยิบชิ้นงานป้อนเครื่อง CNC ซึ่งประกอบด้วยหลาย Operation
ต่อเนื่องกัน: <code>Part Bank Flow In → Robot Load In → Machine Door Close → CNC Machining → Machine Door Open → Robot Load Out</code>
— สังเกตว่ามีทั้ง Robot Operation (หุ่นยนต์หยิบ-วาง) และ Device Operation (ประตูเครื่องเปิด-ปิด, การ Machining ของ CNC) ผสมกัน
ตามแนวคิด BOP ที่เรียนในบทที่แล้ว</p>
<p>ตำแหน่งหยิบ-วางแต่ละจุดถูกเก็บเป็น <strong>Location</strong> ซึ่งสร้าง/แก้ไขได้ผ่านคำสั่ง Manipulate Location และ Add Location
โดยไม่ต้องลบ Operation เดิมทิ้งเมื่อจุดคลาดเคลื่อนเล็กน้อย</p>

<div class="note">
<strong>รู้ไว้:</strong> งานหยิบ-วางแบบเรียงซ้อนชิ้นงานเป็นชั้นๆ (เช่น วางลงพาเลท) มีเทมเพลตสำเร็จรูปเรียกว่า <strong>Cobot Palletizer</strong>
ช่วยลดเวลาสร้าง Operation ซ้ำๆ เมื่อรูปแบบการวางเป็นตาราง/เรียงแถวที่คาดเดาได้
</div>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ถ้าตำแหน่งวาง (Place) อยู่นอกระยะที่หุ่นยนต์เอื้อมถึง จะรู้ได้จากที่ไหนก่อนที่จะรันแล้วเจอปัญหา?
</div>
<div class="tip"><strong>เฉลย:</strong> ใช้ฟีเจอร์ Reach Test/Reachability ตรวจสอบก่อน Teach จริง — ถ้าจุดนั้นอยู่นอกระยะ โปรแกรมจะแจ้งเตือน
ทำให้ปรับตำแหน่งหุ่นยนต์หรือ Fixture ก่อนเสียเวลา Teach ทีละจุด (ดูรายละเอียดใน Basic บทที่ 5)</div>
'''

BODY[("basic", 5)] = '''
<h2>ดูผลลัพธ์หลังรัน</h2>
<p>หลังรันจบ ตรวจสอบผลได้จาก 4 เครื่องมือหลักของ Process Simulate:</p>
<ul>
<li><strong>New Collision Check</strong> — ตั้งค่าและรัน Collision Detection ระหว่างหุ่นยนต์กับสิ่งแวดล้อม</li>
<li><strong>Minimal Distance</strong> — วัดระยะห่างที่น้อยที่สุดระหว่าง Object สองชิ้น แม้จะยังไม่ชนกันจริงก็ตาม ใช้ประเมินว่า "เฉียด" แค่ไหน</li>
<li><strong>Robot Reach Test</strong> — ตรวจว่าหุ่นยนต์เอื้อมถึงทุกตำแหน่ง Pose ได้จริงหรือไม่</li>
<li><strong>Smart Place</strong> — ช่วยหาตำแหน่งวาง Resource/Part อัตโนมัติที่ไม่ชนกับสิ่งแวดล้อม แทนการลากปรับเองทีละนิด</li>
</ul>

<table>
<tr><th>ผลลัพธ์</th><th>ความหมายเมื่อพบปัญหา</th></tr>
<tr><td>Collision Check มีรายการ</td><td>มีจุดที่ชนกันจริง ต้องปรับ Path หรือ Pose ก่อนส่งงานต่อ</td></tr>
<tr><td>Minimal Distance ใกล้ 0 แต่ไม่ชน</td><td>ยังไม่ชนแต่เสี่ยงสูง ควรเว้นระยะเผื่อเพิ่มก่อนส่ง OLP ไปหุ่นยนต์จริง</td></tr>
<tr><td>Cycle Time สูงกว่าที่ตั้งเป้า</td><td>ต้องปรับลำดับ Operation ใน PERT chart หรือลด Path ที่ไม่จำเป็น (ดู Intermediate บทที่ 4)</td></tr>
<tr><td>Reach Test ล้มเหลว</td><td>ตำแหน่งหุ่นยนต์หรือ Fixture ไม่เหมาะสม ต้องย้ายตำแหน่งใหม่ หรือใช้ Smart Place ช่วยหาตำแหน่งใหม่</td></tr>
</table>

<div class="note">
<strong>ข้อควรระวัง:</strong> อย่าลืมกด <strong>Reset</strong> ก่อนรันใหม่ทุกครั้ง ไม่งั้น Pose และสถานะการ Attach/Detach จะค้างจากรอบก่อนหน้า
ทำให้ผลจำลองคลาดเคลื่อน
</div>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> รันจบแล้ว Collision Report ว่างเปล่า (ไม่มีจุดชน) แต่ Cycle Time ยังสูงกว่าที่คาด ควรไปแก้ที่จุดไหนก่อน?
</div>
<div class="tip"><strong>เฉลย:</strong> ไม่มีการชนแปลว่า Path ปลอดภัยแล้ว ปัญหาด้าน Cycle Time ให้ไปดูที่ PERT chart ว่ามี Operation
ที่ควรทำขนานกัน (Parallel) แต่ถูกตั้งเป็นเรียงลำดับ (Sequential) อยู่หรือไม่ — ดูรายละเอียดที่ Intermediate บทที่ 4</div>
'''

BODY[("basic", 6)] = '''
<h2>รูปแบบไฟล์ Study และโครงสร้างข้อมูล</h2>
<p>Process Simulate มีสองรูปแบบการเก็บข้อมูล: แบบ <strong>Standalone (Single-User)</strong> ที่บันทึก Study เป็นไฟล์เดียว
นามสกุล <code>.psz</code> รวม Resource, Operation, Part ไว้ในไฟล์เดียว เหมาะกับงานคนเดียวหรือทีมเล็ก และแบบ
<strong>Process Simulate Multi-User</strong> ที่เก็บ Project เป็นฐานข้อมูลกลาง (Process Designer Database) พร้อมระบบ
Check-in/Check-out ตาม User Account เหมาะกับทีมใหญ่ที่ต้องแก้ไข Study เดียวกันพร้อมกันหลายคน (ดูรายละเอียดที่ Advanced บทที่ 7)</p>

<p>ไม่ว่าจะใช้แบบไหน ชิ้นส่วน 3 มิติที่สร้างเองจะถูกเก็บเป็น <strong>Component</strong> (ไฟล์ <code>.CO</code> หรือ
<code>.COJT</code> ซึ่งอิง JT Format) แยกจากไฟล์ Study หลัก ทำให้นำ Component เดียวกันไปใช้ซ้ำใน Study อื่นได้</p>

{steps}

<div class="tip">
<strong>Tip:</strong> ตั้งชื่อไฟล์ให้สื่อความหมายและใส่เลขเวอร์ชัน เช่น <code>Cell01_PickPlace_v03.psz</code>
แทนการ Save ทับชื่อเดิมตลอดเวลา จะช่วยย้อนกลับไปดูเวอร์ชันก่อนหน้าได้เมื่อแก้ไขแล้วพัง
</div>

<div class="note">
<strong>ข้อควรระวัง:</strong> ไฟล์ <code>.psz</code> ที่มี Resource/Part จำนวนมากอาจมีขนาดใหญ่ — ควร Save เก็บไว้หลายเวอร์ชัน
(ไม่ใช่ไฟล์เดียว) และสำรองไว้นอกเครื่อง เผื่อไฟล์เสียหรือ Study พังจากการแก้ไขผิดพลาด
</div>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> ถ้าทำงานร่วมกับเพื่อนร่วมทีมหลายคนในไฟล์ Study เดียวกัน จะป้องกันปัญหาไฟล์ทับกันได้อย่างไร?
</div>
<div class="tip"><strong>เฉลย:</strong> ใช้ Study Manager บริหารเวอร์ชันและสิทธิ์ Check-in/Check-out แทนการแชร์ไฟล์ <code>.psz</code>
ตรงๆ — ดูรายละเอียดที่ Advanced บทที่ 7</div>
'''.format(steps=step_list([
    "เลือก File → Save As แล้วตั้งชื่อไฟล์ให้สื่อความหมายพร้อมเลขเวอร์ชัน",
    "เลือกโฟลเดอร์เก็บไฟล์ที่มีการสำรองข้อมูล (เช่น โฟลเดอร์ที่ Sync กับระบบสำรองของทีม)",
    "ปิดโปรแกรมแล้วเปิดไฟล์เดิมกลับมาดูอีกครั้งเพื่อยืนยันว่าบันทึกถูกต้อง",
    "ทำสำเนาไฟล์สำคัญไว้อีกที่ก่อนเริ่มแก้ไขใหญ่ๆ",
]))

BODY[("intermediate", 1)] = '''
<h2>Resource ขั้นกลางที่ใช้บ่อย</h2>
<table>
<tr><th>Resource</th><th>ใช้ทำอะไร</th></tr>
<tr><td><strong>Device</strong></td><td>อุปกรณ์ที่มีการเคลื่อนไหวหรือสถานะเปลี่ยนได้ เช่น สายพาน, ประตูนิรภัย, แขนดัน</td></tr>
<tr><td><strong>Fixture</strong></td><td>อุปกรณ์ยึดจับชิ้นงานให้อยู่กับที่ระหว่างกระบวนการ</td></tr>
<tr><td><strong>Gripper / Tool</strong></td><td>อุปกรณ์ปลายแขนหุ่นยนต์ ใช้หยิบจับหรือทำงาน (เช่น ปืนเชื่อม, หัวพ่นสี)</td></tr>
<tr><td><strong>Conveyor</strong></td><td>สายพานลำเลียงชิ้นงานระหว่างสถานี มักผูกกับ Device เพื่อจำลองการเคลื่อนที่</td></tr>
</table>

<div class="note">
<strong>ข้อควรระวัง:</strong> Gripper/Tool ต้องผูกเข้ากับ Robot ก่อนใช้งาน (Mount) ไม่งั้นหุ่นยนต์จะไม่มี Tool Center Point (TCP)
ที่ถูกต้องสำหรับคำนวณตำแหน่ง Pose
</div>

<h2>สร้าง Resource ประเภท Device และดึงจาก Asset Library</h2>
<p>Resource ประเภท Device (เช่น สายพาน, ประตูนิรภัย, แขนดัน) สร้างได้เองจากโมเดล 3 มิติที่นำเข้ามา หรือดึงจาก
<strong>Asset Library</strong> ซึ่งมี Component สำเร็จรูปให้ดาวน์โหลดพร้อมใช้ (Download Asset and Robot) ทั้งหุ่นยนต์และอุปกรณ์มาตรฐาน
แทนการสร้าง Kinematics เองทั้งหมดตั้งแต่ต้น ช่วยประหยัดเวลาได้มากสำหรับ Resource ที่ไม่ต้องปรับแต่งพิเศษ</p>

<h2>เลือกใช้ Resource ให้เหมาะกับสถานการณ์</h2>
<p>หลักคร่าวๆ: ถ้าชิ้นงานต้อง "อยู่นิ่ง" ระหว่างทำงาน ใช้ <strong>Fixture</strong>, ถ้าต้อง "เคลื่อนที่ต่อเนื่อง" ใช้
<strong>Conveyor/Device</strong>, ถ้าเป็นสิ่งที่หุ่นยนต์ "ถืออยู่ที่ปลายแขน" ใช้ <strong>Gripper/Tool</strong></p>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> เซลล์เชื่อมชิ้นงานที่ต้องยึดชิ้นงาน 2 ชิ้นให้นิ่งขณะหุ่นยนต์เชื่อม แล้วปล่อยสายพานพาไปสถานีถัดไป
ต้องใช้ Resource ประเภทไหนบ้าง?
</div>
<div class="tip"><strong>เฉลย:</strong> ใช้ <strong>Fixture</strong> ยึดชิ้นงานระหว่างเชื่อม, <strong>Tool</strong> (ปืนเชื่อม) ติดที่ปลายแขน Robot,
และ <strong>Conveyor/Device</strong> ลำเลียงชิ้นงานหลังเชื่อมเสร็จไปสถานีถัดไป</div>
'''

BODY[("intermediate", 2)] = f'''
<h2>Robot Frame: Base Frame และ Tool Center Point Frame</h2>
<p>ตำแหน่งของหุ่นยนต์อ้างอิงจากสอง Frame หลักเสมอ: <strong>Base Frame</strong> (จุดฐานของหุ่นยนต์ที่ยึดกับพื้น/โครงสร้าง)
และ <strong>Tool Center Point Frame (TCPF)</strong> — จุดอ้างอิงที่ปลาย Gripper/Tool ไม่ใช่ปลายแขนหุ่นยนต์เอง
ทุกครั้งที่หุ่นยนต์เคลื่อนที่ไปยัง Pose หนึ่ง โปรแกรมคำนวณตำแหน่งจาก TCPF เทียบกับ Base Frame หากติดตั้ง Tool ยาวขึ้นหรือเปลี่ยน Tool
ต้องปรับ <strong>ExtTcp</strong> (External TCP) ให้ตรงกับ Tool ตัวใหม่เสมอ ไม่งั้นตำแหน่งที่ Teach ไว้จะคลาดเคลื่อนทั้งหมด</p>

<h2>Motion Type และ Path Editor</h2>
<p>การเคลื่อนที่ระหว่าง Pose แต่ละแบบให้ผลต่างกัน ตั้งค่าได้ผ่าน <strong>Path Editor</strong>:</p>
<table>
<tr><th>Motion Type</th><th>ลักษณะการเคลื่อนที่</th></tr>
<tr><td><strong>Joint</strong></td><td>แต่ละแกนหมุนไปพร้อมกันจนถึงเป้าหมาย เส้นทางไม่แน่นอนแต่เร็วที่สุด</td></tr>
<tr><td><strong>Linear</strong></td><td>TCP เคลื่อนที่เป็นเส้นตรงระหว่างสองจุด ควบคุมเส้นทางได้แน่นอน เหมาะกับงานที่ต้องเลี่ยงสิ่งกีดขวาง</td></tr>
<tr><td><strong>Circle</strong></td><td>TCP เคลื่อนที่เป็นส่วนโค้งผ่าน 3 จุดที่กำหนด ใช้กับงานที่ต้องการเส้นทางโค้งแม่นยำ</td></tr>
</table>

<h2>Frame of Reference เมื่อจัดวางตำแหน่ง</h2>
<p>เวลาใช้ Placement Manipulator ลากจัดตำแหน่ง Object จะอ้างอิงจุดหมุนได้หลายแบบ: <strong>Geometric Center</strong>
(จุดกึ่งกลางรูปทรงของ Object เอง), <strong>Working Frame</strong> (ระบบพิกัดอ้างอิงที่ตั้งไว้ล่วงหน้า) หรือ
<strong>Self</strong> (อ้างอิงตำแหน่งของ Object เองหลัง Placement) — เลือกให้ตรงกับสิ่งที่ต้องการ เช่น จัดวางชิ้นงานให้กึ่งกลาง Fixture
ควรใช้ Geometric Center ไม่ใช่ Self</p>

{step_list([
    "เปิด Attribute ของ Tool ที่ Mount กับ Robot",
    "กำหนดค่า ExtTcp ให้ตรงกับตำแหน่งปลายจริงของ Tool (เช่น ปลายปืนเชื่อม หรือปลาย Gripper)",
    "ทดสอบ Jog หุ่นยนต์แล้วสังเกตว่าจุดหมุนอ้างอิงเปลี่ยนไปตาม ExtTcp ที่ตั้งใหม่",
])}

<h2>Approach / Departure และ Via Point</h2>
<p>การเคลื่อนที่ตรงจากจุดหนึ่งไปอีกจุดหนึ่งอาจทำให้หุ่นยนต์ชนสิ่งกีดขวางระหว่างทาง จึงมักเพิ่มจุดกลาง:</p>
<table>
<tr><th>จุด</th><th>ใช้ทำอะไร</th></tr>
<tr><td><strong>Approach</strong></td><td>จุดก่อนถึงตำแหน่งจริง ให้หุ่นยนต์เข้าใกล้อย่างปลอดภัยก่อนหยิบ/วาง</td></tr>
<tr><td><strong>Departure</strong></td><td>จุดหลังจากหยิบ/วางเสร็จ ให้หุ่นยนต์ถอยออกมาก่อนเคลื่อนที่ไปจุดถัดไป</td></tr>
<tr><td><strong>Via Point</strong></td><td>จุดผ่านระหว่างทาง ใช้บังคับเส้นทางให้อ้อมสิ่งกีดขวาง</td></tr>
</table>

<div class="tip">
<strong>Tip:</strong> ใส่ Approach/Departure ให้ทุก Operation ที่มี Fixture หรืออุปกรณ์อยู่ใกล้ตำแหน่งหยิบ-วาง แม้ Reach test
จะผ่านก็ตาม เพราะเส้นทางตรงอาจตัดผ่านตัว Fixture ได้ในบางมุมของหุ่นยนต์
</div>

<div class="note">
<strong>คำถามฝึกคิด:</strong> เปลี่ยน Gripper ตัวใหม่ที่ยาวกว่าเดิม 5 ซม. แล้วหุ่นยนต์ไปหยิบชิ้นงานพลาดตำแหน่งทุกจุด เกิดจากอะไร?
</div>
<div class="tip"><strong>เฉลย:</strong> ลืมปรับค่า ExtTcp ให้ตรงกับความยาว Gripper ใหม่ — Pose เดิมที่ Teach ไว้อ้างอิงจาก TCP
ของ Gripper ตัวเก่า พอเปลี่ยน Tool ต้องปรับ ExtTcp ก่อน ไม่ใช่ไป Teach ใหม่ทุกจุด</div>
'''

BODY[("intermediate", 3)] = '''
<h2>Weld Point Operation (Spot Welding)</h2>
<p>งานเชื่อมจุด (Resistance Spot Welding) มีวงจรการทำงาน 3 ขั้นตอนต่อจุด: <strong>Motion</strong> (เคลื่อนที่เข้าจุดเชื่อม)
→ <strong>Welding</strong> (ปล่อยกระแสไฟเชื่อม) → <strong>Holding</strong> (กดค้างให้จุดเชื่อมเย็นตัว) — Process Simulate จำลองครบทั้ง 3 ขั้นตอนนี้
เมื่อสร้าง Weld Point Operation</p>

<table>
<tr><th>สิ่งที่ต้องตั้งค่า</th><th>รายละเอียด</th></tr>
<tr><td><strong>Set Kinematics ของ Spot Gun</strong></td><td>กำหนดการเปิด-ปิดหน้าสัมผัส (Electrode) ของปืนเชื่อม</td></tr>
<tr><td><strong>ประเภทปืนเชื่อม</strong></td><td><strong>X Gun</strong> หรือ <strong>C Gun</strong> ตามรูปทรงของปืนที่ใช้งานจริง</td></tr>
<tr><td><strong>Pose Editor / Tool Definition</strong></td><td>กำหนดท่าทางและ TCP ของปืนเชื่อมให้ตรงกับปลาย Electrode จริง</td></tr>
</table>

<div class="tip">
<strong>Tip:</strong> เมื่อสร้าง Weld Point ผ่านคำสั่ง Create Weld Point โปรแกรมมีเครื่องมือ <strong>Pie Chart และ Automatic
Approach Angle</strong> ช่วยแนะนำมุมเข้าจุดเชื่อมที่ปืนเชื่อมไม่ชนกับชิ้นงานหรือ Fixture โดยอัตโนมัติ ลองใช้ก่อนปรับมุมเอง
</div>

<h2>Weld Line Operation (Arc Welding)</h2>
<p>งานเชื่อมอาร์กต่อเนื่องเป็นเส้น (Continuous Arc/Seam Welding) ต้องตั้งค่าพารามิเตอร์เฉพาะที่ Weld Point ไม่มี:</p>
<table>
<tr><th>พารามิเตอร์</th><th>ความหมาย</th></tr>
<tr><td><strong>Travel Angle / Bisector Angle</strong></td><td>มุมเอียงของหัวเชื่อม (Torch) เทียบกับทิศทางเดินเชื่อมและแนวรอยต่อ</td></tr>
<tr><td><strong>Torch Offset</strong></td><td>ระยะห่างจากปลาย Torch ถึงชิ้นงาน มาตรฐานทั่วไปอยู่ที่ประมาณ 10-20 มม.</td></tr>
<tr><td><strong>TCPF (Tool Center Point Frame) ของ Torch</strong></td><td>กำหนดทิศทางเชื่อมผ่านเมนู <code>Tools → Continuous → Location Orientation</code></td></tr>
</table>

<div class="note">
<strong>ข้อควรระวัง:</strong> Weld Line/Arc Welding ต้องกำหนดความเร็วเคลื่อนที่ให้สม่ำเสมอตลอดแนว Welding Seam ไม่งั้นแนวเชื่อมจะหนา-บางไม่เท่ากัน
ต่างจาก Weld Point ที่หุ่นยนต์หยุดนิ่งตอนเชื่อมแต่ละจุด — งานที่มีชิ้นงานทรงกระบอกหรือหมุนได้ มักใช้ <strong>External Axis (Positioner)</strong>
หมุนชิ้นงานเข้าหา Torch แทนการขยับหุ่นยนต์รอบชิ้นงานทั้งหมด
</div>

<h2>การจัดการ Weld Gun Tip</h2>
<p>ปืนเชื่อมแบบ Spot Weld มีปลาย Tip ที่สึกหรอได้จากการใช้งาน โปรแกรมจึงมีการตั้งค่า Tip Dress/Tip Change เป็นระยะ
เพื่อจำลองว่าเมื่อไหร่ต้องหยุดเซลล์ไปเปลี่ยน/เจียร Tip ซึ่งกระทบ Cycle Time รวมของเซลล์ด้วย</p>

<div class="tip">
<strong>Tip:</strong> เมื่อสร้างจุดเชื่อมจำนวนมากในเซลล์เดียว ให้จัดกลุ่มจุดที่อยู่ใกล้กันเรียงลำดับตามความต่อเนื่องของตำแหน่ง
แทนการเรียงตามเลขจุดที่ลูกค้าให้มา จะช่วยลดระยะทางเคลื่อนที่รวมของหุ่นยนต์ได้มาก (ดูตัวอย่างจริงที่ Example File)
</div>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ทำไมงานเชื่อมตัวถังรถยนต์ส่วนใหญ่ใช้ Weld Point Operation มากกว่า Weld Line Operation?
</div>
<div class="tip"><strong>เฉลย:</strong> โครงสร้างตัวถังรถยนต์ส่วนใหญ่เชื่อมแบบจุด (Spot Weld) เพราะแข็งแรงพอและเร็วกว่า
ส่วน Weld Line มักใช้กับงานที่ต้องการรอยเชื่อมต่อเนื่องรับแรงสูง เช่น ตะเข็บถังหรือโครงสร้างที่ต้องกันรั่ว</div>
'''

BODY[("intermediate", 4)] = '''
<h2>Parallel และ Sequential Operation ใน PERT chart</h2>
<p>PERT chart แสดงว่า Operation ไหนต้องรอ Operation ก่อนหน้าให้เสร็จก่อน (Sequential) และ Operation ไหนทำพร้อมกันได้
(Parallel) — การจัดกลุ่ม Operation ที่ไม่ได้พึ่งพากันจริงให้เป็น Parallel คือวิธีหลักในการลด Cycle Time รวมของเซลล์
โดยไม่ต้องเพิ่มอุปกรณ์</p>

<table>
<tr><th>รูปแบบ</th><th>เมื่อไหร่ควรใช้</th></tr>
<tr><td><strong>Sequential</strong></td><td>Operation ที่ผลลัพธ์ของอันก่อนหน้าจำเป็นต่ออันถัดไป เช่น ต้อง Pick ก่อนถึงจะ Place ได้</td></tr>
<tr><td><strong>Parallel</strong></td><td>Operation ที่ทำงานคนละพื้นที่ คนละ Resource และไม่ต้องรอกัน เช่น หุ่นยนต์ 2 ตัวเชื่อมคนละฝั่งของชิ้นงาน</td></tr>
</table>

<h2>Time Attribute</h2>
<p>แต่ละ Operation มี Time Attribute กำหนดเวลาที่ใช้ (เช่น เวลาเชื่อมต่อจุด, เวลาหยิบ-วาง) ค่านี้รวมกันตามลำดับใน PERT chart
กลายเป็น Cycle Time ทั้งหมดของ Study — การมองเห็นว่า Operation ไหนกิน Time Attribute มากที่สุดคือจุดเริ่มต้นของการหาคอขวด</p>

<h2>Object Flow Operation และ Set Current Operation</h2>
<p>เมื่อ Study มี Part ไหลผ่านหลายสถานี (เช่น จากพาเลทต้นทาง ผ่านหุ่นยนต์ ไปจนถึงสายพานปลายทาง) ให้ใช้
<strong>Object Flow Operation</strong> กำหนดเส้นทางการไหลของ Part ตลอดทั้งเซลล์ในภาพเดียว แทนการไล่ดูทีละ Operation
ส่วน <strong>Set Current Operation</strong> คือคำสั่งที่ใช้สลับไปดู/แก้ไข Operation ใดๆ ใน Sequence Editor ได้ทันที
โดยไม่ต้องรันจากต้นทุกครั้งเมื่อต้องการโฟกัสแก้เฉพาะจุด</p>

<div class="tip">
<strong>Tip:</strong> ใช้ <strong>Export to Web</strong> ส่งออกลำดับ Operation และผล Cycle Time เป็นหน้าเว็บดูง่าย เหมาะเวลาต้อง
รายงานผลให้ทีมที่ไม่ได้ใช้ Process Simulate โดยตรงดูความคืบหน้า
</div>

<div class="tip">
<strong>Tip:</strong> ก่อนจะไปปรับ Path ให้เร็วขึ้น ลองดู PERT chart ก่อนว่ามี Operation ที่ควรขนานกันได้แต่ดันเรียงต่อกันอยู่หรือไม่ —
มักลด Cycle Time ได้มากกว่าการปรับความเร็วหุ่นยนต์เพียงอย่างเดียว
</div>

<div class="note">
<strong>คำถามฝึกคิด:</strong> เซลล์มี Robot A เชื่อมจุดฝั่งซ้ายและ Robot B เชื่อมจุดฝั่งขวาของชิ้นงานเดียวกัน แต่ถูกตั้งใน PERT chart
แบบ Sequential (B ต้องรอ A เชื่อมเสร็จก่อน) จะเกิดผลอะไร และแก้ได้อย่างไร?
</div>
<div class="tip"><strong>เฉลย:</strong> Cycle Time รวมจะสูงเกินจำเป็นเพราะ Robot B ว่างงานระหว่างรอ A ทั้งที่ทำงานคนละฝั่งไม่ชนกัน —
ถ้าตรวจสอบด้วย Collision Set (บทที่ 5) แล้วพบว่าไม่มีจุดชน ให้ปรับ PERT chart เป็น Parallel เพื่อให้ทั้งสองตัวเชื่อมพร้อมกัน</div>
'''

BODY[("intermediate", 5)] = '''
<h2>Collision Set คืออะไร</h2>
<p>แทนที่จะตรวจสอบการชนของทุก Object ในเซลล์กับทุก Object (ซึ่งช้าและมี False Positive เยอะ เช่น หุ่นยนต์ "ชน" กับพื้นโรงงานที่ตั้งอยู่)
Process Simulate ให้จัดกลุ่ม Object เป็น <strong>Collision Set</strong> แล้วกำหนดว่าคู่ไหนต้องเช็คการชนกันบ้าง เช่น
"Robot A" กับ "Fixture B" แต่ไม่ต้องเช็คกับพื้นโรงงาน</p>

{steps}

<h2>Static และ Dynamic Collision Detection</h2>
<table>
<tr><th>ประเภท</th><th>ลักษณะการทำงาน</th></tr>
<tr><td><strong>Static</strong></td><td>เช็คการชน ณ ตำแหน่ง Pose หนึ่งจุด เหมาะกับตรวจสอบจุดเริ่ม/จุดจบของ Operation</td></tr>
<tr><td><strong>Dynamic</strong></td><td>เช็คการชนตลอดเส้นทางเคลื่อนที่ระหว่าง Pose สองจุด จับการชนระหว่างทางที่ Static มองไม่เห็น</td></tr>
</table>

<div class="note">
<strong>ข้อควรระวัง:</strong> การเช็คแบบ Static เพียงอย่างเดียวอาจพลาดจุดชนกลางทาง (เช่น แขนหุ่นยนต์กวาดผ่าน Fixture ระหว่างเคลื่อนที่
แม้จุดเริ่มกับจุดจบจะไม่ชนก็ตาม) — งานที่มีอุปกรณ์หนาแน่นควรเปิด Dynamic Collision Detection ควบคู่ไปด้วยเสมอ
</div>

<p>นอกจากรู้ว่า "ชนหรือไม่ชน" ให้ใช้ <strong>Minimal Distance</strong> (จากบท Basic 5) วัดระยะห่างที่น้อยที่สุดระหว่างคู่ Object
ใน Collision Set ที่สนใจ — มีประโยชน์เมื่อ Collision Report บอกว่า "ไม่ชน" แต่ต้องการรู้ว่าเหลือระยะเผื่อความปลอดภัยแค่ไหนจริงๆ</p>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> ทำไมไม่ควรใส่ Object ทุกตัวในเซลล์ (รวมถึงพื้นโรงงานและผนัง) เข้า Collision Set เดียวกันหมด?
</div>
<div class="tip"><strong>เฉลย:</strong> จะทำให้ Collision Report เต็มไปด้วยรายการที่ไม่มีความหมาย (เช่น ฐานหุ่นยนต์ "ชน" กับพื้นที่มันตั้งอยู่)
จนหารายการที่เป็นปัญหาจริงยาก ควรแบ่ง Collision Set ตามคู่ Object ที่มีความเสี่ยงชนกันจริงเท่านั้น</div>
'''.format(steps=step_list([
    "เลือก Object ที่ต้องการตรวจสอบการชน (เช่น Robot, Fixture, Tool)",
    "สร้าง Collision Set ใหม่ แล้วเพิ่ม Object เหล่านั้นเข้ากลุ่ม",
    "กำหนดคู่ที่ต้องการเช็คการชนภายใน Set นั้น",
    "รัน Collision Detection แล้วดูผลใน Collision Report",
]))

BODY[("intermediate", 6)] = '''
<h2>Resource Library และการนำกลับมาใช้ซ้ำ</h2>
<p>เก็บ Robot, Gripper, Fixture มาตรฐานไว้ใน <strong>Resource Library</strong> กลาง แล้วดึงมาใช้ข้าม Study/โปรเจกต์ได้
โดยไม่ต้องสร้างใหม่ทุกครั้ง ช่วยให้ทีมงานหลายคนใช้ทรัพยากรชุดเดียวกันสอดคล้องกัน</p>

<p>ในเชิงโครงสร้างไฟล์ Library ถูกจัดเก็บเป็น <strong>Library Root Folder</strong> ที่รวมโฟลเดอร์ย่อยของ Component และไฟล์อื่นๆ
โดยแต่ละชิ้น Resource คือ <strong>Component</strong> (ไฟล์ <code>.CO</code> / <code>.COJT</code>) — เวลาต้องการหุ่นยนต์หรืออุปกรณ์มาตรฐาน
สามารถดึงจาก <strong>Asset Library</strong> ที่ Siemens จัดเตรียม Component สำเร็จรูปไว้ให้ดาวน์โหลดใช้ได้ทันที
แทนการสร้าง Kinematics เองตั้งแต่ศูนย์ (ดูขั้นตอน Download Asset and Robot ที่ Intermediate บทที่ 1)</p>

<table>
<tr><th>ประโยชน์</th><th>รายละเอียด</th></tr>
<tr><td>ลดเวลาสร้างโมเดลซ้ำ</td><td>Robot/Gripper รุ่นเดียวกันถูกสร้างและตั้งค่าไว้ครั้งเดียว ใช้ได้หลาย Study</td></tr>
<tr><td>ความสอดคล้องของข้อมูล</td><td>ทีมทุกคนใช้ข้อมูล Payload/Reach ของอุปกรณ์ชุดเดียวกัน ลดความผิดพลาดจากการพิมพ์ค่าเอง</td></tr>
<tr><td>ง่ายต่อการอัปเดต</td><td>แก้ค่าที่ Library ครั้งเดียว โครงการที่ดึงไปใช้ภายหลังได้ค่าที่อัปเดตแล้ว</td></tr>
</table>

<div class="tip">
<strong>Tip:</strong> ตั้งชื่อ Resource ใน Library ให้สื่อความหมายเสมอ เช่น <code>Robot_ABB_IRB6700_150kg</code>
เพราะเมื่อ Library มี Resource หลายร้อยตัว การไล่หาโดยไม่มีชื่อที่ชัดเจนจะยากมาก
</div>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ทีมมี Study 5 ไฟล์ที่ใช้ Robot รุ่นเดียวกัน แต่ตั้งค่า Payload ไม่ตรงกันทุกไฟล์ ควรแก้ปัญหานี้อย่างไร
ไม่ให้เกิดซ้ำในอนาคต?
</div>
<div class="tip"><strong>เฉลย:</strong> รวม Robot รุ่นนั้นเข้า Resource Library กลางค่าเดียว แล้วให้ทุก Study ดึงจาก Library แทนการสร้าง
Resource แยกเองในแต่ละไฟล์ — ป้องกันค่าตั้งต้นเพี้ยนกันระหว่างไฟล์ตั้งแต่ต้น</div>
'''

BODY[("advanced", 1)] = '''
<h2>Logic Block และ CEE คืออะไร</h2>
<p>
Process Simulate ใช้ <strong>Logic Block</strong> (Resource ประเภท Logic) ผูกกับ Signal ของอุปกรณ์ เช่น Gripper, Sensor, Door
เพื่อกำหนดเงื่อนไขการทำงาน คล้าย Ladder Logic ของ PLC โดยไม่ต้องเขียนโค้ดข้อความ เบื้องหลัง Logic Block ทั้งหมดถูกประมวลผลโดย
<strong>CEE (Cyclic Event Evaluator)</strong> — ตัวควบคุมตรรกะที่มากับ Process Simulate เอง (ตามที่แนะนำใน Basic บทที่ 1)
ทำให้ Study เปลี่ยนจากโหมด Time-based เป็น <strong>Event-based Simulation</strong> ที่ลำดับงานถูกขับเคลื่อนด้วย Signal จริง
แทนเส้นเวลาตายตัว — เป็นพื้นฐานเดียวกับที่ใช้ทำ Virtual Commissioning เชื่อมต่อ PLC จริงในโปรเจกต์ขนาดใหญ่
</p>

<div class="note">
<strong>ก่อนเริ่ม:</strong> สร้าง Logic Resource จากเมนู <code>Modeling → Logic Block</code> แล้วผูก Input/Output Signal
เข้ากับ Operation หรืออุปกรณ์ที่ต้องการควบคุม
</div>

<h2>ตัวอย่าง Logic: ประตูนิรภัยเปิดเมื่อหุ่นยนต์หยุดสนิท</h2>
<pre><code>// แนวคิด Signal wiring ใน Logic Block
Robot.AtHomePosition == true  AND  CycleComplete == true
    --&gt; SafetyDoor.Open = true</code></pre>

<div class="tip">
<strong>Tip:</strong> ตั้งชื่อ Signal ให้สื่อความหมายเสมอ (เช่น <code>SafetyDoor_Open_Req</code>) เพราะเมื่อ Study มี Signal
หลายสิบตัว การไล่ดู Logic Block จะยากมากถ้าตั้งชื่อไม่สื่อความหมาย
</div>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ทำไมต้องใช้ Logic Block แทนการเขียนเงื่อนไขไว้ใน Operation โดยตรง?
</div>
<div class="tip"><strong>เฉลย:</strong> Logic Block แยกตรรกะควบคุมออกจากลำดับ Operation ทำให้แก้เงื่อนไข (เช่น เปลี่ยนเวลาเปิดประตู)
ได้โดยไม่ต้องไปแก้ทุก Operation ที่เกี่ยวข้อง และดูภาพรวมการเชื่อม Signal ทั้งเซลล์ได้ในที่เดียว</div>
'''

BODY[("advanced", 2)] = '''
<h2>โครงสร้างพื้นฐานของ .NET API</h2>
<p>Process Simulate เปิด .NET API ผ่าน namespace <code>Tecnomatix.Engineering</code> ให้เขียนสคริปต์ C# ควบคุม Study
ได้โดยตรง แทนการคลิกทำเองในโปรแกรมทีละขั้นตอน เหมาะกับงานที่ต้องทำซ้ำจำนวนมาก เช่น ไล่อ่าน Operation หลายร้อยตัว</p>

<p>ตัวอย่างสคริปต์ไล่อ่านรายการ Operation ทั้งหมดใน Study แบบอัตโนมัติ:</p>
<pre><code>using Tecnomatix.Engineering;

public class ListOperations
{
    public static void Run()
    {
        PmStudy study = PS.Study;
        foreach (PmOperation op in study.GetAllOperations())
        {
            Console.WriteLine("Operation: " + op.Name + " | Time: " + op.Time);
        }
    }
}</code></pre>

<div class="note">
<strong>ข้อควรระวัง:</strong> ก่อนรันสคริปต์ตรวจสอบว่ามี Study เปิดอยู่จริง (<code>PS.Study</code> ไม่เป็น null) ไม่งั้นสคริปต์จะ error
ทันทีตั้งแต่บรรทัดแรก
</div>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> ถ้าต้องการนับจำนวน Operation ทั้งหมดที่ Time มากกว่า 5 วินาที จะปรับสคริปต์ตัวอย่างข้างบนอย่างไร?
</div>
<div class="tip"><strong>เฉลย:</strong> เพิ่มตัวแปรนับและเงื่อนไข <code>if (op.Time &gt; 5)</code> ภายในลูป <code>foreach</code> แล้ว
เพิ่มค่าตัวแปรนับทีละ 1 เมื่อเงื่อนไขเป็นจริง จากนั้นพิมพ์ผลรวมหลังจบลูป</div>
'''

BODY[("advanced", 3)] = '''
<h2>สลับ Resource อัตโนมัติแล้วเช็คการชนซ้ำ</h2>
<p>ใช้แทนการปรับ Layout ด้วยมือทีละแบบ เมื่อต้องการเทียบหลาย Scenario เช่น ตำแหน่งหุ่นยนต์หลายจุด</p>
<pre><code>using Tecnomatix.Engineering;

public class CollisionSweep
{
    public static void Run()
    {
        double[] robotOffsets = { 0, 50, 100 };
        foreach (double offset in robotOffsets)
        {
            // ปรับตำแหน่ง Robot Resource แล้วรัน Collision Detection
            PS.CollisionDetection.RunOnce();
            Console.WriteLine("Offset " + offset + " -&gt; collisions: "
                + PS.CollisionDetection.CollisionCount);
        }
    }
}</code></pre>

<div class="tip">
<strong>Tip:</strong> เก็บผลลัพธ์แต่ละ Scenario ลง List หรือเขียนออกไฟล์ CSV แทนการพิมพ์ผลลัพธ์ทาง Console อย่างเดียว
จะช่วยให้เปรียบเทียบหลาย Scenario ย้อนหลังได้ง่ายกว่า โดยเฉพาะเมื่อสลับหลายสิบค่า
</div>

<div class="note">
<strong>คำถามฝึกคิด:</strong> เมื่อไหร่ควรเขียนสคริปต์แบบนี้ แทนการปรับตำแหน่งด้วยมือใน Graphics Viewer?
</div>
<div class="tip"><strong>เฉลย:</strong> เมื่อต้องเทียบหลาย Scenario ที่มีรูปแบบชัดเจน (เช่น สลับตำแหน่งเป็นช่วงๆ) และต้องทำซ้ำบ่อย —
สคริปต์ทำให้ผลลัพธ์แม่นยำสม่ำเสมอและประหยัดเวลากว่าการคลิกปรับเองทีละ Scenario มาก</div>
'''

BODY[("advanced", 4)] = '''
<h2>Online กับ Offline Programming ต่างกันอย่างไร</h2>
<table>
<tr><th>รูปแบบ</th><th>ขั้นตอน</th></tr>
<tr><td><strong>Online (Teaching หน้างาน)</strong></td><td>Move Robot to Location → Record Position, Motion &amp; Speed ผ่าน Pendant จริง → Edit/Run Program บน Controller</td></tr>
<tr><td><strong>Offline (OLP)</strong></td><td>Create/Edit ใน Simulation Software → Upload to Simulation → Download to Controller ผ่าน USB/LAN → Run Program กับหุ่นยนต์จริง</td></tr>
</table>
<p>OLP แปลง Pose/Path ที่ Teach ไว้ในซอฟต์แวร์เป็นโปรแกรมควบคุมในภาษาเฉพาะของยี่ห้อหุ่นยนต์ เช่น RAPID (ABB), KRL (KUKA),
INFORM/TP (FANUC/YASKAWA) แล้วส่งไฟล์นั้นไปโหลดใช้กับ Controller จริงได้ทันที ลดเวลา Teach หน้างานลงมาก</p>

<h2>Motion Planner (MOP): ทำไมความแม่นยำจึงต่างกันตามระดับ</h2>
<p>เบื้องหลังการจำลองการเคลื่อนที่มีหลายระดับความแม่นยำ ให้เลือกใช้ตามความสำคัญของงาน:</p>
<table>
<tr><th>ระดับ</th><th>ความแม่นยำโดยประมาณ</th></tr>
<tr><td><strong>Kinematics (Direct/Inverse)</strong></td><td>คำนวณตำแหน่งจากมุมข้อต่อโดยตรง เร็วแต่ไม่สะท้อนพฤติกรรม Controller จริง</td></tr>
<tr><td><strong>DMC (Dynamic Controller Model)</strong></td><td>จำลองพฤติกรรม Controller แบบทั่วไป แม่นยำประมาณ 80% ของการเคลื่อนที่จริง</td></tr>
<tr><td><strong>DMC + RRS (Realistic Robot Simulation)</strong></td><td>ใช้ RCS (Robot Controller Software ของแต่ละยี่ห้อ) จำลอง Cycle Time และเส้นทางใกล้เคียงหุ่นยนต์จริงที่สุด</td></tr>
</table>
<p>เมื่อเชื่อมต่อ Logic และคำสั่งหุ่นยนต์เข้าด้วยกันแบบเต็มรูปแบบ (RRS + Logic + Robot Command) เรียกว่า
<strong>ESRC (Emulated Specific Robot Controller)</strong> — ใช้สำหรับ Virtual Commissioning ที่ต้องการความแม่นยำสูงสุด</p>

{steps}

<div class="note">
<strong>ข้อควรระวัง:</strong> แม้ตรวจสอบใน Process Simulate แล้วว่าไม่ชนและ Reach ได้ทุกจุด ควรทดสอบ Path ที่ความเร็วต่ำในเครื่องจริงอีกครั้ง
ก่อนรันเต็มความเร็ว เพราะความคลาดเคลื่อนเล็กน้อยของการติดตั้งอุปกรณ์จริงอาจต่างจากโมเดลเล็กน้อย
</div>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> ทำไมต้องเลือก Robot Controller/ยี่ห้อให้ตรงกับหุ่นยนต์จริงก่อน Export เสมอ?
</div>
<div class="tip"><strong>เฉลย:</strong> แต่ละยี่ห้อหุ่นยนต์ใช้ภาษาโปรแกรมและไวยากรณ์คำสั่งต่างกัน (RAPID, KRL, INFORM) การเลือกผิดยี่ห้อจะได้ไฟล์
ที่ Controller จริงอ่านไม่ได้ หรือแปลความหมายคำสั่งผิดจนหุ่นยนต์เคลื่อนที่ไม่ตรงกับที่จำลองไว้</div>
'''.format(steps=step_list([
    "ตรวจสอบว่า Operation และ Pose ทั้งหมดผ่าน Reachability และ Collision Check แล้ว",
    "คลิกขวา Robot → Robot Properties → Robot Setup เพื่อเลือก Controller Setup file ให้ตรงรุ่น",
    "เลือก Controller Version ที่ตรงกับหุ่นยนต์จริง แล้ว Browse ไฟล์ Machine Data (เช่น ALL.PRM, TOOL.CND, UFRAME.CND) จาก USB",
    "Import Tools และ Base Frame Data แล้วสั่ง Create/Update System Frames ให้ตรงกับหุ่นยนต์จริง",
    "Generate Program ส่งออกไฟล์โปรแกรม แล้วโหลดเข้า Controller ของหุ่นยนต์จริงผ่าน USB/LAN",
]))

BODY[("advanced", 5)] = '''
<h2>สร้าง Human ในเซลล์</h2>
<p>นอกจากหุ่นยนต์ Process Simulate ยังจำลองการทำงานของคนในเซลล์ได้ผ่านโมดูล <strong>Process Simulate Human</strong> —
สร้าง Human ได้เร็วด้วย <strong>Quick Create</strong> (เลือกรูปร่างมาตรฐานตามหน่วยงาน เพื่อให้ทุกการวิเคราะห์ใช้สัดส่วนคนชุดเดียวกัน)
หรือบันทึกไว้ใน <strong>Human Library</strong> เพื่อดึงกลับมาใช้ซ้ำโดยไม่ต้องตั้งค่าใหม่ทุกครั้ง — Library ปรับแต่งได้ทั้งฐานข้อมูล
สัดส่วนร่างกาย ขนาดตัวเฉพาะ และรูปลักษณ์ตามภูมิภาค</p>

<h2>Anthropometric Database และ Percentile</h2>
<p>ความแม่นยำของการวิเคราะห์ท่าทางขึ้นกับฐานข้อมูลสัดส่วนร่างกาย (Anthropometric Database) ที่เลือกใช้ ซึ่งมีให้เลือกตามภูมิภาค/มาตรฐาน
เช่น <strong>ANSUR/ANSUR II</strong> (กองทัพสหรัฐฯ), <strong>CHINESE</strong> (GB 10000-88), <strong>GERMAN</strong> (DIN 33402),
<strong>JAPANESE</strong>/<strong>KOREAN</strong> (ISO 7250-1), <strong>NHANES</strong> (ประชากรสหรัฐฯ) — เลือกฐานข้อมูลให้ตรงกับกลุ่มผู้ปฏิบัติงานจริง
เพื่อไม่ให้ผลวิเคราะห์คลาดเคลื่อน</p>
<p>ค่าที่แสดงในตารางสัดส่วนมักอ้างอิงเป็น <strong>Percentile</strong> เช่น <strong>50th percentile</strong> หมายถึงค่าเฉลี่ยที่เป็นไปได้มากที่สุด
ของกลุ่มตัวอย่าง — การออกแบบสถานีงานที่ดีมักตรวจสอบทั้งช่วง Percentile ต่ำและสูง ไม่ใช่แค่ค่าเฉลี่ยเพียงค่าเดียว
เพื่อให้คนตัวเล็กสุดและใหญ่สุดในกลุ่มยังทำงานได้โดยไม่บาดเจ็บ</p>

<h2>Human Posturing</h2>
<p>กำหนดท่าทางของ Human ได้ผ่าน <strong>Posture Library</strong> ซึ่งมีท่าทำงานสำเร็จรูป (เอื้อม, ก้ม, ยก) ให้เลือกใช้แทนการปรับข้อต่อทีละจุดเอง
ใกล้เคียงกับการ Teach Pose ของหุ่นยนต์ในแนวคิด แต่ใช้กับโครงร่างมนุษย์</p>

<h2>เครื่องมือวิเคราะห์การยศาสตร์ (Ergonomic Analysis)</h2>
<table>
<tr><th>เครื่องมือ</th><th>ใช้ประเมินอะไร</th></tr>
<tr><td><strong>RULA</strong> (Rapid Upper Limb Assessment)</td><td>ความเสี่ยงบาดเจ็บช่วงแขน-มือจากท่าทาง แรง และระยะเวลาทำงาน ให้คะแนน 4 ระดับ ตั้งแต่ท่าที่ยอมรับได้ (คะแนน 1-2) ไปจนถึงต้องแก้ไขทันที (คะแนน 7)</td></tr>
<tr><td><strong>OWAS</strong></td><td>วิเคราะห์ท่าทางหลัง แขน ขา และศีรษะ ออกเป็นรหัสท่าทาง 5 หลัก (เช่น 2321-1) บอกระดับความเร่งด่วนในการแก้ไข</td></tr>
<tr><td><strong>NIOSH (Low Back Analysis)</strong></td><td>ประเมินภาระที่หลังส่วนล่างเทียบกับค่ามาตรฐานที่ปลอดภัย</td></tr>
<tr><td><strong>Strain Index</strong></td><td>ความเสี่ยงบาดเจ็บของมือ/ข้อมือ/ปลายแขนจากงานที่ใช้มือซ้ำๆ ความถี่สูง</td></tr>
</table>
<p>Process Simulate ดึงค่าท่าทางจากโมเดลมาใส่ในเครื่องมือวิเคราะห์เหล่านี้ให้อัตโนมัติ ไม่ต้องวัดมุมข้อต่อเอง — ทำให้ตรวจสอบ Ergonomics
ได้ตั้งแต่ขั้นออกแบบเซลล์บนคอมพิวเตอร์ ก่อนมีคนทำงานจริงหน้างาน</p>

<div class="note">
<strong>ข้อควรระวัง:</strong> เมื่อคนและหุ่นยนต์ทำงานในพื้นที่ร่วมกัน ต้องตรวจสอบ Collision และใส่ตรรกะกันชน/Interlock ผ่าน CEE
เช่นเดียวกับกรณีหุ่นยนต์สองตัวทำงานร่วมกัน (ดู Advanced บทที่ 6) เพื่อความปลอดภัยของผู้ปฏิบัติงานจริง
</div>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> ทำไมต้องเลือก Anthropometric Database ให้ตรงกับกลุ่มผู้ปฏิบัติงานจริง แทนที่จะใช้ค่าเริ่มต้นของโปรแกรมเสมอ?
</div>
<div class="tip"><strong>เฉลย:</strong> สัดส่วนร่างกายเฉลี่ยต่างกันตามภูมิภาคและกลุ่มประชากรอย่างมีนัยสำคัญ (เช่น ฐานข้อมูล CHINESE/JAPANESE/KOREAN
ให้ค่าต่างจาก ANSUR ของกองทัพสหรัฐฯ) หากใช้ฐานข้อมูลผิดกลุ่ม ผลวิเคราะห์ RULA/OWAS อาจบอกว่าท่าทางปลอดภัย
ทั้งที่จริงไม่เหมาะกับสัดส่วนคนงานจริงในโรงงาน</div>
'''

BODY[("advanced", 6)] = '''
<h2>ปัญหาเมื่อหุ่นยนต์หลายตัวทำงานร่วมพื้นที่</h2>
<p>เมื่อหุ่นยนต์ 2 ตัวขึ้นไปมีพื้นที่ทำงานที่ทับซ้อนกัน (Shared Zone) การรันแต่ละตัวแยกกันโดยไม่มีการประสานงานเสี่ยงชนกันสูงมาก
แม้แต่ละตัวจะไม่ชนสิ่งกีดขวางอื่นเลยก็ตาม</p>

<h2>Interlock ด้วย Logic Block และ CEE</h2>
<p>แนวคิดคือ ก่อนหุ่นยนต์ตัวหนึ่งเข้า Shared Zone ต้องตรวจสอบว่าอีกตัวไม่อยู่ในโซนนั้น (Lock โซนไว้ให้ตัวเองก่อน) แล้วค่อยปล่อย
(Unlock) เมื่อออกจากโซน ตัวอื่นถึงจะเข้าไปได้ — สร้างเป็น Logic Block ผูก Signal ระหว่างสองหุ่นยนต์ แล้วให้ CEE (บทที่ 1) เป็นตัวประมวลผลเงื่อนไขนี้ระหว่างรัน Event-based Simulation ตามแนวคิดนี้:</p>
<pre><code>// แนวคิด Interlock Logic
Robot1.InZoneA == true  --&gt; Robot2.HoldAtWaitPoint = true
Robot1.InZoneA == false --&gt; Robot2.HoldAtWaitPoint = false</code></pre>

<div class="tip">
<strong>Tip:</strong> กำหนด Wait Point ของแต่ละหุ่นยนต์ให้อยู่นอก Shared Zone เสมอ เพื่อให้หุ่นยนต์ที่ต้องรอไม่กีดขวางเส้นทาง
ของตัวที่กำลังทำงานอยู่ในโซน
</div>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ถ้าไม่ใส่ Interlock จะเกิดอะไรขึ้นเมื่อทั้งสองหุ่นยนต์เข้าพื้นที่ Shared Zone พร้อมกัน?
</div>
<div class="tip"><strong>เฉลย:</strong> Collision Detection จะรายงานการชนกันของแขนหุ่นยนต์ทั้งสองตัวใน Shared Zone —
ในเซลล์จริงคือความเสียหายของอุปกรณ์ จึงต้องมี Interlock ทุกครั้งที่มีพื้นที่ทำงานร่วมกัน (ดูตัวอย่างเต็มที่ Example File)</div>
'''

BODY[("advanced", 7)] = '''
<h2>Standalone เทียบกับ Multi-User</h2>
<p>ย้อนกลับไปที่โครงสร้างข้อมูล 2 แบบจาก Basic บทที่ 6: แบบ <strong>Standalone (Single-User)</strong> เก็บ Study เป็นไฟล์
<code>.psz</code> เดี่ยว เหมาะกับงานคนเดียว ส่วนแบบ <strong>Process Simulate Multi-User</strong> เก็บข้อมูลไว้ใน
<strong>Process Designer Database</strong> กลาง (ฐานข้อมูล Oracle รูปแบบ <code>.dmp</code>) โดยแบ่งเป็น Project
(<code>.xml</code>) และมีระบบ <strong>User Account</strong> พร้อม Check-in/Check-out ผูกกับสิทธิ์ผู้ใช้แต่ละคน — เมื่อทีมงานหลายคน
ต้องแก้ไข Study เดียวกัน การใช้โครงสร้างแบบ Multi-User นี้ป้องกันปัญหาไฟล์ทับกันได้ดีกว่าการส่งไฟล์ <code>.psz</code> ไปมาทาง Email</p>

<table>
<tr><th>แนวคิด</th><th>รายละเอียด</th></tr>
<tr><td><strong>Check-out</strong></td><td>ดึง Cell/Station หรือ Object บางส่วนจากฐานข้อมูลกลางมาแก้ไข — ล็อกไม่ให้คนอื่นแก้ส่วนเดียวกันพร้อมกัน</td></tr>
<tr><td><strong>Check-in</strong></td><td>ส่งงานที่แก้แล้วกลับเข้าฐานข้อมูลกลาง พร้อมบันทึกเป็นเวอร์ชันใหม่</td></tr>
<tr><td><strong>Library Root Folder</strong></td><td>โฟลเดอร์กลางเก็บ Component (<code>.CO</code>/<code>.COJT</code>) ที่ Study ทุกไฟล์อ้างอิงร่วมกัน ไม่ว่าจะใช้ Standalone หรือ Multi-User</td></tr>
</table>

<div class="note">
<strong>ข้อควรระวัง:</strong> Check-out แล้วอย่าลืม Check-in กลับเมื่อทำงานเสร็จ — ถ้าค้าง Check-out ไว้นาน จะกีดขวางไม่ให้เพื่อนร่วมทีม
แก้ไขส่วนนั้นได้ แม้จริงๆ คุณจะทำงานเสร็จไปแล้วก็ตาม
</div>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> ทีม 3 คนต้องแก้ไขคนละสถานีในเซลล์เดียวกันพร้อมกัน ควรวางนโยบาย Check-out อย่างไรให้ทำงานพร้อมกันได้
โดยไม่ชนกัน?
</div>
<div class="tip"><strong>เฉลย:</strong> แบ่ง Check-out เป็นระดับ Object/สถานีย่อยแทนการ Check-out ทั้ง Study เป็นก้อนเดียว —
แต่ละคน Check-out เฉพาะ Resource/Operation ของสถานีตัวเอง ทำให้แก้ไขพร้อมกันได้โดยไม่ต้องรอคนอื่น Check-in ก่อน</div>
'''

BODY[("object-reference", 1)] = '''
<h2>Resource สายหลักที่ใช้บ่อย</h2>
<table>
<tr><th>Resource</th><th>หน้าที่</th><th>ดูรายละเอียดเพิ่มที่</th></tr>
<tr><td><strong>Robot</strong></td><td>หุ่นยนต์อุตสาหกรรม เคลื่อนที่ตาม Pose ที่ Teach ไว้</td><td>Basic บทที่ 4</td></tr>
<tr><td><strong>Device</strong></td><td>อุปกรณ์ที่มีการเคลื่อนไหวหรือสถานะเปลี่ยนได้ เช่น สายพาน, ประตูนิรภัย</td><td>Intermediate บทที่ 1</td></tr>
<tr><td><strong>Fixture</strong></td><td>อุปกรณ์ยึดจับชิ้นงานให้อยู่กับที่ระหว่างกระบวนการ</td><td>Intermediate บทที่ 1</td></tr>
<tr><td><strong>Tool / Gripper</strong></td><td>อุปกรณ์ปลายแขนหุ่นยนต์ ใช้หยิบจับหรือทำงาน เช่น ปืนเชื่อม, หัวพ่นสี</td><td>Intermediate บทที่ 2</td></tr>
</table>

<div class="tip">
<strong>ลองสาธิต:</strong> สร้าง Robot ใหม่ในเซลล์เปล่า Mount Gripper เข้าไป แล้วลอง Jog ดูว่าจุดหมุนอ้างอิง (TCP) อยู่ที่ปลาย
Gripper ไม่ใช่ปลายแขนหุ่นยนต์เอง — เห็นภาพความสัมพันธ์ระหว่าง Robot กับ Tool ได้ชัดที่สุดด้วยตา
</div>
'''

BODY[("object-reference", 2)] = '''
<h2>Operation แต่ละประเภท</h2>
<table>
<tr><th>Operation</th><th>หน้าที่</th><th>ดูรายละเอียดเพิ่มที่</th></tr>
<tr><td><strong>Pick / Place</strong></td><td>หยิบและวางชิ้นงาน — Operation พื้นฐานที่สุด</td><td>Basic บทที่ 4</td></tr>
<tr><td><strong>Weld Point</strong></td><td>เชื่อมเป็นจุด (Spot Weld)</td><td>Intermediate บทที่ 3</td></tr>
<tr><td><strong>Weld Line</strong></td><td>เชื่อมต่อเนื่องเป็นเส้น (Seam/Arc Weld)</td><td>Intermediate บทที่ 3</td></tr>
<tr><td><strong>Paste / Sealing</strong></td><td>ปาดกาวหรือฉีดวัสดุตามแนวเส้นทางที่กำหนด คล้าย Weld Line แต่ปล่อยวัสดุแทนกระแสไฟ</td><td>Case Study บทที่ 1</td></tr>
<tr><td><strong>Human Operation</strong></td><td>งานที่ Human Resource ทำ เช่น เดินไปหยิบ-วางหรือประกอบชิ้นงาน</td><td>Advanced บทที่ 5</td></tr>
</table>

<div class="tip">
<strong>ลองสาธิต:</strong> เปิด Study เดิมที่มี Operation Pick/Place จากบท Basic 4 แล้วลองสร้าง Weld Point Operation เพิ่มในเซลล์เดียวกัน
สังเกตว่า Attribute ที่ต้องตั้งต่างจาก Pick/Place อย่างไรบ้าง
</div>
'''

BODY[("object-reference", 3)] = '''
<h2>Object ประเภทตรรกะและเครื่องมือวิเคราะห์</h2>
<table>
<tr><th>Object</th><th>หน้าที่</th><th>ดูรายละเอียดเพิ่มที่</th></tr>
<tr><td><strong>Logic Block</strong></td><td>ผูก Signal กำหนดเงื่อนไขการทำงานของอุปกรณ์ในเซลล์</td><td>Advanced บทที่ 1</td></tr>
<tr><td><strong>Signal</strong></td><td>ค่าสถานะ (Input/Output) ที่ Logic Block และ Operation ใช้สื่อสารกัน</td><td>Advanced บทที่ 1</td></tr>
<tr><td><strong>Collision Set</strong></td><td>กลุ่ม Object ที่กำหนดคู่ตรวจสอบการชนอย่างมีระบบ</td><td>Intermediate บทที่ 5</td></tr>
<tr><td><strong>PERT chart / Sequence Editor</strong></td><td>เรียงลำดับและกำหนดความสัมพันธ์ก่อน-หลังของ Operation ทั้งหมด</td><td>Basic บทที่ 3, Intermediate บทที่ 4</td></tr>
</table>

<div class="tip">
<strong>ลองสาธิต:</strong> เปิด PERT chart ของ Study ที่มี Operation หลายตัว แล้วลองลากสลับให้ Operation สองตัวที่เคย Sequential
กลายเป็น Parallel ดูว่า Cycle Time รวมที่แสดงเปลี่ยนไปอย่างไรทันที
</div>
'''

BODY[("case-study", 1)] = '''
<h2>บริบทอุตสาหกรรม</h2>
<p>อุตสาหกรรมยานยนต์ใช้ Process Simulate ออกแบบเซลล์เชื่อมตัวถังรถ (Body-in-White) ซึ่งมักมีหุ่นยนต์หลายตัวเชื่อมจุดจำนวนมาก
(หลักร้อยถึงหลักพันจุดต่อคัน) ในพื้นที่จำกัด ต้องวางแผน Cycle Time ให้ทันตามเป้าการผลิตต่อวัน</p>

<h2>โจทย์ตัวอย่าง</h2>
<p>ออกแบบเซลล์เชื่อม 2 สถานีให้รองรับตัวถังรถ 1 คัน โดยมี Robot 4 ตัว (2 ตัวต่อสถานี) เชื่อมจุด Spot Weld รวม 120 จุด
ภายใน Cycle Time เป้าหมายไม่เกิน 90 วินาทีต่อคัน</p>

<h2>โครงสร้างโมเดล</h2>
<ul>
<li>Fixture ยึดตัวถังรถให้นิ่งตลอดกระบวนการเชื่อม (Intermediate บทที่ 1)</li>
<li>Robot แต่ละตัว Mount ปืนเชื่อมและตั้งค่า ExtTcp ให้ตรงกับปลายปืนจริง (Intermediate บทที่ 2)</li>
<li>สร้าง Weld Point Operation ครบทุกจุด จัดกลุ่มตามตำแหน่งเพื่อลดระยะทางเคลื่อนที่ (Intermediate บทที่ 3)</li>
<li>จัดลำดับใน PERT chart ให้ Robot 2 ตัวในสถานีเดียวกันเชื่อมพร้อมกันแบบ Parallel เมื่อไม่ชนกัน (Intermediate บทที่ 4)</li>
<li>ตรวจสอบ Collision Set ระหว่าง Robot คู่ที่ทำงานใกล้กัน (Intermediate บทที่ 5)</li>
</ul>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ถ้าตรวจสอบแล้วพบว่า Cycle Time เกินเป้า 90 วินาทีไปมาก แม้จัด Parallel Operation ทุกจุดที่ทำได้แล้ว
ควรพิจารณาทางเลือกอะไรต่อ?
</div>
<div class="tip"><strong>เฉลย:</strong> พิจารณาเพิ่มจำนวนหุ่นยนต์ต่อสถานี หรือแบ่งจุดเชื่อมออกเป็นสถานีเพิ่มเติม (เพิ่ม Station ขนาน)
แทนการพยายามบีบทุกจุดเชื่อมไว้ในสถานีเดิม — ต้องชั่งน้ำหนักกับต้นทุนอุปกรณ์เพิ่มเทียบกับ Throughput ที่ต้องการ</div>
'''

BODY[("case-study", 2)] = '''
<h2>บริบทอุตสาหกรรม</h2>
<p>งาน Material Handling เน้นความเร็วและความเสถียรมากกว่าความแม่นยำระดับ Weld — หุ่นยนต์ต้องหยิบชิ้นงานจากพาเลทหรือสายพาน
แล้วนำไปบรรจุลงกล่อง/พาเลทปลายทางซ้ำๆ ต่อเนื่องเป็นเวลานาน</p>

<h2>โจทย์ตัวอย่าง</h2>
<p>ออกแบบเซลล์หยิบสินค้าจากสายพาน (Conveyor) แล้ววางเรียงลงกล่องบรรจุภัณฑ์ 6 ชิ้นต่อกล่อง โดยไม่ทำให้สินค้าเสียหาย
และรักษา Cycle Time ให้ทันความเร็วสายพานต้นทาง</p>

<h2>โครงสร้างโมเดล</h2>
<ul>
<li>Conveyor ลำเลียงสินค้าเข้ามาต่อเนื่อง (Intermediate บทที่ 1)</li>
<li>Gripper แบบสุญญากาศหรือกลไกจับที่ไม่ทำให้สินค้าเสียหาย Mount กับ Robot (Intermediate บทที่ 2)</li>
<li>Operation Pick จากสายพาน และ Place ลงกล่องเรียงตามตำแหน่งที่กำหนด (Basic บทที่ 4)</li>
<li>ตรวจสอบ Reachability ทุกตำแหน่งในกล่อง โดยเฉพาะมุมลึกสุดของกล่อง (Basic บทที่ 5)</li>
<li>คำนวณ Cycle Time เทียบกับความเร็วสายพาน ปรับ Parallel Operation หากต้องใช้ Robot มากกว่า 1 ตัว (Intermediate บทที่ 4)</li>
</ul>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ถ้า Robot 1 ตัวหยิบ-วางไม่ทันความเร็วสายพาน จะแก้ปัญหาด้วยวิธีไหนได้บ้างโดยไม่ลดความเร็วสายพาน?
</div>
<div class="tip"><strong>เฉลย:</strong> เพิ่ม Robot ตัวที่สองทำงานสลับหรือขนานกัน (Parallel Operation ใน PERT chart) แบ่งสินค้าที่เข้ามาให้แต่ละตัว
หรือพิจารณาใช้ Gripper แบบหยิบได้หลายชิ้นต่อครั้งเพื่อลดจำนวนรอบที่ต้องทำ</div>
'''

BODY[("case-study", 3)] = '''
<h2>บริบทอุตสาหกรรม</h2>
<p>งาน Robotics Painting ไม่ได้ตรวจแค่ภาพเคลื่อนไหว (Visual Simulation) แต่ต้องประเมิน <strong>ความหนาของสีจริง</strong> ด้วย
เพราะระยะและความเร็วปืนพ่นที่ไม่คงที่ทำให้สีหนา-บางไม่เท่ากันบนชิ้นงานเดียวกัน — Process Simulate มี Paint Workflow เฉพาะทาง
4 ขั้นตอน: <code>Create Path → OLP → Prepare Surface → Paint Simulation</code></p>

<h2>โจทย์ตัวอย่าง</h2>
<p>ออกแบบเซลล์พ่นสีตัวถังชิ้นส่วนพลาสติก โดยหัวพ่น (Paint Gun) ต้องรักษาระยะห่างจากผิวชิ้นงานคงที่ตลอดเส้นทาง และความเร็วเคลื่อนที่สม่ำเสมอ
เพื่อให้ความหนาสีเท่ากันทั้งชิ้น</p>

<h2>โครงสร้างโมเดล</h2>
<ul>
<li>Tool หัวพ่นสี (Paint Gun) Mount กับ Robot และตั้งค่า ExtTcp ให้ตรงกับปลายหัวพ่นจริง (Intermediate บทที่ 2)</li>
<li>ใช้ <strong>Continuous Process Generator</strong> สร้าง Coverage Pattern อัตโนมัติจากการเลือกพื้นผิว (Face Selection) แทนการ Teach จุดพ่นทีละจุด</li>
<li>ใส่ Via Point ตามความโค้งของผิวชิ้นงานเพื่อรักษาระยะห่างคงที่ (Intermediate บทที่ 2)</li>
<li>รัน <strong>Paint Coverage Algorithm</strong> — นับจำนวนครั้งที่แต่ละจุดบนผิวถูก Paint Fan พ่นผ่าน (ต้องมี Collision/Penetration ระหว่าง Fan กับผิวจึงนับ)</li>
<li>รัน <strong>Paint Thickness Algorithm</strong> — คำนวณความหนาสี (หน่วยไมครอน) จาก Paint Graph ต่อ Brush ที่ระยะห่างและความเร็ว TCPF ที่กำหนด</li>
</ul>

<div class="tip">
<strong>คำถามฝึกคิด:</strong> ทำไมงานพ่นสีถึงต้องใส่ Via Point ถี่กว่างานเชื่อมจุดทั่วไปมาก?
</div>
<div class="tip"><strong>เฉลย:</strong> ผิวชิ้นงานพ่นสีส่วนใหญ่มีความโค้งต่อเนื่อง หาก Via Point ห่างเกินไป หุ่นยนต์จะเคลื่อนที่เป็นเส้นตรง
ระหว่างจุด ทำให้ระยะห่างจากผิวชิ้นงานไม่คงที่ (ใกล้ตรงกลางแคบลง ห่างตรงจุดที่ Via Point อยู่) ส่งผลให้สีหนา-บางไม่เท่ากัน</div>
'''

BODY[("case-study", 4)] = '''
<h2>บริบทอุตสาหกรรม</h2>
<p>งานประกอบอิเล็กทรอนิกส์ต้องการความแม่นยำระดับมิลลิเมตรหรือต่ำกว่า และมักทำงานในพื้นที่แคบที่มีอุปกรณ์วางชิดกันมาก
ทำให้ความเสี่ยงชนสูงกว่างานอุตสาหกรรมหนักทั่วไป</p>

<h2>โจทย์ตัวอย่าง</h2>
<p>ออกแบบเซลล์หยิบวางชิ้นส่วนอิเล็กทรอนิกส์ขนาดเล็กลงบนแผงวงจร โดยพื้นที่วางอุปกรณ์รอบข้างเหลือระยะห่างจากแขนหุ่นยนต์
ไม่ถึง 5 ซม. ในบางจุด</p>

<h2>โครงสร้างโมเดล</h2>
<ul>
<li>Fixture ยึดแผงวงจรให้นิ่งสนิทระหว่างวางชิ้นส่วน (Intermediate บทที่ 1)</li>
<li>Gripper ขนาดเล็กแม่นยำสูง Mount กับ Robot และตั้งค่า ExtTcp ละเอียด (Intermediate บทที่ 2)</li>
<li>สร้าง Collision Set เฉพาะคู่ Robot กับอุปกรณ์รอบข้างที่อยู่ใกล้ที่สุด แทนการเช็คทุก Object ในเซลล์ (Intermediate บทที่ 5)</li>
<li>ตรวจสอบ Reachability ทุกตำแหน่งวางชิ้นส่วนบนแผงวงจรก่อน Teach จริง (Basic บทที่ 5)</li>
<li>ใส่ Approach/Departure สั้นๆ ทุกจุดวาง เพื่อลดโอกาสแขนหุ่นยนต์กวาดผ่านอุปกรณ์ข้างเคียง (Intermediate บทที่ 2)</li>
</ul>

<div class="note">
<strong>คำถามฝึกคิด:</strong> ทำไมเซลล์งานอิเล็กทรอนิกส์แบบนี้ถึงควรตั้ง Collision Set เฉพาะคู่ที่เสี่ยงจริง แทนที่จะเช็คทุก Object
ในเซลล์แบบละเอียดที่สุดเพื่อความปลอดภัยสูงสุด?
</div>
<div class="tip"><strong>เฉลย:</strong> พื้นที่แคบทำให้ Object อยู่ใกล้กันตามธรรมชาติอยู่แล้ว การเช็คทุกคู่แบบละเอียดจะทำให้ Collision Report
เต็มไปด้วยรายการที่ไม่เกี่ยวข้อง (เช่น ฐานยึด Fixture ที่อยู่ใกล้กันแต่ไม่มีทางชน) จนหารายการที่เป็นความเสี่ยงจริงยากขึ้น</div>
'''

BODY[("tips-tricks", 1)] = '''
<h2>ทางลัดที่ช่วยให้ทำงานเร็วขึ้น</h2>
<ul>
<li>จัด Layout หน้าต่าง Graphics Viewer/Object Tree/Operation Tree ให้เห็นพร้อมกันตั้งแต่เริ่มงาน แล้ว Save Layout ไว้ใช้ทุกครั้ง</li>
<li>ใช้ Object Tree ค้นหา Resource/Operation ด้วยชื่อ แทนการไล่คลิกหาใน Graphics Viewer เมื่อ Study มี Object จำนวนมาก</li>
<li>ตั้งชื่อ Resource, Operation และ Signal ให้สื่อความหมายตั้งแต่ต้น ประหยัดเวลาไล่หาทีหลังมากกว่าตั้งชื่อสั้นๆ ที่จำยาก</li>
</ul>

<div class="tip">
<strong>Tip:</strong> ก่อนเริ่ม Teach Pose จำนวนมาก ให้ Save ไฟล์ไว้ก่อนเสมอ เผื่อ Jog พลาดจนโปรแกรมค้างหรือ Pose ผิดจำนวนมาก
จะได้ย้อนกลับมาจากจุดล่าสุดแทนเริ่มใหม่ทั้งหมด
</div>
'''

BODY[("tips-tricks", 2)] = '''
<h2>ข้อผิดพลาดที่มือใหม่เจอบ่อย</h2>
<table>
<tr><th>อาการ</th><th>สาเหตุที่พบบ่อย</th></tr>
<tr><td>ชิ้นงานไม่เคลื่อนที่ตามหุ่นยนต์</td><td>ลืมสั่ง Attach ใน Operation Pick (ดู Basic บทที่ 4)</td></tr>
<tr><td>ผลจำลองรอบใหม่คลาดเคลื่อนจากรอบก่อน</td><td>ลืมกด Reset ก่อนรันใหม่ ทำให้ Pose/Attach ค้างจากรอบก่อนหน้า (ดู Basic บทที่ 5)</td></tr>
<tr><td>หุ่นยนต์หยิบ-วางพลาดตำแหน่งหลังเปลี่ยน Gripper</td><td>ลืมปรับ ExtTcp ให้ตรงกับ Tool ตัวใหม่ (ดู Intermediate บทที่ 2)</td></tr>
<tr><td>Collision Report เต็มไปด้วยรายการไม่เกี่ยวข้อง</td><td>ยังไม่ได้จัด Collision Set แยกเฉพาะคู่ที่เสี่ยงจริง (ดู Intermediate บทที่ 5)</td></tr>
</table>

<div class="note">
<strong>ข้อควรระวัง:</strong> เมื่อโมเดลพฤติกรรมแปลกๆ ให้เช็ค 4 จุดนี้ก่อนไล่ดีบักลึกกว่านั้น เพราะเป็นสาเหตุที่พบบ่อยที่สุด
สำหรับคนที่เพิ่งเริ่มใช้โปรแกรม
</div>
'''

BODY[("tips-tricks", 3)] = '''
<h2>เทคนิคทำให้เซลล์ขนาดใหญ่รันเร็วขึ้น</h2>
<ul>
<li>ปิดการแสดงผลกราฟิกรายละเอียดสูง (เช่น Texture, Shadow) ระหว่างทดสอบ Path บ่อยๆ แล้วเปิดกลับตอนต้องการดูผลจริง</li>
<li>จำกัด Collision Set ให้เหลือเฉพาะคู่ Object ที่เสี่ยงชนจริง แทนการเช็คทุก Object กับทุก Object ในเซลล์ (ดู Intermediate บทที่ 5)</li>
<li>ปิดหรือซ่อน Resource ที่ไม่เกี่ยวข้องกับ Operation ที่กำลังทดสอบ ลดภาระการคำนวณ Collision ที่ไม่จำเป็น</li>
</ul>

<div class="tip">
<strong>Tip:</strong> เมื่อต้องทดสอบ Path ซ้ำๆ ระหว่างปรับ Pose ให้เปิด Dynamic Collision Detection เฉพาะ Object ที่กำลังแก้ไข
แล้วค่อยเปิดเช็คแบบเต็มเซลล์อีกครั้งก่อนสรุปผล จะประหยัดเวลารอผลระหว่างขั้นตอนปรับละเอียดได้มาก
</div>
'''

BODY[("tips-tricks", 4)] = '''
<h2>กับดัก .NET API และ Logic ที่พบบ่อย</h2>
<table>
<tr><th>อาการ</th><th>สาเหตุที่พบบ่อย</th></tr>
<tr><td>สคริปต์ error ตั้งแต่บรรทัดแรก</td><td>ไม่มี Study เปิดอยู่จริง ทำให้ <code>PS.Study</code> เป็น null (ดู Advanced บทที่ 2)</td></tr>
<tr><td>Logic Block ไม่ทำงานตามที่ตั้งใจ</td><td>ตั้งชื่อ Signal ซ้ำหรือสื่อความหมายไม่ชัด ทำให้ผูกผิดตัวโดยไม่รู้ตัว (ดู Advanced บทที่ 1)</td></tr>
<tr><td>สคริปต์รันช้าผิดปกติเมื่อ Study ใหญ่ขึ้น</td><td>เรียก Collision Detection แบบเต็มเซลล์ซ้ำๆ ในลูป แทนการจำกัดเฉพาะ Collision Set ที่เกี่ยวข้อง (ดู Advanced บทที่ 3)</td></tr>
<tr><td>หุ่นยนต์สองตัวยังชนกันแม้ใส่ Interlock แล้ว</td><td>ลืมกำหนด Wait Point ให้อยู่นอก Shared Zone จริง (ดู Advanced บทที่ 6)</td></tr>
</table>

<div class="note">
<strong>ข้อควรระวัง:</strong> เมื่อเขียนสคริปต์ควบคุมเซลล์ที่มี Logic Block อยู่แล้ว ให้ตรวจสอบว่าสคริปต์ไม่ไปเขียนทับ Signal
ที่ Logic Block กำลังควบคุมอยู่พร้อมกัน ไม่งั้นจะเกิดพฤติกรรมที่คาดเดาไม่ได้ว่าใครชนะในแต่ละรอบ
</div>
'''

# ---------------------------------------------------------------------------
def chapter_page(section, idx):
    title = SECTIONS[section]["chapters"][idx - 1]
    objs = OBJECTIVES[(section, idx)]
    objs_html = "\n".join(f"          <li>{o}</li>" for o in objs)
    body_content = BODY[(section, idx)].strip()

    # prev/next
    if idx > 1:
        prev_href = chapter_filename(section, idx - 1)
        prev_label = f"← ก่อนหน้า: {idx - 1}. {SECTIONS[section]['chapters'][idx - 2]}"
    else:
        prev_href = SECTIONS[section]["hub"]
        prev_label = f"← กลับหน้ารวมบท {SECTIONS[section]['label'].split(' — ')[0]}"

    n_chapters = len(SECTIONS[section]["chapters"])
    if idx < n_chapters:
        next_href = chapter_filename(section, idx + 1)
        next_label = f"ถัดไป: {idx + 1}. {SECTIONS[section]['chapters'][idx]} →"
    else:
        sec_idx = SECTION_ORDER.index(section)
        if sec_idx < len(SECTION_ORDER) - 1:
            next_sec = SECTION_ORDER[sec_idx + 1]
            next_href = SECTIONS[next_sec]["hub"]
            next_label = f"ถัดไป: {SECTIONS[next_sec]['label']} →"
        else:
            next_href = "index.html"
            next_label = "จบคอร์ส — กลับหน้าแรก"

    body = f'''        <h1>{idx}. {title}</h1>

        <div class="objectives">
          <p>วัตถุประสงค์การเรียนรู้</p>
          <ol>
{objs_html}
          </ol>
        </div>

{body_content}

        <div class="page-nav">
          <a href="{prev_href}">{prev_label}</a>
          <a href="{next_href}">{next_label}</a>
        </div>'''
    return page_html(f"{idx}. {title}", body, expand_section=section, active_top=section, active_chapter=idx)


if __name__ == "__main__":
    for sec in SECTION_ORDER:
        n = len(SECTIONS[sec]["chapters"])
        for i in range(1, n + 1):
            write(chapter_filename(sec, i), chapter_page(sec, i))
    # regenerate basic.html hub via the same generator for full consistency
    write(SECTIONS["basic"]["hub"], hub_page("basic"))
