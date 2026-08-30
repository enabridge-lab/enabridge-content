---
date: 2026-08-30
slug: openai-jalapeno-inference-asic-agent-economics
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: |
  Editorial isometric illustration of a glowing green chile-pepper-shaped
  silicon wafer labeled "JALAPEÑO" on a factory conveyor, sliding past a
  toppled beige data-center rack labeled "GB300" that leaks blue coolant.
  Above the conveyor, three oversized stat panels stacked in a column:
  "700W vs 1,400W", "1.9x TOK / KWh", "3.6x LOWER LATENCY". Behind them a
  faint silhouette of TSMC fab lines and Broadcom logo watermark. Deep
  navy background with a hot red-to-amber rim light on the chile-wafer;
  cold blue rim light on the fallen rack. 1:1 aspect. No real human
  faces. Text and numbers sized to read in a 200px thumbnail.
image: images/26-08-30-0609-01-openai-jalapeno-inference-asic-agent-economics.png
---

# OpenAI ปล่อย benchmarks Jalapeño — inference ASIC ตัวแรกกับ Broadcom, แซง Nvidia GB300 ที่ 1.9x tokens/kWh, 3.6x lower latency

## TL;DR
- **25 ส.ค. 2026** OpenAI + Broadcom เผย benchmarks แรกของ **Jalapeño** — custom inference ASIC ตัวแรกของ OpenAI, tape-out ที่ **TSMC N3P** ใน 16 เดือน; **700W**, **216 GB HBM4**, **13.4 PFLOPs MXFP4**, **15.4 TB/s** package bandwidth
- **เทียบ Nvidia GB300**: **1.5–1.9x tokens/kilowatt**, **สูงสุด 3.6x lower latency** บน interactive workload; **700+ tok/s/user** บน DeepSeek R1, **~1,400 tok/s/user** บน GPT-OSS 120B — ที่กินไฟครึ่งเดียว (700W vs 1,150–1,400W)
- Deploy ในนามผลิตภัณฑ์ของ OpenAI ปลายปี 2026, multi-generation roadmap มาแล้ว
- Signal: **agent unit economics เปลี่ยน** — inference cost/token คือ variable ที่กำหนดว่า agent จะ run 24/7 ได้ economically หรือไม่, และ OpenAI ตัดสายพันธ์กับ Nvidia = frontier lab ทุกที่ (Google TPU, Anthropic Trainium, ตอนนี้ OpenAI) ล้วนมี in-house silicon

## เกิดอะไรขึ้น

25 สิงหาคม 2026 OpenAI ปล่อย technical brief คู่กับ Broadcom press release เผยแพร่ benchmark ชุดแรกของ **Jalapeño** — chip ที่ทั้งสองบริษัทประกาศจะสร้างร่วมกันเมื่อปี 2024, tape-out ที่ TSMC N3P เสร็จภายใน 16 เดือน (rapid ผิดปกติสำหรับ chip ระดับนี้), ใช้ AI-assisted design tool ตลอด pipeline. ผลลัพธ์: **B0 stepping** ของ Jalapeño กินไฟ **700W** ต่อ chip, บรรจุ **6 stack ของ HBM4** รวม **216 GiB @ 15.4 TB/s bandwidth**, compute peak **13.4 PFLOPs ที่ MXFP4** — spec ที่ตั้งใจ optimize ทางเดียวคือ **LLM inference** ไม่ใช่ training

Number ที่ทำให้ Nvidia รอบ Rubin/GB300 ต้อง flinch คือ **performance-per-watt** — Tom's Hardware สรุปว่า Jalapeño ให้ throughput ต่อ kilowatt **1.5–1.9 เท่า** ของ Nvidia GB300 (900–1,150W) และ **3.6 เท่า lower latency** บน interactive workload ที่ user รอ response ทันที — condition ที่ agent เกือบทุกตัวใช้อยู่. บน **DeepSeek R1** Jalapeño ทำได้ **700+ tok/s/user** และบน **GPT-OSS 120B** ที่ OpenAI open-source ปลายปี 2025 ทำได้ **~1,400 tok/s/user** — ตัวเลขที่ TechCrunch เรียกว่า "purpose-built for the agent era". Broadcom investor press release เผยว่า chip นี้จะเข้า deploy ใน production ของ OpenAI ปลายปี 2026, และ Sam Altman บอกวิเคราะห์ Longyield ว่า chip **generation ถัดไป** (Serrano?) ก็ tape-out เข้าคิวไว้แล้ว

