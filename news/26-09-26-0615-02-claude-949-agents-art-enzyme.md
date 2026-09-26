---
date: 2026-09-25
slug: claude-949-agents-art-enzyme
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  A dramatic editorial isometric bio lab at night; a wall of 949 glowing
  purple hexagon nodes (a tessellated grid, sized to read at 200px) each
  stamped with a small Anthropic-A silhouette, all connected by neon lines
  converging to a central petri dish labeled "ART SYSTEM — NEW". Beside
  the dish, three big contrasty stat cards read "949 AGENTS", "21.5 HOURS",
  "215.6M TOKENS". A CRISPR-like DNA helix ribbon threads across the top
  labeled "reverse transcriptase + accessory + repeat array". Editorial
  isometric style, brand-neutral except the Anthropic-A logo, 1:1 aspect,
  no real human faces (silhouetted scientist at a desk in shadow).
image: images/26-09-26-0615-02-claude-949-agents-art-enzyme.png
---

# 949 Claude agents รันเอง 21 ชั่วโมง เจอ enzyme system ใหม่ที่ยังไม่มีใครรู้จัก — เกิด agentic science จริงเป็นครั้งแรก

## TL;DR
- **24 ก.ย.** — Anthropic เผยแพร่ผลการทดลอง molecular biology campaign ที่ **Claude Mythos 5 รันแบบ multi-agent 949 sessions, ใช้เวลา 21.5 ชั่วโมง, เผา 215.6M tokens** — โดยไม่มี human ในลูป — แล้วได้ **enzyme system ใหม่ชื่อ ART** (array-associated reverse transcriptases) ที่ไม่เคยถูก characterize มาก่อน. ประกอบด้วย reverse transcriptase gene + accessory protein + long array ของ DNA repeats คล้าย CRISPR
- Brief ที่ให้ Claude ตอนต้น: "find new reverse transcriptase systems in a database of 1.9 billion protein clusters". Agents recover **200,000 enzyme clusters**, score **3,564 candidate partner families**, file **19 reports** ส่งให้นักวิทย์มนุษย์ review — 1 ในนั้นคือ ART
- Tooling ที่ Claude ใช้เป็น "same tools available to any scientist" (BLAST, HMMER, structural search) + Anthropic internal harness ที่ coordinate parallel sessions. Anthropic บอกว่า **นักวิทย์มนุษย์ต้องใช้ years ทำแบบเดียวกัน** — นี่ไม่ใช่ paper mill; นี่คือ first-in-class demonstration ของ **science discovery ที่ scale ด้วย compute แทน labor**

## เกิดอะไรขึ้น

**24 กันยา 2026** — Anthropic ปล่อย blog "Claude discovers a novel enzyme system" + companion paper. เนื้อหาสรุปได้ว่า: ทีม Claude Science (in-house molecular biology lab ที่ Anthropic ตั้งขึ้นต้นปี) ให้ Claude Mythos 5 (trusted-access variant ของ Fable 5) รัน task เดียว — **หาระบบ reverse transcriptase (RT) ใหม่ในฐาน protein cluster 1.9 พันล้าน entries**. RT คือ enzyme ที่แปลง RNA เป็น DNA, เป็นตัวสำคัญของ retrovirus, telomerase, และ CRISPR-Cas type III — target ทางวิทยาศาสตร์ที่มี commercial value สูงเพราะเป็น backbone ของ gene-editing tools

Campaign รัน **949 concurrent agent sessions** ผ่าน Anthropic internal orchestration harness ที่ coordinate parallel Claude Code + Claude Science instances. รวมเวลาทั้งหมด **21.5 ชั่วโมง**, ใช้ tokens ทั้งหมด **215.6 ล้าน token**. Human intervention = ศูนย์ — ทีมนักวิทย์ setup brief, กด start, ไปนอน. ในช่วง 21 ชั่วโมงนั้น agent วง outer loop scan cluster database, filter, run structural alignment; วง inner loop ทำ hypothesis generation + literature review + candidate scoring. ผลลัพธ์: **200,000 enzyme clusters** ถูก recover, **3,564 candidate RT-partner families** ถูก scored, และท้ายที่สุด agent เขียนออกมาเป็น **19 written reports** ให้ human review

หนึ่งในสิบเก้ารายงานนั้นคือ **ART — array-associated reverse transcriptases**: enzyme system ที่มี 3 ส่วน: (1) reverse transcriptase gene, (2) neighbouring accessory protein ที่ยังไม่รู้หน้าที่, และ (3) long array of evenly-spaced DNA repeats ที่ **โครงสร้างคล้าย CRISPR array**. Feng Zhang lab (MIT/Broad) — ผู้พัฒนา CRISPR-Cas9 — บอกกับ Anthropic ว่า pattern ที่ Claude เจอ **"ไม่เคยอยู่ใน CRISPR literature"** และเป็น candidate ที่สมควรได้ funding ทดลอง in vitro ทันที. Gizmodo headline ตรงจุด: **"Claude Found a Mysterious CRISPR-Like System — but Anthropic Can't Say What It's Capable of"** — เพราะ function จริง (immune defense? gene editing? DNA integration?) ยังต้อง wet-lab confirm

