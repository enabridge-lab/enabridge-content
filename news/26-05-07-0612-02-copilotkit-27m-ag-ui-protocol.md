---
date: 2026-05-06
slug: copilotkit-27m-ag-ui-protocol
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: A central abstract glowing cube representing an enterprise application sits on a deep navy editorial background, its faces shimmering teal. From inside the cube, four bold conduit lines extend outward toward four flat geometric badges of Google, Microsoft, Amazon and Oracle logos arranged around it in symmetric corners — clear brand marks, no faces. A stream of small chat-bubble silhouettes flows along the conduits, fusing into the cube's surface as part of the UI. Bold cream sans-serif headline 'AG-UI' floats top-left, with '$27M' rendered very large in coral on the lower-right corner. Editorial illustration, flat geometric shapes with subtle gradients, slate blue + teal + coral + cream palette, dramatic side-lighting from upper-right.
image: images/26-05-07-0612-02-copilotkit-27m-ag-ui-protocol.png
---

# CopilotKit ระดม $27M — protocol "AG-UI" ที่ Google/Microsoft/Amazon/Oracle ลงเรือพร้อมกัน

## TL;DR
- CopilotKit ปิด Series A $20M (รวม seed ที่ไม่เคยประกาศ $7M = $27M) นำโดย Glilot Capital, NFX, SignalFire — Fortune 500 majority ใช้แล้ว
- AG-UI เป็น open protocol สำหรับ embed agent เข้า UI โดยตรง — Google, Microsoft, Amazon, Oracle adopt เป็น standard ทำให้เกิด layer ใหม่: agent ไม่ใช่ chatbot ข้างหน้าจอแต่ฝังเข้า workflow จริง
- เปิดตัว CopilotKit Enterprise Intelligence — self-hosted bundle สำหรับ deploy agent ใน app ของตัวเอง ลูกค้าหลักคือ Deutsche Telekom, Docusign, Cisco, S&P Global

## เกิดอะไรขึ้น

5 พ.ค. 2026 CopilotKit จาก Seattle ประกาศปิด Series A $20M นำโดย Glilot Capital ร่วมกับ NFX และ SignalFire พร้อมเปิดเผยว่า seed round ก่อนหน้านี้ที่ไม่เคยประกาศมียอด $7M รวมเป็น $27M total funding รอบนี้ บริษัทอ้างว่าได้ใช้งานแล้วโดย Fortune 500 majority และ process millions of agent-user interactions ต่อวันใน production จริง — รายชื่อลูกค้าที่ปล่อยมาให้ดูคือ Deutsche Telekom, Docusign, Cisco, S&P Global

แต่จุดที่ทำให้เรื่องนี้ใหญ่กว่าตัวเลข funding คือ AG-UI — open protocol ที่ CopilotKit เป็นเจ้าภาพ ตัว protocol standardize วิธี agent คุยกับ UI ของแอปลิเคชัน: streaming chat, front-end tool calls, state sharing สามอย่างนี้รวมเป็น spec เดียว และตัว spec นี้ Google, Microsoft, Amazon, Oracle adopt เป็น standard ของ stack agent ของตัวเองแล้ว นี่คือสัญญาณ — เมื่อสี่เจ้าใหญ่ pile-on protocol ของ startup เล็กพร้อมกัน ตลาดกำลัง converge

CEO Atai Barkai บอกใน TechCrunch ว่าวิสัยทัศน์ของบริษัทคือ "kill the AI chatbot era" — แทนที่ user ต้อง chat กับ bot ข้าง ๆ หน้าจอ agent จะฝังเข้าเป็นส่วนหนึ่งของ UI โดยตรง เห็น state เดียวกับ user, เรียก function ของ frontend ได้ และไหลไปกับ workflow แทนที่จะตัดขาดเป็นช่อง chat

CopilotKit เปิดตัวพ่วงคือ CopilotKit Enterprise Intelligence — bundle self-hostable สำหรับองค์กรที่อยากได้ infrastructure ครบเซ็ตเพื่อ deploy agent เข้าแอปของตัวเอง คล้าย Cloudflare Workers AI หรือ Vercel AI SDK แต่เน้นชั้น UI orchestration มากกว่า model serving

## ทำไมสำคัญ

หกเดือนที่แล้ว Anthropic ขับเคลื่อน MCP (Model Context Protocol) ให้กลายเป็น standard เชื่อมต่อ agent กับ data source — ตอนนี้ AG-UI กำลังทำสิ่งเดียวกันแต่อยู่อีกฝั่ง คือ standard ระหว่าง agent กับ user interface แปลว่า stack agent ของอุตสาหกรรมกำลังประกอบครบสามชั้น: MCP สำหรับ tools/data, Agent2Agent (A2A) ของ Google สำหรับ agent คุย agent, AG-UI สำหรับ agent คุย human-facing UI ใครยึด protocol ชั้นไหน ใครเก็บภาษีชั้นนั้น และ CopilotKit เพิ่งปักธงชั้นที่สาม

จุดสำคัญที่ตลาด under-appreciate: AG-UI เป็น "frontend layer" ที่ deep tech VC มัก undervalue เพราะดูเหมือน CSS framework แต่จริง ๆ มันเป็นพื้นที่ที่ agent ส่วนใหญ่ตายในการ deploy enterprise — ไม่ใช่เพราะ model ไม่ดี แต่เพราะ integrate เข้า UI ที่มีอยู่ของลูกค้ายาก, state management ระหว่าง agent กับ user สับสน, และ tool call จาก agent ไม่สามารถสะท้อนไปที่ UI element ได้ทันที CopilotKit แก้ exactly สามจุดนี้

