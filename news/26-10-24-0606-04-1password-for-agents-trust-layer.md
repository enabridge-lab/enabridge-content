---
date: 2026-10-22
slug: 1password-for-agents-trust-layer
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a locked blue vault labeled "1PASSWORD"
  at the center, with a glowing key hovering above. Six translucent AI agent
  avatars stand in a row — each labeled with a tiny banner: "CLAUDE DUET",
  "CHATGPT WORK", "MUSE", "GROK BOT", "DOTS", "TOWN" — presenting unique digital
  keys to the vault door, which stamps a holographic approval badge marked
  "APPROVED — AGENT NEVER SEES PASSWORD". Three stacked numbers float above:
  "$500M ARR", "85% OF FORBES AI 50", "ZERO CREDENTIALS LEAKED". Deep navy and
  1Password blue palette with silver accents, strong contrast for 200px
  thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-24-0606-04-1password-for-agents-trust-layer.png
---

# 1Password for Agents — เลเยอร์ identity ที่ 6 agent (Claude Duet, ChatGPT Work, Muse, Dots, Grok, Town) ใช้ sign-in แทนลูกค้าโดยไม่เห็น password

## TL;DR
- **22 ต.ค.** 1Password เปิด **1Password for Agents** — ให้ AI agent sign-in เว็บไซต์แทนผู้ใช้ **โดย agent ไม่เห็น credential** พร้อมประกาศ **$500M ARR** และ "serving 85% of Forbes AI 50"
- Flow: agent เจอ login form → ยื่น **unique digital key** ให้ 1Password verify → ลูกค้า approve → **1Password fill credential ลงฟอร์มโดยตรง** ไม่ส่งให้ agent → agent ทำ task ต่อ. ลูกค้าตั้งว่า agent ตัวไหนใช้ credential ไหนได้นานเท่าไร
- Launch partners (รายงานใน press): **Claude Duet, ChatGPT Work, Meta Muse, Grok Bot, Dots, Town** — **Google Gemini Spark** และ **Microsoft Scout ไม่อยู่ในลิสต์** (press บอกจะเพิ่มภายหลัง)
- Signal: **agent identity + credential plane** กลายเป็น primitive ใหม่ที่ไม่ใช่ part ของ agent runtime เอง — ชนกับ Walmart Agent Gateway + ServiceNow AI Passport ที่ประกาศวันเดียวกันหรือสัปดาห์เดียวกัน

## เกิดอะไรขึ้น

วันพฤหัสที่ **22 ต.ค.** 1Password ประกาศ **1Password for Agents** พร้อมกับตัวเลข business update ที่น่าสนใจ: **$500M ARR** และบอกว่าตอนนี้ serve **85% ของ Forbes AI 50**. product ตัวใหม่ตอบคำถามที่ enterprise ถาม Microsoft, OpenAI, Anthropic ตลอดครึ่งปีที่ผ่านมา: **"ถ้า agent ต้อง login เว็บไซต์แทนฉัน ฉันจะเก็บ password ยังไงให้ agent ไม่เห็น ไม่ cache ไม่ exfiltrate"**

Flow ของ product (ที่ 1Password เรียกว่า "trust layer for personal AI agents"):

**(1)** User สร้าง "agent policy" ใน 1Password — บอกว่า agent ตัวไหน (เช่น Claude Duet หรือ Dots) ใช้ credential ของ account ไหนได้ (เช่น Gmail, Delta, Expedia), **ภายในระยะเวลาเท่าไร**, และ **"agent approve ตัวเองไม่ได้"** — ลูกค้าต้อง approve แต่ละครั้งหรือ pre-authorize แบบมี expiration

**(2)** agent run task — เจอ login form — ส่ง **unique digital key** (per-agent identifier) ให้ 1Password verify ว่า agent นี้ user approve แล้ว

