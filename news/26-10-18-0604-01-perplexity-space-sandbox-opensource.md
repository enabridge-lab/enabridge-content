---
date: 2026-10-18
slug: perplexity-space-sandbox-opensource
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  A sleek editorial illustration of a vault built from translucent glass, labeled
  "SPACE" in bold capitals, holding nine glowing orbs that each wear a tiny
  framework logo badge (abstract, not real brands). Around the vault, 118 tiny
  arrows bounce off its walls — none penetrate. Three big stacked numbers float
  beside it: "60ms SPIN-UP", "0 ESCAPES", "118 TRIES". Below the vault, three
  cloud ribbons labeled "COREWEAVE", "AKAMAI", "CRUSOE" flow outward. Editorial
  isometric style, cobalt and amber palette, strong contrast for 200px thumbnails,
  1:1 aspect, no real human faces.
image: images/26-10-18-0604-01-perplexity-space-sandbox-opensource.png
---

# Perplexity โยน SPACE sandbox ของ Comet ขึ้น GitHub — ท้าว่า 9 frontier model หนีไม่ออก 118 ครั้งรวด

## TL;DR
- 15 ต.ค. Perplexity open-source **SPACE** — sandbox แบบ Firecracker microVM ที่ Comet agent ใช้งานจริงมาตั้งแต่กรกฎาคม — ภายใต้ Apache 2.0 บน GitHub
- Spin-up VM ใหม่ **60 ms** (median) ต่อ session, มี snapshot/restore, และ credential ไม่เคยถูกเก็บไว้ใน sandbox — inject เฉพาะตอนใช้ แล้วหายไป
- Perplexity report ว่า red team ยิง 118 escape attempt ด้วย 9 frontier model แล้วไม่มีตัวไหนหลุดถึง host — **0/118** ขณะ sandbox อื่นที่ปิด code มี model หลุดอยู่
- CoreWeave, Akamai, Crusoe signed on พร้อมเสิร์ฟ SPACE เป็น managed runtime ให้ลูกค้า — เท่ากับ sandbox ของ Perplexity เพิ่งกลายเป็น **de facto standard runtime** ที่ hyperscaler สามเจ้าแบกต่อ

## เกิดอะไรขึ้น

วันพุธที่ 15 ต.ค. Perplexity ปล่อย **SPACE** — codename ของ sandbox ที่รัน browser agent ใน Comet — ขึ้น GitHub ภายใต้ Apache 2.0 พร้อม arch doc ยาวและสถิติ production ที่ไม่ค่อยเห็นจาก sandbox vendor ด้วยกัน. SPACE ไม่ใช่ project ใหม่ — Perplexity เขียนไว้ตรง ๆ ว่าเริ่มใช้มันแทน commercial sandbox เจ้าหนึ่งตั้งแต่เดือนกรกฎาคม และตอนนี้ handle **"millions of sandbox creations per day"** ใน Comet traffic จริง เท่ากับ open-source ชิ้นนี้ไม่ใช่ reference impl แต่คือ runtime ที่ battle-tested แล้ว

ตัว architecture ใช้ **Firecracker microVM** — virtualization layer ที่ AWS สร้างมารัน Lambda — ไม่ใช่ container หรือ gVisor. Perplexity โฆษณาเลขที่ชัดเจน: median spin-up ลดจาก 185 ms → **~60 ms** หลัง switch, แต่ละ session มี snapshot/restore ของทั้ง VM state (page cache, DOM, cookie), credential ของ user ถูก inject ลงไปเฉพาะตอนที่ tool call ต้องใช้ แล้วไม่เคยถูก persist ไว้ใน VM นั้น — คือ pattern ที่ copy ตรงจาก serverless security ของ AWS มาเป็น agent runtime

Security claim ที่น่าดึงดูดที่สุด: Perplexity ให้ red-team ยิง escape attempt 118 ครั้งผ่าน 9 frontier model (ชื่อ model ไม่เปิด แต่หมายถึง Claude/GPT/Gemini/Grok class). **ไม่มี model ไหนหลุดจาก VM ถึง host เลย** ขณะ sandbox ปิดเจ้าอื่นที่เอามาเทียบมี model หลุด. Perplexity เขียนไว้ให้ fair ว่า "red-teamer บางคนเจอวิธี route network restriction รอบ ๆ" — คือหลุด policy layer ไม่ใช่ VM boundary — ซึ่งแยก threat model ให้ชัดกว่า vendor สี่ส่วนใหญ่

และ 3 cloud: **CoreWeave, Akamai, Crusoe** ประกาศจะเสิร์ฟ SPACE เป็น managed offering ให้ลูกค้าเลย — ไม่ใช่แค่ host repo. Semafor report ว่า CoreWeave กับ Akamai มี workload production รัน SPACE แล้ว. financial term ไม่เปิด — น่าจะคล้าย AWS/Firecracker ที่ Perplexity ปล่อย free-license เพื่อให้ ecosystem รับมันเป็น default

## ทำไมสำคัญ

