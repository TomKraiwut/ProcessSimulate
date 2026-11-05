# -*- coding: utf-8 -*-
"""Lesson 08: AGV -- from the Training/Basic step-by-step deck (Process Simulate 2502)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "เปิด study แบบ Line Simulation Mode (event-based) แล้ว Insert Component",
    "สร้าง AGV, AGV Target และ AGV Carpet (พรมนำทางตามเส้นโค้ง)",
    "สั่งรถด้วย Simulation Panel: Force ความเร็วและเป้าหมาย (TargetIndex = ID ไม่ใช่ชื่อ)",
    "เพิ่ม LiDAR บน KUKA_AGV และสั่งหยุดฉุกเฉินด้วย EmergencyStop",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ให้รถ <strong>AGV</strong> วิ่งไปเป้าหมายด้วย signal ทีละขั้น รวม 12 ขั้น — ตั้งแต่เปิด study แบบ event-based สร้างรถ เป้าหมาย และพรม ไปจนถึงเซนเซอร์ LiDAR และการหยุดฉุกเฉิน</p>

<h2>ภาพรวม: ให้รถ AGV วิ่งไปเป้าหมายด้วย signal</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Line Simulation</td><td>เปิด study แบบ event-based</td></tr>
<tr><td>02</td><td>Create AGV</td><td>ให้ชิ้นส่วนเป็นรถ AGV</td></tr>
<tr><td>03</td><td>Create AGV Target</td><td>จุดหมายที่รถวิ่งไป</td></tr>
<tr><td>04</td><td>Create AGV Carpet</td><td>พรมนำทางรถวิ่งตามเส้น</td></tr>
<tr><td>05</td><td>Simulation Panel</td><td>Force ความเร็วและเป้าหมาย</td></tr>
<tr><td>06</td><td>Target ID</td><td>TargetIndex = ID ไม่ใช่ชื่อ</td></tr>
<tr><td>07</td><td>LiDAR</td><td>เซนเซอร์บน KUKA_AGV</td></tr>
<tr><td>08</td><td>EmergencyStop</td><td>สั่งรถหยุดทันที</td></tr>
<tr><td>09</td><td>Logic Block</td><td>ช่องสั่งและช่องสถานะของรถ</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate 2502 · โฟลเดอร์ <code>08_AGV</code> · <code>Library\\</code> (5 ไฟล์ .cojt) · <code>AGV_Step0</code> ถึง <code>Step3</code> <code>.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>1: เปิดแบบ Line Sim</td><td>System Root, Open in Line Simulation Mode, Insert Component</td><td>Step0</td></tr>
<tr><td>02</td><td>2: AGV + Target</td><td>Set Modeling Scope, Create AGV, Create AGV Target</td><td>Step0</td></tr>
<tr><td>03</td><td>3: Carpet</td><td>Create AGV Carpet จากเส้นโค้ง</td><td>Step1</td></tr>
<tr><td>04</td><td>4: Drive AGV</td><td>Simulation Panel, Force, Play</td><td>Step2</td></tr>
<tr><td>05</td><td>5: LiDAR</td><td>เซนเซอร์บน KUKA_AGV</td><td>Step3</td></tr>
<tr><td>06</td><td>6: E-Stop</td><td>Force EmergencyStop</td><td>Step3</td></tr>
</table>
<p>ใน study (อ่านจากไฟล์ใน PS 2502): <strong>2</strong> รถ AGV (AGV, KUKA_AGV) · <strong>4</strong> เป้าหมาย (AGV_Target_1 ถึง 4) · <strong>49</strong> signal (รถ 17 ต่อคัน + เป้าหมาย 5 ต่อจุด)</p>

<p class="lead" style="max-width:46em;">ให้รถ <strong>AGV</strong> วิ่งไปเป้าหมายด้วย signal ทีละขั้น รวม 12 ขั้น — ตั้งแต่เปิด study แบบ event-based สร้างรถ เป้าหมาย และพรม ไปจนถึงเซนเซอร์ LiDAR และการหยุดฉุกเฉิน</p>

<h2>ภาพรวม: ให้รถ AGV วิ่งไปเป้าหมายด้วย signal</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Line Simulation</td><td>เปิด study แบบ event-based</td></tr>
<tr><td>02</td><td>Create AGV</td><td>ให้ชิ้นส่วนเป็นรถ AGV</td></tr>
<tr><td>03</td><td>Create AGV Target</td><td>จุดหมายที่รถวิ่งไป</td></tr>
<tr><td>04</td><td>Create AGV Carpet</td><td>พรมนำทางรถวิ่งตามเส้น</td></tr>
<tr><td>05</td><td>Simulation Panel</td><td>Force ความเร็วและเป้าหมาย</td></tr>
<tr><td>06</td><td>Target ID</td><td>TargetIndex = ID ไม่ใช่ชื่อ</td></tr>
<tr><td>07</td><td>LiDAR</td><td>เซนเซอร์บน KUKA_AGV</td></tr>
<tr><td>08</td><td>EmergencyStop</td><td>สั่งรถหยุดทันที</td></tr>
<tr><td>09</td><td>Logic Block</td><td>ช่องสั่งและช่องสถานะของรถ</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>08_AGV</code> · <code>Library\\</code> (5 ไฟล์ .cojt) · <code>AGV_Step0</code> ถึง <code>Step3</code> <code>.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>1: เปิดแบบ Line Sim</td><td>System Root, Open in Line Simulation Mode, Insert Component</td><td>Step0</td></tr>
<tr><td>02</td><td>2: AGV + Target</td><td>Set Modeling Scope, Create AGV, Create AGV Target</td><td>Step0</td></tr>
<tr><td>03</td><td>3: Carpet</td><td>Create AGV Carpet จากเส้นโค้ง</td><td>Step1</td></tr>
<tr><td>04</td><td>4: Drive AGV</td><td>Simulation Panel, Force, Play</td><td>Step2</td></tr>
<tr><td>05</td><td>5: LiDAR</td><td>เซนเซอร์บน KUKA_AGV</td><td>Step3</td></tr>
<tr><td>06</td><td>6: E-Stop</td><td>Force EmergencyStop</td><td>Step3</td></tr>
</table>
<p>ใน study (อ่านจากไฟล์ตัวอย่าง): <strong>2</strong> รถ AGV (AGV, KUKA_AGV) · <strong>4</strong> เป้าหมาย (AGV_Target_1 ถึง 4) · <strong>49</strong> signal (รถ 17 ต่อคัน + เป้าหมาย 5 ต่อจุด)</p>

<h2>ขั้นที่ 1: System Root แล้ว Open in Line Simulation Mode</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-01.jpg", "ขั้นที่ 1: System Root แล้ว Open in Line Simulation Mode"),
    step_list([
        'Welcome Page &gt; System Root = ...\\08_AGV\\Library',
        'ปุ่มกลาง Open in Line Simulation Mode',
        'เลือก AGV_Step0_Insert_Component',
        'Open (โหลดราว 15 วินาที)',
    ])
)}

<h2>ขั้นที่ 2: Step0 มีชิ้นส่วน 5 ชิ้นจาก Library</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-02.jpg", "ขั้นที่ 2: Step0 มีชิ้นส่วน 5 ชิ้นจาก Library"),
    step_list([
        'Modeling &gt; Insert Component &gt; Library',
        'AGV, AGV_Target, Carpet, KUKA_AGV, Lidar_sensor',
        'AGV กล่องสีฟ้า (0, 5000)',
        'KUKA_AGV สีเทา (0, -5000)',
    ])
)}

<h2>ขั้นที่ 3: Set Modeling Scope ก่อนปุ่ม Create AGV จึงกดได้</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-03.jpg", "ขั้นที่ 3: Set Modeling Scope ก่อนปุ่ม Create AGV จึงกดได้"),
    step_list([
        'Create AGV เป็นสีเทาเมื่อเลือกชิ้นธรรมดา',
        'แท็บ Modeling &gt; Set Modeling Scope',
        'กลับแท็บ Control: Create AGV กดได้แล้ว',
        'ก่อน: เทา',
        'เลือก KUKA_AGV (ไอคอนเปลี่ยนเป็นเปิดแก้ไข)',
    ])
)}

<h2>ขั้นที่ 4: Create AGV ได้ Logic Block ของรถ</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-04.jpg", "ขั้นที่ 4: Create AGV ได้ Logic Block ของรถ"),
    step_list([
        'ช่องสั่ง (Entries) MotionPlannerType, Speed, TargetIndex ...',
        'ช่องสถานะ (Exits) ActualSpeed, Busy, CurrentTarget ...',
        'OK',
    ])
)}

<h2>ขั้นที่ 5: Create AGV Target แล้วดู signal ที่สร้าง</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-05.jpg", "ขั้นที่ 5: Create AGV Target แล้วดู signal ที่สร้าง"),
    step_list([
        'AGV_Target &gt; Set Modeling Scope &gt; Create AGV Target',
        'ID เลขประจำเป้าหมายใช้สั่งรถ',
        'KUKA_AGV_ 17 signal',
        'AGV_Target_ 5 signal',
    ])
)}

<h2>AGV Logic Block: ช่องสั่งและช่องสถานะ</h2>
{screenshot("assets/images/lessons/08-06.jpg", "AGV Logic Block: ช่องสั่งและช่องสถานะ")}

<h2>ขั้นที่ 6: Create AGV Carpet ให้เส้นเป็นพรมนำทาง</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-07.jpg", "ขั้นที่ 6: Create AGV Carpet ให้เส้นเป็นพรมนำทาง"),
    step_list([
        'เลือก Carpet',
        'เส้น Line, Spline, Arc, Polyline (8 เส้น)',
        'Control &gt; AGV &gt; Create AGV Carpet',
        '&quot;Carpet is now used as AGV carpet&quot; &gt; OK',
    ])
)}

<h2>ไม่มีพรม vs มีพรม: เส้นทางของรถต่างกัน</h2>
{screenshot("assets/images/lessons/08-08.jpg", "ไม่มีพรม vs มีพรม: เส้นทางของรถต่างกัน")}

<h2>ขั้นที่ 7: Simulation Panel ใส่ signal ของรถ</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-09.jpg", "ขั้นที่ 7: Simulation Panel ใส่ signal ของรถ"),
    step_list([
        'Control &gt; Debug &gt; Signals + Simulation Panel',
        'Ctrl+คลิก AGV_Speed, AGV_TargetIndex',
        'AGV_Busy, AGV_CurrentTarget (ดูสถานะ)',
        'รวม 4 signal',
        'ปุ่มแรก Add Signal to Viewer',
    ])
)}

<h2>ขั้นที่ 8: Force ความเร็ว 200 และเป้าหมาย 1 แล้ว Play</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-10.jpg", "ขั้นที่ 8: Force ความเร็ว 200 และเป้าหมาย 1 แล้ว Play"),
    step_list([
        'ติ๊ก Forced',
        'AGV_Speed = 200 (mm/s)',
        'AGV_TargetIndex = 1',
        'ปุ่ม Play ใต้หน้าจอ 3D',
        'รถวิ่งตามพรมถึงเป้าหมาย',
    ])
)}
<div class="note"><strong>ระวัง:</strong> ดับเบิลคลิกช่อง Forced Value แล้วลบค่าเดิมก่อนพิมพ์ ไม่อย่างนั้นตัวเลขต่อท้าย (พิมพ์ 1 ได้ 10) Play ครั้งแรกมีข้อความ Simulation slider กด OK</div>

<h2>ขั้นที่ 9: TargetIndex คือ ID ของเป้าหมาย ไม่ใช่เลขท้ายชื่อ</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-11.jpg", "ขั้นที่ 9: TargetIndex คือ ID ของเป้าหมาย ไม่ใช่เลขท้ายชื่อ"),
    step_list([
        'AGV_Target_2.ID = 4',
        'AGV_Target_1.ID = 3',
        'AGV_Target_4.ID = 2',
    ])
)}

<h2>ขั้นที่ 10: LiDAR Sensor บน KUKA_AGV</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-12.jpg", "ขั้นที่ 10: LiDAR Sensor บน KUKA_AGV"),
    step_list([
        'Detection range 1000 mm',
        'Coverage sector 120°',
        'Number of rays 20',
        'Fields',
        'Monitoring cases (ว่าง)',
        'สร้างใหม่: Control &gt; Sensors &gt; Create LiDAR Sensor',
    ])
)}

<h2>ขั้นที่ 11: Play: LiDAR วิ่งไปพร้อม KUKA_AGV</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-13.jpg", "ขั้นที่ 11: Play: LiDAR วิ่งไปพร้อม KUKA_AGV"),
    step_list([
        'KUKA_AGV + เส้นขอบ LiDAR ตอนเริ่ม',
        'พื้นที่สีเหลือง = รัศมีตรวจจับ วิ่งไปพร้อมรถ',
        'ถึงเป้าหมาย ID 1 ที่ (0, 0)',
    ])
)}

<h2>ขั้นที่ 12: EmergencyStop หยุดรถทันทีแล้ววิ่งต่อ</h2>
{side_by_side(
    screenshot("assets/images/lessons/08-14.jpg", "ขั้นที่ 12: EmergencyStop หยุดรถทันทีแล้ววิ่งต่อ"),
    step_list([
        'KUKA_AGV_Speed 100 / TargetIndex 3',
        'ติ๊ก Forced ที่ KUKA_AGV_EmergencyStop คลิกช่องค่า: แดง = OFF / เขียว = ON',
    ])
)}

<h2>ไฟล์ในบทเรียนและสิ่งที่อยู่ในแต่ละไฟล์</h2>
<table>
<tr><th>ไฟล์</th><th>สิ่งที่มี</th></tr>
<tr><td>AGV_Step0_Insert_Component.psz</td><td>AGV, AGV_Target, Carpet, KUKA_AGV, Lidar_sensor (ยังไม่มี signal)</td></tr>
<tr><td>AGV_Step1_Create_AGV_and_AGV_Target.psz</td><td>+ รถ 2 คันเป็น AGV + เป้าหมาย 3 จุด (signal 44 ตัว)</td></tr>
<tr><td>AGV_Step2_Create_AGV_Carpet.psz</td><td>+ พรม + AGV_Target_4 (signal 49 ตัว)</td></tr>
<tr><td>AGV_Step3_Lidar_Sensor.psz</td><td>+ LiDAR บน KUKA_AGV + ค่า Force ใน Simulation Panel</td></tr>
<tr><td>Library\\ (5 ไฟล์ .cojt)</td><td>AGV, AGV_Target, Carpet, KUKA_AGV, Lidar_sensor</td></tr>
</table>

<h2>เช็กลิสต์: ผู้เรียนทำได้ครบหรือยัง</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th><th>ตรวจด้วย</th></tr>
<tr><td>1</td><td>เปิด study แบบ Line Simulation Mode</td><td>แถบล่างขึ้น Line Simulation Mode</td></tr>
<tr><td>2</td><td>Set Modeling Scope + Create AGV / AGV Target</td><td>signal ของรถและเป้าหมายใน Signals</td></tr>
<tr><td>3</td><td>Create AGV Carpet</td><td>"Carpet is now used as AGV carpet"</td></tr>
<tr><td>4</td><td>Force Speed / TargetIndex แล้ว Play</td><td>รถวิ่งตามพรมถึงเป้าหมาย</td></tr>
<tr><td>5</td><td>อ่าน ID ของเป้าหมาย</td><td>บอกได้ว่า TargetIndex 3 ไปจุดไหน</td></tr>
<tr><td>6</td><td>EmergencyStop ON / OFF</td><td>รถหยุดแล้ววิ่งต่อ</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>เมนู Open in Line Simulation Mode กดไม่ติด</td><td>ใช้ปุ่มกลางใต้ System Root ในหน้า Welcome</td></tr>
<tr><td>Create AGV / AGV Target สีเทา</td><td>เลือกชิ้นนั้นแล้ว Modeling &gt; Set Modeling Scope ก่อน</td></tr>
<tr><td>พิมพ์ Forced Value แล้วได้ค่าผิด (1 เป็น 10)</td><td>ลบค่าเดิมก่อนพิมพ์</td></tr>
<tr><td>รถวิ่งไปผิดจุด</td><td>TargetIndex คือ ID ดูค่า ID ใน Simulation Panel</td></tr>
<tr><td>กด Play แล้วไม่มีอะไรเกิด</td><td>ปิดหน้าต่าง Signals ที่บังปุ่ม Play / กด OK ข้อความ Simulation slider</td></tr>
<tr><td>LiDAR ไม่ทำให้รถหยุดเอง</td><td>ต้องมี Fields / Monitoring Cases จาก SICK · บทนี้สั่ง EmergencyStop ด้วยมือ</td></tr>
</table>
'''
