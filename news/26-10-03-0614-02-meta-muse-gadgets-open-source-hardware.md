---
date: 2026-10-02
slug: meta-muse-gadgets-open-source-hardware
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial isometric illustration of a small Raspberry Pi 5 and an ESP32
  microchip wired to a glowing orb labeled "MUSE". A tiny USB-C dongle
  marked "HOME LINK" plugs into a cartoon router emitting Wi-Fi waves.
  "5,000 UNITS" and "APACHE 2.0" badges float above like neon signs.
  Scattered DIY components — breadboard, jumper wires, button, speaker —
  spill across the frame. Cinematic indigo and electric-green palette,
  sharp contrast for 200px thumbnails, bold text rendering, no real human
  faces, 1:1 aspect. Style of a Wired magazine cover story.
image: images/26-10-03-0614-02-meta-muse-gadgets-open-source-hardware.png
---

# Meta เปิด Muse Gadgets open source — ESP32 firmware + Linux SDK + 5,000 USB-C dongle แจกฟรี, บุก home layer

## TL;DR
- 2 ต.ค. Meta open-source **ESP32 firmware + Linux SDK** ให้ developer เอา Muse AI agent ไปใส่ hardware ของตัวเอง — Raspberry Pi 5, E Ink display, HDMI dongle ทำได้ทั้งนั้น
- เปิดตัว **Muse Home Link** USB-C dongle **5,000 units แจกฟรีให้ US Muse subscriber** จนของหมด — เชื่อม Muse เข้า home network + smart home gear
- Repository `facebookincubator/muse-gadget-sdk` licensed Apache 2.0 — Meta เลือก play เป็น **ambient layer ของ consumer AI** ตรงข้าม OpenAI ที่เล่น productivity

## เกิดอะไรขึ้น
วันที่ 2 ตุลาคม Nat Friedman — ที่ Zuckerberg ดึงเข้าคุม Meta Superintelligence Labs — ประกาศ **Muse Gadgets**: ชุด firmware + SDK ที่ให้ developer เอา Muse AI agent ไปวางบน hardware ของตัวเอง. ที่ Repository `facebookincubator/muse-gadget-sdk` บน GitHub มี **ESP32 Device SDK** สำหรับ off-the-shelf board (ต่อ screen, mic, speaker, sensor อะไรก็ได้) และ **Linux Device SDK** สำหรับ Raspberry Pi 5 หรือ Linux box อะไรก็ได้. License Apache 2.0 เผื่อ commercial use ได้เลย.

พร้อมกันนั้น Meta ประกาศ **Muse Home Link** — USB-C dongle ที่ชาร์จไฟตัวเอง, แจกฟรีให้ US Muse subscriber ชุดแรก 5,000 ตัว "while supplies last". ตัวมันเสียบเข้า home network แล้วทำให้ Muse คุยกับ smart TV, speaker, สายพาน IoT ที่ expose local web interface ได้ทันที — ไม่ต้อง onboard แยกต่อ device. 5,000 ตัวแรกน้อยพอให้ Meta เรียกว่า "launch batch" ไม่ใช่ shipping หลัก — เป็น beta hardware ที่ developer community จะเอาไป hack ก่อนที่ Meta จะ mass produce.

Context ของ announcement นี้สำคัญ. Zuckerberg เพิ่งพูดเมื่อเดือนก่อนว่า **"ภายใน 5 ปีทุกคนจะมี personal AI agent"** — และวันนี้เขาเริ่มเปิดกฎให้ community สร้าง gadget ให้คนทั่วไปโดยไม่ต้องรอ Meta ship ของเองทีละชุด. ESP32 เป็น chip ยอดนิยม DIY ที่ hobbyist/startup ใช้สร้าง smart device ขายเองได้เลย — ราคาต่อยูนิตต่ำกว่า $5 — Meta จึง pattern เหมือน Apple MFi แต่ open กว่า.

## ทำไมสำคัญ
Signal แรกคือ **Meta เลือก distribution layer ตรงข้ามกับ OpenAI**. OpenAI ที่เพิ่งเปิด dots + ChatGPT Space ที่ DevDay มุ่งเป้าไปที่ productivity surface (laptop, Slack, Teams, voice call). Meta Muse เลือก **home + ambient surface** — ของที่เสียบไว้บน TV, ตั้งไว้ที่ครัว, เสียบใน router. ตลาดนี้ Amazon กับ Google ลงทุน Alexa + Nest ไปแสนล้านดอลลาร์ตั้งแต่ปี 2014 แต่ยังไม่มีใครได้ "always-on home AI" ที่ทำได้มากกว่าเปิดไฟปิดแอร์. Meta วาง bet ว่าถ้าปล่อย hardware spec ให้ community สร้างเองได้ hardware diversity จะเกิดเร็วกว่าที่ Amazon กับ Google ทำได้ด้วยทีมฮาร์ดแวร์ของตัวเอง.

Angle ที่คม: **Apache 2.0 + free dongle = anti-Alexa play**. Amazon Alexa Skills ต้อง onboard ผ่าน developer portal, Google Nest Hub ต้องซื้อฮาร์ดแวร์ Google ทำ. Meta ตัด friction นี้ทิ้งหมด — ใครมี Pi กับ ESP32 + Muse subscription สร้าง own device ได้วันนี้. ถ้าภายในปีหน้ามี gadget 100,000 ตัว running Muse SDK ทั่ว US Meta จะมี **data flywheel ที่ Amazon ไม่มี** — เพราะ Alexa เก็บ voice command แต่ Muse เก็บ full context ของ device + sensor + action.

