# -*- coding: utf-8 -*-
"""Lesson 06: Robot Painting -- from the Training/Basic step-by-step deck (Process Simulate 2502)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "ติด brush เข้ากับ gun แล้วติด gun ที่ปลายแขนหุ่นด้วย Mount Tool และดู brush ใน Paint Brush Editor",
    "ตั้งรางให้เป็นแกนที่ 7 ของหุ่นด้วย External Axes",
    "สร้างตาข่ายบนผิวชิ้นงานด้วย Create Mesh แล้วสร้างเส้นพ่นไปกลับด้วย Process Generator (6 เส้น)",
    "เล่น simulation เพื่อดู Coverage บนผิว ตรวจ Reach และตั้งสีของ Coverage Settings",
]

BODY = f'''
<p class="lead" style="max-width:46em;">งานพ่นสีฝากระโปรงรถด้วยหุ่นบนราง ทีละขั้น รวม 17 ขั้น — ติดหัวพ่น สร้างเส้นพ่นบนผิวชิ้นงาน แล้วดูว่าสีครอบคลุมทั่วหรือไม่</p>

<h2>ภาพรวม: ติดหัวพ่นแล้วสร้างเส้นพ่นสีบนฝากระโปรง</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Attach</td><td>ติด brush เข้ากับ gun ก่อน</td></tr>
<tr><td>02</td><td>Mount Tool</td><td>ติด gun ที่ปลายแขนหุ่น</td></tr>
<tr><td>03</td><td>Paint Brush Editor</td><td>brush ที่หุ่นใช้พ่น</td></tr>
<tr><td>04</td><td>External Axes</td><td>ให้รางเป็นแกนที่ 7 ของหุ่น</td></tr>
<tr><td>05</td><td>Create Mesh</td><td>แบ่งผิวชิ้นงานเป็นตาข่าย</td></tr>
<tr><td>06</td><td>Process Generator</td><td>สร้างเส้นพ่นแบบไปกลับ</td></tr>
<tr><td>07</td><td>Coverage</td><td>ระบายสีบนผิวตอน Play</td></tr>
<tr><td>08</td><td>Reach</td><td>หุ่นเอื้อมถึงทุกจุดไหม</td></tr>
<tr><td>09</td><td>Coverage Settings</td><td>สีของจำนวนรอบที่พ่นทับ</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate 2502 · โฟลเดอร์ <code>06_ROBOT_PAINTING</code> · <code>Library\\</code> (หุ่น ราง gun brush รถ) · <code>1_</code> ถึง <code>3_</code> <code>.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>Attach + Mount</td><td>Attach brush เข้ากับ gun แล้ว Mount Tool ที่หุ่น</td><td>บท 1: ไฟล์ 1_</td></tr>
<tr><td>02</td><td>Brush Editor</td><td>ดู brush BrushAsym ของหุ่น</td><td>บท 1: ไฟล์ 1_</td></tr>
<tr><td>03</td><td>External Axes</td><td>Attach หุ่นกับราง + Robot Properties</td><td>บท 1: ไฟล์ 1_</td></tr>
<tr><td>04</td><td>Create Mesh</td><td>ตาข่ายบนผิวรถ</td><td>บท 2: ไฟล์ 2_</td></tr>
<tr><td>05</td><td>Process Generator</td><td>6 เส้นพ่นบนฝากระโปรง</td><td>บท 2: ไฟล์ 2_</td></tr>
<tr><td>06</td><td>Coverage</td><td>Play แล้วดูสีบนผิว</td><td>บท 2: ไฟล์ 3_</td></tr>
</table>
<p>ตัวเลขจากไฟล์ตัวอย่าง (อ่านจาก PS 2502): 4 resource (ราง หุ่น gun brush) · 6 Paint op · 5 จุดต่อเส้น ยาว 2 m · ช่วงวิ่งของราง j1 −500 ถึง 1500 mm · Coverage pattern บนฝากระโปรงห่างกัน 75 mm พ่นเสร็จใน <strong>22.75 วินาที</strong></p>

<p class="lead" style="max-width:46em;">งานพ่นสีฝากระโปรงรถด้วยหุ่นบนราง ทีละขั้น รวม 17 ขั้น — ติดหัวพ่น สร้างเส้นพ่นบนผิวชิ้นงาน แล้วดูว่าสีครอบคลุมทั่วหรือไม่</p>

<h2>ภาพรวม: ติดหัวพ่นแล้วสร้างเส้นพ่นสีบนฝากระโปรง</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>Attach</td><td>ติด brush เข้ากับ gun ก่อน</td></tr>
<tr><td>02</td><td>Mount Tool</td><td>ติด gun ที่ปลายแขนหุ่น</td></tr>
<tr><td>03</td><td>Paint Brush Editor</td><td>brush ที่หุ่นใช้พ่น</td></tr>
<tr><td>04</td><td>External Axes</td><td>ให้รางเป็นแกนที่ 7 ของหุ่น</td></tr>
<tr><td>05</td><td>Create Mesh</td><td>แบ่งผิวชิ้นงานเป็นตาข่าย</td></tr>
<tr><td>06</td><td>Process Generator</td><td>สร้างเส้นพ่นแบบไปกลับ</td></tr>
<tr><td>07</td><td>Coverage</td><td>ระบายสีบนผิวตอน Play</td></tr>
<tr><td>08</td><td>Reach</td><td>หุ่นเอื้อมถึงทุกจุดไหม</td></tr>
<tr><td>09</td><td>Coverage Settings</td><td>สีของจำนวนรอบที่พ่นทับ</td></tr>
</table>
<div class="tip">
<strong>สิ่งที่ต้องมี:</strong> Process Simulate · โฟลเดอร์ <code>06_ROBOT_PAINTING</code> · <code>Library\\</code> (หุ่น ราง gun brush รถ) · <code>1_</code> ถึง <code>3_</code> <code>.psz</code>
</div>
<h2>Workflow: 6 ช่วง</h2>
<table>
<tr><th>ช่วง</th><th>งาน</th><th>ทำอะไร</th><th>ไฟล์</th></tr>
<tr><td>01</td><td>Attach + Mount</td><td>Attach brush เข้ากับ gun แล้ว Mount Tool ที่หุ่น</td><td>บท 1: ไฟล์ 1_</td></tr>
<tr><td>02</td><td>Brush Editor</td><td>ดู brush BrushAsym ของหุ่น</td><td>บท 1: ไฟล์ 1_</td></tr>
<tr><td>03</td><td>External Axes</td><td>Attach หุ่นกับราง + Robot Properties</td><td>บท 1: ไฟล์ 1_</td></tr>
<tr><td>04</td><td>Create Mesh</td><td>ตาข่ายบนผิวรถ</td><td>บท 2: ไฟล์ 2_</td></tr>
<tr><td>05</td><td>Process Generator</td><td>6 เส้นพ่นบนฝากระโปรง</td><td>บท 2: ไฟล์ 2_</td></tr>
<tr><td>06</td><td>Coverage</td><td>Play แล้วดูสีบนผิว</td><td>บท 2: ไฟล์ 3_</td></tr>
</table>
<p>ตัวเลขจากไฟล์ตัวอย่าง (อ่านจากไฟล์ตัวอย่าง): 4 resource (ราง หุ่น gun brush) · 6 Paint op · 5 จุดต่อเส้น ยาว 2 m · ช่วงวิ่งของราง j1 −500 ถึง 1500 mm · Coverage pattern บนฝากระโปรงห่างกัน 75 mm พ่นเสร็จใน <strong>22.75 วินาที</strong></p>

<h2>ขั้นที่ 1: เปิด 1_Open_Paint_Study ดูของในเซลล์</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-01.jpg", "ขั้นที่ 1: เปิด 1_Open_Paint_Study ดูของในเซลล์"),
    step_list([
        'ElevatedRail ราง',
        'IRB5500 หุ่นพ่นสี',
        'Paint_Gun',
        'PaintBrush',
        'gun กับ brush ยังวางอยู่ที่พื้นข้างล้อหน้า',
        'หุ่นที่ท่า HOME',
        '1 Painting ชิ้นงาน (ตัวรถ)',
        'ราง',
    ])
)}

<h2>ขั้นที่ 2: Attach brush เข้ากับ gun</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-02.jpg", "ขั้นที่ 2: Attach brush เข้ากับ gun"),
    step_list([
        'ช่อง Search พิมพ์ Attach',
        'Home &gt; Tools &gt; Attachment &gt; Attach',
        'Attach Objects: PaintBrush (เลือกไว้ก่อน)',
        'One Way',
        'To Object: คลิก Paint_Gun ใน tree',
        'OK',
    ])
)}

<h2>ขั้นที่ 3: Mount Tool ติด gun ที่ปลายแขนหุ่น</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-03.jpg", "ขั้นที่ 3: Mount Tool ติด gun ที่ปลายแขนหุ่น"),
    step_list([
        'เลือกหุ่นใน tree &gt; แท็บ Robot &gt; Mount Tool',
        'Tool: คลิก Paint_Gun ใน tree',
        'Frame: Base Frame (ขึ้นให้เอง)',
        'Mount on: IRB5500_ProArm...',
        'Frame: TOOLFRAME',
        'Apply (ยังไม่ Close)',
    ])
)}

<h2>ขั้นที่ 4: Flip Tool (X) หมุน gun ทีละ 90° ให้หัวพ่นชี้ลง</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-04.jpg", "ขั้นที่ 4: Flip Tool (X) หมุน gun ทีละ 90° ให้หัวพ่นชี้ลง"),
    step_list([
        'หลัง Mount: หัวพ่นชี้ไปด้านข้าง',
        'ท่าที่ถูก: หัวพ่นและ brush ชี้ลงหาผิวรถ (เหมือนไฟล์ 2_)',
        'Flip Tool (X) กด 3 ครั้ง (ครั้งละ 90° รอบแกน X)',
        'ลูกศร: เลือกแกน X / Y / Z แล้ว Close',
    ])
)}

<h2>ขั้นที่ 5: Paint Brush Editor ดู brush ของหุ่น</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-05.jpg", "ขั้นที่ 5: Paint Brush Editor ดู brush ของหุ่น"),
    step_list([
        'เลือกหุ่น &gt; แท็บ Process &gt; Paint Brush Editor',
        'ปุ่ม New สร้าง brush ใหม่',
        'ปุ่ม Edit (เลือก brush ก่อน)',
        'BrushAsym brush ที่มีอยู่แล้ว',
        'Brush Name: BrushAsym',
        'Solid: Brush_200 (รูปทรงละอองสี)',
        'Origin Frame: TIP',
        'Cancel ไม่แก้แล้ว Close',
    ])
)}

<h2>ขั้นที่ 6: Attach หุ่นเข้ากับแคร่ของราง (lnk2)</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-06.jpg", "ขั้นที่ 6: Attach หุ่นเข้ากับแคร่ของราง (lnk2)"),
    step_list([
        'เลือกหุ่น &gt; Attach: Attach Objects = หุ่น',
        'To Object: lnk2 ของ ElevatedRail',
        'OK',
        'lnk1 ฐานราง/lnk2 แคร่ที่เลื่อนได้',
    ])
)}

<h2>ขั้นที่ 7: Robot Properties &gt; External Axes &gt; Add</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-07.jpg", "ขั้นที่ 7: Robot Properties &gt; External Axes &gt; Add"),
    step_list([
        'Search: Robot Properties &gt; แท็บ External Axes',
        'Add...',
        'Device: ElevatedRail',
        'Joint: j1',
        'Name: ElevatedRail:j1',
        'OK',
        'ขึ้นในรายการ &gt; Close',
    ])
)}

<h2>ขั้นที่ 8: Joint Jog เห็นแกนราง j1 เพิ่มเข้ามา</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-08.jpg", "ขั้นที่ 8: Joint Jog เห็นแกนราง j1 เพิ่มเข้ามา"),
    step_list([
        'j1 (ElevatedRail) แถวสุดท้าย',
        'ช่วง -500 ถึง 1500 mm',
        'พิมพ์ 1000 + Tab',
        'หุ่นเลื่อนไปตามราง &gt; Reset, Close',
    ])
)}

<h2>ขั้นที่ 9: Create Mesh บนชิ้นงาน Painting</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-09.jpg", "ขั้นที่ 9: Create Mesh บนชิ้นงาน Painting"),
    step_list([
        'เปิด 2_Paint_Gun_Brush &gt; เลือก Painting &gt; Create Mesh',
        'Painting ในรายการ',
        'เครื่องหมายถูก = มี mesh แล้ว',
        'Distance 20 mm',
        'Deviation 0.5 mm',
        'Angle 15°',
        'Preview แล้ว OK',
        'Preview: ผิวรถเป็นตาข่าย',
    ])
)}

<h2>ขั้นที่ 10: Mesh เดิมมีแล้ว: Yes เพื่อสร้างใหม่</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-10.jpg", "ขั้นที่ 10: Mesh เดิมมีแล้ว: Yes เพื่อสร้างใหม่"),
    step_list([
        '&quot;Mesh already exists ... overwrite?&quot; &gt; Yes',
        '&quot;Part Painting: Mesh created successfully&quot;',
        'OK แล้ว Close หน้าต่าง Create Mesh',
    ])
)}

<h2>ขั้นที่ 11: Continuous Process Generator เลือก face</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-11.jpg", "ขั้นที่ 11: Continuous Process Generator เลือก face"),
    step_list([
        'เลือกหุ่น &gt; Continuous Process Generator · Process: Coverage pattern',
        'Faces (ช่องเขียว): คลิกผิวฝากระโปรง &gt; 1 Faces',
        'Stroke direction Back and forth',
        'Spacing 75 mm',
    ])
)}

<h2>ขั้นที่ 12: Start / End point และจำนวนเส้น</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-12.jpg", "ขั้นที่ 12: Start / End point และจำนวนเส้น"),
    step_list([
        'คลิกช่อง Start point &gt; คลิกปลายล่างซ้ายของ face',
        'คลิกช่อง End point &gt; คลิกปลายบนขวา: ได้ 1 seam',
        'Strokes before 3',
        'Strokes after 2',
        'เส้นสีน้ำเงิน 6 เส้นวิ่งไปกลับ',
        'Number of seams: 6',
    ])
)}

<h2>ขั้นที่ 13: Mfg type = PaintContinuousMfg และค่าของ operation</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-13.jpg", "ขั้นที่ 13: Mfg type = PaintContinuousMfg และค่าของ operation"),
    step_list([
        'Paint_Robotic_Op (เปลี่ยนเอง)',
        'Robot: IRB5500',
        'Tool: Paint_Gun',
        'Mfg type: PaintContinuousMfg',
        '3D folder: Library\\mfg',
        'Tangent ZigZag',
        'Traverse 150 mm',
        'OK',
    ])
)}

<h2>ขั้นที่ 14: ได้ Paint_Robotic_Op 6 operation</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-14.jpg", "ขั้นที่ 14: ได้ Paint_Robotic_Op 6 operation"),
    step_list([
        'จุดพ่นบนผิวฝากระโปรง',
        'Paint_Robotic_Op (compound)',
        'Paint_Robotic_Op_1 ถึง',
        '_6 = 1 เส้นต่อ 1 op',
    ])
)}

<h2>ขั้นที่ 15: เปิด Coverage During Simulation</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-15.jpg", "ขั้นที่ 15: เปิด Coverage During Simulation"),
    step_list([
        'แท็บ Process &gt; ลูกศรของ Paint During Simulation',
        'Coverage During Simulation (ปุ่มเป็นสีฟ้า)',
        'Paint and Coverage Settings: ติ๊ก Coverage',
        'ติ๊ก Brush (เห็นละอองสี)',
        'Color Scale: สีตามจำนวนรอบที่พ่นทับ 1 ถึง 9+',
        'เลือก Paint_Robotic_Op &gt; Operation &gt; Set Current Operation',
    ])
)}

<h2>ขั้นที่ 16: Reach: หุ่นเอื้อมไม่ถึงจุดของเส้นใหม่</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-16.jpg", "ขั้นที่ 16: Reach: หุ่นเอื้อมไม่ถึงจุดของเส้นใหม่"),
    step_list([
        'Play ไฟล์ 2_ ที่สร้างเอง: may not reach Paint_Robotic_Op_1_ls2',
        'แก้ได้ด้วย Rotation / External Axes / Configuration',
    ])
)}

<h2>ขั้นที่ 17: Play ไฟล์ 3_Coverage_Pattern ดูสีบนผิว</h2>
{side_by_side(
    screenshot("assets/images/lessons/06-17.jpg", "ขั้นที่ 17: Play ไฟล์ 3_Coverage_Pattern ดูสีบนผิว"),
    step_list([
        'ละอองสี (brush) ลงบนผิวตามเส้น',
        'พ่นครบ 6 เส้นสีน้ำเงิน = พ่น 1 รอบ',
        'Sequence Editor: 6 op ต่อกันรวม 22.75 วินาที',
    ])
)}

<h2>ไฟล์ในบทเรียนและสิ่งที่อยู่ในแต่ละไฟล์</h2>
<table>
<tr><th>ไฟล์</th><th>สิ่งที่มี</th></tr>
<tr><td>1_Open_Paint_Study.psz</td><td>เริ่มบท 1: รางหุ่น gun brush รถ (gun กับ brush วางที่พื้น)</td></tr>
<tr><td>2_Paint_Gun_Brush.psz</td><td>เฉลยบท 1 / เริ่มบท 2: gun mount, brush attach, หุ่น attach lnk2, External Axis j1, mesh 20 mm</td></tr>
<tr><td>3_Coverage_Pattern.psz</td><td>เฉลยบท 2: Paint_Robotic_Op 6 op (5 จุดต่อเส้น) + via, ฐานหุ่น+100 mm</td></tr>
<tr><td>Library\\resource\\</td><td>elevatedrail, irb5500_proarm, paint_gun, paintbrush, paint_room</td></tr>
<tr><td>Library\\Part\\ และ mfg\\</td><td>Painting (รถ) และเส้น Paint_Robotic_Op_1 ถึง 6</td></tr>
</table>

<h2>เช็กลิสต์: ผู้เรียนทำได้ครบหรือยัง</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th><th>ตรวจด้วย</th></tr>
<tr><td>1</td><td>Attach brush กับ gun แล้ว Mount Tool + Flip</td><td>gun + brush ที่ปลายแขนหัวพ่นชี้ลง</td></tr>
<tr><td>2</td><td>เปิด Paint Brush Editor ดู brush</td><td>BrushAsym: Brush_200 / TIP</td></tr>
<tr><td>3</td><td>Attach หุ่นกับ lnk2 + External Axes</td><td>Joint Jog มี j1 หุ่นเลื่อนตามราง</td></tr>
<tr><td>4</td><td>Create Mesh บน Painting</td><td>Mesh created successfully</td></tr>
<tr><td>5</td><td>Continuous Process Generator</td><td>Number of seams 6 / Paint_Robotic_Op</td></tr>
<tr><td>6</td><td>Coverage During Simulation + Play</td><td>สีน้ำเงินบนฝากระโปรง</td></tr>
</table>

<h2>ปัญหาที่พบบ่อยและวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>Mount แล้ว brush ยังอยู่ที่พื้น</td><td>Attach brush กับ gun ก่อน Mount (Undo ไม่คืนการ Mount ให้เปิดไฟล์ใหม่)</td></tr>
<tr><td>Mount แล้วหัวพ่นชี้ผิดทาง</td><td>Flip Tool (X) ในหน้าต่าง Mount Tool ครั้งละ 90° (ไฟล์นี้ 3 ครั้ง)</td></tr>
<tr><td>หาปุ่ม Attach / Robot Properties ไม่เจอ</td><td>พิมพ์ในช่อง Search มุมขวาบนแล้วคลิกผลลัพธ์</td></tr>
<tr><td>Paint Brush Editor สีเทา</td><td>เลือกหุ่นก่อน (ไม่ใช่ gun)</td></tr>
<tr><td>Relocate หาเฟรมของ gun ไม่ได้</td><td>ลิสต์ To frame มีแค่ Self / Geometric center / Working frame ใช้วิธี Attach แทน</td></tr>
<tr><td>Process Generator ขึ้น Faces are missing</td><td>คลิกผิวในจอ 3D ตอนช่อง Faces เป็นสีเขียว</td></tr>
<tr><td>Play แล้วขึ้น Dynamic Reach Advisor</td><td>จุดไกลเกิน: ขยับฐาน/ใช้ External Axes / ลดจุดหรือเปิดไฟล์ 3_</td></tr>
</table>
'''
