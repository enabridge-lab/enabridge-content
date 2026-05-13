---
date: 2026-05-13
slug: judgment-labs-32m-agent-trajectory-eval-lightspeed
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: A glowing flowchart on a dark blue background showing a long winding "trajectory" path with branching decision nodes, tool-use icons, and memory bubbles. The path passes a magnifying glass that highlights tiny error glyphs hidden in mid-path. Above floats a bold typographic banner reading "JUDGMENT LABS — $32M". On one side a stylized Lightspeed Venture Partners logo rendered as a lightning bolt mark. No human faces. Editorial science-illustration style, cyan and orange accents, high contrast for thumbnail readability, isometric composition, 1:1.
image: images/26-05-14-0605-04-judgment-labs-32m-agent-trajectory-eval-lightspeed.png
---

# Judgment Labs ระดม $32M เพราะ "evaluation" คือคอขวดถัดไปของ agent ทุกตัว

## TL;DR
- Judgment Labs (12 พ.ค.) ปิด $32M รวม seed + Series A — Lightspeed Venture Partners ลง lead ทั้งสองรอบ, joined by Nova Global, Valor, Dynamic, SV Angel
- โฟกัส: evaluate long reasoning trajectory + tool use + memory ของ agent, แล้ว turn production data เป็น improvement loop (ไม่ใช่ chatbot-era evaluation แบบ single-input single-output)
- 3 founders อายุ 22–23 (Alex Shan ex-Stanford NLP, Andrew Li ex-TogetherAI, Joseph Camyre ex-Datadog) — สะท้อนว่า ops layer ของ agentic stack ยังเปิดให้ startup เข้าได้

## เกิดอะไรขึ้น

วันที่ 12 พ.ค. Judgment Labs ที่ตั้งใน SF announce $32M combined seed + Series A — Lightspeed ลง lead รอบแรกแล้ว double-down รอบสอง 6 เดือนต่อมา. Backers อื่นได้แก่ Nova Global, Valor Equity Partners, Dynamic, SV Angel. รอบนี้ valuation ไม่เปิดเผย แต่ Lightspeed signal ว่ารอบ Series A นี้ valuation เพิ่มจาก seed รอบที่แล้วอย่างมีนัยสำคัญ

ปัญหาที่ Judgment Labs แก้ฟังดูเทคนิคแต่กลาย critical. Evaluation เครื่องมือเก่าจากยุค chatbot สร้างขึ้นเพื่อ single input → single output — input prompt หนึ่ง output text หนึ่ง score หนึ่ง. แต่ "deep agent" (agent ที่ทำงานต่อเนื่องหลาย step, เรียก tool หลายตัว, มี memory) สร้าง "trajectory" — ลำดับยาวของ decision + tool call + memory write. เวลามัน fail ความผิดพลาดมัก subtle ที่ขั้นกลาง — final answer ดูถูก แต่ trajectory เอาไป production จะระเบิด. Judgment Labs build infra ที่ inspect trajectory, label patterns ของ failure, แล้ว feed back เข้า fine-tune หรือ prompt iteration loop

POV ของ founder ที่ public มา: Alex Shan (CEO, 22) เคย AI researcher ที่ Stanford NLP group ของ Chris Manning, Andrew Li (Chief Scientist, 23) เป็น early research hire ที่ Together AI, Joseph Camyre (CTO, 23) build infra ที่ Datadog. ทีมเล็ก แต่ background ตรงกับปัญหา — evaluation infra สไตล์ Datadog (observability ที่ scale) + agent science (long trace reasoning)

ลูกค้าจริงที่ disclose: ทีม internal ของ Anthropic, Cursor, และ "Fortune 500 financial services firm" หนึ่งราย (ไม่บอกชื่อ) — ใช้ Judgment เป็น eval harness ของ agent ที่ run ใน production. ตัวเลข deployment/ARR ยังไม่เปิด

## ทำไมสำคัญ

ปี 2024–25 ใครจะลงทุน agent ก็จะลงทุนใน framework (LangChain, CrewAI, AutoGen). ปี 2026 บทเรียนที่ enterprise เริ่มเรียน คือ framework ไม่ใช่ bottleneck — bottleneck คือ "agent ของเราทำงานพอ reliable ที่จะ promote จาก demo เป็น prod ไหม". การ scale agent ขึ้น production เจอปัญหาเดียวกับการ scale microservices — observability + evaluation + continuous improvement ต้องมา. Datadog, Splunk, New Relic ได้ multi-billion valuation เพราะตรงนี้ในยุค cloud-native; Judgment Labs (และ Braintrust, Langfuse, Patronus) กำลังเล่นบทเดียวกันสำหรับยุค agent

