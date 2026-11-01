---
date: 2026-10-30
slug: openai-agents-api-auto-review-time-awareness
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  An editorial isometric illustration of a developer workbench with a
  translucent shield labeled "AUTO REVIEW" guarding a line of command cards
  before they reach a terminal. Behind the shield a glowing clock marked
  "TIME AWARENESS (BETA)" ticks over a to-do list. On the right, a stack
  of three cards reads "ASYNC COMPACTION", "MID-SESSION TOOL UPDATES",
  "AUTO SYSTEM-PROMPT CACHE". Above the bench a bold banner reads
  "OPENAI AGENTS API — OCT 30". A side panel shows a dim gravestone labeled
  "AGENTKIT: SUNSET NOV 30". Charcoal and electric-green palette, 1:1
  aspect, strong contrast for 200px thumbnails, no real human faces.
image:
---

# OpenAI Agents API โยน Codex guardrail ลง primitive — Auto Review + time awareness บอกทิศ coding agent ปี 2027

## TL;DR
- 30 ต.ค. 2026 OpenAI (ผ่าน Steve Coffey + OpenAI Developers account) ประกาศ 5 update ของ **Agents API**: **Auto Review** (ตรวจคำสั่งก่อนรัน แบบ Codex), **async compaction** (compact context background), **time awareness** (experimental — ให้ model track elapsed time), **mid-session tool update** (เปลี่ยน tool list ระหว่าง session), **automatic system prompt caching**
- เรื่องนี้มาพร้อม **AgentKit wind-down** 30 พ.ย. 2026 — Agent Builder (visual) + Evals จะถูกปิด, OpenAI แนะย้ายไป Agents SDK
- Signal: OpenAI กำลังเลือก camp — ยอมแพ้ **low-code visual builder**, double down ที่ **primitive API** และ **code-first SDK**. ชนตรงกับ Cresta/Anthropic ที่เลือก Claude Agent SDK (เรื่อง 03)

## เกิดอะไรขึ้น

วันที่ 30 ต.ค. Steve Coffey — engineer จาก OpenAI API team — ประกาศ 5 feature update ของ Agents API ผ่าน X. OpenAI Developers account repost:

- **Auto Review**: นำกลไกจาก Codex มาเป็น API primitive — ตรวจ command ก่อนรันเพื่อหา behavior ที่น่าเป็นห่วง (file deletion, network call, destructive op). ตัวนี้ตอบ pattern “agent ลบไฟล์ตัวเอง” / “agent push code เสียลง main” ที่เราเห็นในข่าว security ตลอดปี 2026
- **Async compaction**: context compact รัน background → session ยาวไม่ค้าง
- **Time awareness (experimental)**: ให้ model track elapsed time — ตัวอย่าง “timebox CI fix ที่ 10 นาที”. บริษัทบอกตรงๆว่าเป็น experimental และแนะ app ให้มี **hard timeout** คู่กัน
- **Mid-session tool update**: tool list ของ session เปลี่ยนได้ runtime — ไม่ต้องเริ่ม session ใหม่
- **Auto system prompt caching**: system prompt cache ข้าม session อัตโนมัติ — ตัว cost สำคัญสำหรับ multi-session app

ไม่มี benchmark, latency figure, cost saving figure. ไม่มี customer. OpenAI changelog ยังไม่ list — คำสั่ง parameter name จริงต้องรอ docs

การ announcement ครั้งนี้ **มาคู่กับ AgentKit wind-down** — notice ลง 3 มิ.ย. 2026 แต่ cutoff วันที่ **30 พ.ย. 2026** คือ Agent Builder (visual) + Evals ปิดจาก OpenAI platform. OpenAI แนะย้ายไป **Agents SDK** (code-first) สำหรับ workflow ที่ยังต้อง run ต่อ

## ทำไมสำคัญ

**Auto Review** เป็น primitive ที่สำคัญสุดใน batch นี้ — เพราะ **shift agent runtime จาก “sandbox ป้องกัน” → “policy ก่อน execution”**. pattern เดิมคือ: ปล่อย agent รันใน sandbox แล้ว sandbox ป้องกัน. pattern ใหม่: policy engine ตรวจคำสั่งก่อน execute, ตัดสิน allow/block/escalate ด้วย reasoning อีกชั้น. นี่คือ **ReAct + safety** compiled เข้า API ตัวมันเอง

ประเด็นใหญ่: **AgentKit wind-down** คือการที่ OpenAI ยอมรับว่า **visual agent builder ไม่ scale** กับ enterprise ที่ต้อง version control, test harness, PR review. CTO ที่ลงทุนใน Agent Builder มี 1 เดือน (ถึง 30 พ.ย.) เพื่อย้าย — pain ตรงหลังเทียบกับ competitor ของ OpenAI เอง (ChatGPT Apps ที่ยัง non-code สำหรับ end-user)

