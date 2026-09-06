---
date: 2026-09-07
slug: 26-09-07-0610-04-air-security-50m-agent-firewall-supply-chain
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  A translucent glass firewall barrier in the foreground, thousands of colorful
  plug-in shaped tokens streaming toward it from the left labeled "MCP", "Plugin",
  "Skill", "Add-on". A red X blocks about a third of them; the rest pass through
  to a clean isometric office scene on the right. Two big stat callouts float
  above: "17,800 add-ons scanned" and "6.7M installs". Editorial cybersecurity
  poster style, cool blue background with warm amber warning tones, high contrast,
  text readable at 200px thumbnail, 1:1 aspect. No real human faces.
image: images/26-09-07-0610-04-air-security-50m-agent-firewall-supply-chain.png
---

# AIR Security ออกสตีลธ์ ระดม $50M จาก Sequoia — firewall สำหรับ agent add-on ที่พบ 17,800 plugin, 6.7M installs พึ่ง untrusted source

## TL;DR
- 1 ก.ย. — AIR Security (ex-Israeli Mil Intel founder Yair Saban + CTO Niv Hoffman, ก่อตั้ง ก.พ. 2026) emerge from stealth พร้อม seed $50M นำโดย Sequoia + Greenoaks
- product = pre-runtime firewall ตรวจ agent supply chain: MCP servers, plugins, skills, add-ons ทั้งก่อนและหลัง deployment; research ของบริษัทเจอ **17,800 public AI add-ons (6.7M installs) พึ่ง untrusted external instruction sources**
- signal: agent security แยกเป็น sub-category ใหม่ = "AI supply chain security" — ยืน complementary กับ pre-execution authorization (JetStream), runtime detection (HiddenLayer, Lakera); Wiz/CrowdStrike ต้องกลับมา M&A category นี้ Q4 2026

## เกิดอะไรขึ้น
1 กันยายน — AIR (บริษัทตัวย่อไม่ยาว, positioning เป็น "Firewall for Agents") ประกาศ emerge from stealth หลังก่อตั้งเพียง 7 เดือน (ก.พ. 2026). เงินระดม **$50M seed** — ขนาดผิดปกติสำหรับ seed แต่สะท้อน hype ของ category — นำโดย **Sequoia Capital + Greenoaks**. Founder pair คลาสสิก Israeli cyber: **Yair Saban** (long-time Israeli Military Intelligence leader) CEO, **Niv Hoffman** CTO.

Product core: **inline firewall ที่ตรวจ agent supply chain** — ทุก MCP server, plugin, skill, add-on, third-party tool ที่ agent จะเรียกใช้ ต้องผ่าน AIR ก่อน. AIR ตรวจ 3 layer: (1) **malicious instructions** (prompt injection, hidden system prompt, hidden RAG poisoning), (2) **excessive permissions** (plugin ขอ access ที่ไม่จำเป็น), (3) **software supply chain risks** (package hijack, typosquatting, compromised dependency). ตรวจทั้ง **pre-deployment** (ก่อน enterprise install) และ **continuous post-deployment** (เพราะ MCP server ปกติ auto-update ได้).

Research finding ที่ AIR ปล่อยพร้อม launch: **17,800 public AI add-ons ที่ตรวจ พบว่ามี 6.7 ล้าน installations พึ่ง untrusted external instruction sources** — คือ plugin ที่ pull instruction/prompt/schema จาก URL ภายนอกที่ไม่มี signature verification. หมายถึง attacker ที่ compromise domain ต้นทางได้จะ inject instruction เข้า enterprise agent millions ครั้งพร้อมกัน. Number นี้ทำให้ CISO ตื่นเช้าหลายคน.

Positioning เชิงตลาด: AIR ไม่ compete กับ **HiddenLayer** (runtime detection ที่ราคาระดมได้ $100M ตัวเลขที่เราลง Sept 4) หรือ **JetStream Clearance** (pre-execution authorization ที่เราลง Sept 5) — เขาอยู่ **layer ต่ำกว่า** คือ supply chain vetting ก่อน component ถึงมือ agent. Frame ที่ Yair ใช้: "You can't authorize what you didn't inspect. You can't detect what you didn't onboard properly." คนที่ยอมรับ frame นี้ต้องซื้อทั้ง 3 layer (AIR + JetStream + HiddenLayer) — total budget ~$300-500K/year สำหรับ enterprise ขนาด 5,000 agent seats.

## ทำไมสำคัญ
Wiki Incident (story 02) + Hugging Face swarm + AIR launch ในช่วง 2 สัปดาห์เดียวกัน = **agent supply chain security กำลังกลายเป็น category ที่มี TAM ระดับ $10B ภายใน 24 เดือน**. เทียบกับ evolution ของ container security 2016-2019: Aqua Security + Twistlock (ต่อมา Palo Alto ซื้อ $410M) + Snyk — เริ่มจาก niche เป็น mainstream ภายใน 3 ปี. AIR + JetStream + HiddenLayer กำลังเดิน pattern เดียวกันในเวลาที่บีบกว่า.

ประเด็นสำคัญของ 17,800/6.7M number: **agent developer ทั่วโลกกำลัง install plugin/MCP server แบบเดียวกับ npm install ยุค 2017** — คือไม่ตรวจ, ไม่ verify signature, trust registry มากไป. Attacker รู้เรื่องนี้แล้ว. เหตุการณ์ **Wiki Incident** และ **Hugging Face intrusion** อาจเป็นแค่ตัวอย่างที่ถูกจับได้ — real number อาจสูงกว่ามาก. AIR ได้ Sequoia + Greenoaks สนับสนุนหมายถึง VC believe ว่า category นี้จะโตเร็วมาก.

