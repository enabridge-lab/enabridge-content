---
date: 2026-08-10
slug: cloudflare-kitesurf-wallets-agents-week
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  A stylized cloud gateway with two open doors; left door labeled "KITESURF"
  shows a lightweight kite icon and a numeric card "3-7x LESS MEMORY vs CHROMIUM";
  right door labeled "AGENT WALLETS" shows a coin stack with a badge
  "SPEND LIMIT: $50/DAY". Cloudflare logo overhead. Editorial isometric style,
  orange and white palette, 1:1 aspect, no real human faces.
image: images/26-08-11-0616-04-cloudflare-kitesurf-wallets-agents-week.png
---

# Cloudflare Agents Week ปล่อย Kitesurf browser + Wallets — internet ของ agent เริ่ม fork

## TL;DR
- Cloudflare ship Kitesurf — Rust/WASM browser engine ที่รันใน Workers V8 isolates, ใช้ CPU/memory น้อยกว่า Chromium 3-7x สำหรับ agent workload
- ประกอบใน 12 สัปดาห์จาก open-source parts: Blitz render, Firefox Stylo CSS parser, Boa JS engine — จะ open source ภายหลัง
- ควบคู่กับ Agent Wallets: ผู้ใช้เติม stablecoin เข้า account wallet แล้วมอบสิทธิ์ agent wallet ที่จำกัด allowance/merchant/max purchase — anomaly detection flag ให้คนอนุมัติ

## เกิดอะไรขึ้น
สัปดาห์แรกของสิงหาคม Cloudflare จัด Agents Week — และ product ที่ ship ในสัปดาห์นั้น 2 ตัวรวมกันน่ากลัวกว่าที่ทุกคนคาด Kitesurf เปิดตัว 6 สิงหาคม เป็น browser engine ที่**เขียนใหม่จากศูนย์ด้วย Rust แล้ว compile เป็น WebAssembly** รันในตัว V8 isolates เดียวกับ Cloudflare Workers ไม่ใช่ headless Chromium ที่กิน RAM 500MB ต่อ session แต่เป็น engine ~50-100MB ที่ optimize เพื่อ agent อ่านโครงสร้าง page และ take screenshot — ตัด tab, extension, pixel-perfect rendering, media codec ทิ้งหมด

ทีม Cloudflare สร้าง Kitesurf จบใน **12 สัปดาห์** ด้วยการ compose ของ open-source ที่มีอยู่แล้ว: Blitz สำหรับ rendering, Stylo (CSS parser ของ Firefox) และ Boa (JS engine เขียน Rust) ตอนนี้ให้ทดลองฟรีใน beta ผ่าน Browser Run แค่ใส่ `browser=kitesurf` เข้า endpoint เดิม — Cloudflare สัญญาว่าจะ open source ต่อ

Product ที่ทันน่าสนใจกว่าคือ Cloudflare Agent Wallets ที่ ship ในสัปดาห์เดียวกัน โครงสร้าง: มนุษย์ (owner) fund account wallet ด้วย USD-pegged stablecoin แล้วสร้าง agent wallet ที่มีขอบเขต — allowance (เช่น $50/วัน), approved merchant list (เฉพาะ Amazon/DoorDash/Uber), max purchase size ($20/รายการ) ถ้า agent ใช้เงินผิดปกติ (spending spike, merchant นอก list) system flag ให้ owner review ก่อน authorize ครั้งต่อไป

## ทำไมสำคัญ
Kitesurf + Wallets รวมกันคือ **agent-native web stack** ตัวแรกที่ครบวงจร — browsing + payment แยกจาก human infra ที่ built for consumer เห็นภาพชัดว่าอินเทอร์เน็ตกำลังจะ fork เป็น 2 stack: human-facing internet (Chromium, ApplePay/GooglePay, session cookie) และ agent-facing internet (Kitesurf, agent wallet, structured content APIs) — และ Cloudflare ที่ควบคุม 20% ของ traffic โลก positioning ตัวเองเป็น**เจ้าของ layer 3 ของ agent internet**

Signal เศรษฐกิจ: memory saving 3-7x ไม่ใช่แค่ประหยัด cost — มันเปิดให้ agent ที่ crawl web ในสเกลใหญ่ (millions of pages/day) เป็นไปได้ที่ price point ที่ startup ทำได้ เดิม Chromium ที่ browse 1M page ต้อง compute bill $10k-30k/เดือน Kitesurf ทำที่ระดับ $1-5k เท่านั้น — เปิดตลาด agent search, agent competitive intel, agent price monitoring ที่ก่อนหน้าไม่ economic

