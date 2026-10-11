---
date: 2026-10-01
slug: 26-10-12-0615-04-doxxnet-agentic-defined-networking
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial hero: a futuristic internet highway at night with two lanes.
  The left lane is chaotic with glowing bot avatars labeled "SCRAPER" and
  "SPAM" slamming into a wall marked "38M THREATS BLOCKED". The right lane
  is pristine, bordered by neon pylons reading "AGENTIC DEFINED NETWORK"
  and carries a single clean robot pod labeled "AGENT" cruising through a
  tunnel. Above the tunnel floats a ribbon reading "$38M SERIES A — A16Z".
  Isometric vector, electric cyan + hazard yellow accents on obsidian
  background, 1:1 aspect, no real human faces, bold text readable at 200px.
image: images/26-10-12-0615-04-doxxnet-agentic-defined-networking.png
---

# doxx.net ระดม $38M จาก a16z — Barrett Lyon กลับมาสร้างชั้น network ให้เอเจนต์ หลัง 20 ปีของการสร้าง "ท่อ internet"

## TL;DR
- 1 ต.ค. 2026 **doxx.net** ปิด **Series A $38M** นำโดย **Andreessen Horowitz** พร้อม Animo Ventures และ Focal.vc; **Joel De La Garza** partner a16z เข้า board; valuation ไม่เปิดเผย
- ผลิตภัณฑ์คือ **Agentic Defined Networking** — ให้ **AI agent สร้าง / config / operate private network ของตัวเอง** โดย expose SDK สำหรับ agent runtime (iOS, macOS, Android GA; Windows / Linux กำลังมา)
- บริษัทอ้าง block threat 38 ล้านครั้งใน closed beta ตั้งแต่ ธ.ค. 2025 — ตัวเลขที่ยังไม่มี third party verify; ก่อตั้งโดย **Barrett Lyon** คนที่สร้าง BitGravity, Xbot, และ Netography

## เกิดอะไรขึ้น

1 ต.ค. 2026 doxx.net — startup จาก Miami ก่อตั้งโดย **Barrett Lyon** — ประกาศ Series A $38M นำโดย Andreessen Horowitz. Animo Ventures และ Focal.vc ร่วม round. **Joel De La Garza partner ของ a16z เข้า board** (คนเดียวกันที่ลง Cloudflare, Lacework, และหลาย security infra deal). วันเดียวกันกับประกาศ, บริษัทเปิด **public beta** ของ Agentic Defined Networking platform หลังอยู่ใน closed beta มา 10 เดือน

Barrett Lyon ไม่ใช่ชื่อใหม่ในวงการ internet infra. เขาสร้าง **BitGravity** (CDN ที่ Verisign ซื้อปี 2010), **Xbot** (DDoS mitigation ที่ Prolexic ซื้อ แล้ว Akamai ซื้อต่อ), และ **Netography** (ยังอยู่, cloud network security). Lyon เป็นคนที่ "สร้างท่อ internet" มา 20 ปี — การที่เขาเลือกเดิมพันกับ "agent จะต้องการชั้น network ของตัวเอง" คือ signal ที่น่าสนใจกว่าตัวเลข funding

**Product thesis** ของ doxx.net คือ: Internet ปัจจุบันถูกออกแบบมาให้ **มนุษย์** สร้าง session ผ่าน browser + VPN + firewall. Agent ที่วิ่ง autonomously เจอ pain หลายชั้น: (1) **IP reputation** — agent ที่วิ่งจาก data center IP เจอ CAPTCHA / block ที่ merchant / content provider, (2) **TLS fingerprint** — agent ใช้ library ที่ fingerprint ต่าง browser → ถูกตรวจจับ, (3) **Session continuity** — agent ยาวข้าม hour / day เจอ IP rotation ทำให้ login expire, (4) **egress control** — enterprise ไม่ไว้ใจให้ agent วิ่งจาก network ของตัวเองโดยไม่มี audit log

**Agentic Defined Networking** ของ doxx.net เสนอทางออก: ให้ agent มี **"private network" ของตัวเอง** — IP range dedicated, TLS fingerprint ที่ match context, egress policy ที่ agent เป็นคน declare, และ audit log ที่ chain of custody กลับ identity ของ agent (ซึ่ง synergy กับ PAP / PACT ที่คุยกันในเรื่องแรกของวันนี้). SDK พร้อมใช้บน iOS, macOS, Android; Windows กับ Linux กำลังมา. **Pricing ไม่เปิดเผย** และ **valuation ก็ไม่เปิดเผย** — สองสัญญาณที่บอกว่า a16z คงปั้น next-round narrative เอง

