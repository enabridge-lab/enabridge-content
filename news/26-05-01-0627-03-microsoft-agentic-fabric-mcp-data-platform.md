---
date: 2026-04-21
slug: microsoft-agentic-fabric-mcp-data-platform
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: Editorial illustration of layered translucent data lakes stacked vertically with autonomous agents threading between them through a single glowing protocol channel, minimal flat shapes, cool steel blue and copper accents, dramatic vertical lighting, no text no logos no faces
image: images/26-05-01-0627-03-microsoft-agentic-fabric-mcp-data-platform.png
---

# Microsoft ผูก MCP เข้ากับ Fabric — data platform กลายเป็น "AI-native OS"

## TL;DR
- Microsoft ประกาศ Agentic Fabric รอบใหญ่: **Fabric Local MCP** ขึ้น GA, **Fabric Remote MCP** เข้า Preview — agents เรียก data ใน Fabric ผ่าน MCP เป็น native protocol แล้ว
- เป็น signal ชัดที่สุดว่า MCP ขยับจาก "Anthropic standard" เป็น "industry primitive" — ทั้ง Microsoft, GitHub, Cloudflare, Stripe, OpenAI, AWS lined up
- Pattern ที่เกิด: **data platform เป็น AI-native OS** — agents เป็น first-class citizen, ไม่ใช่ทำงานข้างนอกแล้ว pull data เข้ามา

## เกิดอะไรขึ้น

วันที่ 21 เม.ย. Microsoft Fabric ขึ้น blog post ชื่อ "Agentic Fabric: How MCP is turning your data platform into an AI-native operating system" และเปิด milestone สองอันพร้อมกัน — **Fabric Local MCP** ขึ้น GA: รัน MCP server บน machine ของ developer/enterprise เอง agent คุยกับ Fabric API surface ทั้งหมด, build code grounded บน schema จริง, move data ระหว่าง local กับ OneLake โดยไม่ต้องผูก credential เข้า cloud ตลอด — privacy-friendly mode ที่ enterprise IT ฟังแล้วกระเป๋าตังค์เปิด **Fabric Remote MCP** ขึ้น Preview: cloud-hosted server ที่ agent ทำ authenticated operation บน Fabric environment จริง — สร้าง workspace, จัด permission, manage notebook, run pipeline — ไม่ต้อง local setup

Use case ที่ Microsoft ยกมาสามตัวบอก story ครบ: (1) Developer pair-programming กับ GitHub Copilot ใช้ Local MCP เขียน code grounded บน schema จริง — ไม่ใช่ hallucinated table name (2) Autonomous agent ใน Copilot Studio ใช้ Remote MCP จัด workspace + permission แทนทีม — agent มี identity ของตัวเอง (3) CI/CD pipeline ใช้ Fabric CLI deploy change โดยไม่มี human-in-the-loop เลย — full automation จาก commit → production data pipeline

ที่ Microsoft ขายเด่นคือ framing: MCP **ไม่ใช่ feature** แต่เป็น **abstraction layer** ที่ทำให้ Fabric เปลี่ยนจาก "data warehouse + lakehouse + analytics" เป็น operating system ที่ agent run task ผ่าน standard interface ได้ — เหมือน POSIX สำหรับ data platform Microsoft อ้างอิง MCP ว่าเป็น open standard ของ Anthropic ที่ตอนนี้ adopted by GitHub, Cloudflare, Stripe และอื่น ๆ — ภาพรวมที่ Microsoft positioning คือ MCP กลายเป็น default protocol ที่ทุก data + tool layer ต้องพูดได้

## ทำไมสำคัญ

นี่คือ **MCP "tipping point" ที่สอง** ภายใน 6 เดือน: ตัวแรกคือ A2A protocol ขึ้น Linux Foundation พร้อม 150+ org (เม.ย.) ตัวที่สองคือ Microsoft ประกาศชัดว่า Fabric (TAM data platform ระดับ $50B+) จะ run บน MCP เป็น native primitive การที่ Microsoft — ไม่ใช่บริษัทเล็ก, ไม่ใช่ vendor ฝ่าย Anthropic — เลือกใช้ MCP แทนสร้าง protocol ตัวเองคือ **endorsement ที่ทำให้ MCP กลายเป็นมาตรฐานโดยพฤตินัย**

