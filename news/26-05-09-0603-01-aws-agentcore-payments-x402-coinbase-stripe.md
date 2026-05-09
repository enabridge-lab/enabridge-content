---
date: 2026-05-08
slug: aws-agentcore-payments-x402-coinbase-stripe
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: A bold editorial illustration in deep navy and warm cream — at center, a stylized AWS smile-arrow logo in coral acts as a giant cash register drawer flying open, spilling glowing teal USDC coins into a row of small geometric robot silhouettes lined up like customers at a counter. Above the register a cream digital receipt strip reads 'HTTP 402' in big sans-serif letters, with '200ms' rendered very large in coral on the lower-right corner. Tiny Coinbase and Stripe wordmarks sit crisp on the side of the register like sponsor stickers. Editorial flat-vector style, dramatic spotlight, slate navy + cream + coral + teal palette, no human figures, logos crisp for 200px thumbnail readability.
image: images/26-05-09-0603-01-aws-agentcore-payments-x402-coinbase-stripe.png
---

# AWS เปิด AgentCore Payments — agent จ่ายเงิน agent ด้วย USDC ผ่าน x402, settle 200ms ต่ำกว่าเศษเซ็นต์

## TL;DR
- 7 พ.ค. 2026 AWS เปิด **Amazon Bedrock AgentCore Payments (preview)** — managed payment layer ที่ให้ agent autonomous discover, authorize, execute micropayment เองได้ ผ่าน protocol **x402** (HTTP 402) + USDC stablecoin บน Base — partner กับ Coinbase + Stripe ทำ wallet/rails
- ตัวเลขที่ทำลายเกม: settle ~**200ms**, ค่าธรรมเนียม "**less than a fraction of a cent**" ต่อ transaction — เปิดทางให้ pay-per-API-call, pay-per-MCP-call, pay-per-agent-handoff เป็นเรื่องปกติ — ของแบบที่ Stripe/credit card ทำไม่ได้เพราะ overhead เกินค่าของ
- ก่อนหน้านี้ 1 วัน (6 พ.ค.) AWS ก็เปิด **AWS MCP Server GA** + **Agent Toolkit** — agent เข้าถึง 15,000+ AWS APIs ผ่าน IAM/CloudTrail/CloudWatch governance — รวมกันคือ AWS เปิดประตู "agent คือลูกค้าใหม่ของ cloud"

## เกิดอะไรขึ้น

วันที่ 7 พ.ค. 2026 ที่งาน AWS Summit AWS ประกาศเปิดตัว **Amazon Bedrock AgentCore Payments** ในสถานะ preview — managed service ที่อยู่ใต้ AgentCore (runtime สำหรับ agent บน Bedrock) ทำหน้าที่ wallet + spending policy + audit trail ให้ agent จ่ายเงินเองได้โดยไม่ต้องขัด reasoning loop ตัว spec ที่เป็น backbone คือ **x402** — protocol ที่ Coinbase pitch มาตั้งแต่ปลายปีก่อน ฟื้นชีพ HTTP status code 402 (Payment Required) ที่เคยเป็น dead letter ใน RFC 7231 ให้กลายเป็น handshake จริง ระหว่าง client กับ paid resource

วิธีทำงาน: agent ยิง request ไปที่ paid API/MCP server/agent endpoint → ปลายทางตอบ 402 พร้อม payload ที่บอก amount + chain + recipient → AgentCore เห็น 402 ปุ๊บ ตรวจ spending policy ที่ owner ตั้งไว้ (เช่น "ห้ามเกิน $50/วัน, ห้าม recipient นอก allowlist") ถ้า pass → authenticate wallet → จ่าย USDC บน Base → แนบ proof กลับไปที่ original endpoint → response ไหลกลับมาที่ agent ทั้งหมดนี้ Coinbase อ้างว่า settle ใน **~200 มิลลิวินาที** ค่าธรรมเนียม "less than a fraction of a cent" — เลข sub-cent ไม่ใช่ marketing fluff แต่เป็น property ของ Base L2 + USDC ที่ Stripe ผ่าน Privy ไป tokenize wallet ให้ใหม่ทุก agent

จุดที่น่าสังเกตคือ AWS ไม่ได้มาเดี่ยว — Stripe มาเป็น wallet provider ผ่าน Privy (Stripe ซื้อ Privy ปลายปี 2025) Coinbase มาเป็น settlement chain + USDC issuer ทั้งสามฝ่ายเขียน press releases วันเดียวกัน ดูเหมือน choreographed มาก: AWS ขายว่าเป็น "agent infrastructure", Coinbase ขายว่าเป็น "agentic commerce", Stripe ขายว่าเป็น "every AI agent has a wallet by default" ทำให้ narrative กระจายไป 3 community พร้อมกัน — AWS dev, crypto, fintech

