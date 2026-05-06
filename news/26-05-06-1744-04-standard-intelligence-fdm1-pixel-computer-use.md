---
date: 2026-05-06
slug: standard-intelligence-fdm1-pixel-computer-use
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: A massive amber computer monitor fills the center of the frame, with raw pixelated video frames cascading inside it like a waterfall, flowing downward into a slate blue robotic hand silhouette gripping a white car steering wheel below the screen. Above the monitor, a glowing cream banner reads "FDM-1" in bold sans-serif, with a smaller coral tag "11M HOURS" in the upper-right and "50x TOKENS" in the lower-left. Editorial illustration, flat geometric shapes with subtle grain and pixel-art texture, amber + slate blue + cream + coral palette on a deep navy background, dramatic glow from the monitor lighting the hand. No real human faces. 1:1 aspect.
image:
---

# Standard Intelligence ปิด $75M (Sequoia + Spark) — FDM-1 เรียน computer use จาก raw video 11M ชั่วโมง, ขับรถใน SF ด้วย arrow keys, ท้าทาย Anthropic Computer Use ที่ระดับ foundation

## TL;DR
- **Standard Intelligence** (6-คนทีม, Seattle) ระดม **$75M** จาก Sequoia + Spark Capital เพื่อ scale **FDM-1** — "first fully general computer action model" ที่เรียนจาก **raw video ของคนใช้คอมพิวเตอร์ 11 ล้านชั่วโมง**
- เทคโนโลยีคีย์: **inverse dynamics model (IDM)** ที่ auto-label action ระหว่าง video frame ทำให้ scale data ได้ระดับ Tesla self-driving; **custom video encoder ที่ token-efficient 50 เท่า** — 2 ชม. video 30 fps อัดเข้า 1M-token context ได้
- Demo ที่ Sequoia ใช้ pitch: FDM-1 **build mechanical part ใน Blender, debug software ผ่าน UI exploration, ขับรถจริงใน SF ด้วย arrow keys + camera feed** — ไม่มี API, ไม่มี OS-level integration, ใช้แค่ pixel + keyboard input
- Signal: **agent layer แบ่งเป็นสองกลุ่มชัดขึ้น** — (1) "API-first agent" (Claude/GPT/Gemini ผ่าน MCP/connector — clean structured) vs (2) "pixel-first agent" (FDM-1 + Anthropic Computer Use — generalize ทุก software แต่ messier). FDM-1 bet ว่าทาง 2 จะชนะระยะยาวด้วย scaling law

## เกิดอะไรขึ้น

Standard Intelligence ออกจาก stealth ปลายเดือนที่แล้วด้วยรูปแบบที่ไม่ค่อยเห็น: **6 คน, มี foundation model ที่ scale แล้ว, มี Sequoia + Spark ลงทุน $75M รอบเดียว**. Sami Kama, Jim Fan และทีมเล่ารายละเอียดผ่าน blog post + paper — thesis: **computer use ที่ scale ไม่ใช่ Anthropic Computer Use เวอร์ชันเก่งกว่า — เป็น foundation model ใหม่ที่เรียนจาก raw pixel + action ตั้งแต่ scratch** เหมือน Tesla ฝึก self-driving จาก video ของคนขับจริง

ของจริงคือ **inverse dynamics model (IDM)** — แทนที่จะหา human annotator มาบอกว่า frame นี้คนกดอะไร, Standard ฝึก model ตัวกลางที่ดูสองเฟรมติดกันแล้วเดา action ระหว่างนั้นเอง (ขยับเมาส์ไปไหน, กดปุ่มอะไร). ผลลัพธ์: **scale labeling ได้ระดับ 11 ล้านชั่วโมง video** — orders of magnitude ใหญ่กว่า dataset ที่ Anthropic Claude หรือ OpenAI Operator ใช้. ตัวเลขที่ Sequoia เห็นแล้วลงทุน: dataset Standard Intelligence ใหญ่กว่า **MovieLens, ImageNet-21k, รวมทุก public computer-use dataset รวมกัน — โดยอัตโนมัติ** ไม่ต้องจ้างคน

