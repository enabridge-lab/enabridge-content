---
date: 2026-10-30
slug: servicenow-sweep-400m-mcp-crm
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of three cube buildings in a row stamped
  "SALESFORCE", "HUBSPOT", "SERVICENOW" connected by a glowing bridge labeled
  "MCP". A broom-shaped icon labeled "SWEEP" rolls across the bridge sweeping
  stray data crumbs into a central hopper. Above the scene a bold banner
  reads "~$400M · AGENTIC CRM" and a smaller tag "NOW NEXT CRM". ServiceNow
  green and navy palette with a touch of Salesforce blue and HubSpot orange,
  1:1 aspect, 200px-readable, no real human faces.
image: images/26-11-02-0605-02-servicenow-sweep-400m-mcp-crm.png
---

# ServiceNow ซื้อ Sweep ~$400M — Agentic CRM ข้าม Salesforce/HubSpot พร้อม MCP server เข้าสู่ roadmap

## TL;DR
- ServiceNow ซื้อ **Sweep** สตาร์ทอัพ agentic AI สัญชาติอิสราเอล ดีลประเมิน **~$400M** (บางสำนัก "hundreds of millions"); ไม่มี press release ทางการ
- Sweep ทำ **agentic workspace สำหรับ GTM ops** ครอบ **Salesforce + HubSpot + ServiceNow** พร้อม **MCP server** ของตัวเอง
- ลูกค้า Sweep ที่เปิดชื่อ: **LG Electronics, Brex, NBC Sports** — ก่อตั้ง 2021 โดย Ido Gaver + Eran Kirshenboim, ระดมได้ $46M disclosed
- นี่คือ acquisition ที่สองใน 2 เดือน หลังจาก ServiceNow ซื้อ **ai.work**; เสริม "Now Next CRM" program ย้าย legacy CRM user เข้า ServiceNow
- Competitive frame: ServiceNow CRM โตเท่าตัว YoY, แข่งกับ Salesforce Agentforce ซึ่งทั้งคู่แตะ **$1B scale AI revenue** แล้ว

## เกิดอะไรขึ้น

ปลาย ต.ค. 2026 Calcalist + Salesforce Ben + Dealroom รายงานตรงกันว่า **ServiceNow ซื้อ Sweep** สตาร์ทอัพ agentic AI ของอิสราเอล ด้วยดีลประเมินค่า "hundreds of millions" — SaaSRise cite ตัวเลข **~$400M** จาก Geektime. ServiceNow ปฏิเสธ comment เรื่อง term, ไม่มี press release ทางการ — เป็น pattern ที่ ServiceNow ใช้ซ้ำกับการซื้อ **ai.work** เมื่อ ก.ย. 2026 (ไม่ประกาศเงิน แต่ confirm ว่าซื้อ)

Sweep ไม่ใช่ CRM — มันเป็น **agentic workspace layer** ที่วางบน CRM ของคนอื่น. ก่อตั้ง 2021 โดย Ido Gaver (CEO) และ Eran Kirshenboim software monitor metadata, detect misalignment ระหว่าง sales process กับ pipeline reality, generate documentation อัตโนมัติ, และ run agent ที่ take action บน Salesforce, HubSpot, ServiceNow ได้พร้อมกัน. ที่สำคัญสุด Sweep มี **MCP server ของตัวเอง** — แปลว่า agent ภายนอก (Claude Code, OpenAI Agents SDK, Microsoft Agent Framework) สามารถเรียก Sweep tool ผ่าน protocol มาตรฐานได้

Spokesperson ของ ServiceNow (ที่สื่อ cite) ระบุว่า Sweep จะเสริม **"Now Next CRM"** — โปรแกรม migration ที่ย้าย enterprise legacy CRM user เข้า ServiceNow Now Platform ผ่าน channel partner. บริบท: ServiceNow เปิดใน earnings ว่า CRM business **โตเท่าตัว YoY** และ CRM เป็นส่วนหนึ่งใน **16 จาก 20 top deal ของ quarter**. Salesforce Agentforce — ซึ่งคือคู่แข่งโดยตรง — ก็แตะ $1B revenue scale เช่นกัน

