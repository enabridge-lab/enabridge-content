---
date: 2026-05-11
slug: 26-05-11-0606-02-pentagon-shuts-anthropic-8-bigtech-ai-contracts
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: A stylized Pentagon building rendered as a precise geometric icon, glowing seven golden contract scrolls flowing into its gates, each scroll labeled with a tech logo — OpenAI, Google, Microsoft, AWS, Nvidia, SpaceX, Reflection AI. To the side, one orange Anthropic logo is rendered with a red cancellation X stamped over it, frozen in mid-air with a small "Supply Chain Risk" label tag. Composition: editorial geopolitical illustration in muted slate-blue and gold palette, with sharp contrast for thumbnail readability, semi-realistic flat illustration with subtle shadows, dramatic backlighting, 1:1 aspect, no human faces.
image: images/26-05-11-0606-02-pentagon-shuts-anthropic-8-bigtech-ai-contracts.png
---

# Pentagon ปิดประตู Anthropic เซ็นสัญญา AI กับ 7 ยักษ์เทค — values vs procurement scale-up ครั้งแรก

## TL;DR
- 1 พ.ค. 2026 Pentagon ประกาศ partnership AI ข้าม classified network กับ 7 บริษัท: OpenAI, Google, Microsoft, AWS, Nvidia, SpaceX, Reflection AI — Anthropic ถูกตัดออก ทั้งที่ Claude อยู่ใน production ที่ Wall Street/NIH/รัฐบาลกลางอยู่แล้ว
- ที่มา: Anthropic ปฏิเสธปลด clause ห้ามใช้ Claude ใน "fully autonomous weapons + mass domestic surveillance" — Pentagon ตอบโดยติด supply-chain risk label เดือน มี.ค. 2026 (ป้ายที่เคยใช้กับ Huawei/ZTE)
- Anthropic ฟ้องที่ San Francisco + Washington DC; ผู้พิพากษา federal block executive order ของ Trump; Dario Amodei เข้าทำเนียบขาว 17 เม.ย. หลังเปิด Mythos (cyber threat detection tool) — Trump บอก CNBC ว่า deal ยังเป็นไปได้

## เกิดอะไรขึ้น

วันศุกร์ที่ 1 พฤษภาคม 2026 Department of Defense เปิดเผย agreement ใหญ่ที่สุดในประวัติศาสตร์ของ Pentagon บน AI procurement — **classified-network access AI contract ให้ 7 บริษัท**: OpenAI, Google, Microsoft, AWS, Nvidia, SpaceX, และ Reflection AI (startup จาก Mountain View ที่เพิ่งระดมทุนปลายปีก่อน). คำพูดที่ DoD ใช้เปิดประชุมคือ "เป้าหมายให้สหรัฐกลายเป็น AI-first fighting force" — แปลตรง ๆ คือ Pentagon จะใส่ generative AI ใน combat planning, intelligence triage, weapons targeting, ทุก layer ของ command structure ภายใน 18 เดือน

ที่ทำให้ story นี้ดัง คือ **Anthropic ถูกตัดออกอย่างจงใจ** — บริษัทที่ Claude อยู่ในระบบของ JPMorgan, Goldman, Citi, NIH, AWS GovCloud มาก่อนแล้ว; revenue run-rate $30B (3.3x ใน 5 เดือน); Dario Amodei เพิ่งอยู่ใน Wall Street briefing คู่ Jamie Dimon เมื่อสัปดาห์ก่อน. เหตุผลที่ Pentagon ออกมาบอก ไม่ใช่เรื่อง technical capability แต่ **policy disagreement**: Anthropic ปฏิเสธปลด clause ใน usage policy ที่ห้ามใช้ Claude สำหรับ "fully autonomous weapons systems" และ "mass domestic surveillance" — Pentagon ขอ exempt; Anthropic ปฏิเสธ; เดือน มี.ค. 2026 DoD ติด **supply-chain risk label** — label เดียวกับที่ใช้กับ Huawei/ZTE ในยุค Trump 1.0

Anthropic ตอบโต้สองด้าน: (1) ฟ้องที่ San Francisco + Washington DC challenging Trump executive order; ผู้พิพากษา federal ใน Northern District of California block executive order ชั่วคราว เดือน เม.ย.; case ยังอยู่ในศาล. (2) Dario Amodei เข้าทำเนียบขาว 17 เม.ย. พบ Chief of Staff Susie Wiles หลังจาก Anthropic เปิดตัว **Mythos** — frontier model ของ Anthropic ที่ออกแบบมา discover + fix zero-day vulnerability โดย autonomously โดยปล่อย preview ให้ AWS/Apple/Cisco/Google/JPMorgan/Microsoft เข้าถึงก่อน. Trump ตอบ CNBC ตรง ๆ ว่า deal ยังเป็นไปได้ — quote: "They're very smart, and I think they can be of great use" — แต่ Pentagon ยังคงสถานะ exclude