OpenAI framing เอาไว้ว่า Jalapeño ไม่ได้ **แทนที่** Nvidia — จะเป็น complement — แต่ number ที่ปล่อยออกมา + timing (หลัง ต้นเดือน Anthropic ประกาศขยาย Trainium fleet + Google reveal TPU v7e) ชัดว่า frontier lab ทุกที่กำลัง **de-risk** ตัวเองจาก Nvidia supply constraint และ margin. The Register ตั้งชื่อ story ตรง ๆ ว่า "OpenAI's Jalapeño looks like it'll be an inference beast" — และเน้นว่า chip ตัวนี้ถูกเลือก architecture ให้ **serve inference request จาก ChatGPT + Codex + Agent product ของ OpenAI เอง** ก่อน จะไม่ขายเป็น external accelerator เหมือน H100/B200 ของ Nvidia

## ทำไมสำคัญ

Chip นี้ไม่ใช่ story เรื่อง hardware แข่งกัน — เป็น story เรื่อง **agent unit economics** โดยตรง. Agent ที่ run 24/7 workflow (customer support 500,000 conversation/เดือน, credit memo drafting ที่ DBS deploy ให้ 1,500 banker, super-agent ของ Cashfree ที่รับ retry ตลอดวัน) ราคาต้นทุนถูกกำหนดโดย **cost per token × token per request × request per day**. ถ้า OpenAI inference cost/token ลดลง **30–50%** จาก Jalapeño (สมมติจาก tokens/kWh + owning silicon แทนซื้อจาก Nvidia margin), workflow ที่ปัจจุบันขาดทุนที่ enterprise pricing ($20–200/seat/month) จะ break even ทันที — และ workflow ที่ปัจจุบัน break even จะ **profitable enough** ที่ builder จะ commit product roadmap 5 ปี ไม่ใช่ pilot 6 เดือน

Pattern ที่เห็นชัด: **frontier lab ทุกที่ในปี 2026 มี in-house silicon** — Google TPU (v7e generation), Anthropic Trainium fleet + rumor เรื่อง Anthropic Athena chip กับ Marvell, OpenAI Jalapeño กับ Broadcom, Meta MTIA v3 กับ TSMC. Nvidia ยังชนะ training + burst capacity แต่ **inference workload ที่คาดการณ์ pattern ได้** (agent workflow ทุกตัว) จะย้ายไป custom ASIC ที่ owner ตั้งใจ optimize ทาง single-purpose. Longyield analyst เขียนว่านี่คือ "the beginning of the end of Nvidia's inference monopoly" — overstate แต่ direction ถูก

Signal ต่อจากนี้ **6 เดือน**: (1) **AWS/Azure/GCP** จะเร่ง ship native inference primitive ที่ pin ต่อ ASIC ของตัวเอง แทน "GPU as a service" generic; (2) **enterprise negotiation** เรื่อง inference contract จะเริ่มมี term ว่า "silicon guarantee" — hyperscaler bundle Trainium/TPU/Jalapeño capacity เข้า Bedrock/Vertex/Azure OpenAI Service; (3) **agent startup** ที่ต้อง run high-volume inference (Cursor, Windsurf, Perplexity, Devin) จะเริ่มทำ direct silicon deal เอง หรือ negotiate rate ตาม ASIC line ไม่ใช่ H100 hour; (4) **open weight model** จะได้ประโยชน์มหาศาล — ถ้า Jalapeño ทำ 1,400 tok/s บน GPT-OSS 120B ที่ 700W, ที่บ้าน/private cloud รัน open model ราคาถูกลงเร็วเช่นกัน

## มุม AI Agent Platform

**Builders:** ถ้าคุณ build agent framework/runtime — สมมติฐาน "inference cost fixed at $0.X/1M token" ที่ใช้ใน business model ตอนนี้ กำลังจะ **reprice ลง 30–50%** ในไตรมาส 1–2 ปี 2027 เมื่อ Jalapeño + Trainium2 + TPU v7e เต็ม fleet. Product roadmap ที่ 6 เดือนก่อนดูขาดทุน (long-running agent 12 ชม./วัน, multi-agent orchestration ที่ทุกตัว call LLM หลายรอบ, deep research agent ที่ browse 100 page) จะกลับมาน่าลงทุน. Architecture pattern ที่ควร prep: (a) **model routing** ที่รู้ว่า workload ไหนควรไป frontier vs open weight — ใน 6 เดือนเลือกได้ตาม price/latency curve ที่จะ shift, (b) **caching layer** (prompt cache + response cache) ที่ absorb ประโยชน์ทันทีเมื่อ inference cost ลด, (c) **observability** ที่ต่อ token cost ต่อ agent action ให้ finance team อ่านออก — คุณจะต้อง justify agent economics ทุกไตรมาส

