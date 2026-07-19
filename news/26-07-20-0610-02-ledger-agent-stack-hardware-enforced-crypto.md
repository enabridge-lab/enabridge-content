---
date: 2026-07-20
slug: ledger-agent-stack-hardware-enforced-crypto
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  A conceptual editorial illustration split into two panels. Left panel: a
  glowing brain-shaped AI agent surrounded by floating icons of crypto tokens
  and transaction requests, labeled "AGENT PROPOSES". Right panel: a physical
  hardware device — a matte black Ledger-style hardware wallet with an OLED
  screen showing "APPROVE?" and a big glowing button, labeled "HUMAN APPROVES".
  A giant vertical air-gap line separates the two panels, labeled
  "PRIVATE KEYS NEVER CROSS". Bottom banner: "AGENT STACK · OPEN SOURCE".
  Editorial isometric style, high contrast, dark navy background, 1:1 aspect,
  no real human faces.
image: images/26-07-20-0610-02-ledger-agent-stack-hardware-enforced-crypto.png
---

# Ledger Agent Stack: agent วางแผน hardware อนุมัติ — pattern ที่ enterprise agent ควรลอก

## TL;DR
- Ledger เปิด Agent Stack แบบ open-source เมื่อ 15-16 ก.ค. — toolkit ให้ AI agent อ่านยอด, เตรียม transaction, แนะนำ action ใน crypto portfolio โดย **ไม่ต้องถือ private key**
- Core philosophy: "Agents propose, humans approve" — hardware wallet บังคับให้ user กด confirm ทุก transaction ที่ agent จะยิง
- MoonPay + Shisa.ai เข้าใช้ตั้งแต่ launch — signal ว่า pattern "agent วางแผน hardware บังคับ" กำลังจะกลายเป็น security architecture สำหรับ enterprise agent ทั่วไป ไม่ใช่แค่ crypto

## เกิดอะไรขึ้น
Ledger บริษัท hardware wallet ที่ใหญ่ที่สุดในโลก ปล่อย Agent Stack แบบ open-source เมื่อ 15-16 กรกฎาคม 2026 เป็นชุด toolkit ให้ AI agent เข้าถึง crypto portfolio ได้ — อ่านยอด, เตรียม transaction, แนะนำ swap / stake / rebalance — โดย private key ยังคงอยู่ใน secure element ของ hardware device เท่านั้น. เมื่อ agent เตรียม transaction เสร็จ, hardware device จะแสดงรายละเอียดบน OLED แล้ว user ต้องกดยืนยัน — ถ้า agent ถูก compromise หรือ prompt-injection ให้ยิงเงินไปที่อยู่ผิด, hardware จะเป็น last line of defense.

Stack ประกอบด้วย 3 layer: **Device Management Kit Skills** (ให้ agent framework คุยกับ Ledger device ได้), **Ledger Wallet CLI** สำหรับ programmatic access เพื่อเช็คยอดและเตรียม tx, และ **Ledger Enterprise CLI** สำหรับ treasury team ระดับสถาบัน. MoonPay + Shisa.ai ประกาศ integrate ตั้งแต่ launch day. Ledger ยังบอก roadmap ว่า Q3 2026 จะเปิดตัว **Agent Intents & Policies** ที่ให้ developer เขียน hardware-enforced spending rules — เช่น "agent yield-farm ได้ไม่เกิน $10K/day, ห้ามยิงไปที่อยู่ใหม่ที่ไม่ผ่าน allowlist".

Pascal Gauthier CEO ของ Ledger พูดตรงในแถลงการณ์เปิดตัว: agent AI จะกลายเป็น attack surface ใหม่ที่ใหญ่ที่สุดในโลก crypto — model ถูก jailbreak, prompt injection ผ่าน MCP tool, RAG poisoning ผ่าน chain data — Agent Stack คือคำตอบว่า "อย่าให้ agent ถือของแรง, ให้ hardware เป็น trust anchor เสมอ".

## ทำไมสำคัญ
เรื่องนี้ไม่ใช่แค่ประเด็น crypto — เป็น **security architecture pattern ที่ enterprise agent ทุกอุตสาหกรรมควรลอก**. ปีที่ผ่านมา, deployment รอบใหญ่ของ agent เจอปัญหาซ้ำ ๆ: agent ถูกหลอกให้อนุมัติ refund, agent ยิง email ผิดปลายทาง, agent เขียนโค้ดที่มี backdoor, agent ยิง SQL DELETE โดยไม่ถามใคร. คำตอบเดิมคือ "human-in-the-loop" ผ่าน UI — แต่ UI ปลอมได้ (screen-share malware, browser extension) และ user มัก approve แบบ auto-pilot.

Ledger เสนอ pattern ที่แข็งกว่า: **แยก plan/propose ออกจาก execute/approve ผ่าน physical trust boundary**. Agent อยู่ในโลก software เต็มระบบ — LLM, tool call, MCP, planner — แต่ moment ที่จะยิง action ที่มี irreversible cost, ต้องผ่าน device ที่ compromise คนละ threat model. เทียบกับ credit card ที่ต้องเสียบชิป, Passkey ที่ต้อง TouchID, 2FA hardware key — Agent Stack คือ Yubikey ของ agent era.