Dealroom + nowben ระบุว่า Sweep เคยระดม **$46M disclosed** ตลอดอายุ 5 ปี, มี customer tier 1 ที่เปิดชื่อ: **LG Electronics, Brex, NBC Sports**. ตัวเลขรายได้ไม่เปิด แต่ Calcalist tag deal ว่า "มีความสำคัญเชิงยุทธศาสตร์มากกว่ามูลค่า"

## ทำไมสำคัญ

ประเด็นแรก: **ServiceNow เลือกซื้อ layer ที่ cross CRM หลายเจ้า ไม่ใช่ CRM เอง**. ปกติเวลา software company อยาก compete กับ Salesforce จะสร้าง CRM ของตัวเอง (ServiceNow ทำมาแล้ว), แต่ Sweep เพิ่ม angle ใหม่ — เป็น **agentic broker** ที่พูดได้กับ Salesforce ด้วย. แปลว่า ServiceNow ไม่ต้องให้ลูกค้าย้าย CRM ทันที — ปล่อย Sweep ทำงานบน Salesforce ก่อน แล้วค่อยๆ ย้าย workflow เข้า ServiceNow. นี่คือ **"Trojan horse" migration strategy** ที่ Microsoft เคยใช้กับ Dynamics 365 และ Teams

ประเด็นสอง: **MCP server เป็น asset หลักของดีล**. ปี 2025–2026 MCP เริ่มเป็น protocol มาตรฐานของ agent (เรื่อง Mintive, OpenAI MCP marketplace, Anthropic MCP ที่เราคุยไปเมื่อสัปดาห์ก่อน). การที่ Sweep มี MCP server pre-built แปลว่า ServiceNow ซื้อ **interoperability** ไม่ใช่แค่ code — Agentforce ของ Salesforce ที่ยังไม่ fully adopt MCP จะเสียเปรียบในสายตา enterprise ที่ต้องการ multi-vendor strategy

ประเด็นสาม: **CRM เป็นสนามรบของ agent สุดต่อไป**. Salesforce เปิดตัวเลข Agentforce ที่ $1B. ServiceNow CRM โตเท่าตัว. HubSpot เพิ่ม Breeze Copilot. Microsoft Dynamics 365 มี Copilot Agent. แปลว่าปี 2027 enterprise ที่เลือก CRM จะเลือกจาก **คุณภาพของ agent + MCP ecosystem** ไม่ใช่จาก UI หรือ reporting อีกต่อไป. Vendor ที่ไม่มี agent production grade (เช่น Zoho, Pipedrive, Freshsales) จะเหลือเพียง SMB tier

## มุม AI Agent Platform

สำหรับ **builders**: Sweep คือ reference case ของ **vertical agent บน CRM metadata** ที่จบด้วย exit $400M. ถ้าคุณ build agent ที่ cross SaaS 2–3 เจ้าในแนวดิ่งเดียวกัน (เช่น HR tech, finance ops, legal ops) นี่คือ playbook: (a) เลือก niche ที่ CRM-level data กระจัดกระจาย, (b) build MCP server เป็น primitive ตั้งแต่ day 1, (c) ลูกค้า tier 1 2–3 รายคือ validation ที่ Buyer ยอมจ่าย. ปี 2027 vertical agent หลายตัวจะถูก big SaaS vendor กวาดซื้อแบบนี้ — pattern เริ่มแล้วตั้งแต่ Mintive ที่เรารายงานเมื่อสัปดาห์ก่อน

สำหรับ **business users**: ถ้าทีม sales/CS ยังใช้ CRM เดียว (Salesforce only, HubSpot only) โดยไม่เชื่อม — มีโอกาสเสียของ. Sweep แสดงว่า agentic layer ที่มองข้าม CRM boundary สร้างมูลค่าได้ $400M. บริษัทไทย/SEA ที่ run **Salesforce + ServiceNow + HubSpot** พร้อมกันควรเริ่มมองหา **agent broker** (Sweep, ปัจจุบัน Clay, Default, Rev, Vector Database CRM-adjacent) ไม่ใช่รอให้ vendor ตัวเองสร้าง feature นี้

