---
date: 2026-10-07
slug: 26-10-08-0615-02-ox-security-15465-mcp-servers
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  Editorial hero: a vast grey mall-like registry of thousands of identical
  server kiosk doors stretching toward a vanishing point, each stamped with
  a small "MCP" plate. Four doors glow red and are enlarged near the viewer,
  stamped with flags "CN × 19", "RU × 18", "HOME NETWORK", "DOMAIN FOR $4".
  A giant audit stamp overlay reads "15,465 SERVERS · 0 GOVERNANCE". Thin
  broken security tape on several nearby doors. Isometric editorial
  illustration, high-contrast slate grey with warning red accents, 1:1
  aspect, no real human faces.
image: images/26-10-08-0615-02-ox-security-15465-mcp-servers.png
---

# OX Security: 15,465 MCP server สาธารณะ, 0 governance — เอเจนต์คุณกำลังต่อ tool กับโฮมเน็ตเวิร์กที่ไหนไม่รู้

## TL;DR
- **OX Security** รายงาน "15,465 MCP Servers, 0 Governance" — audit จาก 3 registry หลัก (mcp-official-registry, cline-marketplace, github-mcp-registry) + สัปดาห์นี้ Hacker News นำไปวิเคราะห์ซ้ำ
- จาก 5,095 unique hostnames: **15.6%** อยู่นอกสหรัฐ — รวม **19 เซิร์ฟเวอร์ในจีน**, **18 ในรัสเซีย**, จำนวนไม่น้อยซ่อนหลัง consumer tunneling service (ngrok, Cloudflare Tunnel) ชี้มา home network จริง
- **6 โดเมนถูกทิ้ง** พร้อมให้ซื้อใหม่ที่ **$4** — ใครก็ตามซื้อโดเมนเดิมได้แล้วรับ MCP traffic ของ enterprise ที่ยัง config ค้าง

## เกิดอะไรขึ้น

**OX Security Research** เผยแพร่รายงานชื่อ **"15,465 MCP Servers, 0 Governance"** เมื่อ 24 กันยายน แต่ **สัปดาห์นี้ (ต้น ต.ค. 2026)** The Hacker News และ Runtimewire หยิบขึ้นมาวิเคราะห์ซ้ำพร้อมสัปดาห์ของ MCP Dev Summit — timing ที่ทำให้คำถาม "scope ของ MCP ครอบ governance ไหม" กลายเป็น existential question ของทั้ง ecosystem

วิธีการวิจัย: OX สแกน MCP server ที่ลงทะเบียนในสาม public registry หลัก — **mcp-official-registry, cline-marketplace, github-mcp-registry** — รวม 15,465 รายการ, จากนั้น resolve เป็น 5,095 unique hostnames สำหรับวิเคราะห์ infrastructure. ตัวเลขที่ชกเข้าตา: 

- **15.6%** ของ hostname resolve ไป infrastructure นอกสหรัฐ — รวม **19 host ในจีน**, **18 ในรัสเซีย**
- จำนวนมากของที่เหลือเป็น home network จริง — ส่วนใหญ่ซ่อนหลัง **consumer tunneling service** เช่น ngrok, Cloudflare Tunnel, localhost.run — ซึ่งหมายความว่า agent enterprise ที่ connect ไป MCP server นั้นกำลังคุยกับ laptop ส่วนตัวใน Starbucks ที่ไหนสักแห่ง
- **6 โดเมนที่โฆษณาเป็น MCP server endpoint ถูกทิ้ง** และปัจจุบันเปิดให้ซื้อใหม่ที่ **$4 ต่อโดเมน** — ใครก็ตามจ่าย $24 สามารถครอง MCP endpoint ที่ยังมี agent config ค้างได้ทันที

OX ระวังในการสรุป — รายงานไม่ได้บอกว่า enterprise ใช้เซิร์ฟเวอร์พวกนี้จริงหรือเปล่า เป็นแค่ **"potential exposure"**. แต่ประเด็นสำคัญคือ ไม่มี marketplace vetting เลยในสามรายการนั้น. OX ยังเตือนด้วยว่ารายงานก่อนหน้าของพวกเขา (April 2026) เรื่อง MCP SDK stdio transport RCE Anthropic ตอบว่า **"behavior by design — sanitization is the developer's job"** — เป็นสัญญาณว่า ownership ของ security ถูกโยนไปที่ developer / integrator ไม่ใช่ protocol maintainer

ของแถม: **The New Stack** รายงานในสัปดาห์เดียวกันว่า MCP server บางตัวเผา **18,000 token ก่อนเริ่มทำอะไร** เพราะ tool manifest ยาวเกิน — เป็นปัญหา economic อีกชั้นที่ซ้อนทับ security

## ทำไมสำคัญ

Pattern สำคัญคือ **"supply chain ของ agent" ไม่ใช่แค่ model + framework** — มันครอบ MCP server ที่ agent connect ไปด้วย และ layer นี้ไม่มีการ gatekeep. เทียบ npm, PyPI, Docker Hub ที่ใช้เวลา 10+ ปีกว่าจะมี vetting ที่เริ่มใช้งานได้ (signed packages, provenance via SLSA, Trivy / Grype scanner) — MCP registry กำลังถูกใช้จริงทั้งที่ยังไม่มีกลไกเทียบเท่าแม้แต่ชั้นแรก

