---
date: 2026-09-24
slug: intrinsic-core-apache-robotics
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial isometric hero scene at a factory floor lit by dawn light.
  In the foreground, three industrial robot arms of different vendor
  brands work in choreography on a small electronics assembly line, each
  arm labeled with a colored tag "VENDOR A", "VENDOR B", "VENDOR C" to
  show hardware-agnostic. A translucent glowing cube floats above the
  line stamped "INTRINSIC CORE — APACHE 2.0". Inside the cube, four
  labeled modules stack like layers: "REAL-TIME CONTROL" / "MOTION +
  GRASP PLANNING" / "POSE ESTIMATION (NVIDIA FOUNDATIONPOSE)" / "DIGITAL
  TWIN + SIM". Above the factory a neon banner reads "ROSCON 2026 —
  TORONTO — 22 SEP" and a subtitle "PHYSICAL AI GOES OPEN SOURCE". Small
  side-panel widget shows a globe with 115 pin markers and text "5,000+
  DEVELOPERS — 115 COUNTRIES". Brand-neutral editorial isometric style
  with the visible "Intrinsic" and "Google/Alphabet" wordmarks, big
  contrasty labels and numbers sized for a 200px thumbnail, 1:1 aspect,
  no real human faces.
image: images/26-09-24-0615-04-intrinsic-core-apache-robotics.png
---

# Intrinsic Core open source — Alphabet ปล่อย robotics stack ระดับ manufacturing ใต้ Apache 2.0 ที่ ROSCon 2026

## TL;DR
- **22 ก.ย. ที่ ROSCon 2026 กรุง Toronto** — **Intrinsic** (บริษัท robotics ในเครือ Alphabet) เปิด source **Intrinsic Core™** ใต้ **Apache 2.0** — ROS-compatible robotics runtime พร้อม real-time control, motion + grasp planning, pose estimation ที่ base บน **NVIDIA FoundationPose**, digital twin, simulation, camera calibration, hardware driver
- **Positioning:** "**Physical AI** ที่เดินคู่ software agent" — ทีม dev สร้าง robot application ได้เหมือน software engineer สร้าง web app คือ combine building block ที่มีอยู่แล้ว ไม่ต้อง code capability พื้นฐานจากศูนย์
- **สัญญาณ scale:** Intrinsic ประกาศผู้ชนะ "AI for Industry Challenge" ครั้งแรก โฟกัส electronics assembly มี **5,000+ นักพัฒนา จาก 115 ประเทศ** เข้าร่วม; นี่คือชุมชน physical AI open source ระดับใหญ่ที่สุดที่เคยเห็น

## เกิดอะไรขึ้น

**เช้าวันจันทร์ 22 กันยายน ที่ ROSCon 2026 กรุง Toronto** — Intrinsic (บริษัทหุ่นยนต์ที่ Google spin ออกจาก X ในปี 2021, อยู่ใต้ Alphabet holding) ประกาศเปิด source **Intrinsic Core™** — package robotics capability + service ที่บริษัทใช้ใน real manufacturing deployment กับลูกค้าอย่าง Comau, Trumpf, Denso — ใต้ **Apache 2.0** license บน GitHub. Available ทันที pre-configured เป็น local runtime ที่ทำงานบน hardware ทั่วไป (Intel NUC-class, Nvidia Jetson-class) โดยไม่ต้อง cloud connection

**สิ่งที่ Intrinsic Core ประกอบด้วย 6 layer หลัก:**
- **Real-time control framework** hardware-agnostic (ทำงานกับ arm manipulator จาก ABB, Fanuc, UR, Denso, Franka, Kuka)
- **Motion + grasp planning** ที่มี collision detection ผ่าน point cloud + BVH
- **Pose estimation** base บน **NVIDIA FoundationPose** — ระบุตำแหน่ง 6DoF ของวัตถุใน scene จาก single RGB image
- **Digital twin + simulation** ที่ sync กับ physical robot ผ่าน ROS 2 topic
- **Camera calibration + eye-in-hand / eye-to-hand** utility
- **Pre-configured ROS-compatible hardware driver** สำหรับ arm + gripper + sensor 40+ รุ่น

**Positioning ที่ CEO Wendy Tan White อธิบายใน blog:** "**Intrinsic Core is our open source approach to Physical AI**". เรียก philosophy นี้ว่าเดินตาม pattern เดียวกับ software agent ecosystem — ผู้พัฒนา physical AI ควรได้ building block สำเร็จรูป (real-time control, planning, perception) เหมือน software engineer ยุค 2010s ได้ React/Kubernetes/Docker — ให้เอาเวลาไปแก้ปัญหา business layer แทนที่จะ implement kinematics solver จากศูนย์

