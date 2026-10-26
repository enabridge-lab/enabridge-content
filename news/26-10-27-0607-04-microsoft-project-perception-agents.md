---
date: 2026-10-27
slug: microsoft-project-perception-agents
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a glowing bastion labeled "AGENT ID"
  behind a translucent force field; small translucent agent silhouettes line
  up to be scanned at a gate; a large watchtower marked "GUARDIAN" overlooks
  them. Three signs float on the wall: "DYNAMIC PERMISSIONS", "DYNAMIC RISK",
  "60 AGENT TYPES". Cool teal and steel palette, crisp line work, 1:1 aspect,
  no real human faces.
image: images/26-10-27-0607-04-microsoft-project-perception-agents.png
---

# Microsoft ประกาศ "agent คือ insider" — Entra Agent ID + Guardian Agents กลายเป็น default enterprise control plane

## TL;DR
- 19 ตุลาคม Microsoft ขยาย Project Perception ให้ครอบคลุม AI agent ที่ทำงาน "ภายในองค์กร" — เรียกว่า agentic insiders — เพิ่ม 3 capability: Dynamic Permissions, Dynamic Agent Risk, Dynamic Conditional Access
- Microsoft Entra Agent ID ให้ identity แยกระหว่าง agent กับพนักงานเจ้าของ agent — track ownership + enforce policy ได้แยกจาก human user
- Local agent discovery ขยาย 35 ชนิดเป็น 60 ชนิด รวม Claude Code, OpenAI Codex, GitHub Copilot; Hayete Gallot (Head of Microsoft Security) ประกาศ "Guardian Agents" ที่ supervise agent อื่น

## เกิดอะไรขึ้น
เมื่อวันที่ 19 ตุลาคม Microsoft Security publish blog post สองชิ้นเสนอว่า AI agent ที่ทำงานภายในองค์กรต้องถูก treat เป็น "agentic insider" — คือ identity ที่ action ของมันต้องถูก log, review และ control แยกจาก identity ของพนักงานที่เป็นเจ้าของ. Hayete Gallot ซึ่งนำทีม Microsoft Security เขียนตรง ๆ ว่า frontier model "trust ไม่ได้" และบริษัทจะต้องมี Guardian Agent ที่ "supervise และ moderate agent action, ทุกวันตลอด 24 ชั่วโมง, ก่อนที่ action จะเกิดขึ้น".

Project Perception เดิมเปิดตัวในเดือนกรกฎาคมเพื่อ handle external AI-driven threat; รอบ expansion นี้ย้าย capability เดียวกันมาใช้กับ agent ที่อยู่ "ข้างใน" บริษัท. สาม capability หลักคือ: (1) **Dynamic Permissions** — agent ได้สิทธิเฉพาะงานปัจจุบัน ไม่ใช่สิทธิถาวร; (2) **Dynamic Agent Risk** — score ที่ update real-time ตาม behavior; (3) **Dynamic Conditional Access** — gating ที่ปรับระดับตาม risk score. Local agent discovery ขยาย 35 ชนิดเป็น 60 ชนิด รวมถึง agent ที่อยู่นอก Microsoft เองอย่าง Claude Code และ GitHub Copilot.

Entra Agent ID คือองค์ประกอบที่สำคัญที่สุด — agent ทุกตัวได้ identity เป็นของตัวเองที่แยกจาก identity ของพนักงานเจ้าของ. ความสำคัญคือ pattern เดิมของ enterprise คือพนักงานหนึ่งคน = identity หนึ่ง + agent รัน under identity นั้น — ซึ่งทำให้ audit trail งง (คนทำ หรือ agent ทำ?) และ permission ของ agent = permission ของพนักงาน (over-privilege). Entra Agent ID แก้ปัญหาทั้งสองพร้อมกัน. Features ชุดนี้มากับ Microsoft 365 E7.

## ทำไมสำคัญ
Timing มี 2 องค์ประกอบที่สำคัญ. องค์ประกอบแรก: Microsoft เป็น vendor แรก ๆ ที่ประกาศ "agent คือ identity class ใหม่" ด้วย infrastructure จริงที่ enterprise ใช้แล้ว (Entra). วันหลัง OpenAI/Anthropic/Google จะ build identity layer ของตัวเอง หรือจะ delegate ไปที่ Microsoft เป็น default — จุดนี้คือ platform choke point.

