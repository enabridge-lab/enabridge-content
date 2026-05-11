---
date: 2026-05-11
slug: anthropic-mythos-fed-treasury-bank-ceos-cyber
topic: agentic-ai
reading_time_min: 5
sources: 6
image_prompt: A hero illustration of a cracked open digital lock with binary code spilling out, set against a dark city skyline of financial district skyscrapers (Federal Reserve dome silhouette and bank towers). A glowing red shield labeled "MYTHOS" floats overhead, scanning the buildings with a beam of light. In massive condensed white sans-serif headline reads "271 ZERO-DAYS". A smaller second line reads "Fed + Treasury call bank CEOs". Editorial deep crimson and obsidian black palette, high contrast, magazine-cover composition, 1:1 aspect, no real human faces (silhouettes only). Style The Information / Stratechery dark cyber-thriller cover with cinematic depth.
image: images/26-05-12-0609-02-anthropic-mythos-fed-treasury-bank-ceos-cyber.png
---

# Anthropic Mythos จุดวิกฤต cyber ที่ Wall Street — Fed กับ Treasury เรียก CEO ธนาคารใหญ่, Dimon เรียก "very heightened risk", IMF เตือน global financial system

## TL;DR
- ปลายเมษา-ต้นพฤษภา 2026 Anthropic เปิดตัว **Mythos** — model cybersecurity-focused ที่หา vulnerabilities ใน software เก่าได้เร็วและลึกระดับใหม่ Mozilla confirm ว่า Mythos Preview พบ **271 zero-day** ใน Firefox ก่อน release version 150 ตัวก่อนหน้าของ Anthropic หาเจอประมาณ 20 เท่านั้น
- ระบบทั้ง software ตอนนี้ Mythos พบ vulnerability ระดับ **หมื่นรายการ** Dario Amodei เตือนว่ามี window **6-12 เดือน** ที่ต้อง patch ก่อน Chinese AI catch up; **Fed Chair Powell + Treasury Sec Bessent** เรียก CEO bank ใหญ่ประชุม cyber risk; **Jamie Dimon** เรียกว่า "very heightened risk to financial system"; **IMF** ออก formal warning ใส่ AI-driven cyberattacks
- **Project Glasswing** = controlled rollout ของ Mythos ที่ปลอย access เฉพาะ ~40 องค์กร (vendor + critical infrastructure) — asymmetric design ที่ Anthropic อยาก give defender head start ก่อน capability ออกสู่ตลาดกว้าง

## เกิดอะไรขึ้น

ในระยะ 3 สัปดาห์ตั้งแต่ Dario Amodei เข้า White House พบ Susie Wiles + Scott Bessent (17 เม.ย.) แล้ว Anthropic เปิดเปลือก **Mythos** — model ใหม่ที่ Anthropic ไม่ release public แต่ผ่าน **Project Glasswing** ปล่อย access เฉพาะ partner ที่ vetted ราว 40 องค์กร (vendor software + critical infrastructure + regulator) คุณสมบัติของ Mythos ที่ shock ทุกคน: **ความสามารถ identify vulnerability ในระดับ scale + depth ที่ AI ยังไม่เคยทำได้** Mozilla เปิดเผย 7 พ.ค. ว่า Mythos Preview พบ **271 zero-day vulnerabilities** ใน Firefox ระหว่าง pre-release audit ก่อน Firefox 150 release; เทียบกับ model Claude Sonnet 4.5 รุ่นปีที่แล้วของ Anthropic ที่หาเจอแค่ 20 รายการ ใน workload เดียวกัน

ตัวเลขทั้ง catalog vulnerability ที่ Mythos พบรวมทุก software เข้าไปอยู่ระดับ **tens of thousands** ส่วนใหญ่เป็นช่องโหว่ **decades-old** ที่ static analyzer + bug bounty tradition พลาดมาตลอด Anthropic ส่ง memo เข้า DHS + CISA + Treasury — และในช่วง 5-8 พ.ค. **Jerome Powell** (Fed Chair) กับ **Scott Bessent** (Treasury Sec) เรียก CEO ของ JPMorgan / BofA / Citi / Goldman / Morgan Stanley ประชุม cyber risk โดยเฉพาะ; **Jamie Dimon** ออกแถลงต่อสาธารณะว่า Mythos สื่อ "very heightened risk to the financial system" — language ที่ Dimon ใช้น้อยมากในรอบ 10 ปี **IMF** ออก formal advisory เตือน global financial system ว่า AI-driven cyber discovery กำลังเปลี่ยน threat model เร็วกว่าที่ regulator เตรียมตัว

