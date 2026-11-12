---
date: 2026-11-13
slug: bay-50m-agent-runtime-enforcement
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A dramatic editorial scene of a high-tech enterprise security control room —
  a glowing holographic shield hovering between a line of agent silhouettes
  (robot workers) on the left and a stack of corporate systems (Salesforce,
  Workday-like server icons) on the right. The shield pulses with a label
  "BAY ENFORCER" and a ticker "DECIDES IN MS". Behind: a badge "$50M OUT OF
  STEALTH" and another "5-MIN DEPLOY — AGENTLESS". Small IDF Unit 8200
  mascot tucked discreetly in a corner. Editorial cinematic style, deep cool
  blue + neon cyan palette, 1:1 aspect, high contrast so headline text
  readable at 200px, no real human faces (silhouettes OK).
image: images/26-11-13-0604-04-bay-50m-agent-runtime-enforcement.png
---

# Bay $50M ออกจาก stealth — Agent runtime enforcement กลายเป็นหมวดใหม่ที่ Wiz CEO เองยังลงเงิน

## TL;DR
- Bay บริษัท Israeli ออกจาก stealth วันที่ 10 พฤศจิกายน — รวม $50M ($37M Series A โดย Battery Ventures + $13M seed เก่าโดย YL Ventures และ Striker)
- Micron Ventures, M12 ของ Microsoft, Assaf Rappaport (CEO ของ Wiz) ร่วมลงใน Series A
- โปรดักต์ enforce agent action แบบ real-time — ตัดสินใน millisecond ว่า action ของ agent ควร allow ไหม — agentless, 5 นาที deploy

## เกิดอะไรขึ้น
Bay บริษัท Tel Aviv ที่ทำ AI agent security ออกจาก stealth เมื่อวันที่ 10 พฤศจิกายน — $50M รวมสองรอบ Series A $37M lead โดย Battery Ventures และ seed round $13M เก่าโดย YL Ventures + Striker Venture Partners ที่ไม่เคยประกาศมาก่อน ใน Series A มีชื่อ Micron Ventures (ที่เป็นลูกค้าด้วย), Microsoft M12, และ Assaf Rappaport CEO ของ Wiz ร่วมลง

สิ่งที่ Bay ทำคือ runtime enforcement ของ AI agent — ทุก action ที่ agent เสนอจะทำ (เรียก API, update record, delete file, ส่งอีเมล) Bay evaluate ที่ context ของ session ทั้งหมด แล้วตัดสินใน millisecond ว่า allow, block, หรือ require approval policy ที่ guide การตัดสินใจไม่ได้เขียนด้วย human-rule แบบ YARA — แต่ build โดย AI ภายในของ Bay (ที่ชื่อ "Lighthouse") จาก activity history ขององค์กรเอง

Architecture เป็น "agentless" — ไม่ต้องติด persistent endpoint agent, ไม่ต้องมี kernel driver, ไม่ต้องใช้ network proxy deploy ใน 5 นาทีผ่าน existing security infrastructure (identity provider + SIEM) Founders เป็นอดีต IDF Unit 8200 (หน่วยข่าวกรอง cyber ของ Israel ที่เป็น pipeline ของ cyber startup เยอะที่สุด) — CEO Yuval Zacharia ลูกค้าที่เปิดเผยคือ Micron, Peloton, ClickUp, และ Wix

## ทำไมสำคัญ
หมวด "AI agent security" หนาแน่นขึ้นเรื่อย ๆ ปีนี้ — Kindo ($30M วานนี้), Bay ($50M), Prompt Security, Zenity, Lakera, Noma, Aim Security — แต่ส่วนใหญ่ทำ pre-deployment scanning หรือ posture management Bay เป็นหนึ่งใน handful ที่ทำ runtime enforcement จริง — ซึ่งต่างจาก "posture" เพราะเกิดใน loop ของ agent execution ไม่ใช่ตรวจก่อน deploy

สัญญาณสำคัญที่สุดคือ — Assaf Rappaport CEO ของ Wiz ($32B acquisition โดย Google) ลงเงินส่วนตัวใน Bay นั่นคือ endorsement ระดับ founder-to-founder จากคนที่เพิ่งสร้าง category ใหญ่สุดของ cloud security ให้ Google ซื้อ ประสบการณ์ของ Wiz คือ security ที่ยอมรับได้ต้อง agentless + 5-min deploy + policy ที่ organization ไม่ต้อง author เอง — Bay ลอกสูตรนี้ไปใช้กับ AI agent

Caveat — $50M stealth exit บ่งบอกว่า product validation ภายในอาจยังน้อย 4 ลูกค้า (Micron, Peloton, ClickUp, Wix) เป็น reference ที่ดี แต่ไม่รู้ว่า enforce กี่ action ต่อวัน, false-positive rate เท่าไร, latency P99 ของ enforcement เท่าไร — สิ่งเหล่านี้คือตัวเลขที่ security team ต้องการก่อน deploy production การไม่เปิดเลยทั้งที่ออก stealth มี 2 interpretations — อาจเป็นเพราะเป็น early-stage จริง หรือเพราะตัวเลข benchmark ยังไม่ชนะ Prompt Security ชัด

