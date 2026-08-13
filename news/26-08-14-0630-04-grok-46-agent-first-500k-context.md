---
date: 2026-08-14
slug: grok-46-agent-first-500k-context
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  Editorial isometric illustration of a runner-shaped robotic silhouette in a
  long marathon lane; overhead a giant scoreboard reads "AAII 61 — TIED GPT-5.6
  SOL". At the lane markers three price tags float — "$2/M INPUT", "$6/M OUTPUT",
  "500K CONTEXT". A Grok-x logo cheers from a starting block at bottom right,
  Cursor + Vercel + Cloudflare wordmarks line the fence. High contrast, 1:1
  aspect, no real human faces, editorial magazine style.
image: images/26-08-14-0630-04-grok-46-agent-first-500k-context.png
---

# xAI ปล่อย Grok 4.6 — 500K context, ราคา $2/M, เจาะตลาด long-running agent ตรง

## TL;DR
- xAI เปิดตัว **Grok 4.6** วันที่ 12 สิงหาคม 2026 — flagship model ปรับสำหรับ **long-running agent + coding** โดยเฉพาะ
- Context window **500,000 tokens**, pricing **$2/M input + $6/M output** — ราคาต่ำกว่า Claude Sonnet 5 (ที่จะขึ้นเป็น $3/M) และ GPT-5.6 Sol Max
- Artificial Analysis Intelligence Index ได้ **61 คะแนน** ตีเสมอ GPT-5.6 Sol Max ขึ้นจาก Grok 4.5 5 คะแนน — พร้อม launch ใน Cursor, Grok Build, OpenRouter, Vercel, Cloudflare วันเดียวกัน

## เกิดอะไรขึ้น
วันที่ 12 สิงหาคม 2026 xAI ปล่อย Grok 4.6 ผ่าน blog x.ai/news/grok-4-6 พร้อมกัน sync launch กับ Cursor, Grok Build, API และ third-party partners ที่ระดับ tier บนคือ OpenRouter, Vercel, และ Cloudflare — model ใหม่ถูก positioning ตั้งแต่ headline ว่า "built for long-running agents and more ambitious interactive and visual work"

ตัวเลขที่ xAI โชว์: 500,000 tokens context (ใหญ่กว่า Claude Sonnet 5 ที่ 200K และ GPT-5.6 Sol ที่ 400K), และ Artificial Analysis Intelligence Index ที่ 61 คะแนน ตีเสมอ GPT-5.6 Sol Max และแซง Kimi K3 — ขึ้นจาก Grok 4.5 ที่ 56 คะแนน ในเวลา 5 สัปดาห์

Pricing tier เริ่มที่ **$2 per million input tokens และ $6 per million output tokens** ในตัว standard และ 2 เท่าในตัว fast — เทียบกับ Claude Sonnet 5 ที่จะขึ้นจาก $2 → $3/M input วันที่ 31 สิงหาคม และ GPT-5.6 Sol Max ที่ $2.50/M — Grok 4.6 เป็นตัวถูกที่สุดใน tier "reasoning + agentic" ณ วันเปิดตัว

xAI แจกเครดิตพิเศษให้ dev — double usage ฟรีใน Grok Build กับ Cursor สัปดาห์แรก เพื่อดัน adoption ให้เข้า workflow ก่อน model รอบต่อไป

## ทำไมสำคัญ
สามเดือนที่แล้ว Grok ยังถูกมองเป็น "chatbot สำหรับคนตาม Elon ในเรื่อง X.com" — วันนี้ Grok 4.6 กลายเป็น frontier model ตัวหนึ่งใน 3 อันดับแรกของ Artificial Analysis Intelligence Index และเปิดตัวใน Cursor + Vercel วันแรกที่ launch ระดับ integration ที่ Anthropic กับ OpenAI ก็ต้องใช้เวลาหลายเดือนกว่าจะได้เข้า Cursor ตอนแรก

Pattern ที่น่าสนใจ: xAI เลือกเน้น "long-running agent" ในโฆษณา — ไม่ใช่ "smart chat" ไม่ใช่ "reasoning" — เป็นการ signal ว่า xAI มองว่าตลาด model ปีนี้ไม่ได้แข่งกันด้วย benchmark เดี่ยว แต่แข่งด้วย session ยาว, tool use loop, และ context window ที่พอกับ code repo หรือ document set จริง