Pattern ของสัปดาห์นี้ตรงกันเลยกับ NVIDIA ที่เพิ่งเปิด **OpenShell** sandbox ของตัวเอง เดือนก่อน — agent sandbox กำลังกลายเป็น **commodity layer ที่ไม่มีใครอยากขายมัน** คือทุก lab อยากให้ sandbox ของตัวเองเป็น standard ของอุตสาหกรรม เพราะเลเยอร์ที่ขายได้คือ model + agent product ไม่ใช่ VM runtime. การที่ Perplexity เปิด SPACE แบบ Apache 2.0 แล้วมี 3 cloud วิ่งเข้ามาเป็น distribution partner ภายในวันเดียว คือการ **lock-in standard แบบที่ Docker ทำเมื่อสิบปีก่อน** — ใครที่สร้าง agent runtime ตอนนี้ default จะเลือก SPACE แทนที่จะ build เอง เพราะ Firecracker + production telemetry ของ Perplexity ยากที่ startup จะ reproduce

เลเยอร์ที่ลึกกว่านั้นคือ **sandbox คือจุดที่ agent governance จริงเกิดขึ้น** — ไม่ใช่ที่ prompt layer. Credential injection, network policy, snapshot ของ action ล่าสุด — ทั้งหมดอยู่ใน runtime boundary ไม่ใช่ใน system prompt. ถ้า Enterprise security team ยัง skeptic agent (ซึ่งควร) sandbox ที่ open-source + audit ได้ + มี production record 3 เดือน จะเป็นจุด convince CISO ที่หนักกว่า vendor claim มาก — และตอนนี้ที่ wiring ของ CERT-In India report ปัญหา agent breach สดใหม่ ตลาด enterprise จะอยากได้ sandbox ที่เลขหลุด = 0 โชว์ให้เห็น

## มุม AI Agent Platform

สำหรับ **Builders** (framework, agent runtime, orchestration): ถ้าคุณกำลัง roll out agent ที่รัน tool call จริงบน browser หรือ shell การ build sandbox เองคือ **ของเสียเงิน** แล้ว — SPACE + Firecracker + 3 cloud partner คือ reference stack ที่ battle-tested, open source, และฟรี. งานที่ควรโฟกัสคือ layer เหนือ sandbox: tool catalog, policy engine, audit log, agent identity (ซึ่ง ServiceNow Passport + Copilot agent account กำลังเล่น). ส่วน **Users / Business** ที่กำลัง deploy agent ใน workflow: ถาม vendor ตรง ๆ ว่า sandbox อะไร, isolated ขนาดไหน, credential handle ยังไง — ถ้าตอบไม่ได้หรือตอบว่า "container" คือสัญญาณ raw. ส่วน **Ecosystem**: Modal, E2B, Daytona และ sandbox vendor อื่น ๆ มี 2 ทางเลือก — รีบ differentiate ขึ้นไปที่ layer tool/orchestration, หรือ embrace SPACE แล้วขายเลเยอร์เหนือมัน. การเป็น "Firecracker reseller" คงไม่ยั่งยืน

## Sources
- [Perplexity Open-Sources SPACE, Says Zero Escapes in 118 Tries (aiweekly)](https://aiweekly.co/alerts/perplexity-open-sources-space-says-zero-escapes-in-118-tries)
- [Perplexity open sources SPACE, its sandbox for AI agents (Crypto Briefing)](https://cryptobriefing.com/perplexity-open-sources-space-agent-sandbox/)
- [Perplexity open-sources SPACE: VM sandbox with snapshots for agents (ToolNavs)](https://toolnavs.com/article/2599-perplexity-open-sources-space-a-vm-sandbox-with-snapshots-for-agents)

---

## Audio script
วันนี้มีเรื่องที่คนทำ agent ควรฟัง — Perplexity เพิ่งเปิดซอร์ส SPACE sandbox ที่เขาใช้ใน Comet มาตั้งแต่กรกฎาคม ขึ้น GitHub แบบ Apache 2.0 แล้วเลขที่โชว์มันดุมาก. SPACE สร้าง VM ใหม่ใน 60 มิลลิวินาที, เก็บ snapshot ของทั้ง state ได้, และ credential ของ user ไม่เคยถูกเก็บไว้ใน sandbox — inject เฉพาะตอนใช้แล้วหายไป. ที่สำคัญกว่านั้น red team ยิง escape attempt 118 ครั้งผ่าน 9 frontier model แล้วไม่มีตัวไหนหลุดจาก VM ไปถึง host เลย ขณะ sandbox ปิดเจ้าอื่นมี model หลุด. และ CoreWeave, Akamai, Crusoe ประกาศจะเสิร์ฟ SPACE เป็น managed service ให้ลูกค้า — เท่ากับ sandbox ของ Perplexity กลายเป็น de facto standard ภายในวันเดียว. บทเรียนคือ sandbox กำลังกลายเป็น commodity layer เหมือน Docker เมื่อสิบปีก่อน — ไม่มีใครอยากขายมัน ทุกคนอยากให้ของตัวเองเป็น standard. ถ้าคุณสร้าง agent runtime อยู่ การ build sandbox เองคือของเสียเงิน. และถ้าคุณใช้ agent ใน business workflow ให้ถาม vendor ว่า sandbox อะไร isolated ขนาดไหน ถ้าตอบว่าแค่ container คือสัญญาณที่ควร pause.