## มุม AI Agent Platform
Builders — ถ้าคุณกำลัง deploy agent ให้ enterprise customer คำว่า "guardrail" ที่คุณเขียนเองจะไม่พอ enterprise security team ต้องการ enforcement ที่ separate จาก agent process — คือ policy ที่ชัด audit log ที่ tamper-proof การ bundle enforcement เข้าไปใน agent framework ของคุณจะทำให้ failed procurement เพราะ CISO ไม่ยอม "fox guarding the henhouse" — มี opportunity ให้ platform builder ที่ integrate กับ enforcement layer (Bay, Prompt Security, Zenity) ตั้งแต่ design phase

Users/business — ถ้าทีมของคุณจะ deploy agent ที่ touch production system (PII, financial transaction, email ขาออก) ปี 2027 คำถาม procurement ใหม่ที่ต้องเพิ่ม 1) "agent action ทุก step ผ่าน runtime enforcement ไหม" 2) "policy เขียนจาก activity log จริงขององค์กร หรือจาก template vendor" 3) "block action มี 2nd-approval workflow ไหม" ถ้า vendor ไม่มีคำตอบทั้ง 3 อย่า sign contract

Ecosystem — คาด 2027 จะมี consolidation — Microsoft, Palo Alto, CrowdStrike, Zscaler คงซื้อ runtime enforcement player ไปเสริม stack ของตัว Bay ที่มี Microsoft M12 ลงเงิน + Wiz CEO เป็น angel มีโอกาสสูงที่จะเป็น Microsoft acquisition target ภายใน 18-24 เดือน — วันนั้น startup ที่สร้าง agent platform บน customer ระดับใหญ่ต้องเลือกว่าจะ integrate กับ Microsoft ตรง ๆ หรือ hedge ด้วย alternatives

## Sources
- [Bay Raises $50 Million to Control What Enterprise AI Agents Can Do (SecurityWeek)](https://www.securityweek.com/bay-raises-50-million-to-control-what-enterprise-ai-agents-can-do/)
- [Bay Security Raises $50M to Stop Rogue AI Agent Actions (GovInfoSecurity)](https://www.govinfosecurity.com/bay-security-raises-50m-to-stop-rogue-ai-agent-actions-a-33343)
- [Bay raises $50m for AI agent security after nine months in stealth (The Next Web)](https://thenextweb.com/news/bay-50m-ai-agent-security-stealth-battery-ventures)
- [Bay raises $50m as AI agents test enterprise security limits (FinTech Global)](https://fintech.global/2026/11/12/bay-raises-50m-as-ai-agents-test-enterprise-security-limits/)

---

## Audio script
Bay บริษัท Israeli ที่ทำ AI agent security ออกจาก stealth เมื่อวันที่ 10 พฤศจิกายน ระดมทุนรวม 50 ล้านเหรียญ แบ่งเป็น Series A 37 ล้านเหรียญ lead โดย Battery Ventures และ seed round 13 ล้านเหรียญเก่าโดย YL Ventures และ Striker ที่ไม่เคยประกาศมาก่อน ใน Series A มีชื่อ Micron Ventures, Microsoft M12, และ Assaf Rappaport CEO ของ Wiz ร่วมลง สิ่งที่ Bay ทำคือ runtime enforcement ของ AI agent ทุก action ที่ agent เสนอจะทำ Bay evaluate ที่ context ของ session ทั้งหมด แล้วตัดสินใน millisecond ว่า allow, block, หรือ require approval policy ที่ guide การตัดสินไม่ได้เขียนด้วย human-rule แต่ build โดย AI ภายในชื่อ Lighthouse จาก activity history ขององค์กรเอง Architecture เป็น agentless ไม่ต้องติด persistent endpoint agent deploy ใน 5 นาที หมวด AI agent security หนาแน่นขึ้นปีนี้ แต่ส่วนใหญ่ทำ pre-deployment scanning Bay เป็น handful ที่ทำ runtime enforcement จริง สัญญาณสำคัญคือ Assaf Rappaport ของ Wiz ลงเงินส่วนตัวใน Bay เป็น endorsement founder-to-founder จากคนที่เพิ่งสร้าง category ใหญ่สุดของ cloud security ให้ Google ซื้อ สำหรับคนที่ deploy agent ใน enterprise ไทย คำว่า guardrail ที่คุณเขียนเองจะไม่พอ enterprise security team ต้องการ enforcement ที่ separate จาก agent process มี opportunity ให้ integrate กับ enforcement layer ตั้งแต่ design phase
