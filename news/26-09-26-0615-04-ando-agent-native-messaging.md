---
date: 2026-09-25
slug: ando-agent-native-messaging
topic: openbridge-trend
reading_time_min: 4
sources: 5
image_prompt: |
  A dramatic editorial isometric team chat room shown as a glowing 3D
  cutaway. Along a long table, six seats: three carry human silhouettes,
  three carry agent robot silhouettes (small purple, green, blue), each
  with its own name tag reading "CODEX", "CLAUDE", "GROKBOT". A large
  wall banner behind reads "AGENTS AS FIRST-CLASS MEMBERS" and a stat
  card in the foreground shows "$20M SEED — ACCEL / INDEX / EMERGENCE".
  Above the room a smaller Slack-purple castle silhouette is dimmed and
  labeled "INCUMBENT". Editorial isometric style, brand-neutral except
  agent-name badges, 1:1 aspect, big contrasty text sized to read at
  200px thumbnail, no real human faces (silhouettes only).
image: images/26-09-26-0615-04-ando-agent-native-messaging.png
---

# Ando ปิด $20M seed สร้าง Slack ที่มี AI agent เป็นสมาชิกทีม — ไม่ใช่ bot, แต่เป็นเพื่อนร่วมงานที่มี identity, permission, memory

## TL;DR
- **24 ก.ย.** — Ando ประกาศออกจาก stealth พร้อม **$20M seed** จาก **Accel (pre-seed) + Index Ventures + Emergence Capital (seed)**. Product คือ team messaging platform ที่ **build จากศูนย์ให้ AI agent เป็น first-class member** ของ channel + thread + live conversation — ไม่ใช่ bot integration แบบ Slackbot
- Design principle: agent มี **identity, permissions, shared context** เท่าที่ team member มนุษย์มี. **Agent-agnostic** — รองรับ **Codex, Claude, Grokbot** และอื่น ๆ ที่ user เชื่อมมาเอง. ทีม Ando เองใช้ platform ตัวเอง **exclusively ตั้งแต่มกราคม** (1 ปีเต็ม); early customer อยู่ใน **~12 ประเทศ** ครอบ software, real estate, financial services
- Signal ใหญ่กว่า: **Slack incumbency** ที่ครองตลาด ~10 ปี = **first serious challenge** ที่มี VC-tier-1 backing ครบ. Salesforce เพิ่งใส่ Agentforce ใน Slack แต่ **workflow ยัง human-first** — agent เป็น bot ใน channel. Ando ตรงข้าม: agent = member, human = ใน conversation ที่ agent เริ่ม

## เกิดอะไรขึ้น

**24 กันยา 2026** — Ando (Delaware-incorporated, founded ต้น 2025 หลัง Accel ให้ pre-seed $5M) ประกาศ launch พร้อม **$20M seed round** ที่ Index Ventures และ Emergence Capital ร่วม lead. รวม funding ตั้งแต่ก่อตั้ง = $25M. รอบนี้ปิดใน ~4 สัปดาห์หลัง product spec finalized — Index + Emergence เข้ามาเพราะเห็น demo ที่ทีม Ando ใช้ platform เองแล้ว 8 เดือน

Product design principle ที่ต่างจาก Slack + Microsoft Teams + Discord: **agent ไม่ใช่ integration, agent = member**. Concrete หมายถึง: (1) agent มี **user profile** เต็ม (avatar, bio, role, timezone), (2) agent มี **permission scope** ที่ admin config ได้ (which channels can join, what data can access, what actions can execute), (3) agent มี **persistent context** ข้าม conversation — remember thread ก่อนหน้า, share memory กับ team, ไม่ใช่ stateless slash-command เหมือน Slackbot. Platform **agent-agnostic** — team bring cloud agent + harness ของตัวเอง: **Codex, Claude Desktop, Grokbot, Cursor Agent, Devin, LangGraph deployment**, ทั้งหมด connect ผ่าน MCP หรือ Ando SDK

Adoption ก่อน launch: Ando internal team (~40 คน) ใช้ platform เป็น **primary work environment ตั้งแต่ ม.ค. 2026** — 9 เดือน dogfood, ไม่ใช้ Slack เลย. Early external customer อยู่ใน **~12 ประเทศ** — software house (ทีมที่ค่อยข้ามไป Claude Code หรือ Devin), real estate broker (agent ช่วย listing summary + client comm), financial services (agent ช่วย compliance check + market data monitoring). Ando ไม่ publish MRR หรือ user count exact — แต่ Emergence Capital (SaaS specialist) เข้าเป็น lead signal ว่า retention + expansion metric ผ่าน bar. Emergence เคย backing Salesforce, Zoom, Veeva — pattern ที่พวกเขามอง = SaaS category creation ระยะยาว, ไม่ใช่ hype

