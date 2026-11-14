---
date: 2026-11-12
slug: mirendil-1b-series-a-lor-ai-research-lab
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of an empty glass research lab labeled
  "FRONTIER AI R&D" with no chairs or scientists. Instead, dozens of glowing
  agent cubes float at workbenches, each piping code and experiment logs into
  a central tower stamped "LOR". A bold three-line counter dominates the
  scene: "$1B SERIES A", "~$5B VALUATION", "AGENTS WROTE 99%+ OF THE CODE".
  A side panel shows the model name "FERN" with a bar "10M TOKEN CONTEXT".
  Deep indigo and electric lime palette, strong contrast for 200px
  thumbnails, 1:1 aspect, no real human faces (ex-researcher silhouettes
  OK).
image: images/26-11-15-0605-03-mirendil-1b-series-a-lor-ai-research-lab.png
---

# Mirendil ระดม $1B Series A — ex-Anthropic นักวิจัยเดิมพัน "agent รัน AI lab ได้ทั้ง lab" valuation $5B

## TL;DR
- 12 พ.ย. 2026 **Mirendil** ก่อตั้งโดยอดีตนักวิจัย **Anthropic + Google DeepMind** ประกาศ **Series A $1B** นำโดย **Kleiner Perkins + Clearlake Capital** ร่วมด้วย Battery, Google, M13, Pear VC, S32
- Bloomberg รายงานก่อนหน้านี้ valuation ~**$5B**, บริษัทไม่ยืนยันเอง. seed round $200M เพิ่งปิดเมื่อ มิ.ย. 2026 — ครึ่งปี valuation ขึ้นอาจ 10x+
- Thesis: product **Lor** (private beta) coordinate **agent หลายร้อยตัว** เขียน code + รัน experiment ได้หลายวัน; model ตัวเอง **Fern** context **10M token** (~500K lines of code); บริษัทอ้างว่า **agent เขียน code ของ Mirendil-Base มากกว่า 99%**
- Signal: VC ยินดีจ่าย $5B ให้ thesis "AI lab เองก็ถูก disrupt ด้วย agent" — agentic AI กำลังย้ายจาก "เครื่องมือ worker" ไปเป็น "replacement ของ R&D operation ทั้ง function"

## เกิดอะไรขึ้น

**12 พ.ย. 2026** Mirendil ประกาศผ่าน X account หลักและ blog post ตัวเอง: **Series A $1B** นำโดย **Kleiner Perkins + Clearlake Capital** พร้อม syndicate ยาว — **Battery Ventures, Doerr Capital, Gil & Co, Google, M13, Pear VC, S32**. ก่อนหน้านี้ Bloomberg รายงานในกันยายนว่าบริษัทกำลัง raise $1B ที่ valuation ~**$5B** — Mirendil ไม่ confirm ตัวเลข valuation เอง แต่ทุก syndicate member รู้

ก่อนหน้านี้ Mirendil ปิด **seed $200M** เมื่อ **มิ.ย. 2026** นำโดย **Andreessen Horowitz + Kleiner Perkins** แล้ว Nvidia เข้าเติมหลัง — 5 เดือนมาแล้ว valuation อาจขึ้น ~10x. บริษัทก่อตั้งโดย **อดีตนักวิจัย Anthropic และ Google DeepMind** (ไม่ระบุชื่อเฉพาะในแถลงการณ์)

Product หลัก: **Lor** — platform ใน private beta ที่ Mirendil อธิบายว่า coordinate **"agent หลายร้อยตัว"** เขียน code + รัน experiment ต่อเนื่องได้ **หลายวัน**. โมเดลของบริษัทเองชื่อ **Fern** รองรับ context **10 ล้าน token** ซึ่งบริษัทเทียบเป็น **~500,000 บรรทัด code**. Fern เป็น model รองรับ Lor — ไม่ได้ขายแยก

Claim ที่ห้ามไม่คิดซ้ำ: **"agent เขียน code ของโมเดล Mirendil-Base มากกว่า 99%"**. บริษัทไม่เปิด breakdown ว่าหมายถึง autocompletion, pair programming หรือ full autonomy. SiliconANGLE และ WOWTALE รายงาน claim นี้ไว้ แต่ **ไม่มี third-party verification** — ยัง private beta ลูกค้าไม่เปิดชื่อ