**ตัวเลขที่น่าสังเกต**: บริษัทอ้าง blocked threat 38 ล้านครั้งใน closed beta ตั้งแต่ ธ.ค. 2025 — เลข "38" ที่พ้องกับ Series A size ชัดเจนเป็น PR coincidence. ปัญหาคือ **ไม่มี third-party verification**, ไม่เปิด methodology ของนับ "threat" (DDoS attempt? Bot scraping? Phishing?), และไม่บอก customer base ที่ generate 38M event นั้น. ควรถือเป็น company-reported figure และกรอง 50-70% ออกตามปกติ

## ทำไมสำคัญ

**ความสำคัญไม่ใช่ $38M — แต่คือ "network layer คือ gap ที่ยังว่าง"**. ยุค MCP, A2A, PAP, PACT ทำให้ protocol layer เริ่มตกผลึก. **Application layer** (agent framework, orchestrator) ก็มี player เยอะแล้ว. **Model layer** ก็ชัด. แต่ **network layer** — ชั้นที่ determine ว่า agent ของคุณไปเคาะประตูธุรกิจอื่นได้จริงไหม — ยังเป็น gap ที่ Cloudflare, Fastly, Akamai พยายามเติมด้วย product line ตัวเอง (Cloudflare AI Gateway, Agent Shield), แต่ยังไม่มี pure-play startup. doxx.net ชิง positioning ก่อน

**Signal อีกชั้นคือ a16z เลือกลงใน security-adjacent agent startup.** ก่อนหน้านี้ a16z ลงใน Reco ($55M agent security), Prompt Security, Protect AI (ขายให้ Palo Alto ปีที่แล้ว). doxx.net เป็น second security bet ที่โฟกัส **ขา network, ไม่ใช่ขา model**. ซึ่งบอก thesis ของ a16z ชัด: **threat surface ของ agent ปี 2027 ไม่ใช่ prompt injection เท่านั้น แต่คือ network traffic / identity ที่ merchant กับ enterprise ไม่ไว้ใจ**. ลงกับ Lyon ที่ shipped network infra มา 3 รอบ cost ความเสี่ยงน้อยกว่าลงกับ founder ที่ไม่มี track record

