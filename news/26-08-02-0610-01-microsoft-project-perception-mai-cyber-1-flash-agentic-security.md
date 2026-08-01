---
date: 2026-08-02
slug: microsoft-project-perception-mai-cyber-1-flash-agentic-security
topic: agentic-ai
reading_time_min: 5
sources: 7
image_prompt: |
  Editorial isometric composition of a Microsoft-style security operations
  center at night. Three glowing agent silhouettes at a triangular console —
  one labeled "RED" (attack path mapping), one "BLUE" (risk triage), one
  "GREEN" (auto remediation). A bright banner behind them reads
  "MAI-CYBER-1-FLASH" with the stat "96% CyberGym" and a sub-badge
  "-50% COST". A dim benchmark chart shows "MYTHOS 84%" below the winning bar.
  Deep Microsoft-blue + cyber-teal palette, chiaroscuro editorial style, 1:1
  aspect, no real human faces (silhouettes only), text must render sharply at
  200px thumbnail.
image: images/26-08-02-0610-01-microsoft-project-perception-mai-cyber-1-flash-agentic-security.png
---

# Microsoft ทิ้ง MAI-Cyber-1-Flash + Project Perception — โมเดล cyber ตัวแรก, สาม agent สี รบกันเอง, 96% CyberGym แซง Mythos 12 คะแนน

## TL;DR
- **27 ก.ค.** — Microsoft ประกาศ **Project Perception** (agentic security system ใน Defender) + **MAI-Cyber-1-Flash** (first-ever Microsoft cybersecurity model). Public preview เปิด **3 ส.ค.**
- สถาปัตย์ **3 agent color-coded** — Red map attack path, Blue triage risk, Green take corrective action. Runs ใน MDASH (multi-agent vulnerability harness) — handle 90% ของ task เอง, GPT-5.4 held back สำหรับ 10% ที่ยากสุด
- **96% CyberGym** benchmark — เหนือ Anthropic Mythos 12 คะแนน, cost -50% เทียบ config เก่าของ Microsoft เอง
- Signal: **Microsoft เดินก้าวออกจาก "OpenAI-only" strategy** — สร้าง in-house cyber model + multi-agent orchestration ตัวเอง, บวก guardrails ที่ SOC จริงยอมรับ

## เกิดอะไรขึ้น

วันที่ 27 กรกฎาคม Microsoft เปิดหน้าไพ่คู่ที่รอมาสามไตรมาส — **MAI-Cyber-1-Flash** (โมเดล cyber แรกที่ Microsoft build เอง, ต่อจาก MAI-1-Preview เมื่อพฤษภาคม) และ **Project Perception** (agentic security system ที่ประกอบด้วย red / blue / green agents). ทั้งสองจะเข้า **public preview วันที่ 3 สิงหาคม** — ส่งตรงเข้าสู่ Microsoft Defender ที่ enterprise ใช้อยู่แล้ว. Charlie Bell (Microsoft Security EVP) เขียนใน blog post ว่า "we've been running Perception across MSTIC and DART for six weeks — it's already taking corrective action on triage-approved playbooks without human hand-off"

Architecture ของ Perception เป็น three-color multi-agent workflow ที่แบ่ง cognitive load ชัด. **Red agents** map attack surface + vulnerability chain — เดินเข้า repo, IaC, cloud config, identity graph, หา path ที่ attacker น่าจะใช้จริง. **Blue agents** รับ findings จาก red แล้ว **triage** — ตัด false-positive, จัดลำดับ risk, ตัดสินใจว่าอะไรจริง (severity + exploitability + blast radius). **Green agents** ปิดจ๊อบ — quarantine host, rotate credential, patch dependency, ลบ token — เขียน audit trail กลับ SIEM. ระหว่างสามสีมี MDASH (Microsoft Defender Agent Security Harness) เป็น orchestrator ที่ตัดสินใจว่าใช้ MAI-Cyber-1-Flash (90% ของ task), Claude Opus 5 หรือ GPT-5.4 (10% ที่ยากสุด) โดย route ตาม cost-per-token + confidence threshold — vendor-agnostic แต่ default เป็น in-house