เทคนิคที่ใหม่และ defensible: **custom video encoder** ที่ achieve **~50x token efficiency** เทียบ approach เดิม — **2 ชม. video 30fps fit ใน 1M-token context window**. ก่อนหน้านี้ video model ทุกตัวกิน token เยอะมหาศาล (Sora ใช้ patch-level tokenization ที่ 200-500 token/วินาที), Standard เคลม encoder ใหม่ทำได้ที่ ~1.4 token/วินาที โดยรักษา fidelity action prediction. นี่คือ **secret sauce ที่ Sequoia ตี value** — ไม่ใช่แค่ data scale, แต่ encoder ที่ทำให้ training tractable ภายใน budget ที่ 6 คน + $75M ทำได้

Demo ที่ shock ตลาด: FDM-1 (1) **build mechanical gear ใน Blender** จาก prompt "make a 12-tooth gear connected to a 24-tooth gear with 3:1 ratio" — ไม่ใช่ Blender API, ไม่ใช่ Python script — agent มอง screen, ขยับเมาส์, กดปุ่ม shortcut, render gear จริง; (2) **debug software bug ผ่าน UI exploration** — เปิด VS Code, navigate stack trace, ลองแก้ทีละจุด, run test, iterate — เหมือน junior dev; (3) ที่ดูบ้าที่สุด: **ขับ Tesla Model Y ใน San Francisco ด้วย arrow keys + camera feed** — agent ดูภาพถนนผ่าน Tesla camera, output keystroke ไป control vehicle, ขับ 15-20 นาทีบนถนนจริง (ผ่าน safety driver supervision ตามกฎ California DMV). ไม่ใช่ self-driving stack — เป็น **general computer action model ที่ apply ได้กับทุก embodiment ที่รับ keystroke** — Sequoia ตี thesis ว่า **knowledge work + physical control merge เป็น primitive เดียว**

ฉากหลัง: Standard Intelligence ก่อตั้งโดยทีมที่ออกจาก NVIDIA Research + Anthropic Computer Use team ปลายปี 2024. ตอนตั้งตั้ง thesis ตรงข้ามกับ Anthropic — Anthropic ใช้ **Claude เก่าๆ + screenshot training** (post-train), Standard บอก "ผิด, ต้อง pre-train จาก video ตั้งแต่ scratch — เหมือน LLM pre-train จาก text web". Anthropic Computer Use ปัจจุบัน rate accuracy ~70% บน OSWorld benchmark; Standard claim FDM-1 hit **84%** บน same benchmark — ตัวเลขที่ Anthropic ยังไม่ verify ได้

## ทำไมสำคัญ

Pattern ที่ตลาดต้องเลือกข้าง: **ปี 2026-2027 agent layer แบ่งเป็น 2 architectural school** — (1) **API-first**: agent ทำงานผ่าน MCP/connector/structured API (Anthropic Claude + Salesforce Agentforce + Google Gemini Enterprise + OpenAI Workspace Agents) — clean, fast, governable, แต่จำกัดที่ software ที่เปิด API; (2) **Pixel-first**: agent มอง screen, output keystroke (FDM-1 + Anthropic Computer Use + OpenAI Operator) — ทำงานกับ legacy software ที่ไม่มี API, generalize ได้กว้าง, แต่ slower + harder to govern. Standard Intelligence bet ว่า **pixel-first scale ดีกว่าด้วย raw data — เหมือน LLM ชนะ structured NLP ปี 2020-2022**

POV ที่ผมเชื่อ: **ทั้งสอง school จะอยู่ร่วมกัน ไม่ใช่ winner-takes-all** — แต่ pixel-first จะกินตลาดเฉพาะที่ API-first เข้าไม่ถึง: **legacy enterprise software (SAP ECC ที่ยังไม่ migrate, mainframe, internal tool ที่ไม่มี API), Excel/Google Sheets แบบ deep automation, regulated industry ที่ห้าม API ออก**. ตลาดนี้ไม่เล็ก — มี analyst ตี $200B+ legacy software automation. Standard Intelligence จะเป็น **OpenAI ของ pixel-first school** ถ้า scaling law ที่ Sequoia bet พิสูจน์ภายใน 18 เดือน

จุดที่ underrated: **Self-driving as side effect** — fact ที่ FDM-1 ขับรถใน SF ได้ตั้งแต่ pre-train แรก (โดยไม่ได้ specifically ฝึก driving) คือ **strongest signal ของ generalization** ในรอบหลายปี. Tesla FSD ใช้ vision-only แต่ฝึก specifically สำหรับ driving. FDM-1 ฝึก general "human action prediction" แล้วขับได้เป็น byproduct — ถ้า scale ขึ้น 10x, อาจจะเก่งกว่า Tesla FSD โดยที่ไม่ได้ตั้งใจ. นี่คือ thesis ที่ Sequoia bet: **embodiment-agnostic action model**

