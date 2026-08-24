---
date: 2026-08-25
slug: aws-bedrock-agentcore-payments-ga-hyperscaler
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  A wide editorial isometric illustration of a modern glass fintech corridor.
  A small friendly robot agent walks up to a bank-vault gate labeled
  "AGENT PAYMENTS GA" and taps a glowing badge. Two protocol banners hang
  above the corridor: "x402" on the left and "MPP" on the right. A stopwatch
  hovers with big text "UNDER 4 SECONDS" and a receipt strip labeled
  "AUDIT TRAIL" trails behind the robot. A small AWS smile-arrow pin on the
  gate; deep navy, teal, and amber palette; chunky sans-serif labels
  readable at 200px thumbnail; 1:1 aspect ratio; no real human faces.
image: images/26-08-25-0615-02-aws-bedrock-agentcore-payments-ga-hyperscaler.png
---

# AWS Bedrock AgentCore Payments GA — hyperscaler เสียบ agent commerce เข้า console เดียว

## TL;DR
- Amazon Bedrock AgentCore Payments เข้า GA รองรับทั้ง **x402** และ **Machine Payments Protocol (MPP)** — agent จ่ายเงินได้ผ่าน managed layer เดียว
- One-click Coinbase Quick Create, Stripe Privy wallet สำหรับ stablecoin microtx, spending cap ต่อ session, expiry, observability ครบผ่าน CloudWatch
- Solv Labs (first customer proof) ใช้ AgentCore Payments + AWS Nitro Enclaves + policy engine ORACLE รัน verified agent payment **ใต้ 4 วินาที** พร้อม cryptographic audit trail anchor ไป Base chain

## เกิดอะไรขึ้น
วันที่ 18 ส.ค. 2026 AWS ปล่อย Amazon Bedrock AgentCore Payments จาก preview ขึ้นสู่ General Availability เพียง 6 สัปดาห์หลัง Cloudflare กับ Coinbase push x402 กลายเป็น payment protocol กลางของ agent economy รอบก่อน AWS ตัดสินใจไม่เลือกข้าง — รองรับทั้ง x402 (ของฝั่ง Cloudflare/Coinbase) และ Machine Payments Protocol MPP ที่ Google/Anthropic/Circle เชียร์ ผ่าน managed layer เดียว agent developer จะเลือก protocol ไหนก็ได้ตาม vendor ปลายทาง

Feature set ที่ ship มาพร้อม GA ครอบทั้ง lifecycle: one-click Coinbase Quick Create สำหรับสร้าง merchant account, Stripe Privy สำหรับ stablecoin microtx wallet, spending cap ที่ตั้งได้ต่อ session (เช่น $50/session, $1,000/day, $10,000/agent/month), expiry ที่ทำให้ credential หมดอายุอัตโนมัติหลัง run จบ, และ end-to-end observability ที่ทุก transaction ไปโผล่ใน CloudWatch พร้อม trace กลับได้ถึง prompt ที่ trigger การจ่าย

Customer proof ที่ AWS ปล่อยคู่กันคือ Solv Labs — RWA infrastructure ที่ทำ tokenized credit บน Base ใช้ AgentCore Payments คู่กับ AWS Nitro Enclaves (confidential compute) และ policy engine ของตัวเองชื่อ ORACLE รัน verified agent payment ที่ latency **ใต้ 4 วินาที** ต่อ transaction พร้อม cryptographic audit trail ที่ anchor hash กลับ Base chain — ทุก payment ตรวจสอบได้ end-to-end โดย auditor ไม่ต้องเข้าดู internal log ของ Solv เอง

## ทำไมสำคัญ
สัปดาห์นี้เป็นสัปดาห์ที่ agent payments ย้ายจาก spec ไปเป็น hyperscaler default พร้อม 3 layer ในเวลาไม่ถึง 10 วัน: Cloudflare x402 stack เมื่อ 20 ส.ค., Web Search on AgentCore GA เมื่อ 21 ส.ค., และตอนนี้ AgentCore Payments GA ต่อจากนี้ enterprise team ที่อยากให้ agent เรียก paid API, ซื้อ MCP server รายเดือน, หรือจ่าย per-request ให้ agent อีกตัวไม่ต้อง build billing infra เอง — เปิด console AWS แล้วเลือก protocol เสร็จ