Pentagon Under Secretary for Research and Engineering Emil Michael ออกมาให้ context ใน press briefing: "เราจะไม่ใช้ AI provider เดียวอีก never again" — สะท้อนว่า lessons learned จาก vendor concentration risk เดียวที่ตลอดยุค cloud (AWS dominant DoD JEDI/JWCC) สอนไว้ — และที่สำคัญ Reflection AI ใน list ของ 7 บริษัทคือ deliberate choice: Pentagon ต้องการ vendor diversity ที่ frontier model layer ไม่ใช่แค่ application layer

## ทำไมสำคัญ

Story นี้คือ **first values vs scale crossroad ที่ public** ในยุค frontier AI procurement — และ Anthropic เลือก values. ทุก vendor frontier model อื่น (OpenAI, Google, xAI) ปลดหรือไม่เคยมี clause autonomous weapons ตั้งแต่แรก. Anthropic positioning ตัวเองมาตั้งแต่ปี 2023 ว่าเป็น "safety-first lab" — และ Pentagon exclusion พิสูจน์ว่า positioning ตัวนี้มี real-world cost. **Federal government TAM** ที่ AWS/Microsoft Azure Government งานละ $1-10B/ปี แต่ตอนนี้ Anthropic ขายเข้าได้ผ่าน AWS GovCloud (Claude ใน Bedrock) — แต่ contract direct DoD ปิดประตู ไว้แล้ว

Pattern ที่จะเห็นต่อ: (1) **Anthropic จะ double down enterprise non-defense vertical** — Wall Street, Healthcare, Legal, Media — ที่ values-driven positioning เป็น asset ไม่ใช่ liability. Strategy นี้ visible ตั้งแต่ Code w/ Claude 2026 (Dreaming, Outcomes, Multi-Agent Orchestration) + Wall Street briefing 5 พ.ค. + Microsoft 365 add-in + Moody's MCP — ทุกอย่างวิ่งหา Fortune 500 commercial customer (2) **Reflection AI กับ vendor diversity bet** เปิดทางให้ frontier model lab รุ่นสอง (Mistral, Cohere, AI21) จะ pitch DoD แบบ "we have no weapons clause restriction" — ตลาดเฉพาะของ "frontier AI without ethical guardrail" จะกลายเป็น category ใหม่ (3) **Anthropic Mythos** เปิดให้ enterprise commercial — เป็น defensive cybersecurity ที่ตรงข้ามกับ offensive — และเป็น signal ของ middle ground ที่ Anthropic จะลองเปิด door ทำเนียบขาว

ที่สำคัญที่สุด: **AI ethics ไม่ใช่ทฤษฎีอีกต่อไป** — มันคือ procurement filter ที่ตอนนี้แยก vendor ที่ขายได้ vs ขายไม่ได้ในตลาดเฉพาะ. CFO/CISO/General Counsel ของ enterprise non-defense กำลังถาม vendor frontier model ว่า "ใครคือลูกค้าทหารของคุณ?" คำตอบของ Anthropic ("ไม่มี under autonomous weapons clause") กลายเป็น sales weapon ใน healthcare/insurance/legal ที่ liability-aware

## มุม OpenBridge

OpenBridge ไม่ direct เกี่ยวกับ defense procurement — แต่ adjacent insight สำคัญสี่ข้อ:

(1) **Vendor-neutral connector layer คือ value มากขึ้นเมื่อ frontier model market แตก** — เมื่อ JPMorgan ใช้ Claude, Citi ใช้ GPT, Goldman ใช้ทั้งคู่ + Mythos, และ DoD ใช้ OpenAI/Reflection ที่ไม่ใช่ Anthropic — application layer ต้องการ MCP server ที่ทำงานข้าม model. OpenBridge สามารถ position ว่า **"connector ของเราเป็น Switzerland ของ frontier AI war"** — ลูกค้าเลือก model ได้โดยไม่ rewrite integration

(2) **Usage policy + audit trail กลายเป็น default requirement** — ที่ DoD ขอ Anthropic ปลด clause autonomous weapon คือสัญญาณว่าทุก enterprise contract ขนาดใหญ่จะ require **policy enforcement ระดับ tool call**. OpenBridge connector ที่ emit immutable audit log + tag policy (e.g. "this connector call exceeded data classification boundary") จะเป็น compliance asset ที่ขายเข้า regulated industry ได้ — ตลาดเดียวกับที่ AWS GuardDuty, Azure Sentinel กิน

