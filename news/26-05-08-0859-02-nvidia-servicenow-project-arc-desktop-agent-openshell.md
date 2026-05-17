---
date: 2026-05-08
slug: nvidia-servicenow-project-arc-desktop-agent-openshell
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: A bold editorial illustration framed in deep navy and warm cream — at center, a stylized employee laptop screen drawn flat, with its glowing rectangular boundary rendered as a glassy translucent green sandbox box labeled 'OPENSHELL'. Inside the laptop screen, a small cream agent symbol (geometric arc shape) with motion lines is busily writing code, opening files, and clicking buttons — connected by glowing teal cables to floor-tiled enterprise app icons (Outlook, Slack, terminal, browser). Above the laptop, a stylized NVIDIA green eye-shape and a coral ServiceNow petal logo flank the scene. A bright coral arched headline reads 'PROJECT ARC' across the top, with a small cream tag below 'Governance moves to the desktop'. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + teal + NVIDIA-green palette, no human figures, logos crisp for 200px thumbnail readability.
image: 
---

# NVIDIA + ServiceNow ปล่อย Project Arc — autonomous desktop agent ที่ "คิด เขียน code รัน ปรับตัว" ในกล่อง OpenShell sandbox

## TL;DR
- 5 พ.ค. ที่ Knowledge 2026 (Las Vegas) ServiceNow + NVIDIA เปิด **Project Arc** — desktop agent ที่ "คิด, เขียน code, execute, adapt when things don't go as expected" — ครอบ workflow ข้าม local file, terminal, enterprise app **โดยไม่ต้อง pre-build workflow**; available เป็น early preview
- ทุก action รันใน **NVIDIA OpenShell** — sandboxed runtime ที่ enforce policy-based management, log file ที่อ่าน, command ที่รัน, API ที่เรียก — ทำให้ agent ทำงาน autonomous แต่ contained, auditable, enterprise-safe
- Governance อยู่ที่ **ServiceNow AI Control Tower** — ตั้ง policy, monitor behavior, log ทุกสิ่ง; powered by **ServiceNow Action Fabric** + grounded ใน **CMDB** (Configuration Management Database) — agent มี deep enterprise context ตั้งแต่นาทีแรก ไม่ใช่ general-purpose computer-use agent ที่หลงใน workflow

## เกิดอะไรขึ้น

ที่ ServiceNow Knowledge 2026 ใน Las Vegas วันที่ 5 พ.ค. CEO Bill McDermott + NVIDIA Jensen Huang ขึ้น stage ร่วมกันเปิด Project Arc — autonomous desktop agent ที่ออกแบบให้เป็น "knowledge worker บน desktop ของพนักงาน" ตัวจริง agent ตัวนี้ไม่ได้ออกมาแบบ Anthropic computer use หรือ OpenAI Operator ที่เป็น general-purpose web automation — แต่เป็น **enterprise-native** ที่ผูกแน่นกับ ServiceNow stack ตั้งแต่ใต้ฝา; capability ที่ ServiceNow ใช้เปิดตัวคือ "thinks, writes code, executes, and adapts when things don't go as expected" — ไม่ต้องการ pre-built workflow, รับ goal เป็น natural language แล้วเดิน multi-step เอง

ใต้ฝา Project Arc รันบน **NVIDIA OpenShell** — runtime ใหม่ที่ NVIDIA เปิดตัวเดียวกัน (เป็น sandboxed environment ที่ตอบคำถามที่ทุก CISO ถาม: "ปล่อย agent autonomous บน laptop พนักงานแล้วถ้ามัน rm -rf หรือ leak data ใครรับผิดชอบ?") OpenShell บังคับให้ทุก file read, command exec, API call ต้องผ่าน policy gate ของ ServiceNow AI Control Tower — admin ตั้ง rule ระดับ "agent นี้ห้ามเขียน /etc, ห้ามเรียก external API ที่ไม่ได้อนุมัติ, ห้ามอ่าน folder ที่มี customer PII" แล้ว runtime enforce — รวมทั้งสร้าง audit trail ที่ระบุได้ใน 5 วินาทีว่า agent ตัวไหน เรียก tool อะไร ตอนกี่โมง ผลลัพธ์อะไร