a16z newsletter และ Bloomberg ระบุ valuation $5B. ถ้า **ARR ~0** (private beta ยังไม่ขาย) นี่คือ **pure thesis bet** — LP ของ Kleiner Perkins + Clearlake รู้ว่าซื้อ **"option on AI-lab-as-a-service"** ไม่ใช่ซื้อ revenue multiple

## ทำไมสำคัญ

ปี 2025–2026 เราเห็น pattern ซ้ำ: Anthropic + OpenAI + Google DeepMind เปิด claim ว่า **"agent เขียน code ส่วนใหญ่ภายใน"** (Claude Code ภายใน Anthropic, OpenAI Codex ภายใน OpenAI, ใช้ Gemini ที่ DeepMind). แต่ frontier lab ทั้ง 3 ยังเก็บ **ของจริง** — tooling, orchestrator ของพนักงาน, experiment harness — ไว้ภายใน. ไม่มีใครเปิดสาธารณะ

Mirendil คือ **ครั้งแรกที่ "AI lab operation" ออกเป็น product**. ถ้า Lor ทำได้จริงตามที่อ้าง — coordinate agent หลายร้อยตัวเขียน code + รัน exp หลายวัน — แปลว่า **lab ขนาด 10–20 คน** ทำงานได้เหมือน lab 200 คน. Thesis ของ CapitalG ที่เพิ่งเทใน LangChain ($3B) กับ thesis ของ KP+Clearlake ที่เทใน Mirendil ($5B) คือ **คนละชั้น** — LangChain ขายให้ enterprise, Mirendil ขายให้ **คนที่จะไป compete กับ frontier lab**

จุดที่ต้อง skeptical: (1) **99% ของ code** — frontier lab ที่มีจริยธรรมสูง เช่น Anthropic ยังอ้างแค่ "ส่วนใหญ่"; 99% อาจนับ boilerplate + autocompletion ซึ่งไม่ใช่ research contribution จริง; (2) **10M token context** — Google Gemini 2.0 Pro เปิด 2M, Claude Opus ~1M, GPT-5 ~1M; Mirendil อ้าง 10M แปลว่าใช้ sparse attention / hierarchical retrieval ที่แลกคุณภาพกับ context length — ต้องรอ benchmark จริง; (3) **ไม่มี customer / use case / GA date** — Series A $1B ใน **private beta pre-revenue** คือ bet ที่ valuation rise ต้องตามด้วย breakthrough จริงใน 12–18 เดือน ไม่งั้นรอบถัดไปจะ down round

สำหรับ **AI safety community**: Mirendil กำลัง normalize แนวคิดว่า **agent สร้าง model ได้เอง**. ถ้า Lor scale ได้, loop "agent เขียน code → train model → model ให้ agent ใหม่" จะเร็วขึ้นมาก. Policy discussion เรื่อง AI acceleration risk จะต้องแตะเรื่อง **"commercial recursive self-improvement"** ไม่ใช่แค่ hypothetical scenario

## มุม AI Agent Platform

สำหรับ **builders**: Mirendil ยืนยันว่า **"orchestration ของ agent หลายร้อยตัว"** คือ frontier technical challenge ปี 2027 — ไม่ใช่ "แค่ framework prompt chain". ถ้าคุณ build agent platform ให้ enterprise ขนาดเล็ก (10 agent, 1 workflow) ก็ยังมีตลาด แต่ **ceiling ของมูลค่า** อยู่ที่ใครก็ตามที่แก้ orchestration 100–1000 agent ได้. ทีมที่ยังใช้ LangGraph DAG เดียวกับ Celery queue อาจต้อง rethink

สำหรับ **users / business** นอก AI-research vertical: บทเรียนไม่ใช่ "ซื้อ Lor" — มันไม่ใช่ product สำหรับคุณ. บทเรียนคือ **ถ้าทีม research + engineering ของคุณยัง deploy agent 1 ตัวต่อ 1 workflow ให้เริ่มคิด architecture สำหรับ "agent fleet"**. UBS บอกเรา 12,700 personal agent — Mirendil บอก **"ลืม personal agent — agent fleet 100-1000 ตัวทำงานคู่กัน"**. ปี 2027 CTO ที่ไทย/SEA ที่ยังไม่มี platform coordinate agent หลายตัว จะโดน benchmark ด้วย

