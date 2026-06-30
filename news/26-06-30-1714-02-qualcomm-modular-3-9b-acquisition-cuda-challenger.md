---
date: 2026-06-30
slug: qualcomm-modular-3-9b-acquisition-cuda-challenger
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial illustration of a giant green CUDA fortress wall in the center
  being attacked by a bright orange wrecking ball labeled "MODULAR" swinging on
  a Qualcomm-blue crane. Behind the crane stands a hardware factory skyline
  with chips from AMD, Intel, Apple, Qualcomm glowing in a row. A bold floating
  headline reads "QUALCOMM × MODULAR" with stacked numbers "$3.9B DEAL" and
  "$14B FULL STACK" and "$255B INFERENCE MARKET". Small silhouette of LLVM
  creator at the crane controls (back view only, no face). Cinematic action
  composition, palette deep navy + Qualcomm blue + alert orange + green
  fortress, ultra-sharp text rendering for 200px thumbnail readability, 1:1
  aspect ratio, tech-magazine cover style, no real human faces.
image: images/26-06-30-1714-02-qualcomm-modular-3-9b-acquisition-cuda-challenger.png
---

# Qualcomm ทุ่ม $3.9B ซื้อ Modular ของ Chris Lattner — เปิดศึก CUDA โดยตรง พร้อม Tenstorrent รวมเป็น "$14B full-stack" ชน NVIDIA

## TL;DR
- 24 มิ.ย. — Qualcomm ประกาศซื้อ **Modular** (สตาร์ตอัพของ Chris Lattner ผู้สร้าง LLVM/Swift) ด้วย all-stock deal ~**$3.9B**; Modular เป็นเจ้าของ **Mojo programming language** และ **MAX inference engine** ที่ทำให้ AI code วิ่งบน NVIDIA, AMD, Intel, Apple Silicon, Qualcomm hardware ได้ไม่ต้อง rewrite ทีละ chip
- บวกกับการ approach ซื้อ **Tenstorrent ~$8–10B** ที่รั่วก่อนหน้านี้ Qualcomm กำลัง assemble **full-stack ~$14B alternative** สำหรับ AI inference market ที่จะแตะ **$255B** ภายในปลายทศวรรษ — เป็น direct attack บน CUDA moat ของ NVIDIA ที่ครองนักพัฒนา 4 ล้านคน
- ปิดดีลครึ่งหลัง 2026 — Software acquisition ครั้งใหญ่สุดในประวัติ Qualcomm และ signal ชัดว่า **chip war 2026-2027 จะ shift จาก silicon ไป compiler/runtime layer**

## เกิดอะไรขึ้น

24 มิถุนายน 2026 — Qualcomm ประกาศซื้อ **Modular** ในดีล all-stock มูลค่าใกล้เคียง **$3.9B** (รายงานหลายฉบับใช้ตัวเลข $3.92B). ผู้ก่อตั้ง Modular คือ **Chris Lattner** อดีต Apple/Google/SiFive ผู้สร้าง LLVM compiler infrastructure (ที่อยู่ใต้ Swift, Rust, ส่วนหนึ่งของ Clang) — และทีมที่ใช้ infra นี้สร้าง 2 ผลิตภัณฑ์ที่ทำให้ดีลนี้ใหญ่: **Mojo** — ภาษาโปรแกรม superset ของ Python ที่ compile ลง machine code วิ่ง 35,000x เร็วกว่า Python ในบาง benchmark; และ **MAX** — inference engine ที่รัน AI model บน NVIDIA, AMD, Intel, Apple Silicon, Qualcomm ได้ด้วย API เดียว

ดีลนี้ Qualcomm ประกาศ "เพื่อสร้าง software stack สำหรับ Qualcomm Cloud AI 100 + Qualcomm AI Engine ใน data center และ edge device" — แต่ทุก analyst ที่อ่านแถลงการณ์เข้าใจตรงกันว่านี่คือ **direct attack บน CUDA**. CUDA ของ NVIDIA เป็น proprietary software layer ที่ครอง 4 ล้านนักพัฒนาและล็อก enterprise เข้า GPU ของ NVIDIA มาเกือบสองทศวรรษ. Modular MAX คือ runtime ตัวเดียวที่ produce-grade เทียบเคียงได้ — และตอนนี้ Qualcomm ได้เป็นเจ้าของ