**คาดการณ์: หน้าตา stack network layer ปี 2027.** จะเกิดการแยกเลเยอร์ชัดเจน: (1) **agent-native network** (doxx.net, Cloudflare Agent Shield, Netography) ที่ให้ agent วิ่งจาก dedicated infrastructure, (2) **merchant-side agent gateway** (Decagon's Personal Agent Gateway, Cloudflare Bot Management, Akamai Bot Manager) ที่ตรวจและ accept agent traffic, (3) **identity bridge** (PAP, PACT) ที่ link สองฝั่งเข้าด้วยกัน. ทั้งสามเลเยอร์ต้อง interoperate. ใครเขียน spec ของ interface ก่อน จะได้ default position ใน stack

## มุม AI Agent Platform

**Builders:** ถ้าสร้าง agent product ที่วิ่ง autonomously ข้าม internet (web browsing agent, procurement agent, research agent), ควรรู้ว่า **IP reputation + TLS fingerprint + session continuity** เป็น silent killer ที่ demo ไม่เจอ แต่ production จะเจอทันทีที่ scale ไปที่ลูกค้า 10+ ราย. ตัวเลือก: (ก) ใช้ residential proxy (ค่า infra สูง, นโยบายไม่ชัด), (ข) ใช้ serverless agent runtime ที่ provider จัดการ network ให้ (Browser Use, Browserbase, Hyperbrowser), (ค) ใช้ Agentic Defined Networking อย่าง doxx.net ที่ให้ agent มี network ของตัวเอง. ตัวเลือก (ก) ตายเร็ว (ข) ขึ้นกับ provider roadmap, (ค) ใหม่สุดและเสี่ยงสุดแต่ differentiate ได้มากสุด

**Users / business:** CISO ของ enterprise ที่กลัว shadow agent ควร view doxx.net เป็น "VPN ของยุคใหม่" — ให้พนักงานปล่อย agent ของตัวเองวิ่งผ่าน network ที่ IT คุม + audit log + policy enforcement. **Ecosystem:** Cloudflare จะต้องตอบ — น่าจะเร่ง Agent Shield + Agent-side Bot Management ออกเร็วขึ้น. Fastly, Akamai, F5 Networks ต้องเลือก buy-vs-build. Lumen, Equinix, Zayo (telco / IX players) จะเจอโจทย์ใหม่ว่า agent traffic จะเป็น segment ที่ grow เร็วสุดในอีก 24 เดือน. ส่วน startup ไทยที่สร้าง agent product ขายต่างประเทศ, การวิ่งจาก datacenter IP ของไทยเจอ merchant block ซ้ำ ๆ ตัวเลือก doxx.net หรือ equivalent เริ่มน่าทดสอบตอน scaling

## Sources
- [doxx.net Raises $38 Million, Led by Andreessen Horowitz, to Launch Agentic Defined Networking — BusinessWire](https://www.businesswire.com/news/home/20261001294246/en/doxx.net-Raises-$38-Million-Led-by-Andreessen-Horowitz-to-Launch-Agentic-Defined-Networking)
- [doxx.net Raises $38 Million to Prevent AI Agent-on-the-Internet Misadventures — SecurityWeek](https://www.securityweek.com/doxx-net-raises-38-million-to-prevent-ai-agent-on-the-internet-misadventures/)
- [Agentic networking startup Doxx.net raises $38M Series A led by a16z — Axios Pro](https://www.axios.com/pro/enterprise-software-deals/2026/10/01/doxxnet-a16z-lyon-networking)
- [doxx.net opens Agentic Defined Networking public beta, raises $38 million — Help Net Security](https://www.helpnetsecurity.com/2026/10/05/doxx-net-agentic-defined-networking-platform/)
- [doxx.net Raises $38m as AI Agents Face New Network Risks — FinTech Global](https://fintech.global/2026/10/06/doxx-net-raises-38m-as-ai-agents-face-new-network-risks/)

---

## Audio script
วันที่ 1 ตุลาคม doxx.net ปิด Series A 38 ล้านดอลลาร์ นำโดย Andreessen Horowitz. Joel De La Garza partner ของ a16z เข้า board. บริษัทก่อตั้งโดย Barrett Lyon คนเดียวกันที่สร้าง BitGravity, Xbot, และ Netography — คนที่ shipped network infra มา 20 ปี 3 รอบ. ผลิตภัณฑ์คือ Agentic Defined Networking ให้ agent สร้าง config operate private network ของตัวเอง. SDK พร้อมใช้บน iOS macOS Android. Windows กับ Linux กำลังมา. บริษัทอ้าง block threat 38 ล้านครั้งใน closed beta ตั้งแต่ธันวาคม 2025 แต่ยังไม่มี third party verify. ความสำคัญไม่ใช่ตัวเลข 38 ล้าน แต่คือ network layer คือ gap ที่ยังว่าง. ยุค MCP A2A PAP PACT ทำให้ protocol layer เริ่มตกผลึก. Application layer มี player เยอะแล้ว. Model layer ก็ชัด. แต่ชั้น network ที่ determine ว่า agent ของคุณไปเคาะประตูธุรกิจอื่นได้จริงไหมยังว่าง. Cloudflare Fastly Akamai พยายามเติมด้วย product line ตัวเอง แต่ยังไม่มี pure play startup. doxx.net ชิง positioning ก่อน. Signal อีกชั้น a16z เลือกลงใน security adjacent agent startup. ก่อนหน้านี้ลง Reco Prompt Security Protect AI. doxx.net เป็น second security bet ที่โฟกัสขา network ไม่ใช่ขา model. บอก thesis ชัดว่า threat surface ของ agent ปี 2027 ไม่ใช่ prompt injection เท่านั้น แต่คือ network traffic กับ identity ที่ merchant กับ enterprise ไม่ไว้ใจ. Builder ไทยที่สร้าง agent product วิ่ง autonomously ข้าม internet ควรรู้ว่า IP reputation TLS fingerprint session continuity เป็น silent killer ที่ demo ไม่เจอ. การวิ่งจาก datacenter IP ของไทยเจอ merchant block ซ้ำ ๆ. doxx.net หรือ equivalent เริ่มน่าทดสอบตอน scaling