ก่อนหน้านี้แค่วันเดียว 6 พ.ค. AWS ก็ปล่อย **AWS MCP Server GA** พร้อม **Agent Toolkit for AWS** — single MCP server ที่ expose AWS APIs **15,000+** call ให้ coding agent (Claude Code, Codex, Cursor, Copilot) ใช้ผ่าน IAM credential ของลูกค้าเอง มี sandboxed Python execution, CloudTrail audit log, CloudWatch metric ทุก call ฟรีของ AWS เอง (จ่ายเฉพาะ resource ที่ agent สร้าง) และมี mode "read-only" สำหรับ enterprise ที่ paranoid สองข่าวรวมกันคือ AWS เปิดประตูสองด้าน: ด้าน **input** ให้ agent คุย AWS ได้, ด้าน **output** ให้ agent จ่ายเงินคนอื่น (และคนอื่นจ่ายให้ agent) ได้

## ทำไมสำคัญ

นี่คือครั้งแรกที่ hyperscaler ระดับ AWS ยอมรับ public ว่า agent **เป็น economic actor** ไม่ใช่แค่เครื่องมือของคน Stripe เคย ship Agent SDK + bot detection แต่ยังเป็น human-on-the-loop AWS วันนี้ตัด human ออก — agent มี wallet ของตัวเอง, มี budget ของตัวเอง, ทำธุรกรรมเองภายใต้ policy ที่ owner เซ็ตไว้ pattern นี้ตรงกับที่ Anthropic ลาก spec **MCP Payments** ออก draft เมื่อปลายเดือนก่อน — ทุก major lab + cloud กำลัง converge ที่ "agent commerce" เป็น L1 primitive ภายในสิ้นปี 2026 เกือบแน่ว่าจะมี OpenAI version (Workspace Agents Wallet?), Google version (อาจ A2A Payments), และ Microsoft version (Agent 365 Wallet) ออกตามมา

ถ้ามองเชิงเศรษฐกิจ: ค่าธรรมเนียม sub-cent + settle 200ms **ลบ floor ของ pay-per-API ลงไปอีก 100 เท่า** ของ stripe ปกติ — ก่อนนี้ API ที่ value ต่ำกว่า $0.30/call จ่าย credit card ไม่ได้เพราะค่าธรรมเนียมสูงกว่า revenue ตอนนี้ API ที่ value $0.001/call ก็จ่ายได้ — เปิดตลาดใหม่ทั้งหมดของ "atomic API" เช่น single sentiment classification, single OCR call, single tool invocation บน MCP server เปิดทาง economy ที่ MCP server ทำเงินได้เองโดยไม่ต้องผ่าน subscription — เป็น Internet ยุคใหม่ที่ HTTP 402 ทำงานจริงครั้งแรกในรอบ 30 ปี