Benchmark ที่ Microsoft เคลม — **96% บน CyberGym** (benchmark ที่ทดสอบ vulnerability finding across large codebases, สร้างโดยทีม CMU + MITRE). อ้างอิงตัวเลข third-party: Anthropic Mythos (โมเดล security-tuned ที่ Anthropic ปล่อยพฤษภาคม) ทำได้ 84%, Google Gemini Security 3 Pro ที่ 81%. Microsoft claim ว่า **cost -50%** เทียบ config เก่าของตัวเองที่ใช้ GPT-5.4 อย่างเดียว — เพราะ MAI-Cyber-1-Flash เป็น distilled model 8B (คาด) ที่รัน on-prem บน Trainium/Azure Cobalt ก็ได้. TechCrunch สัมภาษณ์ Vasu Jakkal (Microsoft Security VP) บอกว่า Cyber-1-Flash "จะเปิด weight คืน community ภายในไตรมาส 4 ถ้า deployment สะอาด"

## ทำไมสำคัญ

**Microsoft-OpenAI relationship ก้าวออกจาก honeymoon อย่างเป็นทางการ**. ต้นปี 2026 Satya Nadella พูดใน earnings call ว่า "we're pluralistic on models" — วันนี้เห็นภาพชัด: Microsoft build in-house model สำหรับ vertical ที่สำคัญที่สุดต่อธุรกิจ (cyber = $30B ARR ของ Defender + Sentinel). Pattern เดียวกับที่ AWS เพิ่งประกาศเมื่อวาน — Nova wind-down + Frontier Model Research (FMR) — hyperscaler กำลังเลือก **1 in-house model per strategic vertical** แทน general-purpose fleet. Microsoft: cyber. Amazon: FMR (undisclosed vertical, คาด agents). Google: Gemini. Meta: Llama. Foundation-model race กำลัง fragment ไปตาม vertical, ไม่ใช่ต่อสู้ตรงหน้ากับ Claude/GPT อีกต่อไป

**Three-color agent pattern (red/blue/green) เป็น template ที่ SOC เข้าใจอยู่แล้ว** — Microsoft ไม่ต้อง sell architecture ใหม่ให้ CISO. Red team, blue team เป็นภาษาที่ security industry ใช้มา 20 ปี. เพิ่ม green (auto-remediation) เข้าไป = evolution ที่ SOC พร้อมยอมรับเพราะเห็น analog แล้ว. เทียบกับ startup อย่าง Reco, Nudge Security, หรือ Snyk ที่ต้องอธิบาย "agent" ให้ CISO เข้าใจ 6 เดือน — Microsoft เดินข้าม step ด้วย branding เดียว. นี่คือ **incumbent advantage ในการ deploy agent** — ไม่ใช่ตัว model เก่ง แต่คือ language + trust ที่มีอยู่แล้ว

**MDASH = multi-model routing เป็น production pattern จริง**. Microsoft ไม่ได้บอกว่า MAI-Cyber-1-Flash เก่งกว่า GPT-5.4 — บอกว่า **MDASH route 90% ไป Flash แล้วเหลือ 10% ให้ frontier**. นี่คือ economics ของ agent ที่ enterprise เพิ่งเริ่มเข้าใจ: **per-token cost matters, capability ceiling ไม่ใช่ทุก task**. Anthropic วางบท routing แบบเดียวกันใน Claude Cowork (Haiku 4.5 + Opus 5 + Fable 5), Databricks Mosaic AI Gateway ทำเรื่อง cost-optimize routing มา 3 ไตรมาส. Microsoft ยกระดับให้เป็น **standard pattern สำหรับ agentic security** — vendor อื่นต้องตาม

## มุม AI Agent Platform

**สำหรับ builders:** ถ้ากำลังสร้าง security agent framework — architecture red/blue/green + MDASH-style multi-model routing = **playbook ที่ CISO buy ทันที**. Prompt structure สำหรับ Blue agent (triage/risk scoring กับ decision authority level) เป็นจุดที่ Microsoft mostly kept behind curtain — โอกาสของ open-source project (LangSmith, Arize, OpenTelemetry Security SIG) ที่จะ standardize schema. ถ้ากำลัง build บน MCP — Microsoft ประกาศว่า Perception expose **MCP server สำหรับ green-agent tools** ให้ enterprise custom action เพิ่มได้; ควร prototype connector ตอน public preview เปิด 3 ส.ค.

**สำหรับ users/business:** Enterprise ที่ใช้ Defender + Sentinel อยู่แล้ว (~70% ของ Fortune 2000) — เตรียม **pilot Perception ในเดือน ส.ค.-ก.ย.**, focus playbook 2-3 ตัวที่ auto-remediation confidence สูง (credential rotation, malware quarantine, patch known-CVE). Cost signal: MDASH default routing ทำให้ per-incident cost ลดลง ~50% เทียบ Sentinel Copilot เดิม — CFO ยอมทันที. สำหรับ Thai bank / SET50 ที่ยัง run Splunk / IBM QRadar — Microsoft's cyber model + red/blue/green architecture เพิ่ม pressure ให้ vendor พวกนี้ต้องประกาศ agentic story ก่อนสิ้นปี ไม่งั้น renewal cycle 2027 จะโดน replace