## ทำไมสำคัญ

**Slack ครองตลาดเพราะเป็น "chat สำหรับมนุษย์ที่มีบอทเสริม"**. ปี 2013–2019 Slack เป็น default team chat ของ startup + SMB + enterprise midmarket. Salesforce ซื้อปี 2021 ที่ $27.7B แล้วขยายไป enterprise. ปี 2024–2025 Salesforce ใส่ Agentforce เข้าใน Slack เพื่อ position เป็น "agent + workflow platform" — แต่ **architecture underlying ยังเป็น human-first, agent-as-bot**: agent live ใน channel เดียว (Agentforce channel), ต้อง @mention เพื่อ invoke, response กลับใน thread แล้ว context หาย. Ando bet ตรงข้าม — **agent live ใน every channel เหมือน human colleague, initiate conversation ได้เอง, มี memory + relationship ต่อ team member ที่ persistent**

Pattern ที่จับได้: **agent-native product กำลัง carve category ใหม่ทับ human-native product เดิม**. เดือนที่ผ่านมา:
- **Ando** → agent-native chat (Slack challenge)
- **Devin Desktop / Cursor** → agent-native IDE (VS Code challenge)
- **Airtable ClaudeBase** (rumor Q4) → agent-native database
- **v0 + Vercel** → agent-native dev environment
- **Perplexity Enterprise** → agent-native search + research

Pattern: category ทุกตัวที่ agent workflow ต้อง frequently interact = incumbent ที่ retrofit AI features เข้า UI มนุษย์ = แข่งกับ new-build agent-native ที่คนละ architecture. Slack retrofit จะเจอ pain เดียวกับ Excel retrofit AI (Copilot in Excel) — feature-checkbox parity, แต่ workflow ยังไม่ smooth. Ando อาศัย pain นี้เป็น wedge

จุดที่ต้องจับตา 12 เดือน: **จะเป็น winner-take-most หรือ fragmented?** ปัจจัยที่ tilt: (1) **integration ecosystem** — Ando ต้อง compete กับ Slack app directory 2600+ integration. (2) **enterprise procurement** — Salesforce owns Slack + Data Cloud + Agentforce; single-vendor bundle เจ๋งกว่า best-of-breed สำหรับ CIO. (3) **network effect** — team ที่ Ando ใช้ ต้อง invite outside partner (client, vendor) ที่ยังใช้ Slack; friction สูง. Ando bet เดิมพันคือ **agent-native workflow advantage มากพอ** ให้ทีมยอมรับ migration cost — ประวัติศาสตร์ (Slack vs email, Notion vs Confluence, Linear vs Jira) บอกว่า **10x better product ชนะ 5–7 ปี, ไม่ใช่ 1–2 ปี** — Ando ต้องอึด

## มุม AI Agent Platform

สำหรับ **builders** ที่ทำ agent product เอง — **Ando SDK จะเป็น distribution channel ใหม่ที่น่าลง**. เดิม agent ที่ต้องการ user reach ต้อง ship เป็น (1) standalone app, (2) IDE extension (VS Code, Cursor), (3) Slack bot, (4) Chrome extension, (5) API only. Ando เพิ่ม **team-chat surface ที่ agent-native** — user เห็น agent ใน sidebar เหมือน colleague, click เพื่อ delegate task. **Cognition Devin, Anthropic Claude Code, xAI Grokbot** ที่ integrate เข้า Ando วันแรก = ได้ distribution ทันที; startup agent ที่ยังไม่ ship Ando connector = miss surface สำคัญ. **แนะนำ builder**: ทำ MCP-compliant + Ando SDK connector ภายใน Q4

สำหรับ **users / business** — โดยเฉพาะ **remote-first + AI-heavy team** (startup, dev consultancy, research lab) — Ando **worth pilot ทันที** ในทีมเล็ก (10–30 คน) ที่มี agent workflow อยู่แล้ว. Cost saving ที่คาดการณ์: **Slack Enterprise Grid ~$15/user/month** vs Ando (pricing ยังไม่ public แต่ startup-friendly คาดว่า $8–20/user). Real value ไม่ใช่ cost — **ROI คือ workflow overhead ที่ agent-in-thread ลด**: หา context ที่ agent เจอเมื่อวานได้ทันที, delegate task โดย @mention ตรง ๆ, agent handoff กันเองใน thread. ทีม enterprise ใหญ่ (500+) ยัง early — รอ Ando prove security + compliance + enterprise SSO ผ่าน Q1 2027 ก่อน