ที่หนักกว่านั้นคือ AWS เลือกไม่บังคับ protocol เดียว ท่านี้เหมือนสมัย AWS ship RDS ที่รองรับ MySQL, PostgreSQL, MariaDB, Oracle, SQL Server พร้อมกัน — ปล่อยให้ตลาดตัดสินใจแล้ว AWS เก็บค่า managed layer ทั้งสองข้าง สำหรับ enterprise buyer ที่ยังไม่แน่ใจว่า x402 หรือ MPP จะชนะ นี่คือ zero-risk bet — เลือก AWS แล้วปรับ protocol ทีหลังได้

Signal ต่อจากนี้: Azure กับ Google Cloud มีเวลาไม่กี่เดือนก่อนจะโดน Solv Labs-class customer ยกเข้า AWS ทั้งหมด (compliant compute + agent payment ในเจ้าเดียว) และ startup ที่ build "agent payments as a service" เฉย ๆ อยู่ในช่องที่ถูกกินขึ้น — margin จะบีบเข้าหา protocol layer หรือ vertical wrapper เร็ว ๆ นี้

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ agent framework/runtime: ถ้ายังคิดว่า payment เป็น feature "phase 2" ให้กระโดดข้ามได้เลย เพราะ hyperscaler เพิ่ง commodify layer นั้นแล้ว focus ที่ orchestration logic กับ policy layer แทน (approval flow, spending governance, dispute handling) — เขต value ใหม่ของ builder อยู่ที่ "ใครควรอนุมัติ, spending threshold แบบไหนสำหรับ role อะไร, จะ rollback ยังไงถ้า agent จ่ายผิด"

สำหรับ **users/business** ที่ deploy agent ใน workflow: ถ้า infrastructure อยู่บน AWS อยู่แล้ว AgentCore Payments คือ path ที่สั้นที่สุดในการเปิด agent commerce use case — เริ่มจาก procurement automation, API subscription management, หรือ B2B micro-marketplace ก่อน สำหรับลูกค้า Thai SME ที่ Enabridge เข้าไปคุย argument จะเปลี่ยนเป็น "agent จ่ายเงินได้ปลอดภัย ไม่ต้องเปิด credit card แยก ทุก transaction มี audit trail" ซึ่งขายง่ายกว่า "let's talk about x402 spec"

สำหรับ **ecosystem** (Stripe, Adyen, Airwallex, payment processor Thai อย่าง 2C2P): agent payment คือช่องใหม่ที่ไม่ได้เกี่ยวกับ human checkout — trigger, authorization, limit ต่างกันหมด ใครที่ ship agent-first API และ webhook สำหรับ suspicious pattern detection ทัน AWS จะเป็น partner default; ที่ยัง treat agent เป็น regular API caller จะโดน bypass Cloudflare x402 กับ AWS AgentCore Payments กำลังกลาย reference architecture

## Sources
- [Amazon Bedrock AgentCore Payments is now generally available — AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-payments-is-now-generally-available-enabling-agents-to-transact-safely-and-autonomously-at-scale/)
- [Amazon Bedrock AgentCore Payments GA — AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/08/bedrock-agentcore-payments-ga/)
- [How Solv Labs built verifiable, auditable agent payments on AgentCore Payments — AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/pay-with-confidence-how-solv-labs-built-verifiable-auditable-agent-payments-on-amazon-bedrock-agentcore-payments/)

---

## Audio script
วันนี้ AWS ปล่อย Amazon Bedrock AgentCore Payments เข้า General Availability ครับ agent สามารถจ่ายเงินได้ผ่าน managed layer เดียวที่รองรับทั้ง x402 กับ Machine Payments Protocol พร้อมกัน

Feature ที่ ship มาครบชุด one-click Coinbase Quick Create สำหรับสร้าง merchant account, Stripe Privy wallet สำหรับ stablecoin microtx, spending cap ต่อ session, expiry ที่ credential หมดอายุอัตโนมัติ, และ observability ผ่าน CloudWatch trace ได้ถึง prompt ที่ trigger การจ่าย

Customer proof แรกที่ AWS ปล่อยคู่กันคือ Solv Labs ใช้ AgentCore Payments คู่กับ Nitro Enclaves รัน verified agent payment ใต้ 4 วินาทีต่อ transaction พร้อม cryptographic audit trail anchor ไป Base chain

signal สำหรับคนทำ agent platform คือ payment เพิ่งกลายเป็น commodity layer ของ hyperscaler ต่อจากนี้ value ของ builder ต้องขยับไปที่ orchestration กับ governance policy แทน สำหรับ enterprise ที่อยู่บน AWS อยู่แล้ว procurement automation กับ B2B micro-marketplace คือ use case ที่เริ่มได้ทันทีครับ
