---
date: 2026-10-21
slug: anthropic-claude-duet-proactive
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  A split-scene editorial illustration: on the left, a dim bedroom at dawn with
  a glowing phone on a nightstand displaying a stylized "DUET" morning brief
  with three bullet points. On the right, a cloud-shaped computer labeled
  "CLOUD VM" running tasks while a user silhouette walks away. Between them,
  a prominent "APPROVE?" dialog box with yes/no buttons intercepts a payment icon,
  a signature icon, and a trash can icon. Three stacked numbers hover above:
  "OPUS 5.5", "US PRO + MAX", "WAITLIST". Warm amber and deep teal palette,
  strong contrast for 200px thumbnails, 1:1 aspect, no real human faces.
image: images/26-10-22-0605-02-anthropic-claude-duet-proactive.png
---

# Anthropic เปิด Claude Duet — proactive agent ที่ทำงานต่อตอนปิดแอป, run บน Opus 5.5, ขอ approval ก่อนจ่ายเงิน

## TL;DR
- **21 ต.ค.** Anthropic เปิด **research preview** ของ Claude Duet — proactive AI agent บน mobile + desktop ที่ส่ง morning brief, เช็คแอปทุก 2-3 ชั่วโมง, และ run งานใน cloud VM ของตัวเองต่อได้แม้ผู้ใช้ปิดแอป
- รันบน **Opus 5.5** — ตัว top-tier model ของ Anthropic — เปิด **waitlist** ให้แค่ **US Pro + Max subscriber** (ไม่รวม Team/Enterprise)
- Duet ขอ **approval** ก่อนทำ 4 action: ส่งข้อความ, จ่ายเงิน, เซ็นเอกสาร, ลบไฟล์. มี credential isolation + action-approval classifier + prompt-injection defense
- Position: ตอบ Meta Muse (ก.ย.) + OpenAI Dots (ส.ค.) — frontier lab ขยับไปที่ **proactive consumer agent** พร้อมกัน; signal ว่า **เราผ่านยุค "reactive chat" แล้ว**

## เกิดอะไรขึ้น

วันพุธที่ **21 ต.ค.** Anthropic ประกาศ **Claude Duet** — standalone app (iOS + macOS + Windows) ที่ Claude ทำหน้าที่เป็น proactive agent ไม่ใช่ chat window. แทนที่จะรอให้ผู้ใช้เริ่ม conversation, Duet **ส่ง morning brief ทุกเช้า** จาก connected app (Gmail, Google Calendar, Slack, GitHub, Notion, Linear, Jira), เช็คทุก 2-3 ชั่วโมงว่ามีอะไรต้อง surface, และสามารถ **run งานใน cloud VM ของตัวเอง** ที่ Anthropic host — คือเมื่อผู้ใช้สั่งงานแล้วปิดแอป งานยังรันต่อ. ตอน done, Duet ส่ง notification กลับมา

Access: เปิดแค่ **US Pro + Max subscriber** ผ่าน **waitlist**, Team และ Enterprise plan ยัง **ไม่รวม** (Anthropic บอก "จะขยายภายหลัง" ไม่มี timeline). รันบน **Opus 5.5** — ไม่ใช่ Sonnet หรือ Haiku — คือ Anthropic ยอมจ่าย inference cost สูงเพื่อให้ reliability ของ action สูงพอสำหรับ background execution

Safety story ที่ Anthropic เน้น: Duet **หยุดถาม approval** ก่อน 4 action: (1) ส่งข้อความ, (2) ทำ payment, (3) เซ็น document, (4) ลบไฟล์. โครงสร้างมี **credential isolation** (secret ไม่ถูก copy ลงใน VM), **action-approval classifier** (ML model ที่ตัดสินว่า action ไหนต้อง pause), และ **prompt-injection defense** layer. VentureBeat note ตรง ๆ ว่า "เหล่านี้คือ description ของ safeguard — ไม่ใช่หลักฐานว่า agent จะไม่ take unauthorized action ตลอดเวลา"

ตำแหน่งใน market: Duet ตามหลัง **Meta Muse** (ก.ย. 2026) และ **OpenAI Dots** (ส.ค. 2026) ที่เป็น proactive agent สำหรับ consumer เหมือนกัน. ทั้ง 3 lab ขยับไปที่ format นี้ภายใน 10 สัปดาห์ — ไม่ใช่เรื่องบังเอิญ. 9to5Google, MacRumors, VentureBeat ตั้งหัวข่าวตรงกันว่า "Anthropic ตอบ Muse และ Dots" ซึ่งก็เป็น framing ที่ Anthropic เองไม่ค้าน

## ทำไมสำคัญ

Pattern สำคัญคือ **frontier lab ย้าย frontline product จาก chat ไป proactive agent พร้อมกัน**. จุดเปลี่ยนไม่ใช่เรื่อง capability — Opus 5.5, GPT-5 ที่ Dots รันอยู่, และ Muse ของ Meta ไม่ได้ smarter กว่า Opus 4 หรือ GPT-4 มากขนาดนั้น. จุดเปลี่ยนคือ **ความมั่นใจเรื่อง safety ของ action ที่รันแบบ background**. ก่อนหน้านี้ agent "autonomous" คือ demo ที่ลูกค้าต้องยืนดู; ตอนนี้คือ product ที่ตั้งใจให้ลูกค้า "เดินไปทำอย่างอื่น". Approval-before-action pattern — pause เพียง 4 กรณี, ไม่ใช่ทุก action — คือ **compromise ใหม่** ระหว่าง autonomy กับ control ที่ตลาด consumer จะยอมรับ (หรือไม่) ก็ตัดสินในหกเดือนข้างหน้า

