---
date: 2026-08-20
slug: slack-code-multi-agent-channels-salesforce
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  A wide editorial isometric illustration of a Slack-like chat channel window
  with the channel title "#project-launchpad" at the top. Inside the channel,
  five glowing avatar bubbles float side-by-side, each labeled clearly:
  "CLAUDE CODE", "DEVIN", "COPILOT", "VERCEL AGENT", "CHATGPT". A code diff
  panel with green and red highlights hovers to the right, and a small human
  silhouette sits at the bottom-left, reviewing the diff. Deep purple and
  slack-aubergine palette with lime and cyan accent highlights. Chunky
  sans-serif labels legible at 200px thumbnail, 1:1 aspect ratio, no real
  human faces.
image: images/26-08-23-0609-02-slack-code-multi-agent-channels-salesforce.png
---

# Slack Code — Salesforce ดึง Claude Code, Devin, Copilot, Vercel มาอยู่ในแชนแนลเดียวกัน

## TL;DR
- Slack เปิดตัว **Slack Code** วันที่ 20 ส.ค. 2026 — dedicated channel ที่ทีม + AI coding agent ทำงานร่วมกันแบบ real-time
- Agent ที่รองรับตอน launch: **Claude Code (Anthropic), Devin (Cognition), GitHub Copilot, Vercel Agent, ChatGPT (OpenAI)**
- ฟรีทุก plan รวม free workspace — Salesforce ไม่ล็อกไว้แค่ enterprise tier

## เกิดอะไรขึ้น
Salesforce ประกาศ Slack Code วันที่ 20 ส.ค. 2026 — feature ใหม่ที่แปลง Slack channel ให้กลายเป็น shared workspace สำหรับ "vibe coding" ระหว่างคนกับ AI agent หลายตัวพร้อมกัน mention @Claude, @Devin, @Copilot, @Vercel, หรือ @ChatGPT ในแชนแนล แล้ว agent จะกระโดดเข้ามาทำงานให้เห็นบน timeline เดียวกันกับที่ทีมคุยงาน

ทุกคนใน channel เห็น context เดียวกันที่ agent กำลังทำงานจากมัน สามารถ audit code diff ที่ agent เสนอ ดู live preview ของ HTML output ให้ feedback ที่ agent จะเอาไป incorporate และกด approve งานที่เสร็จแล้ว — ทั้งหมดโดยไม่ต้องออกจาก Slack

ที่ต่างจาก launch ทั่วไปคือ Salesforce ยอมปล่อยให้ฟรีทุก plan ตั้งแต่วันแรก แม้แต่ free workspace ก็ใช้ได้ — สื่อสารชัดว่าต้องการให้ทุกทีมเริ่มลองเลย ไม่ใช่กันไว้เป็น sales carrot ของ Business+/Enterprise Grid

## ทำไมสำคัญ
เรื่องนี้เป็นสองสัญญาณพร้อมกัน สัญญาณแรกคือ **coding agent ออกจาก terminal เข้าสู่ collaboration surface** — ตลอดปี 2025 ถึงต้นปี 2026 coding agent อย่าง Claude Code, Devin, Copilot ล้วนเริ่มจาก CLI หรือ IDE plugin ที่คน dev คนเดียวใช้ พอเข้ากลางปี 2026 landscape เริ่มยอมรับว่าการเขียน code จริง ๆ เกิดใน chat channel ที่มี PM/design/QA อยู่ด้วย — Slack Code จึงเป็นแรงกระตุกให้ agent vendor ต้องคิดใหม่ว่า "runtime" ของ coding agent อยู่ที่ไหน

สัญญาณที่สองคือ **Salesforce เดินเกม platform play แทน vendor play** — พร้อมเปิดให้ Anthropic, Cognition, Microsoft, Vercel, OpenAI มาอยู่ในบ้านตัวเองทั้งที่มี Agentforce เป็น first-party อยู่แล้ว มุมนี้เหมือน Microsoft ยอมให้ Slack, Zoom, Google อยู่ใน Windows ตอน early 2000s — ยอมเปิดบ้านเพื่อรักษาสถานะ default surface ที่ทีมใช้งาน แลกกับการเป็น context layer ที่ทุก agent ต้องผ่าน

