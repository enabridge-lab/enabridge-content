---
date: 2026-11-16
slug: bay-50m-agent-action-vetting
topic: agentic-ai
reading_time_min: 3
sources: 4
image_prompt: |
  An editorial isometric illustration of a transparent glass checkpoint
  tunnel at center-stage with three AI agent avatars (small robot
  silhouettes) queued in line. The first agent passes through a gate
  labeled "ALLOW" glowing green; the second hits a red X gate labeled
  "BLOCK"; the third gets escalated via a conveyor to a human silhouette
  above. A big floating title panel reads "$50M - BAY" and below it
  "$37M SERIES A + $13M SEED". Clean editorial style, soft teal and warm
  red palette, 1:1 aspect, no real human faces (silhouettes OK), high
  contrast so numbers read at 200px.
image: images/26-11-17-0605-05-bay-50m-agent-action-vetting.png
---

# Bay โผล่จาก stealth $50M — Battery Ventures + Wiz CEO เดิมพันว่า "ตรวจก่อนปล่อย" คือ moat ของ agent security

## TL;DR
- Bay Security บริษัท Tel Aviv ออกจาก stealth 10 พ.ย. ด้วย $50M รวม — Series A $37M นำโดย Battery Ventures + seed $13M นำโดย YL Ventures
- Product intercept ทุก action ที่ agent เสนอก่อน execute แล้วตัดสิน allow / block / escalate ไปหา human — รันบน device ระดับ endpoint ของ user
- ก่อตั้งมกราคม 2026 มีลูกค้าแล้ว Micron, Peloton, ClickUp, Wix — ARR ทะลุ $3M ภายใน 6 เดือน

## เกิดอะไรขึ้น
10 พ.ย. Bay ประกาศปล่อย platform พร้อม funding รวม $50M แบ่งเป็น Series A $37M นำโดย Battery Ventures (ร่วมด้วย Micron Ventures, Microsoft M12, Assaf Rappaport CEO ของ Wiz) + seed round $13M นำโดย YL Ventures และ Striker Venture Partners บริษัทตั้งมกราคม 2026 — เพียง 10 เดือนก็ raise รวม 50 ล้านพร้อม logo ลูกค้า Micron, Peloton, ClickUp, Wix ตามรายงานของ TheSaaSNews ARR ก็แตะ $3M แล้ว — ตัวเลขที่ดีมากสำหรับอายุไม่ถึงปี

Product จุด unique คือ "on-device action gating" — agent AI ที่ทำงานบน endpoint (desktop, server ภายใน) ทุกครั้งที่จะ execute action — เปิด file, call API, run command, write database — Bay สกัด action นั้นก่อน แล้วเทียบกับ policy แล้วตัดสิน allow / block / escalate ให้มนุษย์ตรวจ Pattern นี้แตกต่างจาก network-level security (เช่น Palo Alto Prisma AIRS หรือ Zscaler) ที่ตรวจ API call ที่ออก internet — Bay ตรวจที่ application layer ของ endpoint ก่อน call ออกไปด้วยซ้ำ

Rappaport CEO ของ Wiz ที่ลงทุนส่วนตัวแปลว่าเขาเห็น pattern — ปี 2020 Wiz ชนะด้วย agentless cloud security ที่ scan ลึก ไม่ต้อง deploy agent ปี 2026 ตลาด agent security ย้อนกลับ — agent คือ attack surface และ "control before execution" กลายเป็น primary control plane

## ทำไมสำคัญ
ตลาด AI agent security กำลัง segment ตัวเองชัดเจนภายใน 6 เดือน — (1) **Identity layer** (Palo Alto/Clutch, Persona, Mintive — ที่ดูแล "ใครเป็น agent"), (2) **Action layer** (Bay, Kindo — ที่ดูแล "agent ทำอะไรได้บ้าง"), (3) **Network layer** (Zscaler, Prisma AIRS — ที่ดูแล "agent คุยกับใครได้"), (4) **Audit layer** (CrowdStrike Guardian, Fiddler — ที่ post-hoc review) ตลาด 4 layer นี้ไม่ compete ตรง — ทุกคนเชื่อว่า enterprise จะซื้อทั้ง 4 layer

Bay มี thesis ที่กล้าเฉพาะตัว — vendor ของ model (Claude, OpenAI) ทำ pre-execution gate บน API server ตัวเองได้จำกัด เพราะไม่รู้ context ของ enterprise (policy เฉพาะ, data sensitivity) — Bay ที่รันบน endpoint ของลูกค้าเห็น context เต็ม จึง enforce policy ที่ granular กว่ามาก เช่น "agent copy paste ข้อความจาก PDF source ไปสู่ external email" blocked ในขณะที่ "agent copy paste ข้อความจากเดียวกันไป internal Slack" ผ่าน — level ของ control ที่ model vendor ตัวเองทำไม่ได้

