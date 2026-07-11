---
date: 2026-07-12
slug: arcade-agent-gateway-azure-aws-marketplace
topic: openbridge-trend
reading_time_min: 4
sources: 4
image_prompt: |
  A wide editorial isometric illustration of a highway toll gate labeled
  "AGENT GATEWAY" with three overhead lanes marked "AZURE MARKETPLACE",
  "AWS MARKETPLACE", and "BYO CLOUD". Small autonomous robot-agents in a
  queue pass under the gate, each getting a stamp reading "AUTH RE-CHECKED"
  in bright cyan. On the side, a bold billboard shows the number
  "1-CLICK DEPLOY" and a smaller sign "$98M RAISED". The scene has a
  fintech/enterprise editorial style, teal and orange palette, high
  contrast, 1:1 aspect, readable at 200px thumbnail, no real human faces.
image: images/26-07-12-0608-02-arcade-agent-gateway-azure-aws-marketplace.png
---

# Arcade ยิง agent authorization runtime ขึ้น Azure + AWS Marketplace — "agent gateway" กลายเป็น control plane ใหม่ของ enterprise AI

## TL;DR
- 3 กรกฎาคม 2026 Arcade เปิดให้ enterprise deploy **agent authorization + tool-execution runtime** ของตัวเองผ่าน **Microsoft Azure Marketplace** และ **AWS Marketplace** — 1-click install เข้า cloud ของตัวเอง, ใช้ existing cloud commitment ไม่ต้องเริ่ม procurement ใหม่
- Arcade อยู่ในหมวด "agent gateway" — Forbes เพิ่งเขียนวันที่ 5 ก.ค. ว่า category นี้กำลังกลายเป็น **control plane ของ enterprise AI** — คู่แข่งทันทีคือ Nutanix + Manufact; ภาพใหญ่คือ security startup ในหมวด agent security ระดมทุนไปแล้ว **~$98M** ในเดือนมิถุนายน
- Value prop ของ Arcade: **decouple authorization จาก live session** — background agent ทำงานภายใต้ delegated user authority ที่ re-check **ทุก action** ไม่ใช่ตอน login ครั้งเดียว

## เกิดอะไรขึ้น
Arcade เป็น startup ที่ตอบคำถามที่ enterprise SecOps ถามกันทุกที่: **"agent ตัวนี้ทำ action ในนามใคร แล้วเรารู้ได้ยังไงว่า user คนนั้นยังมีสิทธิ์ทำเมื่อ agent ทำจริง 3 ชั่วโมงต่อมา?"** — ในโลก interactive session เดิม OAuth token/session cookie handle ได้ แต่ agent ที่ทำงาน asynchronous, long-running, delegated ต้องการ model ใหม่. Arcade แยก "authorization" ออกจาก "live session" — token ผูกกับ user + scope + action, re-check ทุก tool call ที่ agent ยิง ไม่ใช่ตอน launch ครั้งเดียว

3 กรกฎาคม Arcade ประกาศว่าลูกค้า enterprise install runtime นี้เข้า cloud ตัวเองได้ผ่าน **Azure Marketplace** และ **AWS Marketplace** — 1-click. ประเด็นสำคัญไม่ใช่ deployment tech แต่คือ **procurement**: enterprise มี cloud commitment (EDP/AWS Enterprise Discount) ที่ต้อง burn ให้หมด, ซื้อผ่าน marketplace = แปลง commitment เป็น software spend ทันที ไม่ต้องผ่าน vendor onboarding, security review เต็ม cycle, PO ใหม่. เท่ากับ **cut time-to-deploy จาก quarter → week**

Forbes (Janakiram MSV) เขียน 5 ก.ค. ว่า "agent gateway" กำลังกลายเป็น "control plane for enterprise AI" — วาง Arcade ข้าง **Nutanix** (จับตลาด hybrid + on-prem) และ **Manufact** (จับ multi-cloud + edge). ก่อนหน้านั้น 18 มิถุนายน มีข่าว **agent security startup ระดมทุนรวม ~$98M** (Convey + Arcade เป็นแกน) — หมายความว่า VC เชื่อในหมวดนี้พอกับที่เคยเชื่อ observability ปี 2020

## ทำไมสำคัญ
"Agent gateway" คือ layer ที่ **ไม่มีชื่อชัดเจนเมื่อครึ่งปีก่อน แต่ปัจจุบันเริ่มมี taxonomy** — คล้าย API gateway ในยุค microservice ปี 2016 หรือ service mesh ปี 2018. หน้าที่คือควบคุม **traffic ระหว่าง agent กับ tool/model/data** — auth, rate limit, audit log, cost cap, policy enforcement — ทุกอย่างที่ app team ไม่อยากเขียนใหม่ในทุก agent. เมื่อ hyperscaler อย่าง Google เปิด **Agent Gateway** เป็น first-class component ใน Gemini Enterprise Agent Platform (เม.ย. 2026) ก็เท่ากับ **legitimize category** ให้ startup ตัวเล็กเข้ามาเสียบ

