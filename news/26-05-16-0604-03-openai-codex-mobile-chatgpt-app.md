---
date: 2026-05-16
slug: openai-codex-mobile-chatgpt-app
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: A smartphone screen displaying a glowing terminal-style "CODEX" interface with an "APPROVE" green button and "REJECT" red button prominent in the foreground. The phone is being held in the bottom of the frame, while in the background a MacBook with the matching Codex desktop app sits across a desk — connected to the phone via a thick glowing data beam. A floating QR code icon and the OpenAI black-and-white logo. Composition: dramatic over-the-shoulder hero shot, dark background with electric green code accents. Style: editorial product photography render, high contrast for thumbnail legibility, no human faces (only hand silhouette).
image: images/26-05-16-0604-03-openai-codex-mobile-chatgpt-app.png
---

# OpenAI ปล่อย Codex ลง ChatGPT mobile — coding agent อยู่ในกระเป๋า approve งานได้ทุก tier รวม free

## TL;DR
- **14 พ.ค. 2026** — Codex coding agent มาบน ChatGPT app บน iOS/Android, อยู่ใน preview แต่ปล่อยทุก plan รวม **Free และ Go**
- ใช้ QR code pair กับ Codex desktop บน Mac — ตรวจงาน, approve commands, สลับ model, kick off task ใหม่ได้จากมือถือ
- Windows desktop ยังไม่รองรับ ณ launch — OpenAI บอก "เร็ว ๆ นี้" ไม่ระบุวัน

## เกิดอะไรขึ้น

เมื่อวันพฤหัสฯ ที่ 14 พ.ค. OpenAI ประกาศว่า **Codex** — coding agent บน cloud ที่เปิดตัวเป็น desktop app ตั้งแต่ ก.พ. — ตอนนี้ฝังอยู่ใน ChatGPT mobile app ทั้ง iOS และ Android. Setup เป็น flow ง่าย ๆ: update Codex Mac app + ChatGPT mobile → เลือก "Codex mobile" บน Mac → สแกน QR ด้วยมือถือ → พร้อมใช้. หลังจากนั้นผู้ใช้สามารถสลับ thread งานที่ active อยู่, review code ที่ Codex เขียน, approve / reject command, สลับ model หรือ kick off งานใหม่ — ทั้งหมดผ่านจอมือถือ.

จุดที่สะกิดใจคือ **availability** — OpenAI ปล่อยให้ทุก tier ใช้ได้ ตั้งแต่ Free, Go, Plus, Pro, Business. นี่ไม่ใช่ลายเซ็นปกติของ OpenAI ที่มักจะ gate feature ใหม่ไว้ใน Plus/Pro ก่อน — ครั้งนี้ Codex เปิดฟรีหมด distribution-first. Sam Altman ทวีตว่า "Codex now goes wherever you go" — ภาษาที่ฟังเหมือน mobile-first product มากกว่า dev tool. ข้อจำกัดสำคัญ: launch นี้รองรับเฉพาะ **Codex desktop เวอร์ชัน macOS** — Windows ยังไม่ได้ (OpenAI พูดถึง sandbox สำหรับ Windows ที่เพิ่ง announce ในวันเดียวกัน แต่ไม่ระบุวัน GA).

ฝั่ง mobile UX ที่น่าสนใจที่สุดคือ **approval workflow** — ผู้ใช้นั่งกินข้าวอยู่ มือถือสั่น Codex ขอ approve รัน migration บน prod, ผู้ใช้กด approve / reject ทันที. นี่คือ pattern ที่ Devin, Cursor Background Agent และ Claude Code ทำได้แค่บน desktop / web — OpenAI เป็นรายแรกที่ปล่อยลง native mobile app ที่มีคนใช้อยู่แล้ว 800M+ ตามตัวเลขล่าสุด.

## ทำไมสำคัญ

มุมที่สำคัญที่สุดคือ **distribution > model**. ระดับ frontier model ระหว่าง GPT-5, Claude Opus 4.7, Gemini 3 Pro ตอนนี้ใกล้กันมาก — สิ่งที่ตัดสินว่าใครจะชนะ agentic coding คือว่าผู้ใช้เข้าถึงได้จากที่ไหน. OpenAI ใช้ ChatGPT mobile app ที่มี user base ใหญ่สุดเป็น distribution channel ของ Codex — Anthropic / Google ไม่มี mobile app ขนาดนี้, Cursor / Windsurf ไม่มี mobile app เลย. ภายใน 6 เดือน developer ที่เคยรู้จัก Cursor อาจเริ่มเปิด Codex แทนแค่เพราะ "อยู่ในแอปอยู่แล้ว".

