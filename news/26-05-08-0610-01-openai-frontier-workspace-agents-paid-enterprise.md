---
date: 2026-05-07
slug: openai-frontier-workspace-agents-paid-enterprise
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: A bold editorial illustration framed in deep navy and warm cream — at center, a stylized OpenAI swirl logo glows white with an oversized cream price tag dangling from it that reads 'CREDITS' in big sans-serif letters. Below, four geometric flat icons of Slack, Salesforce, AWS Bedrock and Microsoft Teams march in a single row like train cars, each connected by a glowing teal data line that loops back into the OpenAI logo. A bright coral headline 'WORKSPACE AGENTS' arches over the top, with '40%' rendered very large in cream on the lower-right corner indicating enterprise share of revenue. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + teal palette, no human figures, logos crisp for 200px thumbnail readability.
image: 
---

# OpenAI พลิก Workspace Agents เป็น paid + เปิด Frontier เป็น "enterprise OS" — Enterprise แตะ 40% รายได้แล้ว

## TL;DR
- OpenAI ปิด free preview ของ Workspace Agents ในวันที่ 6 พ.ค. 2026 — เริ่มเก็บเงิน credit-based; พ่วงประกาศ "next phase of enterprise AI" ที่ enterprise ทำรายได้ >40% และตั้งเป้า parity กับ consumer ภายในสิ้นปี
- Frontier ถูก position ใหม่เป็น "intelligence layer" ที่กำกับ agent ทั้งบริษัท — ลูกค้าที่ public แล้วมี Oracle, State Farm, Uber; พร้อมขยาย GPT-5.5 + Codex + Bedrock Managed Agents เข้า AWS — แปลว่า OpenAI ยอมแยกตัวจาก Azure exclusivity
- Workspace Agents ออกแบบให้ agent เดียวข้าม tool ได้ — Slack, Salesforce, Google Drive, ChatGPT, Office — มี admin control ระดับ user group และ Codex รันอยู่ใต้ฝา; บริษัทคู่แข่ง custom GPT ที่เคย free จะถูกบังคับ migrate

## เกิดอะไรขึ้น

วันที่ 6 พ.ค. 2026 OpenAI ปิดยุค free preview ของ Workspace Agents อย่างเป็นทางการ — feature ที่เปิดให้องค์กรใน ChatGPT Business, Enterprise, Edu, Teachers สร้าง shared agent ที่ทำ workflow ยาว ๆ แทนคน เริ่มเดินมิเตอร์เก็บเงินแบบ credit-based เต็มตัว วันเดียวกัน OpenAI โพสต์ "The next phase of enterprise AI" บอกว่า enterprise ทำรายได้ทะลุ 40% ของบริษัทแล้ว และคาดว่าจะแตะ parity กับฝั่ง consumer ภายในสิ้นปี 2026 — ตัวเลขที่ทำลายภาพ ChatGPT-as-consumer-app ที่ทุกคนคิดมาตลอดสองปี

หัวใจของ pivot นี้คือคำว่า "Frontier" — OpenAI วาง Frontier เป็น "intelligence layer" ที่อยู่เหนือ agent ทุกตัวในบริษัท ลูกค้าที่ public แล้วมี Oracle, State Farm และ Uber ใช้ Frontier เป็น control plane ที่ agent หนึ่งตัวสามารถเดินข้ามระบบและ data store ได้ — ต่างจาก Custom GPTs (ที่ปลด deprecated หลังจากนี้) ที่ผูกอยู่ในกล่อง ChatGPT Workspace Agents เองคือ "spec-as-product": บริษัทเขียน spec หนึ่งครั้ง agent ตัวเดียวรันได้ทั้งใน ChatGPT, Slack, และระบบที่บริษัทต่อ — มี admin console ควบคุมว่าใครใช้ tool ไหนได้, build ใครใช้ build ได้, share ระหว่าง user group ใหญ่แค่ไหน

ใต้ฝาของ Workspace Agents คือ Codex — model line agentic ของ OpenAI ที่เคยใช้กับ developer-facing งาน คราวนี้ขยายมาเป็น runtime ของ knowledge worker agent ทั้งบริษัท ระบบ run on cloud, persist ระหว่าง session, มี approval gate, และ honor permission ที่ตั้งจาก ChatGPT Enterprise admin — แปลว่า OpenAI ขยับจาก "AI assistant ให้คน" เป็น "AI worker ที่มี HR file ของตัวเอง" และคิดเงินแบบ usage