เลเยอร์ที่ลึกกว่าคือ **ธุรกิจ model ของ frontier lab กำลังเปลี่ยน**. Chat subscription ($20/$100/$200) คือ pricing ที่ scalable ยาก — session จำกัดด้วย human attention. Proactive agent ที่รัน background คือ **compute-driven pricing** ที่ scale ตาม VM-hour ไม่ใช่ตาม active user. Pro + Max เริ่มเป็นแค่ ticket เข้า — "value" จริงจะอยู่ที่ VM-tier ที่ลูกค้าซื้อเพิ่ม (คล้าย AWS). Anthropic ไม่ได้ bundle VM-hour ชัดเจนรอบนี้ แต่ framing "cloud computer" คือ hint ที่หนัก

และ **Enterprise ไม่ได้** — คือ signal สำคัญ. Anthropic เลือก consumer rollout ก่อน Enterprise เพราะ: (1) consumer ยอมรับ "research preview quality" ที่ enterprise ไม่ยอม, (2) credential model ของ enterprise ต้องการ IAM/SSO/audit integration ที่ยัง polish ไม่พอ, (3) prompt-injection risk ใน shared workspace สูงกว่า personal account หลายเท่า. Anthropic กำลัง battle-test ที่ consumer ก่อนตั้งราคา enterprise จริง

## มุม AI Agent Platform

สำหรับ **Builders** ที่สร้าง agent framework (LangGraph, CrewAI, Mastra, Microsoft Agent Framework): Duet-style proactive loop คือ **pattern ที่ framework ควร support out-of-box** — scheduled polling, state ที่ persist ข้าม session, approval callback, VM lifecycle management. ถ้า framework คุณ generation-only ไม่พอ background execution จะหลงยุค. สำหรับ **Users / Business** ที่กำลัง evaluate agent: proactive loop + 4-action approval คือ **spec ขั้นต่ำ** ที่ควรต้องการจาก vendor — ไม่ใช่ nice-to-have. ถ้า vendor demo แค่ chat-based agent, คุณกำลังดู product ของยุคที่แล้ว. สำหรับ **Ecosystem**: Meta Muse + OpenAI Dots + Claude Duet ขยับพร้อมกันคือ frontier lab รับ **"ownership ของ default consumer surface"** กลับคืนจาก assistant OEM (Siri, Google Assistant, Alexa). เลเยอร์ voice/notification จะเป็น **ที่ที่ 3 lab ชนกัน** ในปี 2027 — ไม่ใช่ model performance

## Sources
- [Claude Duet is Anthropic's proactive AI agent answer to Muse and OpenAI's Dots (9to5Google)](https://9to5google.com/2026/10/21/claude-duet-anthropic-ai-agent-waitlist/)
- [Anthropic Launches Claude Duet, a Proactive AI Agent (MacRumors)](https://www.macrumors.com/2026/10/21/anthropic-claude-duet/)
- [Anthropic's answer to Muse is here: Claude Duet (VentureBeat)](https://venturebeat.com/technology/anthropics-answer-to-muse-is-here-claude-duet-a-mobile-and-desktop-ai-agent-that-takes-actions-proactively)
- [Anthropic Opens Claude Duet, an Opus 5.5 Agent, to US Pro and Max (AI Weekly)](https://aiweekly.co/alerts/anthropic-opens-claude-duet-an-opus-55-agent-to-us-pro-and-max)

---

## Audio script
วันพุธที่ 21 ตุลาคม Anthropic เปิดตัว Claude Duet — proactive AI agent ที่รันบน mobile กับ desktop ไม่ใช่แค่ chat window แบบที่ใช้ Claude อยู่ปัจจุบัน. Duet ส่ง morning brief ทุกเช้าจากแอปที่ connect ไว้ เช็คทุก 2-3 ชั่วโมงว่ามีอะไรต้อง surface, และสามารถรันงานใน cloud VM ของตัวเอง — คือเมื่อสั่งงานแล้วปิดแอป งานยังทำต่อแล้วส่ง notification กลับมา. Duet รันบน Opus 5.5 เปิดแค่ US Pro กับ Max subscriber ผ่าน waitlist, Team กับ Enterprise plan ยังไม่รวม. จุดที่น่าสนใจคือ Duet หยุดถาม approval ก่อน 4 action: ส่งข้อความ, จ่ายเงิน, เซ็นเอกสาร, ลบไฟล์ — ไม่ใช่ทุก action ซึ่งเป็น compromise ใหม่ระหว่าง autonomy กับ control. ที่น่าสังเกตคือ Duet ตามหลัง Meta Muse กับ OpenAI Dots ที่เพิ่งเปิดก่อนหน้า — frontier lab 3 เจ้าขยับไปที่ proactive consumer agent พร้อมกันภายใน 10 สัปดาห์ ไม่ใช่เรื่องบังเอิญ. Signal คือเราผ่านยุค reactive chat แล้ว และปี 2027 frontier lab จะชนกันที่เลเยอร์ notification กับ voice ไม่ใช่ที่ model performance อีก