**Signal scale ที่ Intrinsic เปิดวันเดียวกัน:** ประกาศผู้ชนะ **"AI for Industry Challenge"** ครั้งแรก โฟกัส **electronics assembly** — competition ที่มี **5,000+ นักพัฒนา + roboticist จาก 115 ประเทศ** เข้าร่วมในรอบ 4 เดือน. Winner (ทีม 3 คนจาก Berlin) สร้าง end-to-end pipeline ที่ pick-and-place PCB component ที่ต้องการ tolerance ±0.02mm บน hardware standard (UR5e arm + Robotiq gripper + Intel RealSense). Runner-up teams มาจาก Tokyo, Bangalore, São Paulo, Warsaw

**Timing ที่สำคัญ:** Intrinsic เพิ่งปิด transaction กับ Alphabet ในต้นปี 2026 ที่ปรับ status เป็น "independent Alphabet company" — ไม่ใช่ X moonshot อีกต่อไป, มี P&L ของตัวเอง. Open source Intrinsic Core เป็น **first big strategic move** หลัง restructure — บอกชัดว่าจะเดินสาย platform + ecosystem แทนที่จะเดินสาย proprietary service. เทียบ competitor: **Boston Dynamics** (Hyundai) เก็บ stack ปิด, **NVIDIA Isaac** เปิดบางส่วนแต่ก็ยัง lock-in ที่ NVIDIA hardware, **Figure AI** ปิดเต็ม; Intrinsic เดินสวนทาง

## ทำไมสำคัญ

**นี่คือ moment ที่ physical AI stack เดินตาม pattern เดียวกับ software AI stack.** ในโลก software เราเห็น pattern นี้ 2 ครั้ง: (1) Linux + Apache กลาย base ของ web ยุค 2000s, (2) TensorFlow/PyTorch/Hugging Face กลาย base ของ ML ยุค 2020s. Intrinsic Core เป็น candidate ตำแหน่งเดียวกันสำหรับ physical AI — โดยเฉพาะถ้าไม่มี competitor เจ้าไหนที่ open source stack ระดับ production-grade เท่านี้. NVIDIA Isaac เป็น competitor ที่ใกล้ที่สุด แต่ Isaac lock hardware ที่ NVIDIA GPU; Intrinsic Core hardware-agnostic

Pattern signal: **agent boundary กำลังขยายจาก digital ไป physical.** ตลอดปี 2025-2026 นิยาม "AI agent" คือ software agent — LLM ที่ tool-use ทำ workflow บน computer. ตอนนี้เห็นสาม signal ที่บอกว่า physical เป็นเฟสถัดไป: (1) Figure AI ระดม $1.5B Series C ต้นปี, (2) Tesla Optimus V3 spec sheet ประกาศ ก.ค. ว่า enterprise buyer สั่งได้, (3) Intrinsic Core open source. AI framework ต้อง evolve เพื่อรองรับ agent ที่ interact กับ physical world — memory (spatial + temporal), perception, action space ที่ต่างจาก software agent

จุดต้องจับตา 6-12 เดือนข้างหน้า: **community adoption pace**. ROS 2 มี installed base ประมาณ 750,000 นักพัฒนา — เทียบเป็น 1/10 ของ Node.js community. ถ้า Intrinsic Core ดึง 50,000-100,000 downloads ใน 6 เดือนแรก, ecosystem จะเกิด pattern spiral (contributor เพิ่ม, module ใหม่, business แบบ managed service). ถ้าน้อยกว่านั้น อาจจะ repeat pattern ของ Google TensorFlow ที่ open source แต่แพ้ PyTorch เพราะ community owner-ship. Test period คือ Q4 2026 - Q1 2027

## มุม AI Agent Platform

สำหรับ **builders** ที่ทำ agent platform ตอนนี้ — เริ่มคิดเรื่อง **spatial reasoning + tool use ที่มี physical semantics**. ทีมที่สร้าง agent framework (LangGraph, Vercel AI SDK, OpenAI Agents SDK) ยังไม่มีคำตอบ first-class สำหรับ "agent ที่ควบคุม robot arm ทำ task 5 นาที". Interface pattern ตอนนี้ค่อนข้าง forced — LLM plan → ROS action goal → wait → sensor feedback → replan. ควรมีคน think through **multi-timescale planning** (LLM สำหรับ high-level 30-sec-plus decision, dedicated planner สำหรับ millisecond control loop) — Intrinsic Core เป็น starting point ดี