Signal ต่อจากนี้: (1) Anthropic ที่ขึ้นราคา Sonnet 5 เป็น $3/M สิ้นเดือน อาจได้รับ pressure ให้ทบทวน — xAI cutting under และมี compute อีก 200MW จาก dealship กับ Volta + SpaceX (2) Cursor และ Windsurf ตอนนี้เป็น battleground หลักของ model vendor — ใครขึ้น default ตัวไหน จะเปลี่ยน token spend เป็นพันล้านต่อปี (3) OpenRouter ที่รวม 40+ model จะเป็น winner ระหว่างสงคราม pricing เพราะ dev อยาก switch เร็วโดยไม่ต้องเขียน integration ใหม่

## มุม AI Agent Platform
**Builders**: ถ้า agent ของคุณต้อง run long horizon (multi-hour task, deep research, code refactor ทั้ง repo) — Grok 4.6 เป็นตัวที่ต้องทดสอบเทียบกับ Claude ทันที ไม่ใช่แค่ price/token แต่รวม tool use latency, structured output stability, และ context degradation ใน context window ยาว ที่ผ่านมา Grok มีปัญหาเรื่อง output determinism ที่ agent ต้องพึ่งพา — ต้อง evaluate จริงจัง อย่าเชื่อ benchmark เดี่ยว

**Users / business**: อย่ารีบเปลี่ยนไป Grok เพียงเพราะราคาต่ำ — ตัวแปรจริงคือ enterprise procurement (data residency, indemnity clause, uptime SLA) ซึ่ง xAI ยังตามหลัง Anthropic กับ OpenAI แต่ควรใส่ Grok ในการ RFP รอบต่อไปเป็น pressure lever ต่อ vendor ปัจจุบัน

**Ecosystem**: Grok 4.6 เปิดตัวใน Cursor + Vercel วันแรก = signal ว่า xAI ยอมจ่ายเงินก้อนใหญ่ให้ platform tier บนเพื่อขึ้น default ราคาถูก + integration พร้อม = platform (Cursor, Vercel, Cloudflare) มี leverage สูงขึ้นในการ negotiate revenue share และเลือก model default ในปีนี้จะเป็นสงครามที่หนักกว่าปีที่แล้วมาก

## Sources
- [SpaceXAI Releases Grok 4.6: A 500K-Context Frontier Model Tuned for Long-Running Agents (MarkTechPost)](https://www.marktechpost.com/2026/08/12/spacexai-releases-grok-4-6/)
- [SpaceXAI Launches Grok 4.6 for Long-Running Agents (Unite.AI)](https://www.unite.ai/spacexai-launches-grok-4-6-for-long-running-agents/)
- [SpaceXAI debuts Grok 4.6, matching GPT-5.6 Sol on Artificial Analysis (VentureBeat)](https://venturebeat.com/technology/spacexai-debuts-grok-4-6-overtaking-kimi-k3s-performance-and-matching-gpt-5-6-sol-for-worlds-third-best-on-artificial-analysis)

---

## Audio script
วันที่ 12 สิงหาคม xAI ปล่อย Grok 4.6 พร้อม launch ใน Cursor, Grok Build, OpenRouter, Vercel และ Cloudflare วันเดียวกัน model ใหม่ถูก positioning ตั้งแต่ headline ว่าสร้างเพื่อ long-running agent และงาน coding

ตัวเลขที่ xAI โชว์ คือ context window 500,000 token ใหญ่กว่า Claude Sonnet 5 กับ GPT-5.6 Sol และ Artificial Analysis Intelligence Index ที่ 61 คะแนน ตีเสมอ GPT-5.6 Sol Max ขึ้นจาก Grok 4.5 ห้าคะแนนในเวลา 5 สัปดาห์ pricing เริ่มที่ 2 ดอลลาร์ต่อล้าน input และ 6 ดอลลาร์ต่อล้าน output ถูกกว่า Claude Sonnet 5 ที่จะขึ้นเป็น 3 ดอลลาร์วันที่ 31 สิงหาคมและถูกกว่า GPT-5.6 Sol Max

Pattern ที่น่าสนใจคือ xAI เลือกเน้น long-running agent ในการโฆษณา ไม่ใช่ smart chat หรือ reasoning เป็นการ signal ว่าตลาด model ปีนี้ไม่ได้แข่งกันด้วย benchmark เดี่ยว แต่แข่งด้วย session ยาว tool use loop และ context window ที่พอกับ code repo หรือเอกสารจริง

สำหรับคนที่กำลังสร้าง agent ที่ต้อง run long horizon แนะนำให้ทดสอบ Grok 4.6 เทียบกับ Claude ทันที ไม่ใช่แค่ราคาต่อ token แต่รวม tool use latency กับ output determinism ในการรัน tool call หลายรอบ ที่ผ่านมา Grok มีปัญหาเรื่องความคงที่ของ output ที่ agent ต้องพึ่งพา อย่าเชื่อ benchmark เดี่ยว ต้องทดลองบน workload จริงของคุณครับ