Dario Amodei บอก CNBC ว่ามี **"6 ถึง 12 เดือน"** window ที่ defender ต้องใช้ patch tens of thousands vulnerabilities เหล่านี้ ก่อนที่ "Chinese AI" จะ catch up ความสามารถระดับเดียวกัน Anthropic อ้างว่า Project Glasswing intentional design ที่ asymmetric — ให้ defender ได้ตัว tool ก่อน attacker — แต่ tool ดูสุดท้ายจะ leak ผ่าน reverse engineering / open-source clone ภายในไม่กี่เดือน Pentagon (ที่ blacklist Anthropic ตั้งแต่ปลายปี 2025 ด้วย procurement issue) ก็ยังกล่าว Mythos เป็น "separate issue" คือ blacklist ยังอยู่ แต่ NSA ใช้ Mythos แบบลับๆ ตามที่ Axios scoop เมื่อ 19 เม.ย.

## ทำไมสำคัญ

นี่คือ **first prove case** ที่ AI สามารถ "เปลี่ยน threat landscape ระดับ macro" ได้จริง ไม่ใช่ research demo Mythos แสดงว่า model ที่ train + fine-tune สำหรับ specific task (vulnerability discovery) สามารถทำ work ที่ทีม security ทั้ง industry ทำมา 30 ปียัง miss — ในระดับ throughput ที่ economic-feasible สำหรับ vendor ที่จะ run ตัวเอง ใน 18 เดือนข้างหน้า vendor security ทุกราย (Snyk / Wiz / Veracode / Tenable) จะต้อง integrate Mythos-class capability หรือกลายเป็น irrelevant — และ market ของ application security testing ($2B+ ARR ในปัจจุบัน) จะ restructure ทั้งหมด

จุดที่จะกลับมา bite ระบบการเงินคือ **interconnectedness**: bank + payment network + utility share cloud provider + software stack เดียวกันเป็นส่วนใหญ่ ถ้า attacker (ที่ access Mythos-class model — รัฐหรือ criminal group ใหญ่) พบ vulnerability ใน **shared dependency** เช่น Kubernetes / OpenSSL / Java runtime — single exploit cascades ผ่าน sector ทั้งหมดในรอบเดียว นี่คือเหตุที่ Fed + Treasury เรียก CEO meeting; เหตุที่ IMF ออก advisory; และเหตุที่ Dimon ใช้ language ระดับ "very heightened risk" — เพราะเขามอง systemic risk ของ financial system ในแบบที่ regulator ไม่มอง

Contrarian angle ที่ underrated: **Anthropic กำลัง weaponize asymmetric AI security เป็น geopolitical lever** การที่ Dario warn "6-12 month window before Chinese AI catches up" บอกตรงๆ ว่า Anthropic position ตัวเองเป็น **defense partner ของ US government** (และมีโครงการที่ Anthropic + Palantir + SpaceX Colossus ที่ปิด deal $300M 5 พ.ค.) Mythos เป็น **commercial product ที่ทำ national security policy ในเวลาเดียวกัน** — playbook ที่ Lockheed Martin ใช้สมัย Cold War กับ ABM systems Microsoft + OpenAI ตอบไม่ทัน เพราะไม่มี model class นี้ + ไม่มี trust ของ White House ที่ Anthropic build ผ่าน 18 เดือนของ Responsible Scaling Policy + Constitutional AI brand

## มุม OpenBridge

OpenBridge ไม่ใช่ security vendor โดยตรง — แต่ Mythos จะเปลี่ยน expectation ของ **buyer enterprise ทุกคน** ในเรื่อง audit + compliance + data lineage ภายใน 6 เดือนทุก CIO จะถาม vendor MCP/integration ว่า "ถ้า Mythos-class scanner run บน connector ของคุณ เราจะเจออะไร" — OpenBridge ต้อง pre-empt คำถามนี้ด้วยการ run **internal Mythos-equivalent audit** ผ่าน Snyk + Anthropic Code Security partnership (ที่เปิด beta ตั้งแต่ 8 พ.ค.) บน MCP server stack ของเรา และ publish report ระดับ "Mythos-cleared MCP" เป็น differentiator vs competitor