Caveat — model ทางธุรกิจที่ run on-device + endpoint deploy มี friction สูง enterprise IT ต้อง evaluate security ของ agent ตัว Bay เอง (fail open / fail closed?), latency ที่เพิ่มในทุก action, false positive rate ที่ block งาน normal ความเหลื่อมล้ำ product-market fit อีก 12 เดือนจะเห็นว่าใครชนะในแต่ละ layer ถ้า Bay ต้องแข่งกับ Microsoft Defender ที่ embed ใน Windows หรือ CrowdStrike Falcon ที่ deploy แล้ว — distribution ของ incumbent อาจชนะ technology ของ startup

## มุม AI Agent Platform
Builders — ถ้าคุณสร้าง agent product และขาย enterprise นี่คือ signal ว่า "allow/block/escalate framework" กำลังกลายเป็น standard UX — agent ของคุณต้อง expose structured action manifest (what it wants to do, which resource, what parameter) ให้ gate layer อย่าง Bay / Kindo / policy engine ประเมินได้ ไม่ใช่ opaque LLM call Builders ควร support OpenTelemetry + action trace format ที่ emerging — ไม่งั้นลูกค้า enterprise จะ reject ที่ security review

Users/business — ถ้า agent AI ของคุณเริ่ม touch production system (ไม่ใช่แค่ chatbot read-only) ต้องมี plan สำหรับ action-level gate ภายใน 6 เดือน evaluate ว่า jointly deploy Bay, Kindo, หรือ build in-house ขึ้นอยู่กับ (1) จำนวน endpoint ที่ agent รัน, (2) regulatory overlay, (3) ทีม IT size สำหรับ SMB มีทางเลือก outsource via SIEM + MSSP เพิ่มขึ้นในปีหน้า

Ecosystem — Microsoft M12 ลงทุน Bay ในขณะที่ Microsoft ตัวเองก็ ship Defender for AI แปลว่า Microsoft hedge — ไม่เชื่อมั่นว่า Defender จะคุมตลาด agent security ทั้งหมด เป็น pattern เดียวกับ Palo Alto Networks acquired Clutch — vendor ที่ใหญ่สุดยอมรับว่าตลาด agent security ใหม่พอจน startup กินได้ชัด Bay ถ้าโตต่อเนื่อง เป็น candidate acquisition ของ Palo Alto, CrowdStrike, หรือ Wiz เอง ภายใน 18–24 เดือน

## Sources
- [Bay raises $50m to vet AI agent actions before they run (TheNextWeb)](https://thenextweb.com/news/bay-50m-ai-agent-security-stealth-battery-ventures)
- [Bay raises $50 million to control what enterprise AI agents can do (SecurityWeek)](https://securityweek.com/bay-raises-50-million-to-control-what-enterprise-ai-agents-can-do)
- [Bay AI Launches With $50M to Vet AI Agent Actions On-Device (AI Weekly)](https://aiweekly.co/alerts/bay-ai-launches-with-50m-to-vet-ai-agent-actions-on-device)
- [Bay surpassed 3M ARR six months after inception (ARR Club)](https://www.arr.club/bay/bay-surpassed-3m-arr-six-months-after-inception-raising-50m)

---

## Audio script
Bay บริษัท AI agent security จาก Tel Aviv เพิ่งออกจาก stealth เมื่อ 10 พฤศจิกายน ด้วยเงินรวม 50 ล้านดอลลาร์ แบ่งเป็น Series A 37 ล้านนำโดย Battery Ventures และ seed 13 ล้านนำโดย YL Ventures นักลงทุนที่น่าสนใจคือ Assaf Rappaport ซีอีโอของ Wiz ลงทุนเงินส่วนตัว เท่ากับว่าคนที่ชนะในตลาด cloud security รุ่นก่อนเดิมพันว่า agent security คือคลื่นต่อไป

สิ่งที่ทำให้ Bay แตกต่างคือ on-device action gating — ทุกครั้งที่ AI agent จะ execute action เช่นเปิด file call API หรือ write database Bay สกัด action นั้นที่ endpoint ก่อน แล้วเทียบกับ policy แล้วตัดสิน allow block หรือ escalate ไปที่มนุษย์ ต่างจาก network-level security ที่ตรวจ API call ที่ออก internet Bay ตรวจที่ application layer ก่อน call ออกไปด้วยซ้ำ

ตลาด agent security กำลัง segment ตัวเองเป็น 4 layer ชัดเจน identity ใครเป็น agent action agent ทำอะไรได้ network agent คุยกับใคร และ audit หลังเกิดเหตุแล้วต้อง review อะไร Bay อยู่ที่ action layer แข่งกับ Kindo สำหรับ Enabridge และคนที่สร้าง agent platform หมายความว่าต้อง expose action manifest ที่โครงสร้างชัด ไม่ใช่ opaque LLM call ไม่งั้นลูกค้า enterprise ที่ compliance หนัก reject ตอน security review แน่นอนครับ