อีกประเด็น: นี่คือ counter-move ตรง ๆ ต่อ Anthropic credit meter (ดูข่าว #2). วันเดียวกัน Anthropic ขึ้น price ของ agentic Claude, OpenAI ขยาย free tier coverage ของ Codex. Axios เขียนตรง ๆ ว่า "OpenAI courts agent users". การที่ Codex อยู่ใน free tier ทำให้ผู้ใช้ Anthropic Pro ที่กำลังโกรธเรื่อง credit metering มี alternative ใช้ฟรีทันที. นี่คือ retention play จาก OpenAI ที่ฉลาดและ timing ดีมาก.

## มุม OpenBridge

ตรง ๆ ไม่กระทบ B2B integration platform — Codex mobile เป็น dev tool. แต่ adjacent insight ที่ OpenBridge เก็บได้: (1) **mobile approval workflow** จะเป็น UX standard ของ agent ทุกประเภทภายในปีนี้. ลูกค้า enterprise ที่รัน agent กับข้อมูลของ OpenBridge จะต้องการ "mobile checkpoint" — agent ทำ critical action เช่น sync data ระหว่างระบบ ต้องสั่น มือถือ approver ก่อน. ถ้า OpenBridge ทำ native iOS / Android หรือมี integration กับ Slack/Telegram ที่ approve ได้ — จะเป็น feature ที่ลูกค้าขอแน่นอน.

(2) **Codex จะกลายเป็นช่องทางที่ developer เขียน integration เอง** — แทนที่จะใช้ no-code builder ของ OpenBridge / Zapier. OpenBridge อาจคิดว่าควรเปิด CLI / SDK ให้ Codex / Claude Code / Cursor เขียน flow ของ OpenBridge ผ่าน natural language ได้แทน — ใครเปิด agent-native SDK ก่อน คนนั้นได้ developer audience ที่จะกลายเป็น power user ในอีก 1–2 ปี.

## Sources
- [OpenAI says Codex is coming to your phone — TechCrunch](https://techcrunch.com/2026/05/14/openai-says-codex-is-coming-to-your-phone/)
- [OpenAI brings Codex to ChatGPT for iPhone, iPad, and Android — 9to5Mac](https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/)
- [OpenAI Brings Codex Remote Access to ChatGPT Mobile App — MacRumors](https://www.macrumors.com/2026/05/15/openai-brings-codex-chatgpt-mobile-app/)
- [Anthropic tightens Claude limits as OpenAI courts agent users — Axios](https://www.axios.com/2026/05/14/anthropic-claude-price-openai-tokens)

---

## Audio script
ข่าวที่สาม — OpenAI ปล่อย Codex ลง ChatGPT mobile app วันที่ 14 พฤษภาคม รองรับทั้ง iOS และ Android อยู่ใน preview แต่เปิดให้ทุก tier ใช้ได้รวม Free และ Go ด้วย. Setup ง่ายมาก — update Codex Mac app และ ChatGPT mobile เลือก Codex mobile บน Mac แล้วสแกน QR ด้วยมือถือก็เสร็จ. หลังจากนั้นเราสลับ thread งานที่ active อยู่ approve หรือ reject commands สลับโมเดล หรือเริ่มงานใหม่ได้จากมือถือ. จุดที่สะกิดใจคือ Sam Altman เปิดให้ทุก tier ใช้ฟรี — ไม่เคยทำท่านี้กับ feature ใหม่มาก่อน. distribution-first ชัดเจน. ข้อจำกัดคือ pair กับ Codex desktop เวอร์ชัน Mac เท่านั้น Windows ยังไม่ได้. มุมที่สำคัญสุดคือ distribution มาก่อนโมเดล — GPT-5 Claude Opus 4.7 Gemini 3 Pro เก่งใกล้กันมาก สิ่งที่ตัดสินคือเข้าถึงได้จากไหน ChatGPT mobile มีฐานผู้ใช้แปดร้อยล้านคน Anthropic Google ไม่มี mobile app ขนาดนี้ Cursor Windsurf ไม่มีเลย. และนี่คือ counter-move ตรง ๆ กับ Anthropic credit meter ที่ออกวันเดียวกัน — Anthropic ขึ้นราคา agentic Claude OpenAI ขยาย free tier ฉลาดและ timing ดีมาก. มุม OpenBridge: mobile approval workflow จะเป็น UX standard ของ agent ทุกประเภทภายในปีนี้ ลูกค้า enterprise จะอยากได้ mobile checkpoint สำหรับ critical action ที่ agent ทำกับข้อมูล และเราอาจเปิด agent-native SDK ให้ Codex Claude Code Cursor เขียน flow ของ OpenBridge ด้วย natural language — ใครเปิดก่อนได้ developer audience ที่จะกลายเป็น power user.