ประเด็น bigger picture: Wallets คือ commit ของ Cloudflare ที่จะทำ agent payment rail ตัวเอง แข่งกับ Stripe (Agent Toolkit), Visa (Intelligent Commerce), Mastercard (Agent Pay), Cloudflare/Coinbase x402 protocol Wallet ที่ Cloudflare push ใช้ stablecoin ไม่ใช่ credit card — chain กับ crypto rail ที่ settle ทันที ไม่มี chargeback บาย และ merchant ไม่ต้อง verify identity ของ agent เพราะ money settle upfront นี่คือ**การ challenge สถานะ quo ของ payment infrastructure**

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ agent product: ถ้า workload คุณเป็น web-browsing (research agent, competitive intel, deep search, price scraper) Kitesurf ลด infra cost 3-7x ทันทีโดยไม่ต้องเปลี่ยน code เยอะ — bindings เข้ากับ Playwright API เดิมได้ สำหรับ builder ที่ทำ commerce agent, Wallets เปิดทางให้ทดสอบ transactional agent ไม่ต้อง PCI compliance เพราะ Cloudflare เป็นคน handle เก็บ card off system

สำหรับ **users/business**: Cloudflare Agent Wallet ที่กำหนด allowance/merchant/max size คือ pattern ที่ CFO ในองค์กรจะยอมรับได้ — control ที่ CFO ต้องการอยู่ในระบบเลย ไม่ต้อง audit trail หลังบ้าน ตอนนี้ enterprise ที่จะ deploy agent ที่ใช้เงินจริงมี checklist ที่ปิดได้แล้ว สำหรับ **ecosystem/vendor**: Stripe, Visa, Mastercard ต้องดูว่า agent economy จะ settle บน stablecoin rail (Cloudflare/Coinbase) หรือ card rail (Stripe/Visa) เพราะ economics ต่างกันเยอะ — และ Cloudflare ที่เป็น distribution layer อยู่แล้ว มีข้อได้เปรียบ owning end-to-end pipeline ที่ payment company ไม่มี

## Sources
- [Introducing Kitesurf, an agent-first browser on Browser Run (Cloudflare Changelog)](https://developers.cloudflare.com/changelog/post/2026-08-06-kitesurf/)
- [Cloudflare launches Kitesurf, a browser built for AI agents (TechCrunch)](https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/)
- [Cloudflare Builds a Browser Only AI Agents Can Use (IBTimes UK)](https://www.ibtimes.co.uk/cloudflare-ai-browser-wallets-machine-commerce-1813230)

---

## Audio script
Cloudflare จัด Agents Week ครับ แล้ว 2 product ที่ ship ในสัปดาห์เดียวกันน่ากลัวกว่าที่คิด ตัวแรกคือ Kitesurf เป็น browser engine ที่เขียนใหม่จากศูนย์ด้วย Rust compile เป็น WebAssembly รันใน V8 isolates ของ Cloudflare Workers ไม่ใช่ Chromium ที่กิน RAM 500MB ต่อ session ใช้ CPU กับ memory น้อยกว่า Chromium 3 ถึง 7 เท่า Cloudflare สร้างเสร็จใน 12 สัปดาห์เท่านั้น ด้วยการ compose ของ open-source Blitz Stylo Boa อีกตัวคือ Agent Wallets มนุษย์เติม stablecoin เข้า account wallet แล้วสร้าง agent wallet ที่มีขอบเขต allowance ต่อวัน merchant ที่ approve max ต่อรายการ ถ้าใช้ผิดปกติ system flag ให้ owner review ทำไมสำคัญ รวมกันสองตัวนี้คือ agent-native web stack ครบวงจรตัวแรก — browsing กับ payment แยกจาก infra ของมนุษย์ อินเทอร์เน็ตกำลัง fork เป็น 2 stack และ Cloudflare ที่ควบคุม 20% ของ traffic โลก positioning ตัวเองเป็นเจ้าของ layer 3 ของ agent internet สำหรับคนทำ agent ที่ต้อง browse web infra cost ลด 3-7 เท่าทันทีที่เปลี่ยน browser ไม่ต้องแก้ code เยอะ