ที่ทำให้ดีลใหญ่ขึ้น — Bloomberg และ Reuters รั่วก่อนหน้านี้ว่า Qualcomm กำลังเจรจาซื้อ **Tenstorrent** ของ Jim Keller (อดีต Apple/AMD/Intel/Tesla chip architect) ในมูลค่า **$8-10B**. ถ้า Tenstorrent deal ปิดจริง — Qualcomm จะมี **full-stack ~$14B**: silicon (Tenstorrent's RISC-V AI chip + Qualcomm Cloud AI 100) + compiler/runtime (Modular MAX/Mojo) + ตลาด edge ที่ Qualcomm ครองอยู่ใน mobile/auto/IoT. CNBC อ้าง analyst หลายคนเรียกมันว่า "Qualcomm's bet ที่จะกลายเป็น NVIDIA ทางเลือก"

ตัวเลขที่เป็น scaffold ของดีล — inference market. McKinsey และ Bain ประเมินว่า AI inference workload (ที่แตกต่างจาก training) จะแตะ **$255B** ภายในปลาย 2020s — และไม่เหมือน training market ที่ NVIDIA ครอง 90% inference market กระจายกว่ามาก (workload latency-sensitive, edge-resident, vendor-diverse). นี่คือสมรภูมิที่ Qualcomm คิดว่าตัวเองชนะได้ — โดยเฉพาะถ้าได้ Modular มาเปิด software door ให้นักพัฒนา switch hardware ไม่ต้อง rewrite ทุก line

## ทำไมสำคัญ

**ดีลนี้ confirm กลายเป็น "software acquisition" — ไม่ใช่ hardware deal**. Qualcomm จ่าย $3.9B สำหรับบริษัทที่ revenue ปีล่าสุดไม่ถึง $50M และยังไม่มี large enterprise contract — แต่จ่ายเพราะ **moat ของ NVIDIA อยู่ที่ CUDA ไม่ใช่ที่ silicon**. NVIDIA H100/B200/Blackwell Ultra เก่งจริง — แต่ที่ทำให้ AMD MI300, Intel Gaudi 3, Apple M-series ขายไม่ออกใน data center ไม่ใช่เพราะ silicon แพ้ มันคือเพราะนักพัฒนาเขียน CUDA kernel แล้วไม่อยาก port. Modular แก้ exactly issue นี้ — และ Qualcomm รู้ว่าถ้าจะแข่ง NVIDIA ต้องตัด software layer ก่อน

POV ตรง — **Chris Lattner คือ "compiler whisperer" ที่ valuation $4B**. เขาเคยทำ LLVM ฟรีให้ทุกคนใช้ (ผม Apple จ่าย), ทำ Swift ฟรีให้ Apple ใช้, ทำ MLIR ฟรีให้ Google ใช้. Modular คือ first venture เขายอม keep IP — และตอนนี้ Qualcomm จ่าย $3.9B เพื่อ exclusive right. ถ้าใครเคยดูถูก Lattner เพราะ Modular ยังไม่ทำเงิน — เห็นชัดแล้วว่า strategic value ใน LLVM-class compiler ใหม่ มันไม่ใช่เรื่อง revenue ปัจจุบัน

ผลข้างเคียงที่จะกลับมาตี — **NVIDIA จะต้องตอบ**. คำตอบที่ logical ที่สุด: เปิด CUDA partial open-source, หรือซื้อ open-runtime ของตัวเอง (Jax/TVM/IREE, อาจะ vLLM). หรือถ้า extreme — NVIDIA จะ open CUDA ABI ให้ third-party chip implement ได้ (เหมือน Apple Silicon เปิด Vulkan layer). Move ของ Qualcomm บีบให้ NVIDIA ตัดสินใจในกรอบสั้น — และไม่ว่าตัดสินใจอะไร moat ของ CUDA จะรั่วเป็นครั้งแรกตั้งแต่ปี 2008

Pattern ใหญ่กว่า — **agentic AI ต้องการ inference layer ที่ vendor-neutral**. Agent framework ที่ทำงาน production scale (Cursor, Claude Code, Codex) ใช้ inference call หลายร้อยครั้งต่อ user session. ใน 12-18 เดือนข้างหน้า ทุก agent framework จะต้อง support **runtime portability** — ใช้ NVIDIA สำหรับ peak load + AMD/Qualcomm สำหรับ steady-state + Apple Silicon สำหรับ on-device. คนที่ provide layer นี้คือผู้ชนะของชั้น "inference middleware" และ Qualcomm กำลังจะเป็นนั้น

## มุม OpenBridge

ไม่ direct เกี่ยว — OpenBridge ไม่ได้ build silicon และ inference runtime. แต่ adjacent insight สำคัญสำหรับ product roadmap: **agent platform ของ OpenBridge ต้อง assume vendor-portable inference เป็น default ภายใน 12 เดือน**. ลูกค้า enterprise Thai ที่ build agent บน OpenBridge จะอยากเลือก inference provider ตาม cost/latency/data residency — และ Modular MAX (ที่จะกลายเป็น part ของ Qualcomm cloud) เป็น runtime ที่ต้อง integrate ทันที. Recommend: ทำ POC connecter "Modular MAX backend" + "Qualcomm Cloud AI 100" ภายใน Q3 — ก่อนคู่แข่ง

ที่อ้อมขึ้น — **timing window สำหรับ Thai sovereign AI**. NECTEC + AIS ที่กำลังคิด sovereign LLM infra ใน Thailand มี option ใหม่ — แทนที่จะซื้อ NVIDIA cluster ที่แพง + export-restricted สามารถ build บน Qualcomm + Modular stack ที่ portable + ไม่ติด US-China dual-use export rule เท่า NVIDIA. OpenBridge อยู่ในตำแหน่งดีที่จะเป็น **"sovereign inference router"** สำหรับ Thai enterprise — ถ้าทำ partnership Qualcomm SEA + ASEAN ภายในไตรมาสนี้

## Sources
- [Qualcomm Just Spent $4B to Break Nvidia's Software Lock — BERI](https://www.beri.net/article/qualcomm-modular-4b-acquisition-nvidia-cuda-lock-in-enterprise-ai-inference-2026)
- [Qualcomm inks deal for AI startup Modular — CNBC](https://www.cnbc.com/2026/06/24/qualcomm-ai-chip-modular-software.html)
- [Qualcomm's $3.9 billion purchase of Modular — Network World](https://www.networkworld.com/article/4189098/qualcomms-3-9-billion-purchase-of-modular-aims-to-change-the-data-center-dynamic.html)
- [Qualcomm agrees to acquire AI startup Modular — The Tech Portal](https://thetechportal.com/2026/06/24/qualcomm-agrees-to-acquire-ai-startup-modular-for-around-4bn/)
- [Qualcomm Acquires Modular for Nearly $4 Billion — Technobezz](https://www.technobezz.com/news/qualcomm-acquires-modular-for-nearly-4-billion-to-challenge-nvidias-cuda-dominance)

---

## Audio script

วันที่ยี่สิบสี่มิถุนายน Qualcomm ประกาศซื้อ Modular ในดีลสามจุดเก้าพันล้านดอลล่าร์. Modular คือบริษัทของ Chris Lattner ผู้สร้าง LLVM ซึ่งเป็น compiler infrastructure ที่อยู่ใต้ Swift และ Rust. Modular เป็นเจ้าของภาษา Mojo และ inference engine ชื่อ MAX ที่ทำให้ AI model วิ่งบน NVIDIA, AMD, Intel, Apple Silicon, Qualcomm ได้ด้วย API เดียว.

ทำไมดีลใหญ่ — เพราะ Qualcomm กำลังจะ assemble full stack สู้ NVIDIA. ก่อนหน้านี้รั่วว่า Qualcomm จะซื้อ Tenstorrent ของ Jim Keller อีกแปดถึงสิบพันล้าน. รวมแล้วประมาณสิบสี่พันล้านดอลล่าร์ — สำหรับชนเข้าตลาด inference ที่จะแตะสองร้อยห้าสิบห้าพันล้านดอลล่าร์.

POV ของผม — ดีลนี้คือ software acquisition ไม่ใช่ hardware deal. NVIDIA moat อยู่ที่ CUDA ไม่ใช่ที่ silicon. นักพัฒนาเขียน CUDA kernel แล้วไม่อยาก port. Modular แก้ปัญหานี้พอดี. ถ้า Qualcomm ทำ MAX เป็น runtime default ของ enterprise ได้ — moat ของ CUDA ที่อยู่มาตั้งแต่ปี 2008 จะรั่วเป็นครั้งแรก.

มุม OpenBridge — agent platform ของเราต้อง assume inference เป็น vendor-portable ภายในปีหน้า. ลูกค้า Thai bank จะอยากเลือก inference provider ตาม cost และ data residency. Modular MAX ต้อง integrate ภายในไตรมาสนี้ ก่อนคู่แข่ง.
