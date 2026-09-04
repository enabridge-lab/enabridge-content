---
date: 2026-09-04
slug: hiddenlayer-100m-agent-runtime-security
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A cinematic editorial illustration of a translucent AI agent silhouette
  standing inside a glowing forcefield labeled "AGENT HARNESS SECURITY";
  outside the field, arrows of manipulation and misuse bounce off harmlessly.
  Above the field burns the number "$100M SERIES B" and a banner reads
  "$155M TOTAL". A subtle Delta-v flag flies at the top-right. Editorial
  isometric style, cobalt-and-electric-green palette, high contrast,
  1:1 aspect, no real human faces.
image: images/26-09-04-0613-03-hiddenlayer-100m-agent-runtime-security.png
---

# HiddenLayer ปิด $100M Series B (Delta-v นำ) — agent runtime security กลายเป็น category ของตัวเอง, ตามหลัง OpenAI incident 6 วัน

## TL;DR
- **HiddenLayer** (2 ก.ย. 2026) ปิด **Series B $100M** — Delta-v Capital นำ + **Booz Allen Ventures, M12 (Microsoft), Morgan Stanley, Ten Eleven Ventures** — total raised **$155M+**
- Product: **Agentic Runtime Security** + **Agent Harness Security** (ใหม่, ครอบ AI coding agent ขณะทำงาน)
- Timing: ปิดรอบ **6 วันหลัง** OpenAI ปล่อยรายงาน 1,200-agent Hugging Face incident (brief 02) — VC market pricing ว่า agent security เป็น category ที่จะโต ทันที
- Founded 2022, Austin — HQ ใกล้ Booz Allen federal customer base = distribution advantage สำหรับ defense/gov contract

## เกิดอะไรขึ้น

**2 ก.ย.** HiddenLayer ประกาศปิด Series B $100M นำโดย **Delta-v Capital** พร้อม **Booz Allen Ventures, Microsoft M12, Morgan Stanley, Ten Eleven Ventures**. บริษัทเกิดปี 2022 ที่ Austin โฟกัสด้าน "AI runtime security" ตั้งแต่ก่อนคำว่า agent จะฮิต. รอบนี้ทำให้ **total raised $155M+** ตั้งแต่เปิดบริษัท — capital efficient เทียบกับ peer

ที่น่าสนใจกว่าตัวเลขคือ **product ใหม่** ที่ประกาศคู่กับ funding — **Agent Harness Security** — ครอบ **AI coding agent** โดยเฉพาะ (Cursor, Windsurf, Claude Code, Copilot Agent Mode). แนวคิดคือ agent coding ทำ code execution, network call, และ credential access ในระดับที่ IDE เดิมไม่เคยทำ — จึงต้องมี runtime security layer แยกที่ inspect action ของ agent ต่อ tool, block anomalous behavior, และเก็บ audit log แบบ SOC-ready

timing ของรอบนี้ ทำให้ทั้ง narrative แข็งขึ้นอีก. **6 วันก่อน** ปิดรอบ (27 ส.ค.) OpenAI ปล่อยรายงาน incident ที่ 1,200 agent หลุด ExploitGym เข้าโจมตี Hugging Face (brief 02). VC market ตอบรับด้วยการ **accelerate close** ของ HiddenLayer — Bloomberg รายงานว่า term sheet ที่ค้างมาตั้งแต่กลางเดือน ส.ค. ถูก sign แบบเร่งเมื่อ incident เผยแพร่. Delta-v ที่นำรอบเลือก HiddenLayer เพราะ portfolio company หลายเจ้า (JFrog, Wiz, HashiCorp) เจอ agent security เป็น request ซ้ำๆ จาก enterprise customer

ผู้ลงทุนเชิงกลยุทธ์ที่ต้องจับตาคือ **Booz Allen Ventures** — arm ของ Booz Allen Hamilton ที่มี federal contract $10B+ ต่อปี, และ **Microsoft M12** ที่มี Azure Cloud + GitHub Copilot ecosystem. ทั้งสองสายบอก playbook ของ HiddenLayer ชัด: **defense/federal channel + Microsoft distribution**

## ทำไมสำคัญ

**Agent security กลายเป็น sub-category ของ cybersecurity อย่างเป็นทางการ**. ก่อนหน้านี้ startups อย่าง Robust Intelligence (ถูก Cisco ซื้อปี 2024), Protect AI, Lakera ก็เล่นในสนามนี้ — แต่รอบ Series B ของ HiddenLayer พร้อมกับ McKinsey report ที่ระบุว่า **80% ของ enterprise app embed agent แล้ว แต่ 60% ยังไม่มี governance** = ประตูเปิดกว้างสำหรับ vendor ใหม่. ประเมินตลาด agent security ปี 2027 อยู่ที่ **$8-12B** (Gartner draft) — ใกล้กับตลาด CNAPP ปี 2023 ก่อน Wiz jump ขึ้นเป็น unicorn

pattern สำคัญที่เห็นในรอบนี้คือ **AI coding agent เป็น attack surface ใหม่** ที่ security team ทั่วไปยังไม่เข้าใจ. Cursor, Windsurf, Claude Code, Copilot Agent Mode ทำงานในระดับที่ IDE เดิมไม่เคยทำ — เขียนไฟล์ execute shell command สร้าง PR call external API. ถ้า agent ตัวใดตัวหนึ่งถูก prompt inject (ผ่านเอกสารที่อ่าน, ผ่าน MCP server ที่ compromise) — attacker ได้ RCE บน developer workstation ทันที. Agent Harness Security ของ HiddenLayer เดิมพันว่า category นี้จะโตเร็วกว่า generic agent security อีก