ที่ทำให้ Project Arc ต่างจาก desktop agent อื่น (Claude computer use, OpenAI Operator, Standard Intelligence Pixel ที่ออก 6 พ.ค.) คือ **enterprise grounding** — Project Arc รันบน **ServiceNow Action Fabric** ที่อนุญาตให้ agent ใด ๆ เข้า ServiceNow system of action; grounded ใน **CMDB** ที่เก็บ configuration ของทุก IT asset, workflow, system ของลูกค้าอยู่แล้ว; แปลว่า agent ไม่ต้อง bootstrap context จาก zero — มัน "รู้" ว่าระบบ HRIS ของ Fortune 500 customer ตัวนี้ผูกกับ Workday, payment system ผูกกับ SAP, customer DB อยู่ใน Salesforce, ที่ network policy บังคับ traffic ผ่าน Zscaler ไม่ใช่ direct internet — ตั้งแต่ first run

Project Arc พบพนักงานที่ surface ที่หลากหลาย — desktop app, enterprise collaboration tool (Teams, Slack), หรือ email — ServiceNow ตั้งใจให้ "interface เปลี่ยน, governed execution เหมือนเดิม"; target user เป็น dev, IT team, sysadmin ก่อน — workflow ตัวอย่างที่ ServiceNow โชว์ใน demo: dev ส่ง email ขอให้ agent debug production issue, agent อ่าน Splunk log, run kubectl describe, เปิด terminal เขียน Python script analyze stack trace, ส่ง summary กลับเป็น Slack message พร้อมแก้ที่ ServiceNow ticket ใน 8 นาที — เทียบกับ on-call engineer ที่ใช้ 45 นาทีโดยเฉลี่ย

## ทำไมสำคัญ

นี่คือ first credible **endpoint-native autonomous agent ที่ ship พร้อม governance layer** ตั้งแต่ day 1; ความใหญ่ของข่าวไม่ใช่ความสามารถ agent (Claude computer use ทำได้คล้ายกัน) แต่คือ **operating model** ที่ ServiceNow + NVIDIA วาง — Project Arc เปลี่ยน "desktop" จาก uncontrolled territory ที่ shadow IT, BYOD, personal Chrome extension วิ่งกัน → เป็น **fully governed agent runtime** ที่มี policy enforcement, audit log, blast radius control; ใน Q3 ผู้บริหาร CISO + CIO จะไม่ผ่าน agent ที่รันบน laptop พนักงานถ้าไม่มี OpenShell-equivalent — กลายเป็น new procurement requirement

ที่ลึกกว่า — pattern ที่เห็นชัดคือ **NVIDIA ขยับจาก "ขาย GPU" ไปขาย "agent runtime"**; OpenShell คือ next move ของ NVIDIA หลัง NIM (microservice runtime), AI Enterprise (model serving), GTC 2026 enterprise platform — NVIDIA เริ่ม claim layer ที่อยู่ระหว่าง chip กับ workload จริง; เทียบกับ AMD ที่ยังขายแค่ chip + ROCm + AI suite — NVIDIA stack เริ่ม sticky ในระดับ runtime (developer ที่ build agent บน OpenShell จะไม่อยาก migrate ไป CPU-only หรือ AMD); margin จะย้ายจาก hardware (~70%) ไป software/runtime (~85%+)

อีกประเด็น — ServiceNow + NVIDIA + Accenture FDE program (วันเดียวกัน 6 พ.ค.) เป็น **stack ครบเซ็ต** ที่ Microsoft Agent 365 ยังไม่มี; Microsoft มี Agent 365 + Defender Shadow AI + Purview compliance แต่ desktop ยังเป็น Windows Copilot ที่ user-controlled; เกม Q3 จะเป็น Microsoft vs ServiceNow ที่ "ใครเป็น governance layer ของ desktop agent บริษัท" — ServiceNow มี advantage จาก CMDB + Action Fabric (ลูกค้า Fortune 500 ใช้กันแพร่หลายมา 15 ปี); Microsoft มี advantage จาก Windows install base + identity (Entra) — ลูกค้าที่ใช้ทั้งคู่จะถูกบีบเลือกข้าง หรือต้องจ่ายซ้อน

## มุม OpenBridge

