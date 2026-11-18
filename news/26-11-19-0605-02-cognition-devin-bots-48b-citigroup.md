---
date: 2026-11-17
slug: cognition-devin-bots-48b-citigroup
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a Slack-like chat window pinned to a
  giant wall; inside the window, three glowing robot icons labeled "DEVIN BOT"
  are passing a software project ticket to each other. Below the window, a
  big ledger shows stacked figures: "$48B VALUATION", "$1B ARR",
  "14,000 CITI ENGINEERS", "-30% VENDOR SPEND". A clock on the wall reads
  "DAYS → WEEKS". Soft navy, teal, and warm coral palette, editorial style,
  1:1 aspect, no real human faces (silhouettes OK), high contrast so numbers
  read at 200px thumbnail.
image: images/26-11-19-0605-02-cognition-devin-bots-48b-citigroup.png
---

# Cognition กด shipping — Devin Bots มาตรฐานใหม่ของ coding agent ที่อยู่ยาวเป็นสัปดาห์, Citi 14,000 engineers ตัด vendor spend 30%

## TL;DR
- Cognition เปิดตัว Devin Bots (17 พ.ย.) — persistent coding agent ที่จัดการโปรเจกต์ software ได้ระยะ "days or weeks" ผ่าน Slack channel, เลือก model ตาม task, มี budget ของตัวเอง
- บริษัทมูลค่า $48 พันล้าน, annualized revenue run rate เกิน $1B ตั้งแต่กันยายน; Early-access customer (Decagon, Fireworks AI, Reducto) มี Bot usage โต 10 เท่าใน 2 สัปดาห์
- Citigroup มี 14,000 engineers ใช้ Devin เดิมอยู่แล้ว — Citi บอกว่าตัด tech vendor spend ลง 30% year-over-year; ชน head-to-head กับ Anthropic Duet, OpenAI Dots แต่เป็น model-agnostic

## เกิดอะไรขึ้น
Fortune รายงาน exclusive วันที่ 17 พฤศจิกายนว่า Cognition เปิดตัว Devin Bots — รุ่นต่อของ Devin ที่ CEO Scott Wu เคยพูดถึงตั้งแต่กลางปีว่า "ของจริงคือ agent ที่อยู่ในทีมได้นาน ไม่ใช่ copilot ใน IDE" Devin Bots เข้า Slack channel ของทีมเป็นสมาชิก ค้าง context ข้ามสัปดาห์ และติดต่อคนเมื่อ block หรือเจอ decision — pattern ที่ engineer ทำงานกันจริง ไม่ใช่ chat-request-response

ลึกกว่า UX คือ orchestration — Bot แบ่ง project เป็น task แล้ว assign ให้ Devin agent หลายตัว โดย sync output ข้ามกัน เช่น update Android version เมื่อ iPhone version เปลี่ยน แต่ละ Bot เลือก model เอง: ใช้ frontier model สำหรับ planning/design/computer use, และใช้ model ถูกกว่าสำหรับ routine code แต่ละ Bot มี budget ของตัวเอง ที่ measure กับ result ไม่ใช่ token — เป็นครั้งแรกที่ agent product พูดเรื่อง unit economics ใน UI ตรง ๆ

ตัวเลข business ของ Cognition หนักกว่าที่ Fortune คาด — valuation $48 พันล้าน, annualized revenue run rate ทะลุ $1B ตั้งแต่กันยายน (เร็วกว่า OpenAI ตอนถึงเลขเดียวกัน) ลูกค้า early-access ชื่อ Decagon, Fireworks AI, Reducto มี Bot usage โต 10x ใน 2 สัปดาห์ และที่ยกเป็นหลักฐาน anchor คือ Citigroup ที่มี 14,000 engineers ใช้ Devin เดิม Citi แถลงว่าตัด tech vendor spend ลง 30% year-over-year — เป็นตัวเลขระดับ CFO ที่หาได้ยากในวงการ agent

## ทำไมสำคัญ
สิ่งที่ Devin Bots pre-empt คือ OpenAI Dots (always-on proactive agent ที่ integrate กับ Codex) และ Anthropic Duet (always-on สำหรับ Claude Code) — สองตัวนี้ตาม pattern เดียวกันแต่ผูกกับ model ของเจ้าของเอง Devin Bots วาง positioning ตรงข้าม: model-agnostic routing + fine-tuned own models สำหรับ routine code นี่คือ bet ว่า enterprise ไม่อยาก lock-in กับ lab เดียว ซึ่งเป็นสมมติฐานที่ CTO regulated industry จะยอมจ่ายเพื่อ

การที่ Citi ประกาศตัวเลข 30% vendor spend reduction คือ moment ที่วงการ agent หลุดจาก "proof of concept" ไปสู่ "line item ใน budget reallocation" การที่ bank ขนาด G-SIB ยอม disclose ตัวเลขนี้ public แปลว่า competitor bank อื่น (JPMorgan, Goldman, HSBC) จะต้อง justify ว่าทำไมไม่ทำ — pressure wave ที่จะดัน coding agent adoption เข้าสู่ phase ที่ไม่ใช่ early adopter curve อีกต่อไป