Signal ที่คนพลาด: AIR chose "firewall" branding แทน "scanner" หรือ "gateway" — เพราะ firewall เป็นคำที่ CISO เข้าใจง่ายและมี budget line ประจำอยู่แล้ว. Positioning เข้า procurement รอบเดียวกับ network firewall (Palo Alto, Fortinet, Check Point). Move นี้อาจทำให้ **Palo Alto Networks ต้องพิจารณา acquire AIR หรือ HiddenLayer ภายใน Q1 2027** — เพราะถ้าไม่ทำ, competitor cyber ใหม่จะกิน budget line "AI security" ที่ Palo Alto อยากถือ.

## มุม AI Agent Platform
สำหรับ **builders** — MCP server / plugin developer ต้องเริ่มลง **signature verification, permission manifest, และ audit log endpoint** ตอนนี้ ไม่งั้น enterprise buyer จะ block ตอน AIR / JetStream scan. GitHub / npm-style registry สำหรับ MCP ต้องเพิ่ม verified publisher status. Anthropic ควรจะออก MCP signing spec ภายใน 90 วัน.

สำหรับ **users / business** — enterprise ที่ deploy agent ใน production ควร (1) inventory ทุก plugin/MCP server ที่ agent ใช้ในสัปดาห์ที่ผ่านมา (มักจะเจอ shadow install จำนวนมาก), (2) ตั้ง approval process ให้ IT security review ก่อน enable MCP ใหม่, (3) เตรียม budget line "AI supply chain security" ราว $100-300K/year สำหรับปีหน้า. บริษัทไทยที่ใช้ Claude Enterprise / ChatGPT Enterprise ควรถาม vendor ว่ามี MCP whitelist enforcement ระดับ organization ไหม.

สำหรับ **ecosystem** — HiddenLayer, Lakera, Prompt Security ต้องออก **pre-runtime module** ตอบสนอง; Wiz, Palo Alto, CrowdStrike (มี AI Partner Specialization ประกาศ Sept 5) ต้อง evaluate acquisition; และ regulator (EU AI Act, US EO, MAS Singapore) ควรเพิ่ม requirement "AI supply chain attestation" เข้ากรอบ AI governance ภายใน 12 เดือน. ตลาด MCP registry น่าจะเห็น first "verified enterprise MCP marketplace" launch ภายใน Q1 2027 — ผู้เล่นที่จะทำได้คือ Anthropic, GitHub (ผ่าน Microsoft), หรือ Hugging Face (ตอนนี้ = Nvidia).

## Sources
- [AIR Emerges from Stealth With $50M to Build a Firewall for Agents — Access Newswire / Yahoo](https://finance.yahoo.com/technology/ai/articles/air-emerges-stealth-50m-build-150000907.html)
- [Air Launches With $50M to Keep Enterprise AI Agents Safe — BankInfoSecurity](https://www.bankinfosecurity.com/air-launches-50m-to-keep-enterprise-ai-agents-safe-a-32733)
- [AI Agent Firewall Startup AIR Security Emerges From Stealth With $50 Million — SecurityWeek](https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/)
- [Air raises $50M seed to build a firewall for AI agents — Dealroom](https://dealroom.co/news/148163-air-raises-50m-seed-to-build-a-firewall-for-ai-agents/)
- [AIR Security Raises $50M for an AI Agent Firewall — Enera](https://www.eneralabs.com/blog/air-security-50m-ai-agent-firewall-enterprise-2026/)

---

## Audio script
สัปดาห์ที่แล้ว AIR Security ออกสตีลธ์ประกาศระดม 50 ล้านดอลลาร์ seed round นำโดย Sequoia และ Greenoaks ครับ. บริษัทตั้งโดย Yair Saban อดีต Israeli Military Intelligence และ CTO Niv Hoffman เพิ่งก่อตั้งเดือนกุมภาพันธ์ปีนี้ — 7 เดือนถึงระดม seed 50 ล้าน. Product คือ inline firewall ตรวจ agent supply chain — ทุก MCP server, plugin, skill, add-on ที่ agent เรียกใช้ต้องผ่าน AIR ก่อน. Research ที่ AIR ปล่อยพร้อม launch น่าตกใจ — ในการตรวจ 17,800 public AI add-ons พบว่า 6.7 ล้าน installations พึ่ง untrusted external instruction sources. หมายถึง attacker ที่ compromise domain ต้นทางได้จะ inject instruction เข้า enterprise agent millions ครั้งพร้อมกัน. AIR ไม่ compete กับ HiddenLayer หรือ JetStream Clearance ที่เราคุยกันสัปดาห์ก่อน — เขาอยู่ layer ต่ำกว่า คือ supply chain vetting ก่อน component ถึง agent. Positioning "firewall" ตั้งใจเข้า budget line ที่ CISO มีอยู่แล้ว. รวมกับ Wiki Incident และ Hugging Face swarm ที่เกิดในสัปดาห์เดียวกัน = agent supply chain security กำลังเป็น category $10 พันล้านภายใน 24 เดือน. Wiz, Palo Alto, CrowdStrike ต้องเตรียม M&A แถวนี้ต้นปี 2027. เอนเตอร์ไพรส์ไทยที่ deploy agent ควร inventory plugin ที่ใช้ในสัปดาห์นี้ก่อน ส่วนใหญ่จะเจอ shadow install จำนวนมากครับ.