**Users / business:** ที่กำลัง scope agent deployment — timing สำคัญ. Contract ที่ sign เดือนนี้กับ vendor ที่ pass-through Nvidia rate ทั้งหมด จะแพงกว่า contract ที่ sign ต้นปี 2027 หลัง hyperscaler เริ่ม price ตาม ASIC. Negotiate ให้มี **price adjustment clause** ที่ tie กับ hyperscaler published rate หรือ commit volume-based discount, อย่า lock ราคา 3 ปีตอนนี้. **Ecosystem:** Broadcom หุ้นวิ่งขึ้น ~15% ในสัปดาห์นี้ per Palantir/AI Weekly, และ Marvell/Astera Labs จะได้ราคาต่อจากนั้น — signal ว่า **hyperscale silicon supply chain** (ไม่ใช่ Nvidia GPU) คือ where the money moves ต่อจากนี้ 12–24 เดือน. Enterprise ที่ deploy agent ผ่าน AWS Bedrock AgentCore, Google Gemini Enterprise Agent Platform, Azure AI Foundry จะได้ advantage ทันที เพราะ 3 platform นี้ทั้งหมด vertical-integrate silicon–inference–agent runtime อยู่แล้ว vs vendor ที่ยังต้องซื้อ GPU capacity ผ่าน third party

## Sources
- [OpenAI and Broadcom unveil LLM-optimized inference chip — OpenAI](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)
- [OpenAI's Jalapeño chip is built for fast inference at scale, benchmarks show — TechCrunch](https://techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/)
- [OpenAI's 700W Jalapeño ASIC outpaces 1,400W Nvidia flagship GPU — Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks)
- [OpenAI Details Jalapeño, Its First Broadcom-Built Inference ASIC — AI Weekly](https://aiweekly.co/alerts/openai-jalapeno-chip-beats-nvidia-rubin-on-perf-per-watt)
- [OpenAI's upcoming Jalapeño chip looks like it'll be an inference beast — The Register](https://www.theregister.com/systems/2026/08/25/openais-upcoming-jalapeno-chip-looks-like-itll-be-an-inference-beast/5292052)
- [OpenAI and Broadcom Unveil LLM-Optimized Intelligence Processor — Broadcom Investor Release](https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-unveil-llm-optimized-intelligence-processor)

---

## Audio script
สวัสดีครับ วันที่ 25 สิงหาคม OpenAI กับ Broadcom เผย benchmarks แรกของ Jalapeño chip ที่เป็น custom inference ASIC ตัวแรกของ OpenAI ทำ tape out ที่ TSMC N3P ใน 16 เดือน chip นี้กินไฟ 700 วัตต์ต่อตัว มี HBM4 216 GB bandwidth 15.4 terabyte ต่อวินาที compute peak 13.4 petaflops แต่ที่สำคัญคือตัวเลขเทียบ Nvidia GB300 ให้ throughput ต่อ kilowatt 1.5 ถึง 1.9 เท่า latency ต่ำสุด 3.6 เท่าใน interactive workload ที่ user รอ response ทันที บน DeepSeek R1 ทำได้ 700 tokens ต่อ second ต่อ user บน GPT OSS 120B ทำได้ 1,400 tokens ต่อ second ต่อ user OpenAI จะ deploy chip นี้ในผลิตภัณฑ์ปลายปี 2026 และ generation ถัดไปทำ tape out ไว้แล้ว ทำไมสำคัญ เรื่องนี้ไม่ใช่ hardware แข่งกัน มันคือ agent unit economics ตรง ๆ ถ้า OpenAI ลด inference cost per token ลง 30 ถึง 50 เปอร์เซ็นต์ agent workflow ที่ 24 ชั่วโมงต่อวัน customer support 500,000 conversation ต่อเดือน หรือ credit memo drafting แบบ DBS จะ break even ที่ pricing ปัจจุบัน และ workflow ที่ break even แล้วจะ profitable พอที่ builder จะ commit 5 ปีไม่ใช่ pilot 6 เดือน pattern ที่เห็นทุก frontier lab ในปี 2026 มี in house silicon Google TPU Anthropic Trainium OpenAI Jalapeño Meta MTIA Nvidia ยังชนะ training แต่ inference ที่คาดการณ์ pattern ได้ ซึ่งคือ agent workflow ทุกตัว จะย้ายไป custom ASIC ถ้าคุณ build agent runtime prep sample สามอย่าง model routing ที่รู้ workload ไหนควรไป frontier กับ open weight caching layer ที่ absorb ประโยชน์ทันที และ observability ที่ต่อ cost per agent action ให้ finance อ่านออก ถ้าคุณกำลัง sign contract inference กับ vendor อย่า lock 3 ปี ให้ใส่ price adjustment clause tie กับ hyperscaler rate เพราะไตรมาส 1 ปี 2027 ราคาจะขยับลง จบตรงนี้ครับ