Caveat — vendor spend reduction ไม่ได้เท่ากับ net saving ถ้า Citi จ่าย Cognition แทน (งบย้ายจากช่อง A ไปช่อง B) — Fortune ไม่ได้ให้ net breakdown แต่ pattern ที่ CFO สายบัญชีจะดูคือ productivity per engineer-hour ไม่ใช่แค่ vendor consolidation

## มุม AI Agent Platform
**Builders** — Devin Bots validate pattern ที่ agent framework ต้อง support: persistent context ข้าม session ยาว, multi-agent handoff, model routing ที่ cost-aware, และ budget-per-agent เป็น first-class primitive ถ้า framework ของคุณยัง assume short-lived request-response (langchain classic pattern) จะล้าสมัยเร็ว — LangGraph, LlamaIndex Workflow, และ Google Agent Development Kit ต้อง ship primitive เหล่านี้ไม่ช้า

**Users/business** — สำหรับ CTO ไทยที่มี engineering team 50-500 คน หลัก Citigroup -30% vendor spend เป็น upper bound ที่ยาก realistic แต่ pattern ว่า "ตัด SaaS license ซ้ำซ้อน + รวม budget ไว้ที่ coding agent" ทำได้จริง Enabridge ที่ช่วย enterprise ไทย deploy agent ควรออกแบบ pricing ที่ใกล้ "budget per agent" ไม่ใช่ "license per developer" เพื่อ align กับ pattern ที่ Cognition กำลัง set

**Ecosystem** — ที่น่าคิดคือ "ecosystem middle-layer" — ถ้า Devin Bots model-agnostic จริง แปลว่า Cognition กำลังตั้งตัวเป็น layer ที่ Anthropic และ OpenAI ต้องผ่านเพื่อเข้าถึง enterprise engineer อาจจบด้วย: lab อยาก lock-in direct → ลด price หรือเพิ่ม feature ให้ Devin ใช้, หรือ Cognition shift ไปเน้น own fine-tuned model จนกลายเป็น model vendor เอง

## Sources
- [Exclusive: Cognition bets on Devin Bots in challenge to Anthropic's Duet and OpenAI's Dots (Fortune)](https://fortune.com/2026/11/17/exclusive-cognition-bets-on-devin-bots-coding-agents-in-challenge-to-anthropics-duet-and-openais-dots)
- [AI Agents News Brief: November 17, 2026 (AI Agents Directory)](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-17-2026)
- [AI Agents News Brief: November 18, 2026 (AI Agents Directory)](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-18-2026)

---

## Audio script
ข่าวที่สองวันนี้ Cognition เปิดตัว Devin Bots เมื่อ 17 พฤศจิกายน Fortune ได้ exclusive Devin Bots เป็น persistent coding agent ที่อยู่ในทีม software ได้ระยะ days or weeks เข้าไปอยู่ใน Slack channel ของทีมเป็นสมาชิก เก็บ context ข้ามสัปดาห์ และติดต่อคนเมื่อติด decision ไม่ใช่แค่ chat ตอบ Bot แบ่งโปรเจกต์เป็น task แล้ว assign ให้ Devin agent หลายตัว เช่น update Android version เมื่อ iPhone version เปลี่ยน แต่ละ Bot เลือก model เอง ใช้ frontier model สำหรับ planning และ computer use และใช้ model ถูกกว่าสำหรับ routine code แต่ละ Bot มี budget ของตัวเองที่ measure กับ result ไม่ใช่ token เป็นครั้งแรกที่ product agent พูดเรื่อง unit economics ใน UI ตรง ๆ ตัวเลขของ Cognition น่าทึ่ง valuation 48 พันล้านเหรียญ annualized revenue run rate ทะลุ 1 พันล้านเหรียญ ตั้งแต่กันยายน ลูกค้า early-access มี Decagon Fireworks AI Reducto ใช้ Bot โต 10 เท่าใน 2 สัปดาห์ และที่หนักที่สุด Citigroup มี 14,000 engineers ใช้ Devin อยู่แล้ว Citi บอกว่าตัด tech vendor spend ลง 30% year-over-year สิ่งที่ Devin Bots pre-empt คือ OpenAI Dots และ Anthropic Duet ซึ่งเป็น always-on agent ของสอง lab Devin เลือก position ตรงข้าม model-agnostic routing เป็น bet ว่า enterprise ไม่อยาก lock-in กับ lab เดียว สำหรับ CTO ไทยที่มี team 50 ถึง 500 คน pattern ที่ Citi ทำได้คือตัด SaaS license ซ้ำซ้อน และรวม budget ไว้ที่ coding agent ซึ่งเป็น template ที่ realistic กว่าตัวเลข 30 เปอร์เซ็นต์โดยตรง