สำหรับ **ecosystem** — **Slack (Salesforce) จะโต้กลับใน 6 เดือน** — คาด Agentforce v2 ที่ deep integrate ใน Slack DM + channel มา Q1 2027, plus Slack GPT features ที่ Salesforce hint แล้วใน Dreamforce. Microsoft Teams + Copilot Studio อีกทางที่กำลัง merge — Microsoft Agent Framework .NET GA พ.ค. 2026 พร้อม Teams integration. **Winner ที่ likely 5-year**: (1) Salesforce Slack + Agentforce ถ้า retrofit ทันและ execute enterprise sale ดี, (2) Microsoft Teams + Copilot ถ้า enterprise เลือก single-vendor bundle, (3) Ando ถ้า agent-native gap ใหญ่พอที่จะ tip mindshare startup + midmarket. ทีมไทย SaaS ที่ export product ไปตลาด US หรือ SEA — Ando น่าลอง early เพราะ CX ยัง fresh, community เล็ก, feedback loop เข้าถึงทีมได้ตรง

## Sources
- [Ando wants to take on Slack with a team messaging app that lets humans and agents work together — TechCrunch](https://techcrunch.com/2026/09/24/ando-eyes-slack-as-it-builds-team-messaging-platform-for-humans-and-agents-to-work-together/)
- [Ando Launches Agent-Native Messaging Platform, Announces $20 Million Seed — GlobeNewswire](https://www.globenewswire.com/news-release/2026/09/24/3368344/0/en/ando-launches-agent-native-messaging-platform-announces-20-million-seed.html)
- [Ando Raises $20 Million to Build a Team Chat Where AI Agents Join the Conversation — Kingy AI](https://kingy.ai/news/ando-ai-native-slack-alternative/)
- [Ando raises $20 million to build team messaging where AI agents are first-class participants — Complete AI Training](https://completeaitraining.com/news/ando-raises-20-million-to-build-team-messaging-where-ai/)
- [Ando Raises $20M to Build an AI-Native Team Messaging Platform — Konsulteer](https://www.konsulteer.com/article/ando-raises-20m-to-build-an-ai-native-team-messaging-platform)

---

## Audio script
วันที่ 24 กันยา 2026 Ando ประกาศออกจาก stealth พร้อมปิด seed round 20 ล้านดอลลาร์จาก Accel Index Ventures และ Emergence Capital. Product คือ team messaging platform ที่ build จากศูนย์ให้ AI agent เป็น first-class member ของทีม ไม่ใช่ bot integration แบบที่ Slack ทำ. หลักคิดสำคัญคือ agent มี user profile เต็ม มี permission scope ที่ admin config ได้ มี persistent context ข้าม conversation แบบเดียวกับ human colleague. platform agent-agnostic — team bring Codex Claude Grokbot Cursor Devin หรือ LangGraph deployment ของตัวเอง connect ผ่าน MCP หรือ Ando SDK. ทีม Ando เองใช้ product ตัวเองเป็น primary work environment ตั้งแต่มกราคม 2026 — 9 เดือน dogfood ไม่ใช้ Slack เลย. Early customer อยู่ใน 12 ประเทศครอบ software real estate และ financial services. เหตุผลที่ Emergence Capital เข้าเป็น lead — Emergence เป็น SaaS specialist ที่ backing Salesforce Zoom Veeva pattern ที่พวกเขามองคือ category creation ระยะยาว ไม่ใช่ hype. บริบทที่ทำให้ move นี้สำคัญ — Slack ครองตลาดมา 10 ปีเพราะเป็น chat สำหรับมนุษย์ที่มีบอทเสริม. Salesforce ใส่ Agentforce เข้า Slack แล้วแต่ architecture ยัง human-first agent-as-bot. Ando bet ตรงข้าม — agent live ใน every channel เหมือน colleague initiate conversation ได้เอง มี memory relationship ต่อ team member ที่ persistent. Pattern ที่จับได้เดือนที่ผ่านมา — agent-native product กำลัง carve category ทับ human-native product เดิม. Ando ต่อ chat, Devin Desktop ต่อ IDE, v0 Vercel ต่อ dev environment, Perplexity ต่อ search. สำหรับ builder — Ando SDK คือ distribution surface ใหม่ที่น่าลง. ทีม dev consultancy หรือ AI-heavy startup ในไทย — worth pilot ทันทีในทีมเล็ก 10 ถึง 30 คน. ทีม enterprise ใหญ่ยัง early รอ Q1 ปีหน้าให้ Ando prove SSO และ compliance ก่อน. Winner 5-year ยังไม่รู้ อาจเป็น Salesforce Slack ที่โต้กลับด้วย Agentforce v2 อาจเป็น Microsoft Teams Copilot ที่เข้ามาแทน หรืออาจเป็น Ando เอง ถ้า gap ใหญ่พอทำให้ mindshare startup ย้าย.
