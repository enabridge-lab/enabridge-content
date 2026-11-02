---
date: 2026-10-29
slug: island-enterprise-browser-agents-mcp
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration split into two halves. On the left, a
  chaotic desktop with a Chrome window exploding colored tokens labeled
  "PASSWORDS", "SESSION COOKIES", "PAYMENT TOKENS" into a model-shaped
  silhouette; red "LEAK" markers scatter. On the right, a clean studio
  stamped "ISLAND" with a dark glass browser frame marked "HEADLESS", a
  firewall gate labeled "MCP POLICY" filtering tagged tool calls into a
  side container labeled "SCOPED CREDS: NEVER IN MODEL CONTEXT". Three
  big stacked numbers in center: "$6.4B VALUATION", "$400M SERIES F",
  "SAME POLICIES AS HUMANS". Charcoal and sea-green palette with warm
  yellow accents, 1:1 aspect, strong contrast for 200px thumbnails,
  no real human faces.
image: images/26-11-03-0605-03-island-enterprise-browser-agents-mcp.png
---

# Island เปิด Enterprise Browser for Agents — เสนอ browser เป็น "agent control plane" แทน MCP extension ของ AI vendor

## TL;DR
- 29 ต.ค. 2026 Island (unicorn enterprise browser, $400M Series F ที่ $6.4B valuation) เปิด **Enterprise Browser for Agents** — headless browser build ที่ให้ AI agent เข้า SaaS, internal app, และเว็บ ภายใต้ policy เดียวกับ user คน
- Agent เรียกผ่าน **Island MCP server** ที่ built-in ใน browser (ไม่ใช่ MCP extension ของ Perplexity/OpenAI/ChatGPT); admin กำหนดได้ว่า agent ตัวไหนเข้าได้, condition ไหน, ใช้ tool อะไร
- Credential **scoped + time-boxed + context-aware** และ **ไม่ไหลผ่าน model context window** — ตอบ attack surface ที่ Zenity + Oasis Threat Research แฉว่า MCP เป็น compromised blast radius ใหม่
- Deploy ได้ทั้ง device + cloud, ไม่พึ่ง cloud-hosted browser ของ vendor อื่น

## เกิดอะไรขึ้น

Island ประกาศ Enterprise Browser for Agents วันที่ 29 ตุลาคม 2026 ผ่าน blog + press. บริษัทขาย Enterprise Browser (Chromium-based แต่ build governance + DLP + session recording เข้าไปใน browser เลย ไม่ใช่ extension) ให้องค์กรใหญ่มาตั้งแต่ 2022 — ลูกค้ามีทั้ง bank, insurance, pharma. Series F $400M ที่ $6.4B valuation ปิดก่อนหน้านี้ในปี 2026

ที่เปิดวันนี้คือ **headless mode** ที่ให้ AI agent (Claude, ChatGPT, custom agent) ใช้ browser session ของ user คน แทนที่จะเรียก API ตรงไปหา service. Agent เข้ามาผ่าน **Island MCP server** ที่ embed อยู่ใน browser เอง — ไม่ใช่ MCP extension ที่ติดตั้งจาก provider อื่น. Admin กำหนด policy ตรง Island console: agent ตัวไหนเข้า browser ได้, เงื่อนไข (เวลา, device posture, IP), tool ไหนเรียกได้ (ScreenReader, FormFill, FileUpload, etc.)

**Design philosophy ที่ sharpest**: Credential (session cookie, OAuth token, API key) ที่ agent ใช้ **ไม่ไหลผ่าน model context window**. Island claim ว่า agent "เห็น" result แต่ไม่เห็น secret — low-level browser API ของ Island ส่ง response เป็น structured object ที่ไม่มี raw credential. นี่คือการตอบ pattern attack ที่ Oasis Threat Research กับ Zenity แฉมาตลอดปี 2026 ว่า MCP server รุ่นแรกส่ง credential ผ่าน context ให้ model ประมวลแล้วหลุดง่าย (Claude vulnerability + OpenClaw case ใน Q2 2026)