เลข **$4 per abandoned domain** คือข้อมูลที่น่ากลัวที่สุดสำหรับ CISO: cost ของ attack ถูกกว่า Starbucks แก้วเดียว. ประวัติศาสตร์ supply chain attack (SolarWinds, event-stream, left-pad) บอกเราแล้วว่าแค่ควบคุม upstream artifact เดียวก็เข้าถึง enterprise ได้มหาศาล — การ ยึด MCP domain เดิมคือ playbook เดียวกันในชั้นใหม่

Signal กับตลาด: หมวด **"MCP Gateway / MCP firewall / MCP identity"** จะเป็นหมวด hot ของปี 2027 — คล้ายที่ **container security** (Aqua, Sysdig, Prisma Cloud) โตขึ้นมาเมื่อ docker adoption แตะ scale. ดู funding ของ **AIR Security** ($50M รอบ Sept 2026) เป็น signal แรก. คาดการณ์ว่า Palo Alto, CrowdStrike, Wiz จะออก MCP posture product ภายใน Q1 2027 — ไม่ใช่เพราะ visionary แต่เพราะ customer board room ถามไปแล้ว

## มุม AI Agent Platform

**Builders:** ถ้า framework / agent SDK ของคุณ default อ่าน MCP registry โดยไม่มี allowlist + signature check — คุณกำลังสร้าง supply chain hole ให้ user. ต้อง ship **built-in MCP posture check** (DNS freshness, SSL cert chain, provenance signature) และ **allowlist mode เป็น default ของ enterprise tier**. **Users / business:** ถ้า organization เริ่ม pilot MCP ควร vendor-side ของ MCP server (own คนและ domain) ก่อนเสมอ หรือทำ internal MCP registry — ห้าม agent ภาคสนาม connect ไป public registry โดยตรง. **Ecosystem:** AAIF (ที่เพิ่งเห็นที่ Toronto) น่าจะต้อง fast-track **MCP server attestation standard** — ไม่งั้นปีหน้าจะมี incident report แรกและ regulator จะเข้ามาเขียน rule เอง (ซึ่งปกติจะ worse than ecosystem self-regulation ที่ทำช้า)

## Sources
- [Welcome to the Jungle: What We Found Inside 15,465 Public MCP Servers - The Hacker News](https://thehackernews.com/2026/10/welcome-to-jungle-what-we-found-inside.html)
- [OX Security says MCP servers reach China, home networks and abandoned domains - Runtimewire](https://runtimewire.com/article/ox-security-mcp-servers-governance-risks)
- [New Research: MCP Servers Connect AI Agents to China, Russia, Home Networks and Abandoned Domains - Webull](https://www.webull.com/news/15633012586906624)
- [One MCP server used 18,000 tokens before doing anything. Here's the workaround. - The New Stack](https://thenewstack.io/pi-agent-mcp-codemode)

---

## Audio script
สัปดาห์นี้ OX Security กลับมาอยู่หน้าหนึ่ง หลัง Hacker News เอา report เก่าของเขาเรื่อง 15,465 MCP Servers Zero Governance มาเล่าใหม่ตรงสัปดาห์ MCP Dev Summit Toronto. ตัวเลขที่ชกเข้าตา. จาก 5,095 unique host ที่สแกน 15.6% อยู่นอกสหรัฐ. 19 host ในจีน 18 ในรัสเซีย. จำนวนมากซ่อนหลัง ngrok กับ Cloudflare Tunnel ชี้มา home network จริง. และ 6 โดเมนถูกทิ้ง เปิดให้ซื้อใหม่ที่ 4 เหรียญต่อโดเมน. ใครก็ตามจ่าย 24 เหรียญครอบ MCP endpoint ที่ enterprise ยัง config ค้างไว้ได้. ประเด็นสำคัญคือ MCP registry กำลังถูกใช้จริงโดยไม่มี vetting แม้แต่ชั้นแรก. ถ้า npm กับ PyPI ใช้เวลา 10 ปีกว่าจะมี signed package กับ provenance MCP เริ่มจากศูนย์. ต่อ builder ถ้า SDK ของคุณ default อ่าน MCP registry โดยไม่มี allowlist กับ signature check แปลว่าคุณกำลังสร้าง supply chain hole ให้ user. ต่อ enterprise CIO ที่กำลัง pilot MCP ควรเป็นเจ้าของ MCP server เองก่อนเสมอ ห้าม agent ภาคสนาม connect public registry โดยตรง. ต่อ ecosystem หมวด MCP Gateway กับ MCP posture product จะเป็นหมวดฮอตปี 2027. ดู AIR Security 50 ล้านเหรียญ Sept เป็นสัญญาณแรก. คาด Palo Alto CrowdStrike Wiz ออก product ภายใน Q1 ปีหน้า