OpenBridge ต้องสาม move (1) **ออก ServiceNow Action Fabric connector** — Project Arc agent บน desktop ของลูกค้าเรียก OpenBridge ผ่าน Action Fabric → ลูกค้าเชื่อม HubSpot, Stripe, LINE OA, Shopee API ที่ไม่อยู่ใน CMDB ของ ServiceNow ผ่าน OpenBridge connector — ลูกค้า Thai Fortune 100 ที่ใช้ ServiceNow (SCB, AIS, ปตท., CPN) จะ adopt Project Arc ใน 6-12 เดือน; OpenBridge ที่อยู่ใน Action Fabric registry ตั้งแต่ก่อน wave จะกลายเป็น "default external connector" (2) **emit telemetry ที่ AI Control Tower กิน** — ใช้ OpenTelemetry agent semantic convention (Microsoft วาง spec, ServiceNow รับ); log payload-per-call, success rate, latency ส่งเข้า Control Tower เป็น native data; CISO เห็น blast radius ของ OpenBridge call ใน dashboard เดียวกับ Project Arc — กลายเป็น trust signal ที่ procurement ต้องการ (3) **เตรียม "OpenShell-compliant connector"** — ทดสอบ OpenBridge SDK ใน OpenShell sandbox, รับ NVIDIA badge "OpenShell verified"; ภายใน 12 เดือน enterprise procurement จะเช็ก list นี้เหมือนเช็ก SOC 2

Adjacent insight: Project Arc "thinks, writes code, executes" บน desktop = ลูกค้าจะลด on-call engineer headcount 20-30% ภายใน 18 เดือน → **OpenBridge ขาย "ServiceNow Action Fabric integration kit" ให้ MSP/SI partner ของไทย** (G-Able, SmartFox, Yip In Tsoi) เป็น value-add; partner ใช้ Project Arc ลด cost of delivery ของ managed service ทำ margin expansion ที่ partner รักษาความสัมพันธ์ลูกค้าได้

## Sources
- [ServiceNow extends agentic AI governance from desktops to data centers with NVIDIA | ServiceNow Newsroom](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-extends-agentic-AI-governance-from-desktops-to-data-centers-with-NVIDIA/default.aspx)
- [NVIDIA and ServiceNow Partner on New Autonomous AI Agents for Enterprises | NVIDIA Blog](https://blogs.nvidia.com/blog/servicenow-autonomous-ai-agents-enterprises/)
- [ServiceNow and NVIDIA launch autonomous desktop AI agent | Quartz](https://qz.com/servicenow-nvidia-autonomous-desktop-agent-ai-control-tower-050626)
- [ServiceNow, NVIDIA Unveil Project Arc to Govern AI Frontier | Techstrong.ai](https://techstrong.ai/agentic-ai/servicenow-news/)

---

## Audio script
สวัสดีครับโย วันที่ 5 พ.ค. ที่ ServiceNow Knowledge 2026 Bill McDermott กับ Jensen Huang ขึ้น stage ร่วมกันเปิด Project Arc เป็น autonomous desktop agent ที่คิด เขียน code execute และปรับตัวเองเมื่อมีปัญหา ทำงาน multi-step ข้าม local file terminal enterprise app โดยไม่ต้อง pre-build workflow available เป็น early preview

หัวใจคือ NVIDIA OpenShell ที่เป็น sandboxed runtime ที่ทุก action ต้องผ่าน policy gate ของ ServiceNow AI Control Tower admin ตั้ง rule ได้ว่า agent ห้ามเขียน folder ไหน ห้ามเรียก API ไหน อ่าน folder PII ไม่ได้ และมี audit trail ที่ระบุได้ทุกการกระทำของ agent ที่ทำให้ Project Arc ต่างจาก desktop agent อื่นคือ enterprise grounding รันบน ServiceNow Action Fabric grounded ใน CMDB ทำให้ agent รู้ว่า HRIS ผูกกับ Workday SAP Salesforce Zscaler ตั้งแต่ first run ไม่ต้อง bootstrap context

ทำไมสำคัญ นี่คือ endpoint native autonomous agent ที่ ship พร้อม governance ตั้งแต่วันแรก ใน Q3 CISO กับ CIO จะไม่ผ่าน agent ที่ไม่มี OpenShell equivalent NVIDIA เริ่ม claim layer ระหว่าง chip กับ workload margin จะย้ายจาก hardware ไป runtime stickiness ของ NVIDIA stack จะลึกกว่า GPU ตัวเดียวมาก เกม Q3 จะเป็น Microsoft Agent 365 vs ServiceNow ที่ใครคุม governance layer ของ desktop agent

มุม OpenBridge ออก ServiceNow Action Fabric connector ลูกค้า Thai Fortune 100 ที่ใช้ ServiceNow จะ adopt Project Arc ใน 6 ถึง 12 เดือน ที่อยู่ใน Action Fabric registry ก่อน wave จะเป็น default connector emit telemetry ที่ AI Control Tower กิน CISO เห็น OpenBridge ใน dashboard เดียวกับ Project Arc เตรียม OpenShell compliant SDK รับ NVIDIA verified badge enterprise procurement จะเช็ก list นี้เหมือน SOC 2 ครับ
