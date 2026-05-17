---
date: 2026-05-08
slug: atlassian-teamwork-graph-mcp-third-party-agents
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: A bold editorial illustration in deep navy and warm cream — at center a stylized blue Atlassian double-A logo glows like a glass dome, with golden filaments labeled "150B CONNECTIONS" weaving through its core. Around the dome, four exterior flat-vector logos — Claude Code, Cursor, OpenAI ChatGPT, and a generic "MCP" plug icon — extend cables that snap into the dome through visible "MCP / CLI" gates. A bright coral headline "OPEN GRAPH" arches over the top, with "14M ACTIONS / MONTH" rendered very large in cream sans-serif on the lower-right corner. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + Atlassian blue palette, no human figures, logos crisp for 200px thumbnail readability, 1:1 aspect ratio.
image: images/26-05-08-0927-01-atlassian-teamwork-graph-mcp-third-party-agents.png
---

# Atlassian เปิด Teamwork Graph ให้ agent ค่ายอื่นเข้าถึงผ่าน MCP — 14M actions/เดือน + 90% ลูกค้า enterprise ใช้ Rovo

## TL;DR
- ที่ Team '26 (6 พ.ค. 2026) Atlassian เปิด Teamwork Graph ที่มี 150B+ connections ให้ third-party agent (Claude Code, Cursor, ChatGPT) เข้าถึงผ่าน MCP server + CLI 300+ คำสั่ง — เป็น open beta แล้ว ไม่ต้องอยู่ใน ecosystem Atlassian ก็ต่อได้
- 90%+ ของ enterprise cloud customer ใช้ Rovo แล้ว, agentic automation โต 7x ใน 6 เดือน, 14M+ Rovo-assisted actions/เดือน — ตัวเลขที่ใหญ่ที่สุดในกลุ่ม horizontal SaaS ที่ pivot เป็น agent
- Customer numbers: SpotOn deflect ticket จาก 40% เป็น 53% (95% question answer rate), Teach for All รัน weekly report 60–70% อัตโนมัติ, Lendi Group ผ่าน Jira+Confluence+Slack ด้วย agent เดียว — ของจริง, มีปลายทาง

## เกิดอะไรขึ้น

วันที่ 6 พ.ค. 2026 ที่ Team '26 ใน Anaheim Atlassian วาง pivot ที่ใหญ่ที่สุดของบริษัทในรอบสิบปี — เปิด Teamwork Graph ให้ AI agent ค่ายอื่นเข้าถึงโดยตรง ผ่าน Rovo MCP Server (open beta) และ Teamwork Graph CLI ที่มี 300+ commands ตัวอย่างที่ Atlassian โชว์: dev เปิด Claude Code หรือ Cursor บนเครื่องตัวเอง พิมพ์ query ที่ดึง Jira issue, Confluence page, Bitbucket PR, และ Loom transcript กลับมาในคำสั่งเดียว พร้อมเขียนกลับเข้าไปใน graph ได้ — ตัว agent ไม่ต้องอยู่ใน Atlassian product เลย

ตัวเลขที่ Atlassian โชว์อ่านแล้วน่าทึ่ง: Teamwork Graph ตอนนี้มี 150 billion connections ระหว่าง work artifact, Rovo-assisted action ทำไป 14+ ล้านครั้งใน 30 วันที่ผ่านมา, agentic automation เพิ่มขึ้น 7 เท่าใน 6 เดือน, และ 90%+ ของ enterprise cloud customer ใช้ Rovo อย่างน้อยหนึ่ง surface — ตัวเลขกลุ่ม horizontal SaaS ที่ pivot ไป agentic ที่หาได้ยาก คนส่วนใหญ่ยังไม่ผ่าน 30% สำคัญที่สุดคือเขาให้ stat ว่า "AI ที่ ground บน Teamwork Graph ตอบถูก 44% มากกว่า + ใช้ token น้อยกว่า 48%" — ข้ออ้างแรกที่ context layer ลด hallucination ได้ measurably ในระดับ enterprise

Customer story มีน้ำหนัก: SpotOn ใช้ Rovo deflect support ticket จาก 40% เป็น 53% (clean deflection) โดย answer rate ของคำถามอยู่ที่ 95%, Teach for All สร้าง agent ที่ generate weekly report 60–70% โดยอัตโนมัติ, Lendi Group ใช้ agent เดียวเดินข้าม Jira, Confluence, Slack — Matthew Hargreaves CTO ของ Lendi พูดประโยคที่จะ quote ในทุก deck ปีนี้: "Rovo and Atlassian's Teamwork Graph are the connective spine. That's what takes us from AI hovering at the edges to AI embedded in the core" — แปลตรง ๆ คือ "ใครไม่มี graph ที่ทำงาน AI อยู่ขอบ ไม่ได้อยู่ในเนื้อ"