## มุม OpenBridge

**ไม่ direct เกี่ยว** กับ workflow product ของ OpenBridge ตอนนี้ (OpenBridge เป็น API-first) — แต่ adjacent insight + future-proofing signal:

(1) **API-first agent ที่ OpenBridge serve = ตลาด majority แต่จำกัด ceiling** — API-first จะครอบ enterprise software ที่ทุกระบบเปิด API (ChatGPT, Salesforce, Slack, Notion, GitHub, FlowAccount). ตลาด Thai SMB หลัก 80% อยู่ในนี้. แต่ pixel-first จะกิน 20% ที่ยากที่สุด (โรงงานเก่ารัน Windows XP control panel, ระบบ ERP ภาษาไทยที่ไม่มี API, ระบบราชการ). OpenBridge ไม่ต้องลง pixel-first ตอนนี้ — แต่ต้อง **track FDM-1 + Anthropic Computer Use** เป็น roadmap candidate ปี 2027

(2) **ถ้า FDM-1 ออก commercial API ใน 2027, OpenBridge ควรเป็น first integrator ในไทย** — wrap FDM-1 เป็น "PixelAgent" tool ที่ workflow ของ OpenBridge เรียกได้ตอนเจอ legacy software ที่ไม่มี API. Customer Thai industrial (โรงงาน, โรงพยาบาล, ราชการ) จะเป็นคนที่ pay premium สูงสุดเพราะ pain biggest

(3) **Hiring signal:** ถ้า OpenBridge ขยายทีม research/product engineer, **คนที่มีพื้น computer vision + RL + foundation model** จะเป็น hire ที่ underprice ในไทย — Standard Intelligence จ่ายระดับ Bay Area (~$300-500k/year), แต่ Thai hire ที่มีพื้น (KMUTT, Chula, Mahidol grad ที่ทำ research) ราคาต่ำกว่า 60-70% และ quality ใกล้เคียง. ลง 1-2 hire ตอนนี้ = build pixel-first capability ใน 2027 โดยไม่ต้อง wait FDM-1 commercial release