สำหรับ **ecosystem**: ดีลนี้บอก Salesforce ว่าต้องเร่ง MCP adoption กับ Agentforce — ไม่งั้นจะโดน ServiceNow ใช้ MCP เป็น wedge แย่งลูกค้าไป. Microsoft (Dynamics + Copilot) อยู่ในตำแหน่งน่าสนใจเพราะมี Agent Framework ที่ support MCP native อยู่แล้ว. HubSpot ซึ่งเป็น underdog ในเกมนี้ ควร partner เร็ว — ไม่งั้นถูก ServiceNow Trojan Horse ย้ายลูกค้า SMB ที่โตขึ้น enterprise ออก

## Sources
- [ServiceNow Acquires Sweep in Deal Worth Hundreds of Millions (Salesforce Ben)](https://www.salesforceben.com/servicenow-acquires-sweep-in-deal-worth-hundreds-of-millions/)
- [ServiceNow buys Israeli AI startup Sweep (Calcalist via Dealroom)](https://dealroom.co/news/149192-servicenow-buys-israeli-ai-startup-sweep-in-deal-estimated-in-the-hundre/)
- [ServiceNow sharpens Salesforce attack with Sweep acquisition (SaaSRise)](https://www.saasrise.com/deals/servicenow-sharpens-its-salesforce-attack-with-sweep-acquisition-3881f696-1f9a-45d7-9ff9-b81fc4f9372a)
- [ServiceNow acquires agentic AI company Sweep (NowBen)](https://nowben.com/servicenow-acquires-agentic-ai-company-sweep/)

---

## Audio script
ข่าวใหญ่สองวันนี้ที่ enterprise agent builder ต้องรู้ ServiceNow เพิ่งซื้อ Sweep สตาร์ทอัพ agentic AI อิสราเอลด้วยดีลที่สื่อประเมินราวสี่ร้อยล้านดอลลาร์ ไม่มี press release ทางการ ServiceNow ปฏิเสธคอมเมนต์เรื่อง term ที่น่าสนใจคือ Sweep ไม่ใช่ CRM แต่เป็น agentic workspace ที่วางบน Salesforce HubSpot และ ServiceNow พร้อมกัน มี MCP server ของตัวเอง ลูกค้าที่เปิดชื่อคือ LG Electronics Brex NBC Sports ก่อตั้งปี 2021 ระดมได้สี่สิบหกล้านดอลลาร์ก่อน exit สิ่งที่สำคัญคือ ServiceNow เลือกซื้อ layer ที่ข้าม CRM หลายเจ้าไม่ใช่ CRM เอง นี่คือ Trojan Horse migration strategy ที่ปล่อย Sweep ทำงานบน Salesforce ของลูกค้าก่อนแล้วค่อยย้าย workflow เข้า ServiceNow ซึ่งเป็น program ที่ ServiceNow เรียกว่า Now Next CRM สนามรบของ CRM เปลี่ยนไปแล้ว Salesforce Agentforce ServiceNow CRM Microsoft Dynamics Copilot ทั้งหมดแตะ scale หนึ่งพันล้านดอลลาร์ต่อปี ปีหน้า enterprise จะเลือก CRM จากคุณภาพของ agent และ MCP ecosystem ไม่ใช่จาก UI สำหรับทีมที่ build vertical agent บน SaaS cross หลายเจ้าดีลนี้คือ playbook เริ่มจาก niche ที่ data metadata กระจัดกระจาย build MCP server เป็น primitive วัน day one มีลูกค้า tier หนึ่งสามรายคือ validation สำหรับทีมในไทยที่ run Salesforce ServiceNow HubSpot พร้อมกันควรเริ่มมองหา agent broker ไม่ใช่รอให้ vendor สร้าง feature นี้เองครับ