สำหรับ **users / business** ที่กำลัง evaluate physical AI — **cost ลดชัด**. ก่อน Intrinsic Core, ทีม robotics ในโรงงานที่จะเขียน pick-and-place pipeline ต้องซื้อ commercial stack (Fanuc RoboGuide, ABB RobotStudio) ประมาณ $50k-$200k per station + license per year. ตอนนี้เริ่ม prototype ด้วย hardware standard + Intrinsic Core free — ROI ที่ break-even ระดับ 20 station จะเปลี่ยนจาก 3-4 ปีเป็น 12-18 เดือน. Enterprise ที่ manufacturing (electronics, automotive supplier, food processing) ควร run pilot Q4 นี้

สำหรับ **ecosystem** (cloud/edge, sensor vendor, protocol) — NVIDIA จะเจอ dilemma: Intrinsic Core hardware-agnostic แต่ default computation จะไป NVIDIA GPU (FoundationPose base อยู่แล้ว), เพราะ integration ดีที่สุด. Sensor vendor (Intel RealSense, Zivid, Orbbec) ที่มี ROS 2 driver ดีจะได้ share; ผู้ที่ยังไม่มีจะเสีย. Managed service tier กำลังจะเปิดหน้าใหม่ — เจ้าที่ทำ "Intrinsic Core as a Service" managed สำหรับโรงงานที่ไม่อยากจัดการ infra เอง = business idea ที่ยังไม่มีเจ้าจับ. คาดว่าจะเห็น 5-10 startup รอบ seed ในหกเดือนข้างหน้า

## Sources
- [Introducing Intrinsic Core™: An open source approach to Physical AI — Intrinsic](https://www.intrinsic.ai/blog/posts/introducing-intrinsic-core)
- [Intrinsic Open-Sources Core Robotics Capabilities at ROSCon 2026 — Unite.AI](https://www.unite.ai/intrinsic-open-sources-core-robotics-capabilities-at-roscon-2026/)
- [Google's robotics unit Intrinsic open-sources its foundational infrastructure — SiliconANGLE](https://siliconangle.com/2026/09/22/googles-robotics-unit-intrinsic-open-sources-its-foundational-infrastructure-for-intelligent-robots/)
- [Intrinsic open sources key parts of its platform for easier development — The Robot Report](https://www.therobotreport.com/intrinsic-open-sources-key-parts-platform-easier-development/)
- [Alphabet's Intrinsic open-sources the core of its industrial robotics platform under Apache 2.0 — Shopifreaks](https://www.shopifreaks.com/alphabets-intrinsic-open-sources-the-core-of-its-industrial-robotics-platform-under-apache-2-0-with-control-and-motion-planning/)

---

## Audio script
เรื่องสุดท้ายวันนี้เป็นข่าวจากฝั่ง physical AI ที่กำลังตามฝั่ง software agent ทัน. เมื่อวานยี่สิบสอง กันยา ที่งาน ROSCon 2026 กรุง Toronto Intrinsic ซึ่งเป็นบริษัทหุ่นยนต์ในเครือ Alphabet ประกาศเปิด source Intrinsic Core ใต้ Apache 2.0 license. Intrinsic Core คือ package ของ capability พื้นฐานที่ต้องมีในการสร้าง robot application — real-time control ที่ทำงานกับ hardware หลายเจ้า, motion และ grasp planning, pose estimation ที่ base บน NVIDIA FoundationPose, digital twin, simulation, camera calibration, และ hardware driver สำเร็จรูปกว่าสี่สิบรุ่น. Wendy Tan White CEO ของ Intrinsic เรียก philosophy นี้ว่า open source approach to Physical AI คือทำให้นักพัฒนา robot ได้ building block สำเร็จรูปเหมือนที่ software engineer ยุค 2010s ได้ React หรือ Kubernetes เอาไปใช้ต่อ. Signal ของ scale — งาน AI for Industry Challenge ครั้งแรกที่ Intrinsic organize มีนักพัฒนา roboticist ห้าพันคนจากร้อยสิบห้าประเทศเข้าร่วม. เทียบ competitor Boston Dynamics ยังปิด, NVIDIA Isaac เปิดแต่ผูก GPU, Figure ปิดเต็ม — Intrinsic เดินสวนทาง. เรื่องนี้บอกว่า agent boundary กำลังขยายจาก digital ไป physical. AI framework ยุคหน้าต้อง support ทั้งสอง. สำหรับทีมในไทยที่ manufacturing electronics, automotive, food processing — เริ่ม pilot Q4 นี้ เพราะ cost break-even จะสั้นลงจากสามสี่ปีเป็น หนึ่งปีครึ่ง.