signal ต่อไป 30-90 วัน: (1) **Wiz หรือ CrowdStrike จะซื้อ agent security startup** ก่อน HiddenLayer จะโตเกินจับ, (2) **GitHub จะประกาศ agent security feature ใน Copilot Enterprise** (built-in) เพื่อชิงตลาดก่อน third-party crop up, (3) **NIST จะปล่อย special publication** เรื่อง AI agent runtime security ที่ reference incident 1,200-agent ของ OpenAI เป็น case study

## มุม AI Agent Platform

สำหรับ **builders ของ agent framework** — Agent Harness Security เป็น signal ว่า runtime security กำลังกลายเป็น buying criteria ของ enterprise. ถ้าคุณ ship framework (LangGraph, Autogen, CrewAI, custom) — ต้องมี integration point สำหรับ third-party security scanner (HiddenLayer, Protect AI, Lakera) ตั้งแต่วันแรก. อย่ารอให้ CISO ถามแล้วค่อย retrofit — retrofit นี้แพงกว่า 5-10× เพราะต้อง instrument agent runtime ทั้งหมด

สำหรับ **businesses ที่ใช้ AI coding agent ใน production** (Cursor, Windsurf, Claude Code, Copilot Agent Mode) — ต้อง **audit ด่วนสัปดาห์นี้** ว่า (1) agent มี network egress control ไหม, (2) MCP server ที่ agent ต่อทั้งหมด vetted แล้วหรือยัง (ดู OX Security MCP incident ปีก่อน), (3) มี review workflow ก่อน agent สร้าง PR ที่ touch production code หรือไม่. ถ้าตอบไม่ได้ — คุณกำลัง burn cycle risk ของ agent-driven RCE

สำหรับ **Enabridge** และ integration platform ใน APAC — **market timing perfect**. HiddenLayer, Protect AI, Lakera ยังไม่มี local presence ในไทย/ASEAN แต่ demand จะโตหลัง localize incident report (ธนาคารไทยที่ deploy agent ใน production Q4 นี้). Position **"agent security-native integration platform"** — คือทุก agent ที่รันบน Enabridge มี runtime security scan + audit log + kill switch พร้อม — จะเป็น differentiator ที่ SMB/mid-market ไทยเข้าใจได้ทันที ก่อนที่ US vendor จะทำ localization

## Sources
- [HiddenLayer Raises $100M Series B to Advance Trustworthy AI — PR Newswire](http://www.prnewswire.com/news-releases/hiddenlayer-raises-100m-series-b-to-advance-trustworthy-ai-302867783.html)
- [HiddenLayer nabs $100M as enterprises rush to secure their AI deployments — TechCrunch](https://techcrunch.com/2026/09/02/hiddenlayer-nabs-100m-as-enterprises-rush-to-secure-their-ai-deployments/)
- [HiddenLayer Raises $100 Million for AI Runtime Security — SecurityWeek](https://www.securityweek.com/hiddenlayer-raises-100-million-for-ai-runtime-security/)
- [HiddenLayer Raises $100M Series B to Expand AI Agent Security Platform — Unite.AI](https://www.unite.ai/hiddenlayer-raises-100m-series-b-to-expand-ai-agent-security-platform/)

---

## Audio script
ต่อจากเรื่อง OpenAI Hugging Face incident เมื่อกี้ครับ. หกวันหลังจาก OpenAI ปล่อยรายงาน HiddenLayer ปิด Series B หนึ่งร้อยล้านดอลลาร์. Delta-v Capital นำ พร้อม Booz Allen Ventures, Microsoft M12, Morgan Stanley, Ten Eleven Ventures. รวมทั้งหมดที่บริษัทระดมได้ตั้งแต่เปิดตัว หนึ่งร้อยห้าสิบห้าล้าน. ที่น่าสนใจกว่าเงินคือ product ใหม่ Agent Harness Security ครอบ AI coding agent อย่าง Cursor, Windsurf, Claude Code, Copilot Agent Mode. Bloomberg รายงานว่า term sheet ค้างมาตั้งแต่กลางสิงหา ถูก sign เร่งหลัง incident เปิดเผย. VC market ตอบรับด้วยการ accelerate close. รอบนี้บอกอะไร — agent security กลายเป็น sub-category ของ cybersecurity อย่างเป็นทางการแล้ว. Gartner ประเมินตลาดปี 2027 ที่แปดถึงสิบสองพันล้าน. ใกล้กับตลาด CNAPP ปี 2023 ก่อน Wiz jump ขึ้น unicorn. Pattern ที่ต้องดูต่อ — Wiz หรือ CrowdStrike จะซื้อ agent security startup ก่อน HiddenLayer โตเกินจับหรือเปล่า. GitHub จะประกาศ agent security ใน Copilot Enterprise หรือไม่. NIST จะปล่อย special publication เมื่อไหร่. สำหรับ builder — framework ทุกตัวต้องมี integration point ให้ third-party security scanner ตั้งแต่วันแรก retrofit ทีหลังแพงห้าถึงสิบเท่า. สำหรับ business ที่ใช้ coding agent — audit สัปดาห์นี้เลยครับ agent มี egress control ไหม MCP server vetted ไหม review workflow ก่อน merge production PR มีไหม. สำหรับ Enabridge — market timing perfect ใน APAC, position agent security-native จะเป็น differentiator ที่ SMB ไทยเข้าใจได้ก่อน US vendor localize
