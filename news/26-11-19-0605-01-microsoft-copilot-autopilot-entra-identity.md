---
date: 2026-11-18
slug: microsoft-copilot-autopilot-entra-identity
topic: agentic-ai
reading_time_min: 5
sources: 4
image_prompt: |
  An editorial isometric illustration of a corporate security badge terminal. A
  robotic agent silhouette stands at the badge reader, holding its own glowing
  ID card marked "ENTRA IDENTITY — AGENT". Behind it, a vault door is cracked
  open revealing a vast data warehouse labeled "19.5 EXABYTES". A banner above
  the scene reads "COPILOT AUTOPILOT" and a sub-label reads "ALWAYS-ON". Soft
  turquoise, navy and warm amber palette, clean editorial style, 1:1 aspect,
  no real human faces (silhouettes OK), high contrast so numbers stay legible
  at 200px thumbnail.
image: images/26-11-19-0605-01-microsoft-copilot-autopilot-entra-identity.png
---

# Microsoft ให้ agent มี Entra ID ของตัวเอง — Copilot Autopilot เปลี่ยน agent จาก "เครื่องมือ" เป็น "พนักงาน" ที่มีตัวตน

## TL;DR
- Microsoft เปิดตัว Copilot Autopilot ใน Ignite 2026 (18 พ.ย.) — autonomous agent ตัวแรกที่มี Microsoft Entra identity ของตัวเอง, log action ภายใต้ account แยกจากคน
- WorkIQ เป็น reasoning layer กลางที่ดึง context ข้าม 19.5 exabytes ของ Microsoft 365 customer data — agent ต่าง ๆ แชร์ context กันโดยไม่ชนกัน
- เปิดตัวพร้อม Agent 365 Business Analytics (budgeting ค่า compute ของ agent) + AI Transparency Initiative กับ 40+ บริษัท (Accenture, Adobe, KPMG, Mastercard, Volvo) — Microsoft กำลังวาง governance layer ก่อนที่ regulator จะเข้ามา

## เกิดอะไรขึ้น
วันที่ 18 พฤศจิกายน CMO ของ Microsoft Jared Spataro ขึ้นเวที Ignite 2026 keynote เปิดตัว Copilot Autopilot — ตัวที่ Microsoft เรียกว่า "the first always-on autonomous AI agent with its own Microsoft Entra identity" การที่ agent มี Entra ID ของตัวเองแทนที่จะ act ในนามของผู้ใช้ แปลว่า action ของมันถูก log ภายใต้ account แยกต่างหาก ซึ่งทีม security สามารถ audit แยกจาก activity ของคนได้ — เป็นการแก้ปัญหา "agent ทำอะไรในนามของใคร" ที่ CISO ทั่วโลกกำลังกังวล

เบื้องหลังของ Autopilot และ Copilot agent ทั้งตระกูลคือ WorkIQ — reasoning layer ที่ Microsoft อ้างว่าดึง data จาก 19.5 exabytes ของ Microsoft 365 customer data เพื่อ interpret intent, retrieve context และ prioritize information ให้ agent ต่าง ๆ ทำงานประสานกันโดยไม่ชนกัน Autopilot เองยังอยู่ใน Frontier early-access program ไม่ใช่ GA แต่ Copilot Home, Office in Copilot และ Managed Runtime ถึง GA ในวันเดียวกัน พร้อม 100+ prebuilt skills ของ Dynamics 365 ครอบ sales/service/finance และ 38 CRM skills จาก partnership กับ Salesforce ชื่อ "Copilotforce"

วันเดียวกัน Satya Nadella ประกาศ AI Transparency Initiative กับ 40+ องค์กร — Accenture, Adobe, KPMG, Mastercard, Volvo Cars ร่วมด้วย Microsoft ขยาย participation ใน NIST SI Agent Standards Initiative เพื่อพัฒนา industrywide standards ให้ agent activity verify ได้อย่างอิสระ และ Microsoft จะฝัง capability นี้ลงใน Microsoft AI, Foundry, และ Copilot เพื่อให้ลูกค้าเอา evidence ไปใช้กับ security tool ของตัวเองได้ Hayete Gallot, EVP ฝ่าย Microsoft Security บอกว่า "For security controls to be effective, every organization needs greater transparency into the model itself"

## ทำไมสำคัญ
Entra identity สำหรับ agent คือ signal ที่ enterprise architect รอมาทั้งปี — pattern เดิมที่ agent impersonate user account แล้ว act ในนามของเขาเป็น audit nightmare เพราะ security team แยกไม่ออกว่า action ไหนคน ทำ action ไหน agent ทำ การที่ Microsoft ยอมสร้าง primitive ใหม่ (agent-as-first-class-identity) และ ship มันเข้า Entra ที่มี install base ของ enterprise ทั่วโลกคือการเปลี่ยน default ของทั้ง industry ไม่ใช่แค่ feature

Agent 365 Business Analytics เป็น detail ที่คนจะมองข้าม แต่สำคัญ — Microsoft กำลังยอมรับว่า agent compute spend จะกลายเป็น line item ใน IT budget ที่ CFO ต้องเห็น ไม่ใช่เลขที่ซ่อนอยู่ใน license cost การ anchor "agent budget as separate P&L" จะทำให้ buyer เริ่มถาม ROI per agent ไม่ใช่ ROI ของ Copilot license ภาพรวม ซึ่งจะกดดัน vendor ทุกราย (Salesforce Agentforce, ServiceNow Now Assist, Workday Illuminate) ต้อง show attribution ที่ชัดกว่าเดิม