ที่ต้องระวัง: ถ้า agent มี wallet + autonomous spending — surface area ของ fraud + prompt injection + supply chain attack ขยายตัว exponential agent ที่ถูก inject prompt ให้จ่าย $50 ไปยัง wallet ที่ attacker ควบคุม จะเป็นเรื่องปกติภายใน 6 เดือน — และ Snyk เพิ่งเปิดตัว Evo Agent Security (ดู brief #02) สำหรับเคสแบบนี้พอดี ไม่ใช่บังเอิญที่ทุกอย่างทยอย ship สัปดาห์เดียวกัน

## มุม OpenBridge

OpenBridge ต้องอ่านสามอย่างจากข่าวนี้ **(1) MCP server ของ OpenBridge สามารถกลายเป็น revenue source โดยตรง** — ทุก connector ที่ enterprise ต่อผ่าน OpenBridge MCP (HubSpot lookup, Stripe charge, Shopify order) ตอบ 402 พร้อมกำหนดราคาเอง → AgentCore ของลูกค้าจ่ายผ่าน USDC อัตโนมัติ → revenue per-call แบบ on-demand ไม่ต้อง onboard sales call โมเดล "pay-per-MCP-call" ทำให้ OpenBridge ไม่ต้องไล่ subscription ของ enterprise ที่ความถี่ใช้ irregular — ลูกค้า Fortune 500 ที่ใช้ HubSpot connector 100 calls/วัน vs 10,000 calls/วัน จ่าย proportional โดยไม่ต้อง renegotiate contract

**(2) policy enforcement ที่ AgentCore Payments จะกลายเป็น "ภาษีกลาง" ของทุก agent transaction** — OpenBridge ต้อง emit metadata ที่ AgentCore policy engine กิน: invoice ID, ราคา, expected latency, vendor reputation score, region of compute สิ่งเหล่านี้คือ schema ใหม่ที่ทุก connector ต้องทำเพื่อให้ enterprise admin set policy "OpenBridge connector อนุญาตได้, ราคาห้ามเกิน 0.05 USDC/call" — connector ไหน emit metadata ไม่ครบ จะถูก default block

**(3) AWS MCP Server GA = template ของ "official MCP server" ที่ enterprise คาดหวัง** — มี IAM-equivalent, CloudTrail-equivalent audit log, sandboxed execution OpenBridge MCP ต้อง match ให้ครบ: per-tenant credential isolation, structured audit log ที่ ingest เข้า ServiceNow Control Tower / Microsoft Purview / Splunk ได้, sandbox สำหรับ tool ที่ run code; ถ้าออกแบบ MCP server ที่ "AWS-grade" ตั้งแต่วันแรก จะ slot เข้า enterprise ได้โดยไม่ต้อง security review ยาว 3 เดือน

## Sources
- [Agents that transact: Amazon Bedrock AgentCore now includes Payments (preview) | AWS](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-agentcore-payments-preview/)
- [Agents that transact: Introducing Amazon Bedrock AgentCore payments, built with Coinbase and Stripe | AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/)
- [Amazon Bedrock Launches AI Agent Payment Capabilities With Coinbase, Stripe | PYMNTS.com](https://www.pymnts.com/amazon-payments/2026/amazon-bedrock-launches-ai-agent-payment-capabilities-with-coinbase-stripe/)
- [The AWS MCP Server is now generally available | AWS](https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/)
- [Amazon's new AI wallet: AWS, Coinbase, and Stripe build payment rails for bots | CoinDesk](https://www.coindesk.com/business/2026/05/07/amazon-rolls-out-ai-agent-stablecoin-payments-platform-with-coinbase-and-stripe)

---

## Audio script
สวัสดีครับโย วันนี้ AWS ทำสองข่าวในสองวันที่เปลี่ยนเกม agent infrastructure ระดับ foundational ครับ วันที่ 6 พ.ค. ปล่อย AWS MCP Server GA agent เข้าถึง AWS API หนึ่งหมื่นห้าพันตัวผ่าน IAM, CloudTrail, CloudWatch ใช้ฟรีจ่ายเฉพาะ resource ที่สร้าง วันรุ่งขึ้น 7 พ.ค. ปล่อย AgentCore Payments preview ให้ agent ค้นหาจ่ายเงินเองผ่าน HTTP 402 และ x402 protocol ใช้ USDC บน Base settle 200 มิลลิวินาที ค่าธรรมเนียมต่ำกว่าเศษเซ็นต์

partner คือ Coinbase ดูแล chain Stripe ดูแล wallet ผ่าน Privy ที่ Stripe ซื้อปลายปีก่อน ทำให้ทุก agent มี wallet default มี spending policy ที่ owner เซ็ต เช่นห้ามเกิน 50 ดอลลาร์ต่อวัน ห้าม recipient นอก allowlist agent ไม่ต้องมี human อนุมัติแต่ละครั้ง

นี่คือครั้งแรกที่ hyperscaler ยอมรับว่า agent เป็น economic actor ไม่ใช่เครื่องมือของคน ค่าธรรมเนียม sub cent ลบ floor ของ pay per API ลง 100 เท่า เปิดตลาด atomic API ที่ value ต่ำกว่า 1 cent ต่อ call เป็นไปได้ MCP server ทำเงินได้เองโดยไม่ต้องผ่าน subscription HTTP 402 ทำงานจริงครั้งแรกในรอบ 30 ปี

มุม OpenBridge สามเรื่อง หนึ่ง MCP server ของเรากลายเป็น revenue source โดยตรง ทุก connector ตอบ 402 พร้อมราคา AgentCore จ่ายอัตโนมัติ ลูกค้าจ่ายตาม usage จริงไม่ต้อง subscribe สอง policy enforcement ของ AgentCore จะเป็นภาษีกลาง connector ต้อง emit metadata invoice ID ราคา latency vendor score ครบไม่งั้น default block สาม AWS MCP Server เป็น template ที่ enterprise คาดหวัง OpenBridge ต้อง match per tenant credential, structured audit log, sandbox ให้ครบ ออกแบบ AWS grade ตั้งแต่วันแรก slot เข้า enterprise ได้โดยไม่ต้อง security review สามเดือนครับ
