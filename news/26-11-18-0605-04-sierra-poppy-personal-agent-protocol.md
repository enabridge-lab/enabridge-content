---
date: 2026-11-18
slug: sierra-poppy-personal-agent-protocol
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of a handshake between two glowing
  robot hands — one labeled "USER AGENT", the other "BUSINESS AGENT" —
  forming a bridge over a river of OAuth tokens. Around the bridge, a ring
  of store-logo silhouettes glow: Shopify, Stripe, Walmart, Meta. Above the
  scene, a big banner reads "POPPY 1.0" and three stacked labels show:
  "OPEN STANDARD", "100+ DESIGN PARTNERS", "EVERY SHOPIFY STORE".
  Clean editorial style, soft lavender and warm rose palette, high
  contrast so labels stay readable at 200px thumbnail, 1:1 aspect,
  no real human faces (silhouettes OK).
image: images/26-11-18-0605-04-sierra-poppy-personal-agent-protocol.png
---

# Poppy 1.0 เปิดสเปค — Sierra กับ Meta วางรางให้ "agent คุยกับธุรกิจ" ผ่าน OAuth, Shopify เปิดทุกร้านทันที

## TL;DR
- Sierra ปล่อย Personal Agent Protocol (ชื่อเล่น Poppy) v1.0 เมื่อ 13 พ.ย. — open standard สำหรับให้ personal agent ของ user คุยกับระบบของ business บน OAuth
- Design partner 100+ รวม Meta, Shopify, Stripe, Walmart, Genesys — live แล้วใน Meta Muse และเปิดอัตโนมัติให้ Shopify merchant ทุกร้าน
- Spec แรกยัง ไม่มี payments — ชัดเจนว่าจะเป็น extension ที่ตามมา และต้องแข่งกับ agent protocol ของ Visa ที่ Stripe + Shopify เซ็นด้วยอยู่แล้ว

## เกิดอะไรขึ้น
ย้อนกลับไป 6 ตุลาคม Bret Taylor กับ Clay Bavor ที่ Sierra ประกาศแนวคิด Personal Agent Protocol ร่วมกับ Meta — ชื่อโค้ด Poppy — เป็น open standard สำหรับให้ personal AI agent ของ user (เช่น Muse ของ Meta) คุยกับธุรกิจได้ในรูปแบบเดียวกันทั้งหมด วันที่ 13 พฤศจิกายน Sierra ปล่อย Spec v1.0 ออกมาจริง พร้อมประกาศ design partner เพิ่มอีก 35 ราย รวมแล้วมี 100+ ธุรกิจเข้าร่วมแล้ว รวม Genesys, Instinct, Rocket Mortgage, Shopify, Stripe, Walmart และ NiCE บน site poppy.md มี implementation ของ spec และ reference code

เทคนิค Poppy ตั้งอยู่บน OAuth 2.0 — model การทำงานคือ user agent ไปที่ URL ของธุรกิจ discover ว่า agent endpoint อยู่ที่ไหน จาก manifest file ขอ guest session ก่อน แล้วถ้า user authorize แล้ว agent จะได้ read-only หรือ read-write token กับ scope ที่ธุรกิจกำหนด ธุรกิจเลือกได้ว่า expose ผ่าน web endpoint, API ของตัวเอง หรือผ่าน agent ของตัวเองก็ได้ Sierra ยืนยันว่า Poppy ไม่ใช่ replacement ของ MCP — MCP คุย "agent-to-tool", Poppy คุย "agent-to-business"

คลื่นแรกของการใช้งานจริงน่าสังเกต Meta Muse (personal agent ของ Meta) รองรับ Poppy ทันที และที่ชัดเจนที่สุดคือ Shopify เปิด Poppy endpoint ให้ merchant ทุกร้านอัตโนมัติ — แปลว่าร้านค้าออนไลน์กว่าสองล้านร้านทั่วโลก พร้อมให้ personal agent ของ user เข้ามา browse, คุยกับ bot ของร้าน และ (ในอนาคต) ซื้อของได้โดย merchant ไม่ต้อง deploy อะไรเพิ่ม

## ทำไมสำคัญ
Protocol war ที่หลายคนรออยู่ กำลังจะชัดขึ้น Poppy อยู่ฝั่งที่ให้ business expose capability แบบเปิดและ agent-agnostic — ใครก็ใช้ได้ ไม่ว่าจะเป็น Muse, ChatGPT หรือ Claude ด้าน Visa มี Visa Trusted Agent Protocol ที่เน้น commerce + payment โดยมี Stripe กับ Shopify ร่วมด้วย ทำให้ตอนนี้ Stripe กับ Shopify "เข้าร่วม" ทั้งสองค่าย — ซึ่งเป็น hedge ที่สมเหตุสมผลจากมุมของธุรกิจเหล่านั้น เพราะไม่รู้ standard ไหนจะชนะ