เทียบกับสัปดาห์ก่อนที่ Salesforce Agentic Enterprise Index บอกว่า median enterprise ใช้ agent 13 ตัว/องค์กร Slack Code คือ answer ต่อคำถามที่ตามมา — "แล้ว agent 13 ตัวจะอยู่ตรงไหนให้คนเห็นได้"

## มุม AI Agent Platform
สำหรับ **builders**: multi-agent surface กำลังกลายเป็น battleground ใหม่ — ไม่ใช่แค่ทำ agent เก่ง แต่ agent ต้องพูดกับ agent อื่นในบริบทเดียวกัน (A2A protocol ที่คลุมไปในรอบก่อนจะเริ่ม matter จริง ๆ ตรงนี้) ถ้า builder ยังคิดว่า agent ของตัวเองต้องมี UI ของตัวเอง ให้คิดใหม่ — agent runtime กำลังย้ายไปอยู่ใน chat channel ที่คนอยู่แล้ว

สำหรับ **users/business**: นี่คือจังหวะที่ team lead ควรทดลอง Slack Code กับงาน internal tool หรือ prototype จริง — ต้นทุน onboarding เกือบเป็นศูนย์ และช่วยตอบคำถาม "cost/benefit ของ coding agent จริง ๆ เท่าไร" ที่ engineering manager หลายคนยังไม่มี baseline วัด

สำหรับ **ecosystem**: Vercel, Anthropic, Cognition, Microsoft, OpenAI ยอมเข้าบ้าน Slack เพราะรู้ว่า distribution ทั้ง 40M+ DAU ของ Slack คือช่องทางถึง developer เร็วที่สุด — สำหรับ Enabridge ในฐานะ AI Agent Platform สัญญาณคือถ้าอยากให้ agent ของ platform ตัวเองไปอยู่ในมือ developer ต้องมี native integration กับ chat surface (Slack, Teams, LINE, Discord) เร็วที่สุด ก่อนที่ Salesforce/Microsoft จะเป็นตัวกลางกำหนดว่าใครเข้าได้บ้าง

## Sources
- [Introducing Slack Code — Salesforce Blog](https://www.salesforce.com/introducing-slack-code/)
- [Slack Code Puts AI Coding Agents in Dedicated Project Channels — Unite.AI](https://www.unite.ai/slack-code-puts-ai-coding-agents-in-dedicated-project-channels/)
- [Slack wants to drag AI coding out of the terminal and into the group chat — VentureBeat](https://venturebeat.com/orchestration/slack-wants-to-drag-ai-coding-out-of-the-terminal-and-into-the-group-chat)

---

## Audio script
Salesforce เปิดตัว Slack Code เมื่อวันที่ 20 สิงหาคมที่ผ่านมา แนวคิดง่ายมากครับ — แปลง Slack channel ให้กลายเป็นห้องทำงานร่วมกันระหว่างทีมกับ AI coding agent หลายตัวพร้อมกัน

Agent ที่รองรับตั้งแต่วันแรกคือ Claude Code จาก Anthropic, Devin จาก Cognition, GitHub Copilot, Vercel Agent และ ChatGPT จาก OpenAI — mention agent ในแชนแนล แล้ว agent จะเข้ามาทำงานให้เห็นบน timeline เดียวกันที่ทีมคุยงาน review code diff ได้ ดู live preview ได้ approve งานได้ ทั้งหมดโดยไม่ต้องออกจาก Slack

ที่น่าสนใจคือฟรีทุก plan รวม free workspace — Salesforce ยอมเปิดบ้านให้ competitor อย่าง Microsoft, Anthropic, OpenAI มาอยู่ในบริบทเดียวกันเพื่อรักษา status ของ Slack ในฐานะ default surface ของทีม dev

สำหรับใครที่กำลังคิดจะ deploy coding agent ในองค์กร นี่คือ moment ที่จะลองแบบ zero-cost — และเป็นสัญญาณว่า agent runtime กำลังย้ายจาก terminal ไปอยู่ใน chat ที่ทีมอยู่แล้วครับ