อีกข้อ — Lightspeed ที่ลงทั้ง seed แล้ว double-down series A ใน 6 เดือนเป็น signal ที่หนัก. ปกติ VC จะ delegate Series A ให้ partner อื่นเพื่อ diversify. การที่ Lightspeed ลงเอง 2 รอบรวด แปลว่า conviction สูงผิดปกติ — หรือ Lightspeed กลัวว่า Sequoia/a16z จะกระโดดเข้ามาแย่งใน Series A

POV: market ของ agent eval/improvement กำลังจะ consolidate ภายใน 18 เดือน. ผู้ชนะคือคนที่ get adoption จาก agent framework ใหญ่ (Anthropic Claude Agent SDK, OpenAI Agents SDK, Google ADK) เป็น default eval layer — เหมือนที่ DataDog เป็น default observability ของ AWS workload. Judgment ถ้า ship integration กับ Claude Agent SDK แบบ "one-line wrap" จะกินตลาดได้เร็ว

## มุม OpenBridge

ไม่ direct เกี่ยว แต่ adjacent insight สำคัญ. OpenBridge ทำ integration platform — ใน world ที่ agent run ผ่าน OpenBridge connector มากขึ้น, traffic ของ agent ที่ผ่าน platform กลายเป็น "trajectory data" ที่มีค่าสูง. data นี้สามารถ feed กลับเป็น:
1. eval signal สำหรับลูกค้า ("agent คุณ fail ที่ tool call นี้ 12% ของเวลา")
2. improvement product ("เราเสนอ prompt rewrite ที่ลด fail rate ลง 4%")
3. moat — เพราะ trajectory data มาจาก real production traffic ของลูกค้า ที่ใครก็ replicate ไม่ได้

Pattern ที่ Judgment Labs ทำ คือ pattern ที่ integration platform น่าทำเองเหนือ pipe layer ตัวเอง. ถ้า OpenBridge ใส่ "agent trajectory observability" เข้าใน product (เป็น dashboard ของลูกค้า) จะเปลี่ยน positioning จาก commodity transport เป็น operations-of-record ของ agent traffic — ใกล้กับสิ่งที่ Datadog เป็นให้ infra

## Sources
- [Judgment Labs Closes $32M in Seed and Series A Funding — BusinessWire](https://www.businesswire.com/news/home/20260512621556/en/Judgment-Labs-Closes-$32M-in-Seed-and-Series-A-Funding-to-Build-the-Continuous-Improvement-Layer-for-AI-Agents)
- [Judgment Labs Raises $32M to Build Evaluation Tools for Deep AI Agents — citybiz](https://www.citybiz.co/article/845551/judgment-labs-raises-32m-to-build-evaluation-tools-for-deep-ai-agents/)
- [Judgment Labs — Company site](https://www.judgmentlabs.ai/)

---

## Audio script
Judgment Labs ระดม 32 ล้านเหรียญรวม seed กับ series A เมื่อวานนี้ Lightspeed ลง lead ทั้งสองรอบ ซึ่งหายากมาก. ปัญหาที่บริษัทแก้ฟังเทคนิคแต่ critical — evaluation เครื่องมือเก่ายุค chatbot สร้างขึ้นเพื่อ single input single output. แต่ deep agent ที่ทำงานต่อเนื่องหลาย step เรียก tool หลายตัว มี memory สร้าง trajectory ยาวมาก เวลามัน fail ความผิดพลาดมัก subtle ที่ขั้นกลาง — final answer ดูถูก แต่พอเอาไป production จะระเบิด. Judgment build infra ที่ inspect trajectory label pattern ของ failure แล้ว feed กลับเข้า improvement loop. founder อายุ 22 23 ทั้งทีม background ตรงปัญหา — Stanford NLP, TogetherAI, Datadog. ลูกค้า disclose มี internal team ของ Anthropic Cursor และ Fortune 500 financial firm. มุมที่น่าคิดสำหรับ OpenBridge — เมื่อ agent run ผ่าน OpenBridge connector traffic ที่ผ่านกลายเป็น trajectory data ที่มีค่า. ถ้าใส่ agent observability เข้าใน product จะเปลี่ยน positioning จาก commodity pipe เป็น operations layer ของ agent traffic ใกล้กับสิ่งที่ Datadog เป็นให้ infra.