สำหรับ **ecosystem**: Nvidia + Google ใน syndicate คือ signal ว่า **compute + model layer ยัง bet ว่า "agent orchestration = ลูกค้าใหญ่ของ compute"**. GPU cluster ที่ Mirendil จะใช้เพื่อ train Fern + run Lor จะเป็น demand ใหม่ที่ไม่เหมือน LLM pre-training — **บยาบฝั่ง inference / long-running agent loop** จะโตเร็วกว่า pre-training ใน 2027. ใครขาย inference-optimized chip (Groq, Cerebras, Google TPU) ได้ประโยชน์

## Sources
- [Mirendil Raises $1B to Democratize Frontier AI R&D (Mirendil)](https://mirendil.com/news/series-a/)
- [Mirendil raises $1B in funding to speed up AI model development (SiliconANGLE)](https://siliconangle.com/2026/11/13/mirendil-raises-1b-in-funding-to-speed-up-ai-model-development/)
- [Ex-Anthropic researchers' startup Mirendil raises $1B to let AI agents do the work of an AI lab (MLQ.ai)](https://mlq.ai/news/ex-anthropic-researchers-startup-mirendil-raises-1-billion-to-let-ai-agents-do-the-work-of-an-ai-lab/)
- [Mirendil $1B Series A: Kleiner Perkins + Clearlake lead Lor platform (WebProNews)](https://www.webpronews.com/mirendil-1-billion-series-a-kleiner-perkins-clearlake-ai-agents-lor)

---

## Audio script
วันนี้มีข่าว round ใหญ่มากของ Mirendil บริษัท AI ที่ก่อตั้งโดยอดีตนักวิจัยจาก Anthropic กับ Google DeepMind ปิด Series A ที่ 1 พันล้านดอลลาร์ นำโดย Kleiner Perkins กับ Clearlake Capital ร่วมด้วย Battery Google M13 Pear VC S32 Bloomberg เคยรายงานก่อนหน้านี้ว่า valuation อยู่ที่ประมาณ 5 พันล้านดอลลาร์ แต่บริษัทไม่ยืนยันเอง เพียงครึ่งปีก่อนเพิ่งปิด seed ที่ 200 ล้านดอลลาร์ แปลว่า valuation ขึ้นอาจ 10 เท่าในเวลา 5 เดือน Product หลักของบริษัทชื่อ Lor ยังอยู่ใน private beta coordinate agent หลายร้อยตัวให้เขียน code และรัน experiment หลายวัน model ของบริษัทเองชื่อ Fern context 10 ล้าน token ประมาณ 5 แสนบรรทัด code บริษัทอ้างว่า agent เขียน code ของ Mirendil-Base มากกว่า 99 เปอร์เซ็นต์ ส่วนที่น่าสังเกตคือทุก frontier lab อย่าง Anthropic OpenAI Google DeepMind มี internal tooling ประมาณนี้แต่เก็บเงียบ Mirendil คือเจ้าแรกที่ยอมเปิดเป็น product นี่เป็น bet ว่า AI lab operation เองก็ถูก disrupt ได้ด้วย agent ที่ต้อง skeptical คือ 99 เปอร์เซ็นต์ของ code อาจหมายถึง autocomplete บวก boilerplate ไม่ใช่ research contribution จริง และ 10 ล้าน token context ยังไม่มี benchmark independent สำหรับคน build agent app ในไทย บทเรียนคือ orchestration ของ agent หลายร้อยตัวคือ frontier challenge ของปีหน้า ไม่ใช่แค่ chain prompt ธรรมดา สำหรับ CTO ไทย ที่ยังมี agent หนึ่งตัวต่อ workflow ควรเริ่มคิด architecture สำหรับ agent fleet 100 ถึง 1000 ตัว UBS บอกเรา 12,700 personal agent Mirendil กำลังบอกว่าลืม personal agent ไปเถอะ agent fleet 100 ถึง 1000 ทำงานคู่กันต่างหากคือ future ครับ