Island ยัง argue ตรง ๆ ว่า **browser MCP server รุ่นอื่น** (Perplexity's Comet, ChatGPT Atlas, OpenAI extension) **ใช้ screenshot เป็นหลัก** แทน low-level browser API — ช้ากว่า, ไม่เสถียร, และ expose capability เกินที่ควร. การ frame นี้คือการวาง Island เป็น "**anti-vendor browser**" สำหรับ enterprise ที่ไม่อยากพึ่ง browser agent ของ model vendor

Deploy ได้สอง mode: **on-device** (agent รันในเครื่อง employee ภายใต้ session ของเขา) และ **cloud** (headless agent รันบน Island cloud, สำหรับ background task + unattended workflow). ไม่พึ่ง cloud-hosted browser ของ vendor อื่น — point แก้ Chrome Enterprise + Comet Enterprise ที่ pin ลูกค้าเข้า Google/Perplexity cloud

สิ่งที่ยังไม่เปิด: ไม่มี **ตัวเลข early customer**, ไม่มี **pricing ใหม่** (คิดเหมา enterprise license เดิม?), ไม่มี **benchmark** vs Chrome Enterprise หรือ Comet. Gartner (ที่ Island quote) ยังแนะนำให้ block AI browser ทุกตัวทันที — Island พยายามพลิก position นั้นให้เป็น "Island เท่านั้นที่ Gartner อนุญาต" โดยยังไม่มี Gartner statement ยืนยัน

## ทำไมสำคัญ

ชัดเจนขึ้นเรื่อย ๆ ว่า **enterprise agent stack ปี 2027 ไม่ใช่ one-layer** แต่เป็น stack ที่เลือกชั้น ๆ. Island กำลัง pitch ว่า "browser = ชั้นที่ enterprise ควบคุมได้โดยไม่ต้อง re-plumb SaaS vendor ทีละตัว" — คำตอบที่ sharp เพราะ MCP endpoint ของแต่ละ SaaS vendor จะใช้เวลา 2-3 ปีกว่าจะพร้อม (Dayforce beta → GA ปี 2027, Workday ยังไม่เปิด, SAP เพิ่งประกาศ Joule). ระหว่างที่รอ, agent ที่ "ล็อกอิน SaaS ผ่าน browser ของ user" คือทางลัดที่ไม่ต้องรอ vendor

ประเด็นที่ Island ตีถูก: **credential ที่ไหลผ่าน model context คือ attack surface ที่ไม่มีใครยอมรับใน enterprise**. OWASP + NIST ยังอยู่ในช่วง draft สำหรับ LLM security framework; ไม่มีมาตรฐานบอกว่า credential ที่ MCP server ส่งเข้า context นั้นควรเก็บยังไง. Enterprise ที่ compliance strict (bank, insurance, healthcare ที่ไทย เช่น KBank, SCB, BDMS) จะชอบ story "secret ไม่เคยเข้า context" มาก — แต่ต้องมี third-party pen-test รับรอง, Island ยังไม่มี

ที่ Island **เสี่ยง**: Chrome Enterprise ของ Google กำลัง bundle AI coworker + agent governance ให้ 3.8B user. Microsoft Edge for Business ก็เริ่ม bundle Copilot เข้า browser. Island ไม่ใหญ่พอจะชนะ distribution — ต้องชนะด้วย **governance depth + Fortune 500 reference**. ที่คนไม่ค่อยพูดคือ Island เก็บเงินได้แค่ตอน IT team ยอมเปลี่ยน browser default ของทั้งองค์กร, ซึ่งเป็น change management ที่ยากที่สุดใน enterprise IT

## มุม AI Agent Platform

สำหรับ **builders**: ถ้าคุณสร้าง agent ที่ต้องเข้า SaaS ภายในลูกค้า (เช่น Cresta, Salesforce Agentforce, Rein ที่ต้องเข้า CRM/ERP ของ user), **คุณมีสองทางเลือก**: (1) build MCP connector เองสำหรับ SaaS vendor ทุกตัว (Workday + Dayforce + SAP + Oracle + ServiceNow + …), ใช้เวลา 18-36 เดือน, (2) build on top of browser agent plane เช่น Island — ได้ coverage ทันที แต่ depend บน Island หลาย ๆ อย่าง. ตัวเลือกที่ 2 คือ shortcut สำหรับ seed/Series A startup; ตัวเลือกที่ 1 คือ moat ของ Fortune 500 vendor

สำหรับ **users / business**: ถ้าคุณเป็น enterprise ที่ยังไม่มี enterprise browser, นี่คือ wake-up — **AI agent ที่พนักงานใช้วันนี้ (ChatGPT Atlas, Perplexity Comet, Claude Chrome extension) run session ที่ expose credential + browser history ของพนักงานให้ model vendor**. เลเยอร์ป้องกันคือ enterprise browser (Island, Talon ที่โดน Palo Alto ซื้อ, Chrome Enterprise). เริ่ม audit ทันทีว่าพนักงานกี่ % ใช้ consumer AI browser อยู่

สำหรับ **ecosystem**: ยืนยัน thesis ที่ว่า **ปี 2027 "browser" จะไม่ใช่ product class เดียวกับ 2024 อีกต่อไป**. จะมีสาม tier: (1) consumer agent browser (Comet, Atlas, Dia), (2) enterprise browser with agent governance (Island, Chrome Enterprise, Edge for Business), (3) headless agent runtime (Browserbase, Steel.dev — infra สำหรับ agent รัน browser session). Island เลือกวาง bet ที่ tier (2) แล้ว pivot headless mode เข้า (3) — strategy ที่ชอบและเสี่ยงพร้อมกัน

## Sources
- [Island: The Enterprise Browser for AI Agents (Island blog, 29 ต.ค.)](https://www.island.io/blog/island-the-enterprise-browser-for-ai-agents)
- [Island Brings the Enterprise Browser to AI Agents (Press release)](https://www.island.io/press/island-brings-the-enterprise-browser-to-ai-agents)
- [Island raises $400m at a $6.4bn valuation to govern AI agents (TNW)](https://thenextweb.com/news/island-series-f-400m-6-4bn-valuation-ai-agents)
- [Islands 6.4B valuation validates a different kind of agent security (Forkast)](https://forkast.news/islands-6-4b-valuation-validates-a-different-kind-of-agent-security-and-it-starts-in-the-browser/)

---

## Audio script
Island ซึ่งเป็น unicorn enterprise browser ที่เพิ่ง ระดมทุน Series F 400 ล้านดอลลาร์ที่ valuation 6.4 พันล้าน เปิด Enterprise Browser for Agents เมื่อ 29 ตุลาคม 2026 ครับ idea หลักคือให้ AI agent เข้า SaaS กับ internal app และเว็บ โดยใช้ browser session ของ user คนภายใต้ policy เดียวกัน แทนที่จะเรียก API ตรงไปหา service agent เข้ามาผ่าน Island MCP server ที่ build in อยู่ใน browser ไม่ใช่ MCP extension ที่ติดตั้งจาก provider อื่น admin กำหนดได้ตรง Island console ว่า agent ตัวไหนเข้าได้ เงื่อนไขอะไร tool ไหนเรียกได้ จุดที่ sharp ที่สุดคือ Island claim ว่า credential ที่ agent ใช้ ไม่ไหลผ่าน model context window agent เห็น result แต่ไม่เห็น secret ตอบ attack pattern ที่ Oasis Threat Research กับ Zenity แฉมาตลอดปีว่า MCP server รุ่นแรกส่ง credential ผ่าน context ให้ model ประมวลแล้วหลุดง่าย ส่วน browser MCP server รุ่นอื่น เช่น Comet หรือ ChatGPT Atlas Island บอกว่าใช้ screenshot เป็นหลัก ซึ่งช้ากว่าและไม่เสถียร การเลือก frame แบบนี้คือการวาง Island เป็น anti vendor browser สำหรับ enterprise ที่ไม่อยากพึ่ง browser agent ของ model vendor ที่ชอบคือ Island deploy ได้สอง mode on device กับ cloud ไม่ pin เข้า Google หรือ Perplexity cloud ที่ยังไม่เปิดคือตัวเลข early customer ราคาใหม่ และ benchmark ที่น่า takeaway ที่สุด ชัดเจนขึ้นเรื่อย ๆ ว่า enterprise agent stack ปี 2027 มีหลายชั้นไม่ใช่ one layer Island กำลัง pitch ว่า browser คือชั้นที่ enterprise ควบคุมได้โดยไม่ต้อง re plumb SaaS vendor ทีละตัว ซึ่งเป็นคำตอบที่ sharp เพราะ MCP endpoint ของแต่ละ SaaS vendor จะใช้เวลา 2 ถึง 3 ปีกว่าจะพร้อม ระหว่างที่รอ agent ที่ล็อกอิน SaaS ผ่าน browser ของ user คือทางลัดที่ไม่ต้องรอ vendor สำหรับ CIO ไทย ก่อนลงทุน AI browser ต้อง audit ทันทีว่าพนักงานกี่ เปอร์เซ็นต์ ใช้ consumer AI browser อยู่