Anthropic emphasize ว่า tooling ที่ Claude ใช้เป็นของ **public standard** — BLAST, HMMER, InterProScan, PDB structural search — "same tools available to any scientist ที่มี laptop และ subscription". สิ่งที่ต่างคือ scale ของการ orchestrate: 949 agent รันคู่ขนาน = throughput ที่มนุษย์ทีมเดียวใช้ **years** ทำได้เอง. Anthropic ไม่ใช่ประกาศ product; ประกาศ **capability demonstration** — signal ว่า agent-driven science คือ genre ใหม่ที่พร้อมใช้แล้ว

## ทำไมสำคัญ

**นี่เป็นครั้งแรกที่ multi-agent AI ทำ novel scientific discovery ที่ทดสอบได้จริง**. เดิมทีเรามี AlphaFold (2020) ที่ทำ prediction, และ Nobel Chemistry 2024 ให้ Baker + Hassabis ว่า AI protein folding = milestone. แต่ AlphaFold ทำนายโครงสร้างของสิ่งที่ scientist เลือก input; ART campaign ตรงข้าม — **agent เลือก question เอง, run experiment ของตัวเอง (in-silico), และ report finding ที่ human ไม่เคยเห็น**. Difference คือ agency: AlphaFold = tool ที่มนุษย์ใช้; Mythos 5 in ART campaign = collaborator ที่มนุษย์ให้ brief กว้าง ๆ

Pattern ที่จับได้: **science discovery กำลังกลายเป็น compute-bounded, ไม่ใช่ labor-bounded อีกต่อไป**. เดิมค่าใช้จ่ายหลักของ research lab = PhD/postdoc time (~$150k/year ต่อคน) + wet lab + equipment. Campaign นี้ Anthropic ใช้ ~$5–15k ของ compute (215.6M tokens × ~$40–70/million สำหรับ Mythos 5 tier) ทำงานเท่า postdoc 2–3 คนตลอดปี. **นี่คือ curve ที่ Sam Altman พูดเรื่อง "compute > headcount" มา 3 ปีแล้ว** — ตอนนี้เห็นเป็นตัวเลขจริงในสายชีววิทยา, พื้นที่ที่คนคิดว่า AI จะเข้าถึงยากที่สุด

จุดที่ต้องจับตา: **Anthropic ยังไม่บอกว่า ART ทำอะไรได้บ้าง** — Gizmodo กด question ตรง ๆ, ทีมตอบว่า "we cannot say what it's capable of" จนกว่าจะ in vitro test. Signal 2 อย่าง: (1) Anthropic กำลัง treat capability disclosure แบบเดียวกับ security research — release finding แต่ hold details ที่อาจถูก misuse (ART มี structural similarity กับ CRISPR-Cas ที่ dual-use ในการ gene editing); (2) **Mythos 5 = ตัวเดียวกับ Fable 5 แต่ safeguards ยกออก** — สำหรับ trusted-access เท่านั้น (Anthropic Fable 5.1 vs Mythos 5.1 launched 1 ก.ย.) — bio-adjacent capability คือเหตุผลว่าทำไมทั้งสองรุ่นต้องมี tier ต่างกัน

## มุม AI Agent Platform

สำหรับ **builders** ที่ทำ agent orchestration framework (LangGraph, Google ADK, AutoGen, CrewAI, OpenAI Agents SDK, Microsoft Agent Framework) — **Anthropic internal harness ที่ coordinate 949 parallel Claude sessions คือ template ใหม่ที่ open-source จะไล่ตาม**. Framework ปัจจุบันส่วนใหญ่ handle 5–50 agent max; 949 agent × 21 ชั่วโมง × 215.6M tokens = infrastructure requirement คนละเรื่อง (state management, cost budgeting, deduplication, failure recovery, cross-session memory). ใครสร้าง open-source harness ที่ scale ระดับ 1000+ agent ใน production ได้ก่อน = ครอง mind-share developer

สำหรับ **users / business** — โดยเฉพาะ **pharma, biotech, materials science, chemistry** — ROI model ควรเปลี่ยน. Case ที่เดิม uneconomic (ค่า postdoc + wet lab นาน 1–3 ปี ต่อ hypothesis ที่มี 5–10% chance work) ตอนนี้ **triage step แรก (screen 1M+ candidates → 20 leads) ทำได้ด้วย compute ราว ~$10–50k แทน $500k+ ของ labor**. ทีม R&D ที่ปรับ workflow ให้ AI screen ก่อน wet-lab last = throughput เพิ่ม 5–10x. **Pharma majors (Pfizer, Novartis, Roche)** และ **Xaira/Formation Bio/Recursion** จะเป็น first mover — ทีมไทย SCG, PTT, Betagro ที่มี R&D lab ควรเริ่ม pilot 1 project ภายในปีนี้