วันเดียวกัน OpenAI ประกาศย้าย GPT-5.5 + Codex ขึ้น Amazon Bedrock พร้อมเปิด Bedrock Managed Agents ที่ powered by OpenAI — ย้ำว่า lock-in กับ Azure ที่บางคนกลัวมาตลอดเริ่มคลายตัว ลูกค้า Bedrock ขนาด Capital One, Pfizer, BMW ที่แต่ก่อนเข้าถึง OpenAI ผ่าน partner ตอนนี้สามารถ deploy ผ่าน AWS เองได้ — และ OpenAI กับ Anthropic ก็จะอยู่ใน Bedrock ร่วมกัน ลูกค้า Fortune 500 ที่ต้องการ multi-model fallback จะรู้สึก unblocked ทันที

## ทำไมสำคัญ

ที่ enterprise โต 40% ของรายได้ + ตั้งเป้า parity ปลายปี + เริ่มเก็บเงิน Workspace Agents วันเดียวกัน คือ signal ว่า OpenAI เลิก subsidize free product เพื่อ user growth แล้ว — อยู่ใน phase "monetize seriously" บริษัทไหนที่ยัง POC ฟรีอยู่จะเริ่มเห็นใบ invoice ใน Q3 และตัด budget จากที่อื่น pattern คล้าย AWS ปี 2010 ที่บีบ free credit จน startup ต้องเลือกข้าง — ปลายทางคือ OpenAI กลายเป็น utility ที่บริษัทจ่ายเหมือนจ่ายไฟฟ้า แต่ราคา elastic ตาม usage ของ agent ที่บางตัวรัน 24/7

อีกประเด็นคือ Frontier เป็นชื่อที่จงใจซ้อนกับ "AI operating system" ที่ Salesforce, ServiceNow, IBM, Microsoft ออกของพร้อมกันในเดือนเดียวกัน — Salesforce มี Agentforce 360, ServiceNow เปิด AI Control Tower, Microsoft GA Agent 365 ($15/user/month), IBM ออก watsonx Orchestrate next-gen + Concert ที่ Think 2026 ทุกค่ายกำลัง claim "intelligence layer" เหนือ agent stack — กระดานเปลี่ยนจาก "ใครมี LLM ดีกว่า" เป็น "ใครเก็บ rent ระดับ orchestration ได้" สำคัญที่สุดคือ ใน Workspace Agents และ Frontier ลูกค้าจะเขียน spec ครั้งเดียวแล้วรันได้ทุก surface — ใครยอมให้ลูกค้า portable ก่อน คนนั้นชนะ

ที่น่าจับตา: GPT-5.5 บน Bedrock + Codex บน AWS แปลว่า OpenAI ยอมรับว่า exclusivity Azure ไม่ scale พอ และต้องเปิด surface ให้ลูกค้า AWS ที่เป็น majority ของ Fortune 500 พ่วงกับข่าวที่ Anthropic ยอมจ่าย $200B ให้ Google เพื่อ TPU — ภาพรวมคือ ทุก foundation model lab กำลัง diversify cloud ให้ขนานกัน ปี 2026 ตลาดยอมรับแล้วว่า "AI = multi-cloud" ไม่ใช่ "AI = hyperscaler เดียว"

## มุม OpenBridge