AI Transparency Initiative ที่มี Accenture, Adobe, KPMG, Mastercard, Volvo เซ็น MOU คือ Microsoft กำลังเล่น regulator-proofing — EU AI Act มีผลเต็มรูปแบบปีหน้า และ federal AI governance rule ของสหรัฐฯ กำลังร่าง การตั้ง industrywide standard ก่อนที่ regulator จะกำหนด แปลว่า Microsoft คุม narrative ของ compliance แทนที่จะถูก define ภายหลัง — playbook เดียวกับที่ Microsoft ใช้กับ security baseline ใน Windows ยุค 2000s

## มุม AI Agent Platform
**Builders** — ถ้าคุณสร้าง agent framework หรือ orchestration layer ของตัวเอง ตอนนี้ต้องคิดว่า agent ของคุณจะ integrate กับ identity provider อย่างไร เพราะ Entra เป็น IdP อันดับหนึ่งของ enterprise (Okta เป็นอันดับสอง) ถ้า agent ของคุณไม่ได้ first-class ID แยกจาก user แปลว่าคุณจะขายไม่ได้ในลูกค้า regulated industry — ต้องสร้าง integration layer หรือ fallback ให้ agent มี service principal แยก

**Users/business** — สำหรับ Thai enterprise ที่ใช้ Microsoft 365 อยู่แล้ว การ shift ไป agent-with-Entra-identity เป็น path ที่ "free" กว่าการสร้าง agent platform ของตัวเองใหม่ Enabridge ที่ช่วยลูกค้า deploy agent ควร benchmark ว่า Copilot Autopilot จะ cover use case ไหนได้ก่อน เพื่อให้ custom agent focus เฉพาะ gap — ไม่ใช่สร้างของที่ Microsoft กำลังจะ GA ใน 6 เดือนข้างหน้า

**Ecosystem** — Salesforce ชัดเจนว่าเลือกร่วมมือ (Copilotforce กับ 38 CRM skills + Zero Copy Fabric–Data 360 integration) แทนที่จะแข่งเต็มตัว ซึ่งต่างจาก Slack vs Teams ยุคก่อน ServiceNow และ Workday ต้องเลือกว่าจะ integrate ลึก (รอให้ Autopilot ดึง context เข้า workflow ตัวเอง) หรือจะสร้าง identity layer แข่งผ่าน Okta — ทั้งสองทางมี cost ไม่น้อย

## Sources
- [Microsoft and organizations across industries launch AI Transparency Initiative (Microsoft Source)](https://news.microsoft.com/source/2026/11/17/microsoft-and-organizations-across-industries-launch-ai-transparency-initiative-to-strengthen-enterprise-trust-in-ai-models-and-agents/)
- [Microsoft Copilot Autopilot Launches With Agent Identity (Emergent)](https://emergent.sh/news/microsoft-copilot-autopilot-launches-agent)
- [Microsoft unveils new enterprise AI agents and tools at Ignite 2026 (Storyboard18)](https://www.storyboard18.com/brand-makers/microsoft-unveils-new-enterprise-ai-agents-and-tools-at-ignite-2026-ws-l-114984.htm)
- [AI Agents News Brief: November 18, 2026 (AI Agents Directory)](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-18-2026)

---

## Audio script
วันนี้ขอเริ่มจากข่าวที่น่าจะเปลี่ยน default ของ enterprise agent ทั้งอุตสาหกรรม Microsoft เปิดตัว Copilot Autopilot ใน Ignite 2026 เมื่อวันที่ 18 พฤศจิกายน Autopilot เป็น autonomous agent ตัวแรกที่มี Entra identity ของตัวเอง แปลว่าเวลามันทำอะไร action ถูก log ภายใต้ account แยกจากคน ซึ่ง CISO ทั่วโลกรอฟีเจอร์นี้มานานเพราะ pattern เดิมที่ agent ทำงานในนาม user account เป็น audit nightmare เบื้องหลัง Autopilot คือ WorkIQ ซึ่งเป็น reasoning layer ที่ Microsoft อ้างว่าดึง context ข้าม 19.5 exabytes ของ Microsoft 365 data ทำให้ agent หลายตัวทำงานประสานกันได้ Autopilot ยังอยู่ใน early access แต่ Copilot Home, Office in Copilot และ Managed Runtime ถึง general availability ในวันเดียวกัน พร้อม Dynamics 365 skills 100 กว่าตัว และ CRM skills จาก Salesforce 38 ตัวในชื่อ Copilotforce วันเดียวกัน Satya Nadella ประกาศ AI Transparency Initiative กับ 40 กว่าองค์กร มี Accenture, Adobe, KPMG, Mastercard, Volvo ร่วมด้วย เป้าหมายคือพัฒนา industrywide standard ให้ agent activity verify ได้อย่างอิสระ สำหรับคนที่สร้าง agent platform signal คือต้องคิดเรื่อง identity ตั้งแต่วันแรก เพราะ Entra จะกลายเป็น default ของ regulated industry สำหรับ Thai enterprise ที่ใช้ Microsoft 365 อยู่แล้ว ควร benchmark ว่า Autopilot จะ cover use case ไหนก่อนจะไปสร้าง custom agent แข่งกับของที่ Microsoft กำลังจะ ship ฟรี