(3) **Mythos-style defensive AI** เป็น product category ใหม่ที่ OpenBridge อาจ enable — ไม่ใช่สร้างเอง แต่เป็น **connector ที่ทำงานกับ defensive cyber agent** (Anthropic Mythos, CrowdStrike Charlotte, Microsoft Defender XDR) — feed asset inventory, vulnerability scanner result, threat intel ตรงเข้า agent decision loop. Enterprise SOC ที่ deploy agent ที่ access ข้อมูลใน 30 ระบบ ต้องการ trusted connector layer ที่มี audit trail

(4) **Thai/SEA defense procurement** ขยับช้ากว่า US 12-24 เดือน — แต่ pattern เดียวกัน. ถ้า OpenBridge build ภาพลักษณ์ "vendor neutral + audit-ready connector" ตั้งแต่ตอนนี้ จะเป็น default choice ของกระทรวงกลาโหมไทย/Indonesia/Singapore ตอนเริ่มดีล AI procurement ในปี 2027-2028 — ไม่ใช่เพราะเราขาย defense แต่เพราะ enterprise IT ที่ procure จะใช้เกณฑ์เดียวกัน

## Sources
- [Pentagon strikes deals with 8 Big Tech companies after shunning Anthropic (CNN)](https://www.cnn.com/2026/05/01/tech/pentagon-ai-anthropic)
- [Pentagon freezes out Anthropic as it signs deals with AI rivals (Defense News)](https://www.defensenews.com/news/pentagon-congress/2026/05/01/pentagon-freezes-out-anthropic-as-it-signs-deals-with-ai-rivals/)
- [Pentagon will 'never again' rely on a single AI provider (Defense One)](https://www.defenseone.com/policy/2026/05/pentagon-will-never-again-rely-single-ai-provider-official-says/413409/)
- [Pentagon Signs AI Deals With OpenAI, Google, Microsoft, Nvidia, and Others (gHacks)](https://www.ghacks.net/2026/05/04/pentagon-signs-ai-deals-with-openai-google-microsoft-nvidia-and-others-cutting-out-anthropic/)

---

## Audio script
วันที่ 1 พฤษภาคม 2026 Pentagon ประกาศ partnership AI ใหญ่ที่สุดในประวัติศาสตร์ของกระทรวงกลาโหมสหรัฐ เซ็นสัญญาเข้าถึง classified network ให้กับ 7 บริษัทเทคใหญ่ — OpenAI, Google, Microsoft, AWS, Nvidia, SpaceX และ Reflection AI. แต่ที่กลายเป็นข่าว คือชื่อที่หายไป — Anthropic ที่ Claude อยู่ใน production ของ JPMorgan, Goldman, Citi, NIH อยู่แล้ว ถูกตัดออกอย่างจงใจ. เหตุผลคือ Anthropic ปฏิเสธปลด clause ใน usage policy ที่ห้ามใช้ Claude สำหรับ autonomous weapons และ mass surveillance — Pentagon ขอ exempt, Anthropic ปฏิเสธ, แล้วเดือน มี.ค. ติดป้าย supply chain risk เหมือนที่เคยใช้กับ Huawei. Anthropic ฟ้องที่ศาล federal สองที่ และ Dario Amodei เข้าทำเนียบขาวพบ Chief of Staff Susie Wiles เมื่อ 17 เม.ย. หลังเปิด Mythos — tool หา zero-day vulnerability แบบ autonomous. Trump บอก CNBC ตรงๆว่า deal ยังเป็นไปได้ แต่ Pentagon ยังคงสถานะ exclude. ความหมายของ story นี้: AI ethics ไม่ใช่ทฤษฎีอีกต่อไป — มันกลายเป็น procurement filter ที่แยก vendor ที่ขายได้ vs ขายไม่ได้ในแต่ละตลาด. Anthropic เลือก values แล้วเสียตลาด defense ใหญ่ — แต่ได้ moat ใน Wall Street, healthcare, legal ที่ liability-aware. สำหรับ OpenBridge อ่านได้สี่อย่าง: connector layer ที่ vendor neutral มี value มากขึ้นเมื่อ frontier market แตก; usage policy และ audit trail ต้องเป็น default ใน wire format; ตลาด defensive cyber agent style Mythos กำลังโต OpenBridge สามารถเป็น connector layer; และ Thai SEA defense procurement จะตามมา 12 ถึง 24 เดือน ลักษณะเดียวกัน