**(3)** 1Password **fill credential ลงฟอร์มของ target site โดยตรง** ไม่ relay ผ่าน agent context — agent ไม่เคย "เห็น" password string. หลังจาก fill, credential **ถูกลบจาก session context** ของ agent ทันที (claim ของ NewsCord, อ้างอิง secondary — ยังไม่มี formal spec public)

**(4)** agent ทำ task ต่อหลัง login state ใน browser session ที่ user เลือก

Launch partners ที่ 1Password press release ยกชื่อ: **Anthropic Claude Duet, OpenAI ChatGPT Work, Meta Muse, xAI Grok Bot, Dots, Town**. ที่ **ไม่อยู่** ในลิสต์ (ที่สื่อสังเกต): **Google Gemini Spark**, **Microsoft Scout**. 1Password บอกว่า "additional integrations to come" — แต่การที่ Google + Microsoft ไม่อยู่ day 1 สื่อสัญญาณว่าทั้งสองรายน่าจะเดิน identity primitive ของตัวเอง (Google Titanium IPU + Microsoft Entra ID for AI Agents)

Statement จาก Chief Business Officer ของ 1Password: *"Our customers decide which credentials an agent can use and for which task, and for how long. The agent can't approve its own access."* ซึ่งเป็น positioning ที่ชัด: 1Password ไม่สร้าง agent, ไม่สร้าง browser — สร้างแค่ **permission layer ระหว่าง agent กับ web**

## ทำไมสำคัญ

สองสัญญาณใหญ่

**หนึ่ง — agent identity ไม่ใช่ feature ของ agent runtime**. ตั้งแต่กลางปี 2026 สี่เรื่องนี้ประกาศคู่กัน: Walmart Agent Gateway (approved agent list), ServiceNow AI Passport (silicon-rooted identity), Amazon Bedrock AgentCore identity, และ 1Password for Agents (credential proxy). ทั้งหมดบอกเรื่องเดียวกัน: **"identity ของ agent ต้องแยกจากตัว agent"** — เพราะ (a) agent หลายตัวจาก vendor ต่างกันทำ task ให้คนเดียวกัน, (b) credential ที่อยู่ใน agent context = attack surface, (c) regulated industry (finance, health) ต้อง audit trail ที่ agent ไม่สามารถแก้ได้. 1Password เป็น **neutral vendor ที่ไม่ใช่ hyperscaler** — ตีความได้ว่าเป็นเลเยอร์ที่ enterprise วางใจกว่าของ Microsoft/Google ที่ขาย agent runtime เอง

**สอง — $500M ARR + 85% ของ Forbes AI 50 = ตลาด agent credential โตเร็วกว่าที่คาด**. 1Password business line เดิมคือ enterprise password management (~$300M ARR เมื่อ 2024). ตัวเลข $500M ARR ตอนนี้แปลว่า 1Password เติบโต ~65% ใน 2 ปี — เลขที่ชี้ว่า **personal + enterprise AI agent สร้างความต้องการ credential management ใหม่หมด**. ตลาดที่ CyberArk, Okta, HashiCorp เคยครองจะต้องปรับตัว — เพราะ workflow "agent ใช้ password แทนคน" ไม่เหมือน "service account ใช้ API key แทนระบบ"

Pattern ต่อไปที่ต้องดู: **(1)** Browser (Chrome, Arc, Comet, Dia) จะ expose standard API สำหรับ "credential injection by trust provider" ที่ 1Password / Dashlane / Bitwarden hook เข้าได้ไหม, **(2)** Visa, Mastercard, Stripe จะทำเลเยอร์เดียวกันสำหรับ payment credentials ไหม — ที่ Walmart Agent Gateway บอกว่า "agent ไม่ได้ card details" แปลว่าตลาดนี้ว่างอยู่

## มุม AI Agent Platform

