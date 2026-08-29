# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_site import page_html, write

BODY = '''        <h1>Example File: ตัวอย่างเซลล์การผลิตจริง</h1>
        <p class="lead" style="max-width:46em;">
          ฝึกทำตามตัวอย่างเหล่านี้เพื่อความเข้าใจที่ลึกขึ้น ไฟล์ Study จริงของ Process Simulate ใช้นามสกุล <code>.psz</code>
          วางเพิ่มได้ในโฟลเดอร์ <code>examples/</code> ของ repo นี้
        </p>

        <div class="note">
          <strong>วิธีเพิ่มไฟล์ตัวอย่างจริง:</strong> วางไฟล์ <code>.psz</code> ลงในโฟลเดอร์ <code>examples/</code>
          แล้วใส่ลิงก์ดาวน์โหลดในหน้านี้ เช่น <code>&lt;a href="examples/cell-01.psz"&gt;ดาวน์โหลด&lt;/a&gt;</code>
        </div>

        <h2>ตัวอย่างที่ 1: เซลล์หยิบ-วางเดี่ยว (Single Robot Pick and Place)</h2>
        <p>เกี่ยวข้องกับ <a href="basic-04.html">Basic บทที่ 4</a></p>
        <p><strong>โครงสร้าง:</strong> <code>Robot → Operation(Pick) → Operation(Place)</code></p>
        <ul>
          <li>Robot: 6-axis ติดตั้ง Gripper แบบ 2 นิ้ว</li>
          <li>Part: ชิ้นงานที่จุดหยิบ 1 ตำแหน่ง จุดวาง 1 ตำแหน่ง</li>
          <li>Cycle Time เป้าหมาย: ไม่เกิน 8 วินาทีต่อรอบ</li>
        </ul>
        <p><strong>คำถามฝึกคิด:</strong> รันแล้วชิ้นงานไม่เคลื่อนที่ตามหุ่นยนต์ตอน Place ทั้งที่ Pose ถูกต้อง เกิดจากอะไร?</p>
        <div class="tip"><strong>เฉลย:</strong> ลืมสั่ง <code>Attach</code> ชิ้นงานเข้ากับปลายแขนหุ่นยนต์ใน Operation Pick — ต้อง Attach ตอนหยิบ และ Detach ตอนวาง ไม่งั้นชิ้นงานจะค้างอยู่ตำแหน่งเดิมตลอดการจำลอง</div>

        <h2>ตัวอย่างที่ 2: สองหุ่นยนต์ทำงานร่วมกันในเซลล์เดียว (Dual Robot Cell)</h2>
        <p>เกี่ยวข้องกับ <a href="advanced-06.html">Advanced บทที่ 6</a></p>
        <p><strong>โครงสร้าง:</strong> <code>Robot1 (Weld) + Robot2 (Handling)</code> ทำงานพร้อมกันในพื้นที่ที่มีจุดตัด (Shared Zone)</p>
        <p>ใช้ Logic Block ผูก Signal กันชนกัน (Interlock) ระหว่างสองหุ่นยนต์</p>
        <pre><code>// แนวคิด Interlock Logic
Robot1.InZoneA == true  --&gt; Robot2.HoldAtWaitPoint = true
Robot1.InZoneA == false --&gt; Robot2.HoldAtWaitPoint = false</code></pre>
        <p><strong>คำถามฝึกคิด:</strong> ถ้าไม่ใส่ Interlock จะเกิดอะไรขึ้นเมื่อทั้งสองหุ่นยนต์เข้าพื้นที่ Shared Zone พร้อมกัน?</p>
        <div class="tip"><strong>เฉลย:</strong> Collision Detection จะรายงานการชนกันของแขนหุ่นยนต์ทั้งสองตัวใน Shared Zone — ในเซลล์จริงคือความเสียหายของอุปกรณ์ จึงต้องมี Interlock ผ่าน Logic Block/CEE ทุกครั้งที่มีพื้นที่ทำงานร่วมกัน</div>

        <h2>ตัวอย่างที่ 3: จุดเชื่อม Weld Point และการลด Cycle Time</h2>
        <p>เกี่ยวข้องกับ <a href="intermediate-03.html">Intermediate บทที่ 3</a> และ <a href="intermediate-04.html">บทที่ 4</a></p>
        <p>Study ที่มี Weld Point Operation 20 จุด เรียงลำดับใน PERT chart แบบเส้นตรง (Sequential)</p>
        <p><strong>คำถามฝึกคิด:</strong> จะลด Cycle Time รวมของ Study นี้โดยไม่ลดจำนวนจุดเชื่อมได้อย่างไร?</p>
        <div class="tip"><strong>เฉลย:</strong> จัดกลุ่มจุดเชื่อมที่อยู่ใกล้กันให้หุ่นยนต์เคลื่อนที่เป็นเส้นทางสั้นที่สุด (Path Optimization) และพิจารณาใช้ 2 หุ่นยนต์เชื่อมคนละฝั่งพร้อมกัน (Parallel Operation ใน PERT chart) แทนการเรียงจุดแบบ Sequential ทั้งหมด</div>

        <div class="page-nav">
          <a href="tips-tricks-04.html">← ก่อนหน้า: Tips and Tricks บทที่ 4</a>
          <a href="index.html">กลับหน้าแรก</a>
        </div>'''

if __name__ == "__main__":
    write("examples.html", page_html("Example File", BODY, active_top="examples"))