Pattern นี้ตอบโจทย์ AI Act ของ EU และ US Executive Order ที่กำลังพูดเรื่อง "meaningful human control" over autonomous systems ในสัปดาห์ที่ผ่านมา. ในโลกที่ agent จะถือ credential กับ SaaS งาน finance, HR, procurement, การมี trust anchor ที่ compromise แยกจาก application layer จะไม่ใช่ nice-to-have — จะเป็น compliance requirement.

## มุม AI Agent Platform
สำหรับ **builders**: ถ้าคุณสร้าง agent framework, เริ่มออกแบบ approval boundary ตั้งแต่วันแรก. อย่าให้ agent ถือ credential ที่สั่งจ่ายเงินโดยตรง — ให้ agent เขียน "intent" (transfer $500 to vendor X for invoice Y), ส่ง intent ผ่าน queue ที่มี policy engine, แล้วให้ human sign ผ่าน device แยก (hardware key, mobile app ที่มี biometric). Ledger กำลัง set precedent ว่า SDK สำหรับ agent boundary เป็น product แยกที่ขายได้ — คาดว่า Okta, CyberArk, HashiCorp จะออกคู่แข่งใน 6 เดือนข้างหน้า.

สำหรับ **users / business ที่ deploy agent**: ถามคำถามนี้ทุกครั้งก่อน deploy — "ถ้า agent ตัวนี้โดน prompt injection วันนี้, worst case damage คือเท่าไหร่ กี่ transaction ถึงเราหยุดทัน?". ถ้าคำตอบคือ "เยอะ" หรือ "ไม่รู้", แปลว่ายังไม่มี hardware-level boundary. สำหรับ **ecosystem**: crypto industry มักจะเป็น testing ground ของ security pattern ก่อน mainstream (hardware wallet, MPC, TSS, zero-knowledge proof ล้วนเริ่มที่นี่). "Agent propose, hardware enforce" อาจจะเป็น pattern ต่อไปที่ enterprise IAM vendor ต้อง ship ภายในสิ้นปี.

## Sources
- [Ledger Agent Stack: open-source AI crypto toolkit launch](https://quasa.io/media/ledger-launches-open-source-agent-stack-for-ai-crypto-management)
- [CoinDesk: Ledger wants AI agents to manage crypto without holding your keys](https://www.coindesk.com/tech/2026/07/15/ledger-wants-ai-agents-to-manage-crypto-without-holding-your-keys)
- [SiliconANGLE: Ledger launches Agent Stack to keep AI agents away from crypto keys](https://siliconangle.com/2026/07/16/ledger-launches-agent-stack-keep-ai-agents-away-crypto-keys/)
- [The Block: Ledger unveils hardware-backed Agent Stack](https://www.theblock.co/post/408549/ledger-unveils-hardware-backed-agent-stack)

---

## Audio script
วันนี้มีข่าวที่ทีมทำ agent ทุกอุตสาหกรรมควรฟังครับ Ledger บริษัท hardware wallet ที่ใหญ่ที่สุดในโลก ปล่อย Agent Stack แบบ open-source เมื่อ 15-16 กรกฎา เป็น toolkit ให้ AI agent อ่านยอด เตรียม transaction แนะนำ action ในกระเป๋า crypto โดยที่ private key ไม่เคยออกจาก hardware device เลย core philosophy สั้นมากครับ Agents propose humans approve agent วางแผน คนกดยืนยัน ถ้า agent โดน jailbreak หรือ prompt injection ให้ยิงเงินไปที่อยู่แปลก hardware wallet บน OLED จะเป็น last line of defense คนต้องกดปุ่มจริงถึงจะยิงได้ Stack มี 3 layer ครับ Device Management Kit Skills ให้ agent framework คุย device ได้ Wallet CLI สำหรับ programmatic access และ Enterprise CLI สำหรับ treasury team MoonPay กับ Shisa.ai เข้าใช้ตั้งแต่วันแรก ทำไมผมมองว่าเรื่องนี้ใหญ่กว่า crypto ปีที่ผ่านมา deployment agent เจอปัญหาซ้ำๆ agent ถูกหลอกอนุมัติ refund agent ยิง email ผิดปลายทาง agent เขียนโค้ดฝัง backdoor คำตอบเดิมคือ human in the loop ผ่าน UI แต่ UI ปลอมได้ user ก็มัก approve แบบ auto pilot Ledger เสนอ pattern ที่แข็งกว่าคือแยก propose ออกจาก execute ผ่าน physical trust boundary agent อยู่ในโลก software เต็มระบบ แต่ moment ที่จะยิง action ที่มี irreversible cost ต้องผ่าน device ที่ compromise คนละ threat model นี่คือ Yubikey ของ agent era ครับ ผมคาดว่า Okta CyberArk HashiCorp จะออกของแบบเดียวกันใน 6 เดือน สำหรับทีม deploy agent ถามคำถามนี้ทุกครั้งครับ ถ้า agent ตัวนี้โดน prompt injection วันนี้ worst case damage เท่าไหร่ กี่ transaction กว่าเราจะหยุดทัน ถ้าตอบไม่ได้ แปลว่ายังขาด hardware level boundary