สำหรับ **Builders** (agent framework, autonomous agent product): ถ้า agent คุณต้อง login ที่ไหนก็ตาม, **integrate 1Password for Agents API** คือ fastest path to enterprise acceptance — ไม่ต้องสร้าง secret vault ของตัวเอง (ซึ่งเป็น liability). agent ที่ bypass 1Password แล้วเก็บ password ใน context จะโดน CISO reject ตั้งแต่ POC. สำหรับ **Users / Business**: ถ้าคุณใช้ 1Password Business อยู่แล้ว, policy ของ "agent + credential" ควร reuse infrastructure ที่มี — ไม่สร้างระบบใหม่. agent policy ควรเริ่มที่ **"approval ทุก transaction"** ก่อน relax เป็น **"auto-approve ถ้าใน scope"** หลังเก็บ incident log ครบไตรมาส. สำหรับ **Ecosystem**: Dashlane, Bitwarden, Keeper, 1Password's archrival Okta จะต้องตอบใน 6 เดือน — เลเยอร์นี้มี winner-take-most dynamic เพราะ agent vendor ไม่อยาก integrate กับ password manager 5 รายพร้อมกัน. 1Password's **early day-1 partnerships กับ 6 agent รายใหญ่** คือ moat ที่ยากจะ catch up

## Sources
- [1Password launches a way for AI agents to log in on your behalf without seeing your password (TechCrunch)](https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/)
- [1Password for Agents Launches as the Trust Layer for Personal AI Agents (1Password Press)](https://1password.com/press/2026/october/1password-for-agents-trust-layer-personal-ai-agents)
- [1Password will let Muse, Dots and Grok Bot sign in to sites for you without getting your credentials (Engadget)](https://www.engadget.com/2293844/1password-opens-up-ai-agents-muse-dots-grok/)

---

## Audio script
วันพฤหัสที่ 22 ตุลาคม 1Password เปิดตัว 1Password for Agents พร้อมประกาศ $500M ARR และบอกว่าตอนนี้ serve 85% ของ Forbes AI 50. product ตอบคำถามที่ enterprise ถาม hyperscaler ตลอดครึ่งปีที่ผ่านมา ถ้า agent ต้อง login เว็บไซต์แทนฉัน จะเก็บ password ยังไงให้ agent ไม่เห็น ไม่ cache ไม่ exfiltrate. Flow คือ user สร้าง agent policy บอกว่า agent ตัวไหนใช้ credential ไหนได้นานเท่าไร agent ตัดสินใจเองไม่ได้. agent เจอ login form ยื่น unique digital key ให้ 1Password verify ลูกค้า approve แล้ว 1Password fill password ลงฟอร์มของเว็บเป้าหมายโดยตรงไม่ส่งผ่าน agent context — agent ไม่เคยเห็น password. launch partners ที่ press ยกชื่อคือ Claude Duet, ChatGPT Work, Meta Muse, Grok Bot, Dots, Town. ที่ไม่อยู่ลิสต์คือ Google Gemini Spark และ Microsoft Scout — น่าจะเดิน identity primitive ของตัวเอง สองสัญญาณใหญ่คือ identity ของ agent กำลังแยกเป็นเลเยอร์ของตัวเองไม่ใช่ feature ของ agent runtime ตลาดเดียวกับที่ Walmart Agent Gateway กับ ServiceNow AI Passport กำลัง build. และสองคือ $500M ARR กับ 85% ของ Forbes AI 50 แปลว่า personal บวก enterprise agent สร้างความต้องการ credential management ใหม่หมด ตลาดที่ CyberArk Okta HashiCorp เคยครองต้องปรับตัว. สำหรับทีมที่ build agent — ถ้า agent ต้อง login ที่ไหน integrate 1Password for Agents คือทางเร็วที่สุดเข้า enterprise agent ที่เก็บ password เองจะโดน CISO reject ตั้งแต่ POC. สำหรับ ecosystem — Dashlane, Bitwarden, Keeper, Okta ต้องตอบใน 6 เดือน เพราะ agent vendor ไม่อยาก integrate กับ password manager 5 รายพร้อมกัน