องค์ประกอบที่สอง: Gallot พูดชัดว่า frontier model trust ไม่ได้ — คำพูดนี้มาจาก Microsoft ซึ่งเป็น partner ใหญ่สุดของ OpenAI และเป็นผู้ปล่อย Copilot เองในหลายผลิตภัณฑ์. การยอมพูดต่อสาธารณะว่า model ของตัวเอง trust ไม่ได้ และต้องมี "Guardian Agent" กำกับ เป็น shift ของ narrative จาก "AI ทำได้ทุกอย่าง" ไปเป็น "AI ต้องมี guard rail". เป็นการ pre-empt regulator ด้วย — ถ้า EU AI Act หรือ US AI order ขยับ Microsoft มี story พร้อมแล้ว.

ตัวเลขที่ secondary source อ้างจาก Gartner (ไม่ยืนยัน) บอกว่า 54% ของ organization ยังไม่มี defined approach ในการจำกัด agent access — ซึ่งเป็น TAM ที่ Microsoft เล็ง.

## มุม AI Agent Platform
สำหรับ **builders**: ถ้า agent ของคุณจะ deploy ใน enterprise ที่ใช้ Microsoft stack ภายในปี 2027 คุณต้อง comply กับ Entra Agent ID — คือ register agent, scope permission, และ accept การถูก audit โดย Guardian Agent. Startup ที่ bypass หรือ work around จะ hit wall ใน procurement.

สำหรับ **users / business**: เป็นประโยชน์ชัด — audit trail ที่ clean + permission ที่ scope ลด risk ของ agent sprawl. ถ้าคุณใช้ Microsoft 365 อยู่แล้ว upgrade เป็น E7 เป็น no-brainer ก่อนที่ compliance team จะมาทวง. สำหรับ ecosystem: ตามมา Opsin ($21M รอบนี้) และ Mave Security ($34M) ที่เสนอ agent governance แบบ cross-vendor — ตลาดกำลังแยกเป็น "Microsoft-native" vs. "neutral multi-vendor" และ enterprise จะเลือกข้าง.

## Sources
- [Microsoft Expands Project Perception for Agentic Insiders (eWeek)](https://www.eweek.com/news/microsoft-project-perception-ai-agent-controls/)
- [Microsoft expands Project Perception to address security risks from AI agents (Redmond Magazine)](https://redmondmag.com/articles/2026/10/19/microsoft-expands-project-perception-to-address-security-risks-from-ai-agents.aspx)
- [Microsoft Points Project Perception at the Agents Already Inside (Futurum Group)](https://futurumgroup.com/?p=96986)
- [Microsoft Extends Project Perception for Agentic Insiders (Let's Data Science)](https://letsdatascience.com/news/microsoft-extends-project-perception-for-agentic-insiders-a0e44022)

---

## Audio script
ข่าวที่สี่วันนี้เรื่อง Microsoft ประกาศของใหญ่ 2 ชิ้นในวันเดียวกันเมื่อวันที่ 19 ตุลาคม ที่น่าจะเป็นจุดเปลี่ยนของการใช้ AI agent ในองค์กรใหญ่. ของแรกคือการขยาย Project Perception ให้ครอบคลุม agent ที่อยู่ภายในองค์กรเอง ไม่ใช่แค่ภัยคุกคามจากข้างนอก. ของที่สองคือ Microsoft Entra Agent ID คือ identity สำหรับ agent ที่แยกออกจาก identity ของพนักงานเจ้าของ. Hayete Gallot หัวหน้าทีม security ของ Microsoft พูดตรง ๆ ว่า frontier AI model ตอนนี้ trust ไม่ได้ และต้องมีสิ่งที่เขาเรียกว่า Guardian Agent คอยกำกับ agent อื่นตลอด 24 ชั่วโมง. การ discover agent ที่อยู่บนเครื่องพนักงานขยายจาก 35 เป็น 60 ชนิด รวม Claude Code และ GitHub Copilot ด้วย. เรื่องนี้สำคัญเพราะ Microsoft กำลัง claim บทบาท identity provider สำหรับ AI agent ในองค์กร ซึ่งคือ choke point ที่ platform ไหนก็อยากคุม สำหรับคนที่สร้าง agent ที่จะขายให้ enterprise ภายใน 2 ปีข้างหน้า ต้อง comply กับ Entra Agent ID ไม่งั้นจะไม่ผ่านด่าน procurement