Action ตรง: (1) **partner กับ Snyk** ที่มี Claude integration ในการ scan OpenBridge MCP code base + connector ทุกตัว — ออก quarterly SOC-style report; (2) **เพิ่ม "agent action audit log"** ที่ regulator-grade ทุก MCP call ของ OpenBridge ต้อง emit cryptographically-signed log ที่บ่งบอก agent identity + intent + outcome — เพราะใน world ที่ Mythos-class attacker fake agent ได้, audit trail ที่ tamper-proof จะกลายเป็น compliance requirement ของทุก SEA bank; (3) **partner กับ Bank of Thailand + SET cybersecurity unit** offer free Mythos-equivalent baseline audit ของ MCP integration ที่ Thai financial institution ใช้ — building trust ที่ frontier vendor ต่างประเทศไม่มี เพราะไม่มีคนภาษาไทยและไม่ได้นั่งคู่ regulator local

## Sources
- [Anthropic CEO warns 'moment of danger' as Mythos exposes vulnerabilities — CNBC](https://www.cnbc.com/2026/05/05/anthropic-ceo-cyber-moment-of-danger-mythos-vulnerabilities.html)
- [Anthropic's Mythos set off a cybersecurity 'hysteria.' Experts say the threat was already here — CNBC](https://www.cnbc.com/2026/05/08/anthropic-mythos-ai-cybersecurity-banks.html)
- [Claude Mythos Finds 271 Firefox Vulnerabilities — SecurityWeek](https://www.securityweek.com/claude-mythos-finds-271-firefox-vulnerabilities/)
- [Jamie Dimon Warns Anthropic's Mythos Represents 'Very Heightened Risk' To Financial System — CU Today](https://www.cutoday.info/Fresh-Today/Jamie-Dimon-Warns-Anthropic-s-Mythos-Represents-Very-Heightened-Risk-To-Financial-System)
- [How Anthropic's Mythos has rewritten Firefox's approach to cybersecurity — TechCrunch](https://techcrunch.com/2026/05/07/how-anthropics-mythos-has-rewritten-firefoxs-approach-to-cybersecurity/)
- [Claude Mythos Preview — red.anthropic.com](https://red.anthropic.com/2026/mythos-preview/)

---

## Audio script
ข่าวที่ต้องเข้าใจวันนี้คือ Anthropic ปล่อย model ชื่อ Mythos ที่หา vulnerability ของ software ได้ในระดับที่เปลี่ยน threat landscape ทั้งวงการ Mythos Preview พบ 271 zero-day ใน Firefox ก่อน release version 150 model รุ่นก่อนของ Anthropic หาได้แค่ 20 รายการในงานเดียวกัน รวม catalog vulnerability ที่ Mythos พบทุก software อยู่ระดับหมื่นรายการ ส่วนใหญ่เป็นช่องโหว่เก่าที่ static analyzer พลาดมาหลายสิบปี Fed Chairman Powell กับ Treasury Sec Bessent เรียก CEO ของ JPMorgan BofA Citi Goldman Morgan Stanley ประชุม cyber risk โดยเฉพาะ Jamie Dimon ใช้คำว่า very heightened risk to financial system IMF ออก formal warning ใส่ AI-driven cyberattacks Dario Amodei บอกว่ามี window 6 ถึง 12 เดือนต้อง patch ก่อน Chinese AI catch up Anthropic ปล่อย access เฉพาะ 40 องค์กรเรียกว่า Project Glasswing เป็น asymmetric design ให้ defender ได้ tool ก่อน attacker จุดที่จะกลับมา bite financial system คือ interconnectedness bank payment network utility ใช้ Kubernetes OpenSSL Java runtime ร่วมกัน ถ้าใครเจอ exploit ใน shared dependency เดียว มันจะ cascade ทั้ง sector ในรอบเดียว สำหรับ OpenBridge ภายใน 6 เดือนทุก CIO จะถาม vendor MCP ว่า ถ้า Mythos-class scanner run บน connector คุณจะเจออะไร เราต้อง pre-empt ด้วย Snyk Anthropic integration และ tamper-proof audit log ระดับ regulator-grade ครับ
