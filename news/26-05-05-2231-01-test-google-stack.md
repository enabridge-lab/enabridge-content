---
date: 2026-05-05
slug: test-google-stack-migration
topic: agentic-ai
reading_time_min: 1
sources: 0
image_prompt: A bold cream sans-serif wordmark "TEST" sits centered on a deep navy background, with the words "GOOGLE STACK" stacked below in slate blue smaller caps. In the upper-right corner, a large coral stencil-style label reads "NANO BANANA". A small pale-yellow footer reads "26-05-05-2231". Abstract geometric shapes — interlocking flat hexagons in slate blue and coral — radiate outward from the wordmark, suggesting a network or pipeline activating. Editorial illustration, flat geometric shapes with subtle gradients, slate-blue + coral + cream palette on deep navy, dramatic side-lighting from the wordmark, 1:1 hero composition optimized to remain legible at 200px thumbnail.
image: images/26-05-05-2231-01-test-google-stack.png
---

# Test brief — Google stack migration end-to-end

## TL;DR
- Pipeline test สำหรับ migration PR #22: Gemini Nano Banana Pro (image) + Google Cloud TTS Chirp 3 HD voice Achernar (TTS)
- ถ้า GHA รันเสร็จ + Telegram preview ส่ง MP3 + image ที่ render คำว่า TEST / GOOGLE STACK / NANO BANANA แสดงว่า migration ใช้ได้จริง
- หลัง confirm: close test PR + delete `daily/26-05-05-2231` branch + merge migration PR #22

## เกิดอะไรขึ้น
นี่คือ throwaway brief เพื่อ trigger workflow `daily-branch-build.yml` บน branch ที่ base on `migrate/google-stack` — ไม่ใช่ daily content จริง

## Sources
- N/A — test run ของ migration PR

---

## Audio script
นี่คือ test run ของ Google stack ใหม่ครับ Yoh เป็นการทดสอบ pipeline สอง stack — Gemini Nano Banana Pro สำหรับ image generation และ Google Cloud Text-to-Speech Chirp 3 HD voice Achernar สำหรับเสียงไทย ถ้าคุณกำลังฟังเสียงนี้อยู่ใน Telegram แสดงว่า workflow ใหม่ทำงานครบ pipeline ภาพ hero ของ test brief นี้กำลัง render คำว่า TEST GOOGLE STACK และ NANO BANANA ซึ่งเป็น capability ที่ stack เดิมของ DALL-E ทำไม่ได้ ถ้าทุกอย่างดู OK เรา merge migration PR เข้า main ได้เลยครับ