**สำหรับ ecosystem:** losers ชัด — CrowdStrike Charlotte AI (ยังเป็น "assistant" ไม่ใช่ agent), SentinelOne Purple AI (คล้ายกัน), Palo Alto Cortex XSIAM (agentic ต้องรอ Prisma AIRS 2). ทั้งสามจะต้องเปิด agentic-first roadmap ในไตรมาส 3 หรือเสี่ยง perception ล้าหลัง. Winners: **Anthropic (Mythos ยัง benchmark #2 = referable enterprise choice ที่ไม่ใช่ Microsoft), OpenAI (Microsoft ยังใช้ GPT-5.4 ใน 10% ที่ยากสุด — pricing power ยังมี), agent security infrastructure startups (Upwind, Zenity, Prompt Security) — เพราะ SOC ต้อง monitor agents ที่ take action จริง**. Enabridge angle: ถ้ากำลังคุยกับลูกค้า Thai enterprise เรื่อง agent deployment ใน regulated workload, red/blue/green + MDASH เป็น reference architecture ที่ใช้ pitch ได้ทันที

## Sources
- [Microsoft launches its first cyber model and a new agentic cybersecurity system — TechCrunch](https://techcrunch.com/2026/07/27/microsoft-launches-its-first-cyber-model-and-a-new-agentic-cybersecurity-system/)
- [Microsoft Project Perception launches AI agents, specialized model for cybersecurity — Axios](https://www.axios.com/2026/07/27/microsoft-unveils-new-cyber-model-agentic-security-tools-to-fight-hackers)
- [Microsoft built an agentic security system with red, blue, and green team AI agents — TNW](https://thenextweb.com/news/microsoft-project-perception-agentic-security-cyber-model)
- [Microsoft's Project Perception Bets on Agents That Act, Not Just Alert — Futurum](https://futurumgroup.com/insights/microsofts-project-perception-bets-on-agents-that-act-not-just-alert/)
- [Microsoft Launches MAI-Cyber-1-Flash and Project Perception — Genius Firms](https://www.geniusfirms.com/news/microsoft-launches-mai-cyber-1-flash-and-project-perception/)
- [Project Perception | Microsoft Security](https://www.microsoft.com/en-us/security/business/ai-powered-cybersecurity/project-perception-agentic-system)
- [Microsoft escalates the AI security race with 'Project Perception' — GeekWire](https://www.geekwire.com/2026/microsoft-escalates-the-ai-cybersecurity-race-with-project-perception-and-a-new-in-house-model/)

---

## Audio script
วันที่ 27 กรกฎาคม Microsoft เปิดหน้าไพ่ใหญ่ในตลาด security. สองของใหม่พร้อมกัน. หนึ่งคือ MAI-Cyber-1-Flash — โมเดล cybersecurity แรกที่ Microsoft สร้างเอง ไม่พึ่ง OpenAI. สองคือ Project Perception — ระบบ agentic security ที่ประกอบด้วย agent สามสี. Red agents map เส้นทางที่ attacker น่าจะใช้. Blue agents triage risk. Green agents ลงมือแก้ automatic — rotate credential, quarantine host, patch CVE. ทั้งหมด public preview เปิด 3 สิงหาคมนี้ ส่งตรงเข้า Microsoft Defender.

Number ที่ Microsoft เคลม — 96 percent บน CyberGym benchmark, เหนือ Anthropic Mythos 12 คะแนน, และ cost ต่ำกว่า 50 percent เทียบ config เก่าของ Microsoft เอง. ที่สำคัญกว่า number คือ pattern. Microsoft ใช้ multi-model routing — 90 percent ของงานให้ Cyber-1-Flash ที่ถูก, 10 percent ที่ยากสุดค่อยยิงเข้า GPT-5.4. นี่คือ economics ของ agent จริงในโลก production.

Signal ที่สำคัญ — hyperscaler ทุกเจ้ากำลัง build in-house model ต่อ vertical เชิงกลยุทธ์. AWS ทิ้ง Nova ไปทำ Frontier Model Research. Microsoft ทำ Cyber-1-Flash. Google มี Gemini. Foundation model race ไม่ใช่ head-to-head แล้ว. สำหรับ Enabridge — ถ้าคุยกับ Thai enterprise เรื่อง agent security, red-blue-green architecture คือ reference ที่ CISO เข้าใจทันที เพราะเป็นภาษาที่ SOC ใช้มา 20 ปีอยู่แล้ว.