## Sources
- [The First Fully General Computer Action Model (Standard Intelligence blog)](https://si.inc/posts/fdm1/)
- [Standard Intelligence Raises $75M to Build AI That Uses Computers (AI2Work)](https://ai2.work/blog/standard-intelligence-raises-75m-to-build-ai-that-uses-computers)
- [FDM-1: AI Trained on 11M Hours of Screen Footage (Digital Applied)](https://www.digitalapplied.com/blog/standard-intelligence-fdm-1-video-training-guide)
- [Standard Intelligence Raises $75M From Sequoia and Spark Capital (Pulse2)](https://pulse2.com/standard-intelligence-raises-75-million-from-sequoia-and-spark-capital-to-scale-agi-research/amp/)
- [Standard Intelligence Launches FDM-1 (Metaverse Post)](https://mpost.io/standard-intelligence-launches-fdm-1-ai-system-capable-of-learning-complex-computer-tasks-from-video/)

---

## Audio script
Standard Intelligence ออกจาก stealth ปลายเดือนที่แล้วด้วยรูปที่ไม่ค่อยเห็น. หกคนทีม Seattle. มี foundation model ที่ scale แล้ว. มี Sequoia บวก Spark ลงทุนเจ็ดสิบห้าล้านดอลลาร์ในรอบเดียว. ของจริงคือ FDM 1 first fully general computer action model ที่เรียนจาก raw video ของคนใช้คอมพิวเตอร์สิบเอ็ดล้านชั่วโมง.

thesis ตรงข้ามกับ Anthropic Computer Use. Anthropic ใช้ Claude เก่าบวก screenshot training. post train. Standard บอกผิด ต้อง pre train จาก video ตั้งแต่ scratch. เหมือน LLM pre train จาก text web.

เทคนิค key คือ inverse dynamics model. แทนที่จะหา human annotator มาบอกว่า frame นี้คนกดอะไร. Standard ฝึก model ตัวกลางที่ดูสองเฟรมติดกันแล้วเดา action ระหว่างนั้น. scale labeling ได้สิบเอ็ดล้านชั่วโมง video อัตโนมัติ. orders of magnitude ใหญ่กว่า dataset ที่ Anthropic OpenAI ใช้.

ที่สอง custom video encoder ที่ achieve ห้าสิบเท่า token efficiency. สองชั่วโมง video สามสิบ fps fit ใน หนึ่งล้าน token context window. ก่อนหน้านี้ video model กิน token มหาศาล. Standard เคลม encoder ใหม่ทำได้ที่หนึ่งจุดสี่ token ต่อวินาที. นี่คือ secret sauce ที่ Sequoia ตี value.

demo ที่ shock ตลาด. หนึ่ง build mechanical gear ใน Blender จาก prompt make a twelve tooth gear connected to twenty four tooth gear three to one ratio. ไม่ใช่ Blender API. ไม่ใช่ Python script. agent มอง screen ขยับเมาส์ กดปุ่ม shortcut render gear จริง. สอง debug software bug ผ่าน UI exploration. เปิด VS Code navigate stack trace ลองแก้ run test iterate. เหมือน junior dev. สาม ที่ดูบ้าที่สุด ขับ Tesla Model Y ใน San Francisco ด้วย arrow keys บวก camera feed. สิบห้าถึงยี่สิบนาทีบนถนนจริง ผ่าน safety driver supervision. ไม่ใช่ self driving stack. เป็น general computer action model ที่ apply ได้กับทุก embodiment ที่รับ keystroke.

pattern ที่ตลาดต้องเลือกข้าง. ปี 2026 2027 agent layer แบ่งเป็นสอง school. หนึ่ง API first. agent ทำงานผ่าน MCP connector structured API. clean fast governable แต่จำกัดที่ software ที่เปิด API. สอง pixel first. agent มอง screen output keystroke. generalize กว้าง ทำงานกับ legacy software ที่ไม่มี API แต่ slower harder to govern.

POV ของผม. ทั้งสอง school จะอยู่ร่วมกัน ไม่ใช่ winner takes all. แต่ pixel first จะกินตลาดเฉพาะที่ API first เข้าไม่ถึง. legacy enterprise software. SAP ECC ที่ยังไม่ migrate. mainframe. internal tool ที่ไม่มี API. Excel deep automation. regulated industry ที่ห้าม API ออก. ตลาดนี้ไม่เล็ก analyst ตีสองร้อยพันล้านดอลลาร์ legacy software automation.

ที่ underrated คือ self driving as side effect. fact ที่ FDM 1 ขับรถใน SF ได้ตั้งแต่ pre train แรก โดยไม่ได้ specifically ฝึก driving คือ strongest signal ของ generalization ในรอบหลายปี. Tesla FSD ใช้ vision only แต่ฝึก specifically สำหรับ driving. FDM 1 ฝึก general human action prediction แล้วขับได้เป็น byproduct. ถ้า scale ขึ้นสิบเท่า อาจจะเก่งกว่า Tesla FSD โดยไม่ได้ตั้งใจ. embodiment agnostic action model.

สำหรับ OpenBridge. ไม่ direct เกี่ยวกับ product ตอนนี้ที่เป็น API first. แต่สาม signal. หนึ่ง API first ที่เรา serve คือตลาด majority แปดสิบเปอร์เซ็นต์ของ Thai SMB. แต่ pixel first จะกินยี่สิบเปอร์เซ็นต์ที่ยากที่สุด. โรงงานเก่ารัน Windows XP control panel. ระบบ ERP ภาษาไทยที่ไม่มี API. ระบบราชการ. ไม่ต้องลง pixel first ตอนนี้ แต่ต้อง track FDM 1 บวก Anthropic Computer Use เป็น roadmap candidate สองพันยี่สิบเจ็ด. สอง ถ้า FDM 1 ออก commercial API ใน สองพันยี่สิบเจ็ด OpenBridge ควรเป็น first integrator ในไทย. wrap FDM 1 เป็น PixelAgent tool ที่ workflow OpenBridge เรียกได้ตอนเจอ legacy software ที่ไม่มี API. customer Thai industrial โรงงาน โรงพยาบาล ราชการ จะ pay premium สูงสุด. สาม hiring signal. คนที่มีพื้น computer vision RL foundation model จะ underprice ในไทย. Standard จ่ายระดับ Bay Area สามแสนถึงห้าแสนต่อปี. Thai hire จาก KMUTT Chula Mahidol research grad ราคาต่ำกว่าหกสิบเจ็ดสิบเปอร์เซ็นต์ quality ใกล้เคียง. ลงหนึ่งสองคนตอนนี้ build pixel first capability ในสองพันยี่สิบเจ็ดโดยไม่ต้องรอ FDM 1 commercial release.