สำหรับ **ecosystem** — Anthropic กำลัง carve out **"science and bio partnership" niche** ที่ OpenAI ยังตามไม่ทัน. **AWS Bedrock, Google Vertex, Azure AI** จะเป็น distribution layer หลัก — Mythos tier require enterprise contract, distribution ผ่าน hyperscaler มี compliance framework พร้อม. Open-weight model (Llama, Mistral, DeepSeek) ยัง gap ใหญ่ — bio-adjacent capability ต้องการ tool-use + long-context reasoning + safeguards layer ที่ open-source ยังไม่ crack. **Signal 3 เดือน:** OpenAI น่าจะตอบด้วย "Deep Research Bio" หรือ Astra variant, Google น่าจะขยาย Isomorphic Labs deal, DeepMind อาจ open access ให้ AlphaFold 4 หรือ AlphaGenome. Race นี้ตัดสินกันที่ agent orchestration ไม่ใช่ base model quality อีกต่อไป

## Sources
- [Claude discovers a novel enzyme system — Anthropic](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)
- [Anthropic's 950 Claude agents found an enzyme system in 21 hours, and nobody knows what it does — mixed-news](https://mixed-news.com/en/claude-950-agents-art-enzyme-system-21-hours-harrington/)
- [Anthropic says Claude found a new enzyme system with CRISPR-like repeats — The Next Web](https://thenextweb.com/news/anthropic-claude-enzyme-system-crispr-like-repeats)
- [Claude Found a Mysterious CRISPR-Like System — but Anthropic Can't Say What It's Capable of — Gizmodo](https://gizmodo.com/claude-found-a-mysterious-crispr-like-system-but-anthropic-cant-say-what-its-capable-of-2000816906)
- [Anthropic's Claude AI discovers CRISPR-like enzyme system — Quartz](https://qz.com/anthropic-claude-crispr-like-enzyme-system-bacteriophage-092426)

---

## Audio script
วันที่ 24 กันยา 2026 Anthropic ปล่อย blog เรื่องที่จะเปลี่ยนความหมายของคำว่า agentic AI ในสายวิทยาศาสตร์ไปตลอด. ทีม Claude Science ให้ Claude Mythos 5 รันแบบ multi-agent 949 sessions พร้อมกัน ใช้เวลา 21 ชั่วโมงครึ่ง เผา 215 ล้าน token โดยไม่มีมนุษย์อยู่ในลูปเลย. brief ที่ให้ตอนต้นสั้นแค่ประโยคเดียว — หา reverse transcriptase system ใหม่ในฐาน protein cluster 1.9 พันล้าน entries. Agent วง outer scan database, agent วง inner ทำ hypothesis generation กับ candidate scoring. ผลลัพธ์ recover 200,000 enzyme cluster, score 3,564 candidate partner family, filed 19 report ให้นักวิทย์มนุษย์ review. หนึ่งในนั้นคือ ART หรือ array-associated reverse transcriptases — enzyme system ใหม่ที่ประกอบด้วย reverse transcriptase gene + accessory protein + long array ของ DNA repeat ที่โครงสร้างคล้าย CRISPR. Feng Zhang lab ที่ MIT ผู้พัฒนา CRISPR-Cas9 บอกว่า pattern แบบนี้ไม่เคยอยู่ใน literature มาก่อน. เจอเดียวยังไม่รู้ว่าทำอะไรได้ ต้อง wet-lab confirm อีก แต่ signal ใหญ่คือ — เป็นครั้งแรกที่ multi-agent AI ทำ novel discovery ที่ทดสอบได้จริง ในสาขาที่คนคิดว่า AI จะเข้าถึงยากที่สุด. ตัวเลขที่ควรจำ — Anthropic ใช้ compute ประมาณ 5 ถึง 15 พันดอลลาร์ทำงานเท่า postdoc 2 ถึง 3 คนตลอดปี. Curve ที่ Sam Altman พูดเรื่อง compute แทน headcount มา 3 ปีแล้ว ตอนนี้เห็นเป็นตัวเลขจริงในสายชีววิทยา. สำหรับ builder ที่ทำ agent orchestration framework — Anthropic internal harness ที่ handle 949 parallel session ระดับ production คือ template ใหม่ที่ open-source ต้องไล่ตาม. LangGraph, ADK, AutoGen ปัจจุบัน handle 5 ถึง 50 agent max. ใครสร้าง harness ที่ scale ระดับ 1000+ agent ได้ก่อน = ครอง mind share developer. สำหรับ pharma และ biotech ไทย — SCG, PTT, Betagro หรือ university R&D lab — ควรเริ่ม pilot 1 project ภายในสิ้นปีนี้ triage step แรกที่เดิม cost postdoc 500k ต่อ hypothesis ตอนนี้ทำได้ด้วย compute 10 ถึง 50k. ROI curve เปลี่ยนคนละโลก.