มี implication สำหรับ data platform vendor อื่น: Snowflake, Databricks, BigQuery ต้องปรับ — ทาง Snowflake/Appian พึ่งประกาศ MCP integration เมื่อ 30 เม.ย. ทันต่อกระแสนี้พอดี ใครยังไม่ขยับใน 60 วันข้างหน้า จะถูก agent stack ข้ามหัว — เพราะถ้า Copilot Studio agent เรียก Fabric ผ่าน MCP ได้สะดวก แต่เรียก Snowflake ต้องใช้ custom connector ที่ context cost สูง — agent ก็จะ default ใช้ Fabric Pattern เดียวกับ Cloudflare Code Mode: efficiency ของ context = competitive advantage

อีก signal ที่ลึกกว่าคือ **agent identity** — Remote MCP บอกชัดว่า agent มี identity แยกต่างหากจาก human user, ทำ authenticated operation, มี audit trail นี่คือ infrastructure ที่ทำให้ "agent-as-employee" หรือ "agent-as-customer" model ที่ Cloudflare ก็ขยับเหมือนกัน เป็นไปได้จริง — ไม่ใช่แค่ chat session ของ user คนหนึ่ง

## มุม OpenBridge

ตรงกับ thesis ของ OpenBridge มาก: **integration platform ที่ไม่พูด MCP ภายใน 90 วัน คือ legacy** ที่ Microsoft + Cloudflare + Stripe + GitHub ทำพร้อมกัน — มาตรฐานนี้ผ่าน "early adopter" phase แล้ว เข้า "table stakes" phase อย่างเป็นทางการ OpenBridge ควรมี roadmap ชัด: (1) MCP server expose ของตัวเอง (สำหรับให้ agent ภายนอกเรียก OpenBridge) (2) MCP client built-in (ให้ workflow ของ OpenBridge เรียก MCP servers ปลายทางอื่น) (3) MCP gateway/portal pattern แบบ Cloudflare — ที่ลูกค้า enterprise vendor หลายตัวเข้ามาผ่านจุดเดียว

โดยเฉพาะ angle (3) มีอุปทานหายาก — Cloudflare ทำเป็น infrastructure-level, Microsoft ทำเฉพาะ Fabric — ตลาดยังว่างสำหรับ "MCP gateway สำหรับ enterprise integration" ที่มี governance, observability, cost optimization ครบ OpenBridge ที่อยู่ตรง integration layer อยู่แล้ว มี natural advantage ลงทำ — ก่อน Workato/Zapier/Make ขยับ

## Sources
- [Agentic Fabric: How MCP is turning your data platform into an AI-native operating system — Microsoft Fabric Blog](https://blog.fabric.microsoft.com/en-US/blog/agentic-fabric-how-mcp-is-turning-your-data-platform-into-an-ai-native-operating-system/)
- [Microsoft Fabric Just Exposed Its MCP Architecture — DEV Community](https://dev.to/om_shree_0709/microsoft-fabric-just-exposed-its-mcp-architecture-heres-what-it-actually-changes-for-data-teams-1i4e)
- [FabCon 2026: What Microsoft Fabric's Biggest Announcements Mean for Your Data Strategy — VNB Consulting](https://vnbconsulting.com/2026/04/microsoft-fabric-fabcon-2026-key-updates-data-strategy/)

---

## Audio script
Microsoft ประกาศ Agentic Fabric รอบใหญ่ ปลายเมษา เปิด Fabric Local MCP ขึ้น GA แล้ว และ Fabric Remote MCP เข้า Preview — agents เรียก data ใน Fabric ผ่าน MCP เป็น native protocol ได้แล้ว framing ที่ Microsoft ขายคือ data platform กลายเป็น "AI-native operating system" — agents เป็น first-class citizen ไม่ใช่ทำงานข้างนอกแล้ว pull data เข้า สำคัญตรงที่นี่คือ MCP tipping point ที่สอง ในรอบ 6 เดือน ตัวแรกคือ A2A protocol ขึ้น Linux Foundation ตัวที่สองคือ Microsoft ระดับนี้เลือกใช้ MCP แทนสร้าง protocol ตัวเอง — endorsement ที่ทำให้ MCP กลายเป็นมาตรฐาน de facto สำหรับ OpenBridge เป็น signal ชัดมาก ใน 90 วันถ้า integration platform ไม่พูด MCP คือ legacy เราต้อง roadmap ทั้ง MCP server expose ของตัวเอง MCP client ภายใน และที่น่าสนใจสุดคือ MCP gateway pattern สำหรับ enterprise integration — ตลาดนี้ยังว่าง คนที่อยู่ที่ integration layer อยู่แล้วมี advantage