ถึงจุดนี้ Meta Muse เริ่มเป็น platform ที่ serious. 5,000 ตัวแรก sell out แน่ (ของฟรี + hobbyist community แห่กันไป) — แล้วเดือน 2-3 จะเห็น third-party gadget ขายใน Amazon ที่ bundle Muse. ความเสี่ยงมีสองอย่าง: (1) privacy backlash ถ้า Muse Home Link ถูก hack หรือ leak audio, (2) regulatory scrutiny ตามที่ FTC ส่อว่าจะดูเรื่อง Big Tech + home device. แต่ open source + free hardware เป็น narrative ที่ relationship PR ดีกว่า closed ecosystem.

## มุม AI Agent Platform
**Builders** — ถ้าคุณสร้าง agent framework สำหรับ consumer หรือ smart home ยาน Muse Gadget SDK เป็น reference ที่ควร study ทันที. Pattern **ESP32 firmware + local actuator + cloud reasoning** จะเป็น stack ที่ IoT startup หลายพันเจ้าใช้ภายในปีหน้า. ถ้า framework ของคุณไม่ support edge device + sync กับ cloud agent ตอนนี้ คุณพลาด market segment ใหญ่. **Users/Business** — SMB ที่ขาย smart building, hospitality, retail hardware ควร pilot Muse SDK แทนที่จะรอ Alexa for Business หรือ Google Nest Business. Deployment speed สำคัญกว่า brand ตอนนี้ — ลูกค้าสนใจผลลัพธ์ (occupancy automation, voice ordering, assisted booking) ไม่ใช่ชื่อ brand. **Ecosystem** — Amazon Alexa + Google Nest เจอคู่แข่งที่ไม่ได้แข่งผ่าน hardware ของตัวเอง แต่แข่งผ่าน developer army. Apple HomeKit position แข็งขึ้นเพราะ Apple มี distribution advantage (iPhone) แต่ Siri still trailing. Startup voice stack (Picovoice, Sonos Era) ต้องเลือกจะเป็น "Muse-compatible layer" หรือ "alternative stack" — ทางเลือก alternative ยากขึ้น 10 เท่าตั้งแต่ประกาศนี้.

## Sources
- [Meta Open-Sources Muse Gadget SDKs for DIY AI Hardware Devices — Unite.AI](https://www.unite.ai/meta-open-sources-muse-gadget-sdks-for-diy-ai-hardware-devices/)
- [Meta's Muse Lets You Build Your Own AI Gadgets — iPhoneInCanada](https://www.iphoneincanada.ca/2026/10/02/metas-muse-lets-you-build-your-own-ai-gadgets/)
- [Techmeme: Meta announces Muse Gadgets, providing an open source ESP32 microchip firmware and a Linux SDK (Engadget)](https://www.techmeme.com/261002/p24)
- [Meta Muse Gadgets Opens the AI Agent to DIY Hardware, With a Free Home Link for US Subscribers — Tech My Money](https://techmymoney.com/2026/10/02/meta-muse-gadgets-opens-the-ai-agent-to-diy-hardware-with-a-free-home-link-for-us-subscribers/)

---

## Audio script
ข่าวใหญ่สนาม consumer AI วันนี้ครับ. 2 ตุลาคม Nat Friedman จาก Meta Superintelligence Labs ประกาศ Muse Gadgets — ชุด open source firmware กับ SDK ที่ให้ developer เอา Muse AI agent ไปวางบน hardware ของตัวเอง. Repository ที่ facebookincubator/muse-gadget-sdk บน GitHub มี ESP32 Device SDK สำหรับ board ราคาถูกต่ำกว่า 5 ดอลลาร์ และ Linux Device SDK สำหรับ Raspberry Pi 5. ทั้งหมด license Apache 2.0 เอาไปใช้ commercial ได้เลย. พร้อมกัน Meta แจก Muse Home Link USB-C dongle ฟรี 5,000 ตัวให้ US subscriber ชุดแรก — ตัวมันเสียบเข้า home network แล้วให้ Muse คุยกับ smart TV, speaker, IoT ได้ทันที. Signal สำคัญคือ Meta เลือก distribution layer ตรงข้ามกับ OpenAI. OpenAI ยัด dots เข้า productivity surface — laptop, Slack, Teams. Meta เลือก home กับ ambient surface — ของที่ตั้งบน TV, เสียบในครัว. ตลาดนี้ Amazon กับ Google ทุ่มเงินแสนล้านไปแล้วยังไม่ได้ always-on home AI. Meta วาง bet ว่า ถ้าปล่อย spec ให้ community สร้างเองได้ hardware diversity จะเกิดเร็วกว่า. Angle ที่คมคือ Apache 2.0 กับ free dongle = anti-Alexa play. Amazon ต้อง onboard ผ่าน developer portal Google ต้องซื้อ Nest Hub. Meta ตัด friction ทิ้งหมด — ใครมี Pi กับ ESP32 สร้าง own device ได้วันนี้. ภายในปีหน้า Meta จะมี data flywheel ที่ Amazon ไม่มี เพราะ Muse เก็บ full context ของ device + sensor + action. Impact ต่อ builder ชัดเจน. Pattern ESP32 firmware + local actuator + cloud reasoning จะเป็น stack ที่ IoT startup หลายพันเจ้าใช้ภายในปีหน้าครับ.