Pattern ใหญ่: ปี 2026 เราเห็น **low-code agent builder ถดถอยทั่วตลาด** — Microsoft Copilot Studio เน้น Power Fx + code มากขึ้น, Google Vertex AI Agent Builder shift ไป ADK, Salesforce AgentForce builder ซับซ้อนขึ้นจน developer-only. ชนะคือ **code-first + strong primitive** (Claude Agent SDK, Agents SDK) — pattern ที่ Cresta (เรื่อง 03) ยืนยัน

Time awareness น่าสังเกต: ตัวเองไม่ใช่ feature แปลก (ตั้ง clock ให้ model เห็น) แต่การ **ที่ OpenAI ปล่อยเป็น experimental พร้อมคำเตือน “ยังไม่พึ่งพาได้”** หมายความว่า orchestration layer ด้านบน (LangGraph, CrewAI, Mastra) ยังเป็น critical path สำหรับ real-world agent ที่ต้อง timebox / retry / escalate

## มุม AI Agent Platform

**Builders** ที่สร้าง framework ครอบ OpenAI/Anthropic API: Auto Review + mid-session tool update ทำให้ framework ต้อง rewrite abstraction. เดิม LangGraph จัดการ guardrail เอง — ตอนนี้ API มี primitive. framework ที่ไม่ pass-through feature เร็วจะดูล้าสมัย. LangChain 1.4 เพิ่ม per-call approval กันบางส่วนไว้แล้ว

**Users / business** ที่ run agent ใน prod: ตรวจ **AgentKit** usage — ถ้า team ใช้ visual Agent Builder, มี 30 วันเหลือก่อน migrate. ถ้า team ใช้ Agents SDK + Agents API อยู่แล้ว เรื่องนี้คือ **free upgrade** — enable Auto Review แล้ว log การ block ไว้ 2 สัปดาห์เพื่อ tuning policy

**Ecosystem**: Anthropic + OpenAI กำลังชิงเลเยอร์ **agent runtime** — ไม่ใช่ model layer อีกต่อไป. ชนะที่ enterprise จะคือใครมี **primitive guardrail + SDK + observability** ที่พึ่งพาได้. Google (Gemini Enterprise Agent Platform ที่ประกาศเม.ย.) ยังเล่น visual game — จะเสียเปรียบถ้าไม่เร่ง pivot

## Sources
- [OpenAI Agents API Auto Review, Async Compaction, Time Awareness (AI Coder)](https://aicoder.com/news/news-20261030-openai-agents-api-auto-review-async-compaction-time-awareness)
- [OpenAI AgentKit wind-down notice](https://openai.com/index/introducing-agentkit/)
- [OpenAI DevDay 2026 recap (God of Prompt)](https://godofprompt.ai/blog/openai-devday-2026/)

---

## Audio script
วันที่ 30 ตุลาคม OpenAI ประกาศ 5 update ของ Agents API ผ่าน X ตัวแรก Auto Review นำกลไกจาก Codex มาเป็น API primitive ตรวจ command ก่อนรันเพื่อหา behavior ที่น่าเป็นห่วง เช่นลบไฟล์ส่งคำขอ network destructive op ตอบ pattern agent ลบไฟล์ตัวเอง หรือ push code เสียลง main ที่เราเห็นในข่าว security ตลอดปี 2026 ตัวที่สอง async compaction compact context รัน background session ยาวไม่ค้าง ตัวที่สาม time awareness ให้ model track elapsed time เพื่อ timebox งาน บริษัทบอกว่ายัง experimental แนะให้มี hard timeout คู่ ตัวที่สี่ mid session tool update เปลี่ยน tool list ระหว่าง session ได้ ตัวที่ห้า automatic system prompt caching ข้าม session ตัว cost สำคัญสำหรับ multi session app ที่น่าสังเกต update นี้มาพร้อม AgentKit wind down 30 พฤศจิกายน Agent Builder visual จะถูกปิด OpenAI ยอมรับว่า low code visual builder ไม่ scale กับ enterprise CTO ที่ลงทุน Agent Builder มี 1 เดือนย้ายไป Agents SDK pattern ใหญ่ที่เห็นปีนี้คือ low code agent builder ถดถอยทั่วตลาด Microsoft Google Salesforce ขยับไปทางเดียวกัน ชนะคือ code first strong primitive และ Anthropic กับ OpenAI กำลังชิงเลเยอร์ agent runtime ไม่ใช่ model layer อีกต่อไปครับ