ที่ surface ของ Rovo Studio ก็ general available แล้ว — no-code agent builder ที่มี role/approval/version/audit ครบ พร้อม Max Mode (early access) ที่ใช้ reasoning model ทำ autonomous planning + execution ไม่ใช่แค่ Q&A เหมือนเดิม Atlassian วาง Rovo ให้เป็น "agent OS ของ knowledge work" คล้าย ServiceNow Control Tower แต่จับฝั่ง engineering + project management แทน IT/HR ใต้ฝาคือ MCP server + CLI ที่เปิดให้ outside agent เข้ามากินข้อมูลเดียวกัน — เป็น declared open posture ที่หาได้ยากใน enterprise SaaS ใหญ่

## ทำไมสำคัญ

ที่ Atlassian ยอมเปิด Teamwork Graph ผ่าน MCP คือ admit ที่ตรงไปตรงมาว่า agent ที่ลูกค้าจะใช้จริง ไม่ใช่ Rovo อย่างเดียว — Claude Code กับ Cursor ครองใจ dev อยู่แล้ว ChatGPT ครองใจ exec; ถ้า Atlassian ปิด graph ลูกค้าจะ scrape ข้อมูลจาก API หรือไม่ก็ย้าย system of record ไป Linear/Notion ที่เปิดกว้างกว่า Atlassian เลือก strategy ที่ตรงข้ามกับ Microsoft ที่ใช้ Agent 365 ห่อทุกอย่างไว้ภายใน — เปิดกว้าง วาง bet ว่า graph เป็น moat ที่จริง ไม่ใช่ chat UI

ที่อันตรายของ pivot นี้คือ: ถ้า third-party agent มีประสิทธิภาพดีกว่า Rovo (และมีโอกาสสูง — Cursor + Claude Code มี data flywheel ของตัวเอง) Atlassian จะกลายเป็น "data warehouse for agents" ที่เก็บเงินจาก storage + write-back ไม่ใช่ application layer แบบเดิม นี่คือ pattern ที่ Twilio เจอในยุค SMS API — เก็บเงินจาก call ไม่ใช่ UX ราคา per-action ของ Rovo จะเป็น signal สำคัญใน earning call Q3 ว่า strategy นี้ทำงานหรือไม่

อีกประเด็น: 44% accuracy uplift + 48% token saving จาก Teamwork Graph grounding คือ marketing claim ที่ปะทะกับทุก vector DB / context platform โดยตรง (Cohere, Pinecone, Glean) — ถ้าตัวเลขนี้ verify ได้ใน third-party benchmark Atlassian จะกลายเป็น default substrate ของ enterprise RAG agent ทันที กระดานอุตสาหกรรมตอนนี้ split ชัด: Microsoft (closed Agent 365), ServiceNow (closed Control Tower), Salesforce (Agentforce + Data Cloud), Atlassian (open via MCP) — ใครชนะขึ้นกับว่า dev จะเลือก agent ของตัวเองข้าม graph ใคร และลูกค้าจะ pay rent ให้ใคร

## มุม OpenBridge

นี่คือข่าวที่ OpenBridge ต้องอ่านสองรอบ — เพราะ Atlassian เปิดเส้นทางที่ OpenBridge อยู่ห่างจากการเป็นเจ้าของแค่ก้าวเดียว (1) **Teamwork Graph CLI + MCP server เป็น blueprint ที่ OpenBridge ควรลอกในรอบนี้** — OpenBridge มี integration metadata ของ HubSpot, Stripe, Shopify, LINE OA, SAP อยู่แล้ว ถ้าเปิด "OpenBridge Graph CLI" ที่ Claude Code/Cursor ดึง entity relationship ระหว่าง customer/order/invoice ข้ามระบบลูกค้าได้ใน command เดียว = positioning ตรงกับ Atlassian แต่จับ B2B commerce stack แทน knowledge work (2) **44% accuracy + 48% token saving คือ benchmark ที่ OpenBridge ต้อง measure** — ถ้า connector ของเรา ground agent ดีกว่า raw API call (เพราะมี schema + relationship + business logic) ตัวเลขนี้คือเหตุผลที่ลูกค้าเลือกจ่าย OpenBridge แทน build เอง (3) **Rovo MCP server เปิดเตียงให้ Claude Code วิ่งบน Jira ของลูกค้า — Yoh agent ของ OpenBridge ก็ควรวิ่งบน Jira ของลูกค้าได้เช่นกัน** ผ่าน Rovo MCP เพื่อ orchestrate cross-system ticket: เปิด Jira issue → trigger HubSpot deal stage change → ลง Stripe invoice — เคสจริงของ B2B SaaS ที่ใช้ทั้ง Atlassian + commerce stack