OpenBridge ต้องอ่านสามอย่างจากข่าวนี้ทันที (1) **Workspace Agents จะมาเรียก OpenBridge ผ่าน MCP/connector** — agent ของลูกค้าที่ build ใน ChatGPT Enterprise จะ invoke tool บน HubSpot, Stripe, Shopify ผ่านเรา; ถ้าเรามี MCP server ที่ "auto-discover" ใน ChatGPT registry, dev ของลูกค้าต่อใช้ใน 5 นาที — กลายเป็น default integration layer; ถ้าไม่มี OpenAI จะใช้ official partner connector แทน (2) **credit-based pricing ของ Workspace Agents = ลูกค้าจะ optimize per-call cost** — connector ไหนเรียก expensive call (Salesforce SOAP, Shopify REST ที่ rate-limit) จะถูก benchmark; OpenBridge ที่ออกแบบ connector ให้ batch + cache ไว้ตั้งแต่วันแรก จะ win ที่ "ราคาต่อ outcome" ไม่ใช่ "feature count" (3) **Frontier vs ServiceNow vs Microsoft Agent 365 = ลูกค้าจะใช้หลายค่ายพร้อมกัน** — OpenBridge ต้อง emit telemetry ที่ทุก control plane กิน — ใช้ OpenTelemetry agent semantic convention ที่ Microsoft วางไว้, ส่งไป ServiceNow Control Tower, log ลง Frontier audit trail — กลายเป็น "Switzerland of agent telemetry"

Adjacent insight: ที่ enterprise = 40% ของ OpenAI revenue + GPT-5.5 ขึ้น Bedrock = ลูกค้า Thai Fortune 500 จะเริ่มจ้าง integration partner เร็วขึ้นใน H2 — OpenBridge ควรเตรียม "Workspace Agents starter pack" ที่ pre-wire HubSpot/Salesforce/LINE OA/SAP ให้ดี ก่อนคู่แข่ง regional (Sea, GoTo) ลงสนาม

## Sources
- [The next phase of enterprise AI | OpenAI](https://openai.com/index/next-phase-of-enterprise-ai/)
- [Introducing workspace agents in ChatGPT | OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)
- [OpenAI unveils Workspace Agents, a successor to custom GPTs for enterprises that can plug directly into Slack, Salesforce and more | VentureBeat](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more)
- [OpenAI, Anthropic expand services push, signaling new phase in enterprise AI race | CIO](https://www.cio.com/article/4167787/openai-anthropic-expand-services-push-signaling-new-phase-in-enterprise-ai-race.html)

---

## Audio script
สวัสดีครับโย วันนี้ OpenAI ทำสามอย่างพร้อมกันที่เปลี่ยนเกม enterprise หนึ่งคือปิด free preview ของ Workspace Agents เริ่มเก็บเงินแบบ credit base ตั้งแต่ 6 พ.ค. สองคือเปิดเผยว่า enterprise ทำรายได้เกิน 40% ของบริษัทแล้ว ตั้งเป้าเท่าฝั่ง consumer ภายในสิ้นปี และสามคือย้าย GPT 5.5 กับ Codex ขึ้น Amazon Bedrock พร้อมเปิด Bedrock Managed Agents ที่ powered by OpenAI

หัวใจของ pivot คือ Frontier ที่ OpenAI วางเป็น intelligence layer เหนือ agent ทุกตัวในบริษัท ลูกค้าที่เผยตัวคือ Oracle State Farm Uber Workspace Agents เองคือ spec ที่เขียนครั้งเดียว แล้วรันได้ทั้งใน ChatGPT Slack Salesforce Google Drive และระบบของบริษัท Codex อยู่ใต้ฝา persistent run on cloud มี approval gate มี admin control ระดับ user group

ที่สำคัญคือทุกค่าย ServiceNow Salesforce IBM Microsoft กำลัง claim ตำแหน่ง intelligence layer แบบเดียวกัน เกมไม่ใช่แข่ง LLM ใครเก่งกว่าแล้ว แต่เป็นใครเก็บ rent ระดับ orchestration ได้ ใครยอมให้ลูกค้า portable ก่อน คนนั้นชนะ

มุม OpenBridge สามเรื่อง หนึ่งคือ Workspace Agents จะเรียก OpenBridge ผ่าน MCP เรียกผ่าน connector ของเรา ถ้ามี MCP server auto discover ใน ChatGPT registry dev ต่อได้ใน 5 นาทีกลายเป็น default สองคือ credit pricing ทำให้ลูกค้า optimize per call cost connector ที่ batch กับ cache ดีจะ win ที่ราคาต่อ outcome สามคือลูกค้าใช้หลาย control plane พร้อมกัน OpenBridge ต้อง emit telemetry ที่ Frontier ServiceNow Microsoft กินได้หมด เป็น Switzerland ของ agent telemetry ครับ