การ list บน Azure + AWS Marketplace ในเวลาเดียวกันเป็น play ที่ smart: **Arcade ไม่แข่งกับ hyperscaler แต่ใช้ distribution ของ hyperscaler** — enterprise ที่ standardize บน Azure ใช้ได้, enterprise ที่ standardize บน AWS ก็ใช้ได้, และเพราะ runtime อยู่ใน cloud ของลูกค้า (ไม่ใช่ SaaS) → data ไม่ leave environment, satisfy compliance ทันที. ต่างจาก vendor SaaS ที่ต้องเจรจา DPA แต่ละราย

Signal ต่อจากนี้: **procurement friction** จะกลายเป็น moat สำคัญกว่า tech. Startup ที่ list marketplace ได้เร็ว, มี co-sell agreement, และเข้า commit-burn ได้ = ชนะ startup ที่ tech ดีกว่าแต่ต้อง sell direct. เท่ากับตลาด agent infrastructure จะ **consolidate เร็วกว่าที่ predict** — ใครไม่ list marketplace ในไตรมาสนี้ อาจตกขบวน

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าสร้าง agent framework/runtime อยู่ ต้อง priority list marketplace (AWS/Azure/GCP) เป็น go-to-market channel หลัก ไม่ใช่ afterthought — และต้องมี **BYO cloud deployment model** เพราะ enterprise แพ้เรื่อง data residency ไม่ยอม SaaS-only. สำหรับ **users/business**: ถ้ากำลัง deploy agent มากกว่า 1-2 use case ตั้งคำถามให้ vendor: "authorization ของ agent ผมทำงานยังไง? re-check ทุก tool call ไหม? audit log traceable ไหม?" — ถ้าตอบไม่ได้ ให้เพิ่ม gateway layer ก่อน scale. สำหรับ **ecosystem**: หมวด agent security/gateway จะ consolidate ใน 6-12 เดือนข้างหน้า — คาดว่าจะมี M&A ระหว่าง hyperscaler กับ Arcade/Nutanix/Manufact เกิดขึ้น เพราะ hyperscaler อยากได้ full stack และ startup อยากได้ scale

## Sources
- [Agent Gateways Are Becoming The Control Plane For Enterprise AI — Forbes](https://www.forbes.com/sites/janakirammsv/2026/07/05/agent-gateways-are-becoming-the-control-plane-for-enterprise-ai/)
- [Arcade MCP Runtime — AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=seller-qbstsdnxkltx6)
- [Enterprise AI Agent Security Startups Raise $98M — TechTimes](https://www.techtimes.com/articles/318616/20260618/enterprise-ai-agent-security-startups-raise-98m-convey-arcade-tackle-production-gap.htm)
- [Arcade Docs — arcade.dev](https://docs.arcade.dev/en/home)

---

## Audio script
3 กรกฎาคมที่ผ่านมา Arcade ประกาศว่า enterprise ติดตั้ง agent authorization runtime ของเขาได้ผ่าน Microsoft Azure Marketplace กับ AWS Marketplace แบบ 1-click แล้ว จุดที่สำคัญไม่ใช่แค่ tech แต่คือ procurement เพราะ enterprise ส่วนใหญ่มี cloud commitment ที่ต้องเผาให้หมด ซื้อผ่าน marketplace เท่ากับแปลง commit เป็น software spend ทันที ไม่ต้องเริ่ม vendor onboarding ใหม่ ตัด time-to-deploy จากไตรมาสเป็นสัปดาห์

Forbes เพิ่งเขียน 5 กรกฎาคมว่า agent gateway กำลังกลายเป็น control plane ของ enterprise AI — เป็นหมวดเดียวกับที่ Nutanix กับ Manufact กำลังลง และเดือนมิถุนายน startup ในกลุ่มนี้ระดมทุนรวมประมาณ 98 ล้านดอลลาร์แล้ว ตัว value prop ของ Arcade คือ decouple authorization ออกจาก live session — background agent ทำงานภายใต้ delegated user authority ที่ re-check ทุก action ไม่ใช่แค่ตอน login

pattern ที่เห็นชัดคือ agent infrastructure จะ consolidate ผ่าน marketplace ใน 6-12 เดือนข้างหน้า และ procurement friction จะกลายเป็น moat สำคัญกว่า tech ถ้าคุณกำลังสร้าง agent runtime อยู่ ต้อง priority list marketplace และมี BYO cloud model ตั้งแต่วันแรก และถ้าคุณเป็นคน deploy agent ในองค์กร ถามคำถามให้ vendor ว่า auth ของ agent ทำงานยังไง audit ได้ไหม re-check ทุก tool call ไหม ถ้าตอบไม่ได้ ให้เพิ่ม gateway layer ก่อน scale