Adjacent insight: 90% enterprise cloud customer ใช้ Rovo แปลว่า ลูกค้า Thai Fortune 500 ที่ใช้ Atlassian อยู่แล้ว (SCG, KBank, AIS, CP) จะถูกบังคับ procure Rovo ใน renewal cycle ถัดไป OpenBridge ที่ทำ partnership กับ Atlassian Solution Partner ใน region (เช่น Adaptavist Asia, Eficode) จะได้ deal flow ที่ pre-qualified — เคลื่อนเร็วก่อน Sea/GoTo จะลงสนาม

## Sources
- [Atlassian opens Teamwork Graph and pushes Rovo into agentic execution at Team '26 | SiliconANGLE](https://siliconangle.com/2026/05/06/atlassian-opens-teamwork-graph-pushes-rovo-agentic-execution-team-26/)
- [Rovo makes AI-native teamwork real for the enterprise | Atlassian](https://www.atlassian.com/blog/company-news/rovo-team-26)
- [The new, unified Rovo Studio — more to build, easier than ever | Atlassian](https://www.atlassian.com/blog/company-news/rovo-studio-team-26)
- [Atlassian Opens Teamwork Graph to Third-Party AI Agents | The Letter Two](https://thelettertwo.com/2026/05/06/atlassian-teamwork-graph-open-third-party-ai-agents)

---

## Audio script
สวัสดีครับโย วันนี้เรื่องใหญ่จาก Atlassian ที่ Team '26 เมื่อวาน บริษัทเปิด Teamwork Graph ที่มี 150 billion connections ให้ AI agent ค่ายอื่นเข้าถึงโดยตรงผ่าน MCP server กับ CLI 300 กว่า command แปลว่า dev เปิด Claude Code หรือ Cursor บนเครื่องตัวเอง พิมพ์ query เดียว ดึง Jira issue Confluence page Bitbucket PR กลับมาพร้อม เขียนกลับเข้าไปใน graph ได้ ตัว agent ไม่ต้องอยู่ใน product Atlassian เลย

ตัวเลขที่โชว์อ่านแล้วน่าทึ่ง 14 ล้าน Rovo assisted action ในเดือนที่ผ่านมา 90% ของ enterprise cloud customer ใช้ Rovo agentic automation โต 7 เท่าใน 6 เดือน ที่สำคัญคือ Atlassian อ้างว่า AI ที่ ground บน Teamwork Graph ตอบถูกขึ้น 44% แถมใช้ token น้อยกว่า 48% เป็น claim แรกที่ context layer ลด hallucination ได้แบบ measurable ใน enterprise scale

Customer story ก็มีน้ำหนัก SpotOn deflect ticket จาก 40% เป็น 53% Teach for All สร้าง agent ที่ generate weekly report 60 ถึง 70% อัตโนมัติ Lendi Group เดินข้าม Jira Confluence Slack ด้วย agent เดียว CTO ของ Lendi พูดประโยคที่ดี ว่า Rovo กับ Teamwork Graph คือ connective spine ที่ทำให้ AI ฝังในเนื้อแทนที่จะ hover อยู่ขอบ

ที่สำคัญคือ Atlassian เลือก strategy ตรงข้าม Microsoft ที่ Agent 365 ห่อทุกอย่างไว้ Atlassian เปิดกว้างวาง bet ว่า graph เป็น moat จริง ไม่ใช่ chat UI ความเสี่ยงคือถ้า third party agent ดีกว่า Rovo Atlassian จะกลายเป็น data warehouse for agent เก็บเงินจาก storage แทน UX

มุม OpenBridge เรื่องนี้ใหญ่ครับ Teamwork Graph CLI กับ MCP server คือ blueprint ที่ OpenBridge ควรลอก เรามี metadata ของ HubSpot Stripe Shopify SAP อยู่แล้ว เปิด OpenBridge Graph CLI ให้ Claude Code Cursor ดึง entity relationship ข้ามระบบลูกค้าใน command เดียว positioning ตรง 44% accuracy 48% token saving คือ benchmark ที่ OpenBridge ต้อง measure ถ้า connector เรา ground agent ดีกว่า raw API นี่คือเหตุผลที่ลูกค้าจ่ายเรา และที่ Thai Fortune 500 ใช้ Atlassian อยู่แล้วเยอะ partnership กับ Atlassian Solution Partner คือ deal flow ที่ pre-qualified เคลื่อนเร็วก่อน Sea กับ GoTo ลงสนามครับ