จุดที่ Poppy ยังเสี่ยงคือเรื่อง payments — spec v1.0 ไม่ครอบ และ Sierra บอกว่าจะเป็น extension ที่ตามมา ซึ่งแปลว่าช่วง 6-12 เดือนข้างหน้า Visa มีช่องว่าง ที่จะไล่ claim ตลาด agent commerce จริง ๆ ก่อน ส่วน Poppy เหมาะกับ interaction นอก payment (search, booking, support) ที่มีจำนวนมากกว่า แต่ monetize ยากกว่า

ที่ Meta เลือกเป็น partner ก่อตั้ง ไม่ใช่ Google หรือ OpenAI มีนัยยะ — Meta ต้องการ distribution สำหรับ Muse ที่ไม่ผูกกับ Google (เพราะ Muse คุยกับ Google ไม่ได้อยู่ดี) การผลักดัน open standard ที่ตัวเองเป็นเจ้าของร่วม = การสร้างสนามที่ไม่มี incumbent dominant นี่คือ playbook เดียวกับที่ Facebook ใช้กับ React เมื่อสิบปีก่อน

## มุม AI Agent Platform
สำหรับ **Builders** — ถ้าคุณกำลังสร้าง agent ที่ต้อง interact กับ business จริง นี่คือ spec ที่ควรอ่านทันที 100+ partner ใน 5 สัปดาห์หลังประกาศ คือ velocity ที่ MCP ใช้เกือบหนึ่งปี การ support Poppy เร็วอาจเป็น competitive advantage ในปีหน้า คำถามคือ จะ dual-stack กับ Visa Trusted Agent Protocol ไหม — โดยทั่วไปคำตอบคือใช่ ตราบใดที่ cost implementation ไม่แพงมาก

สำหรับ **Users / business** — ถ้าคุณมี website หรือ API ที่ลูกค้าใช้ ลองดู poppy.md แล้วประเมินว่าใช้เวลากี่ชั่วโมงถึงจะ expose Poppy endpoint ได้ Shopify merchant ไม่ต้องคิด — ของมาอัตโนมัติ — แต่ถ้าคุณอยู่บน platform อื่น อาจต้องเสีย sprint หนึ่งเพื่อให้พร้อม เมื่อ user ถือ Muse หรือ ChatGPT ที่ speak Poppy ธุรกิจที่ expose ก่อนจะได้ visibility ก่อน และสำหรับ ecosystem overall — การที่ Stripe + Shopify สนับสนุนทั้ง Poppy และ Visa protocol สะท้อนว่า standard war จะยืดเยื้ออีกอย่างน้อยหนึ่งปี

## Sources
- [Sierra announces Personal Agent Protocol, an open standard for personal AI agents — TNW](https://thenextweb.com/news/personal-agent-protocol-sierra-meta)
- [Sierra releases Poppy 1.0 with Shopify-wide agent discovery — Runtime Wire](https://runtimewire.com/article/sierra-ships-poppy-1-0-and-puts-personal-agents-on-every-shopify-store)
- [Genesys, NiCE Join Sierra, Meta on Open Standard for Personal AI Agents — CMSWire](https://www.cmswire.com/contact-center/genesys-joins-sierra-meta-on-open-standard-for-personal-ai-agents-01/)
- [Poppy (Personal Agent Protocol): Spec Status & Comparisons — poppy.md](https://poppy.md/)

---

## Audio script
Sierra ของ Bret Taylor เพิ่งปล่อย Personal Agent Protocol version หนึ่ง ชื่อเล่น Poppy เมื่อสี่วันก่อน พร้อม design partner กว่าร้อยราย รวม Meta, Shopify, Stripe, Walmart, Genesys โปรโตคอลนี้ตั้งอยู่บน OAuth model การทำงานคือ personal agent ของ user ไปหา business discover ว่า agent endpoint อยู่ที่ไหน ขอ guest session ก่อน แล้วถ้าเจ้าของ business authorize จะได้ read-only หรือ read-write token ธุรกิจเลือกได้ว่าจะ expose ผ่าน website, API หรือ agent ของตัวเอง

ที่น่าสังเกตคือ Shopify เปิด Poppy endpoint ให้ร้านค้าทุกร้านอัตโนมัติ สองล้านกว่าร้านทั่วโลก พร้อมให้ personal agent ของ user เข้ามา browse แต่ spec version แรกยังไม่ครอบ payments ซึ่งเป็นช่องว่างที่ Visa มี Trusted Agent Protocol ของตัวเองรออยู่ Stripe กับ Shopify เลยเข้าร่วมทั้งสองค่ายเพื่อ hedge นี่คือ protocol war ที่หลายคนรอ และสัญญาณสำหรับ builders คือ Poppy ขึ้นเร็วกว่า MCP ตอนเปิดตัว การ support Poppy เร็วอาจเป็น edge ในปีหน้า สำหรับธุรกิจ ถ้ามี website หรือ API ของตัวเอง ลองประเมินว่าจะเปิด endpoint ได้ใน sprint ไหน เพราะเมื่อ user ถือ agent ที่คุย Poppy ได้ ธุรกิจที่เปิดก่อนจะได้เข้าสายตา agent ก่อน