ที่ตอกย้ำว่า AG-UI ไม่ใช่ protocol toy คือรายชื่อ adopter — Google, Microsoft, Amazon, Oracle ไม่ใช่กลุ่มที่ adopt อะไรเล่น ๆ และเทียบกับ Vercel ที่ระดม $100M ไปแล้วเพื่อทำ AI SDK + Vercel Agent ของตัวเอง การที่ CopilotKit ดึง Glilot และ NFX (ที่ไม่ใช่ deep AI VC แต่เก่ง enterprise SaaS) แปลว่า strategy ของบริษัทคือ horizontal protocol play ไม่ใช่ vertical product

## มุม OpenBridge

นี่คือเรื่องที่ใกล้ตัว OpenBridge ที่สุดในรอบนี้ — เพราะ AG-UI กับ MCP คือสอง protocol layer ที่ "agent-native integration platform" ในอนาคตจะตั้งอยู่บน OpenBridge ปัจจุบัน position ตัวเองเป็น integration backend (data + connector) แต่ถ้า horizon 12 เดือนข้างหน้า agent กลายเป็น primary user ของ integration ที่เราสร้าง, เราต้องตอบสองคำถาม: (1) connector ของเราพูด MCP ได้ไหม เพื่อให้ agent ของลูกค้า invoke tool ผ่านเราโดยไม่ต้องเขียน wrapper, (2) เรามี SDK ฝั่ง UI ที่พูด AG-UI ได้ไหม เพื่อให้ลูกค้าฝัง integration UI ของ OpenBridge เข้า frontend ของแอปตัวเองได้แบบ agent-native

ข้อเสนอ practical: ทีมควรประเมินอย่างน้อยว่า — ถ้าออก OpenBridge SDK ที่พูด AG-UI ตอนนี้ developer ที่กำลังสร้าง CopilotKit-powered app จะต่อ connector ของเราได้ใน 5 นาทีไหม? ถ้ายังต้องเขียน boilerplate 200 บรรทัด นั่นคือ moat ที่ไม่จำเป็น ขณะที่ adopter ของ AG-UI กำลังเพิ่มเร็ว — เป็น window เปิดที่จะวาง OpenBridge ให้เป็น default integration layer ของ Fortune 500 ที่ใช้ CopilotKit

## Sources
- [CopilotKit raises $27M to help devs deploy app-native AI agents | TechCrunch](https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/)
- [CopilotKit raises $27M Series A | CopilotKit Blog](https://www.copilotkit.ai/blog/series-a)
- [Seattle's CopilotKit raises $27M, as some of the biggest names in tech adopt its AI agent protocol | GeekWire](https://www.geekwire.com/2026/seattles-copilotkit-raises-27m-as-some-of-the-biggest-names-in-tech-adopt-its-ai-agent-protocol/)
- [CopilotKit raises $27M to embed AG-UI agents inside apps | Mezha](https://mezha.net/eng/bukvy/7eb21e76_copilotkit_raises_-27m/)

---

## Audio script
อีกเรื่องที่อยากให้สนใจ คือ CopilotKit จาก Seattle ปิด Series A $20 ล้าน บวก seed เก่าที่ไม่เคยประกาศอีก $7 ล้าน รวม $27 ล้าน นำโดย Glilot Capital, NFX, SignalFire ลูกค้าหลักคือ Deutsche Telekom, Docusign, Cisco, S&P Global บริษัทบอกว่ามี Fortune 500 ส่วนใหญ่ใช้แล้ว

ที่ใหญ่กว่าตัวเลข funding คือ protocol ที่บริษัทเป็นเจ้าภาพ ชื่อ AG-UI เป็น open standard สำหรับให้ agent ฝังเข้า UI ของแอปได้โดยตรง ไม่ใช่ chatbot ข้าง ๆ จอแบบเดิม เปิด state สื่อสารกับ user ได้ และ Google Microsoft Amazon Oracle ก็ adopt เป็น standard ของตัวเองแล้ว

ความหมายเชิง stack คือ ตอนนี้อุตสาหกรรม agent ครบสามชั้น MCP สำหรับเชื่อม data tool, Agent2Agent ของ Google สำหรับ agent คุย agent, แล้ว AG-UI ของ CopilotKit สำหรับ agent คุย UI ใครคุม protocol ชั้นไหน คนนั้นเก็บภาษีชั้นนั้นยาว ๆ

มุม OpenBridge เรื่องนี้ใกล้ตัวที่สุดในรอบนี้ ถ้า horizon ปีข้างหน้า agent คือ user หลักของ integration ที่เราสร้าง connector ของเราต้องพูด MCP ได้ และเราควรมี SDK ฝั่ง UI ที่พูด AG-UI ด้วย ถ้า dev ที่ใช้ CopilotKit ต่อ OpenBridge ได้ใน 5 นาที เราจะกลายเป็น default integration layer แต่ถ้ายังต้องเขียน boilerplate 200 บรรทัด นั่นคือ moat เปล่า ๆ ที่ปิด opportunity ตัวเอง window กำลังเปิดอยู่ครับ
