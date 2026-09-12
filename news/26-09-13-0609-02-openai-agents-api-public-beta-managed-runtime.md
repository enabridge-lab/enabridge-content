---
date: 2026-09-13
slug: openai-agents-api-public-beta-managed-runtime
topic: agentic-ai
reading_time_min: 5
sources: 5
image_prompt: |
  An editorial isometric illustration of a large control room labeled
  "AGENTS API" with a central glowing pipeline that pulls in tiny boxes
  stamped "JOB QUEUE", "STATE DB", "SANDBOX", "COMPACTION", "RETRY"
  from the periphery and outputs a single sleek unified stream on the
  right. Around the pipeline, small partner tags read "MODAL", "E2B",
  "VERCEL", "ORACLE", "CLOUDFLARE"; three stacked bold numbers above
  read "PUBLIC BETA", "9 SANDBOXES", "MCP-READY". Editorial style,
  deep teal background with orange highlights, high-contrast readable
  at 200px thumbnail, 1:1 aspect, no real human faces.
image: images/26-09-13-0609-02-openai-agents-api-public-beta-managed-runtime.png
---

# OpenAI เปิด Agents API เป็น public beta — Codex harness กลายเป็นบริการ, sandbox 9 ค่ายพร้อมยิง, กติกา builder เปลี่ยนอีกครั้ง

## TL;DR
- OpenAI ปล่อย **Agents API** เข้า **public beta** เมื่อ **10 ก.ย.** — เอา **agent harness + infrastructure ที่วิ่งอยู่หลัง Codex** ออกมาเป็น managed service ให้ developer เรียกใช้ตรง
- OpenAI จะ manage ให้: **durable session**, **context compaction**, **retry policy**, **sandbox orchestration**, **tool + MCP server binding** — เหล่านี้เมื่อก่อนต้องต่อเองด้วย job queue + state DB + sandbox fleet
- **9 sandbox partner แบบ first-class** — Blaxel, Cloudflare Dev, Daytona, DigitalOcean, E2B, Modal, Oracle Cloud, Runloop, Vercel — หรือใช้ OpenAI-hosted / self-VPC ก็ได้; ไม่มี additional fee ตอน beta (จ่ายแค่ usage)
- Signal: OpenAI ต้องการเปลี่ยน narrative จาก "model provider" เป็น **agent runtime layer** — ที่ LangChain / CrewAI / Semantic Kernel วางเอาไว้ กำลังโดน OpenAI absorb เข้าเป็น native

## เกิดอะไรขึ้น

**10 กันยายน 2026** — OpenAI ปล่อย **Agents API** เข้า public beta ผ่าน release note ทั่วไป ไม่มี event ใหญ่แยก ไม่มี DevDay stage — signal ว่า OpenAI ตั้งใจให้เป็น **infrastructure release ปกติ** ไม่ใช่ hype moment. ตัว API แพ็ค 5 อย่างเข้าเป็นบริการเดียว:

1. **Managed Codex harness** — session ที่วิ่ง agent ต่อเนื่องหลาย turn ได้เป็นวัน ๆ โดยไม่ต้อง persist state เอง
2. **Automatic context compaction** — เมื่อ context ใกล้ full, service จะ compress ให้เอง (ไม่ต้อง roll ของเอง)
3. **Retry + recovery policy** — session ล้ม service ต่อกลับให้เอง
4. **Sandbox orchestration** — OpenAI-hosted sandbox ให้ default, หรือ point ไป self-hosted ก็ได้
5. **Tool + MCP server binding** — bind tool schema + MCP server เข้า session แล้ววิ่งได้ทันที ไม่ต้อง route traffic เอง

Amit Kumar Jena ที่ Kanerika ให้ quote ที่ frame หัวข้อได้ดี: **"A long-running agent built by hand needs a job queue, a state database, a sandbox fleet, a compaction routine and a retry policy. Fewer moving parts."** — นี่คือ pitch หลัก. เดิม builder ที่จะทำ agent จริงต้อง compose 5 layer จาก 5 vendor คนละที่; ตอนนี้ OpenAI ยอมเก็บของ 5 อย่างนั้นไปวิ่งให้

Sandbox partner ที่ OpenAI จับมือเป็น first-class มี 9 ค่าย: **Blaxel AI, Cloudflare Dev, Daytona, DigitalOcean, E2B, Modal, Oracle Cloud, Runloop AI, Vercel** — ครอบ hyperscaler (Oracle, Cloudflare), sandbox-as-a-service (Modal, E2B, Daytona), และ dev platform (Vercel, DigitalOcean). Deploy สามทางเลือก: (a) OpenAI-managed sandbox, (b) sandbox provider ข้างต้น, (c) sandbox ใน customer VPC เอง

ระยะ beta ไม่มี additional fee — จ่ายเท่า token/tool call usage ปกติ — signal ว่า OpenAI อยากให้ developer switch มาเร็ว. ไม่มี timeline GA แต่ pattern OpenAI ปกติ beta → GA ใน 60–90 วัน

## ทำไมสำคัญ

Pattern ที่เห็นชัดสุดคือ **OpenAI absorb "orchestration layer"** เข้าเป็น native. เดิม LangChain, LlamaIndex, CrewAI, Semantic Kernel, AutoGen มีตลาดเพราะ OpenAI API แค่ให้ chat completion + tool call เดี่ยว ๆ ไม่มี state, ไม่มี long-running session, ไม่มี sandbox. Agents API เก็บส่วนที่ orchestration framework ทำอยู่ (state machine, retry, compaction) ให้เอง — ทำให้ framework เหล่านั้นเหลือคุณค่า 2 อย่างคือ **agent design pattern (multi-agent choreography)** และ **portability layer (LLM-agnostic)**

signal ที่ควรอ่านคู่กันคือ **Anthropic Claude Code อัพเดต 9 ก.ย.** เปลี่ยน `CLAUDE_CODE_SUBAGENT_MODEL` เป็น default flag (ไม่ override ทุกที่แล้ว) และ ship durable session ที่ดีขึ้น. Google กำลังผลัก **ADK 2.7** (แม้ CVE-2026-79696 จะทำให้ต้อง delay — ดูคลิปถัดไป). ทั้ง 3 frontier lab กำลัง converge ที่จุดเดียว: **agent runtime กลายเป็นบริการ, framework กลายเป็น glue**. Builder ที่ยังลงทุนหนักใน orchestration framework แบบ generic (LangChain) จะเห็น differentiator หดลงเรื่อย ๆ

จุดคมที่ 3 คือ **sandbox industry กำลังโตขึ้นจากตรงนี้**. E2B, Modal, Daytona, Runloop — 4 ค่ายที่อยู่ในกลุ่ม first-class — คือ sandbox pure-play ที่ระดม funding รอบ $50-200M มาแล้วในปีที่ผ่านมา. การที่ OpenAI ยอมให้ tool กำหนดว่าเป็น "official partner" ตัวเลือกแรก ๆ ทำให้ **sandbox layer กลายเป็น commodity ที่ราคาแข่งกันหนัก** — Vercel + Cloudflare Dev ที่มี dev platform อยู่แล้วก็จะกินตลาดนี้เร็ว. ตลาด "agent sandbox startup" อาจ consolidate ภายใน 12–18 เดือน

## มุม AI Agent Platform

**สำหรับ Builders** ที่มี agent product อยู่แล้ว: (1) ประเมิน migration cost จาก LangChain/CrewAI ไป Agents API — ถ้า agent จะรันข้าม OpenAI/Anthropic/Gemini ให้ชะลอ; ถ้าล็อค OpenAI แล้วให้ **ย้ายเร็วเพื่อลด infrastructure ownership**; (2) **MCP server จะกลายเป็น key differentiator** — Agents API bind MCP ตรง, builder ที่มี MCP server ที่ดี (data connector, workflow tool, internal API) จะ leverage ได้ทันที; (3) sandbox choice ต้องคิด — Modal/E2B/Daytona ให้ per-agent isolation ดี, Vercel/Cloudflare ให้ latency ดีกับ user, Oracle ให้ compliance/data residency

**สำหรับ Users / Business** ที่ deploy agent ในองค์กร: (1) **procurement risk** — Agents API เป็น managed service = **lock-in สูงกว่า** LangChain + own infrastructure เดิม; ประเมินก่อนย้าย; (2) **compliance question** — session state OpenAI เก็บที่ไหน, retention เท่าไหร่, EU AI Act / Thai PDPA compliance? ถ้ายังไม่ชัดให้ใช้ self-VPC sandbox; (3) **cost model change** — ไม่มี additional fee ตอน beta แต่ GA แน่นอนมี premium; งบประมาณต้องเผื่อ 20-40% เพิ่ม

**สำหรับ Ecosystem** (framework / cloud / orchestrator): orchestration framework generic ที่ไม่มี **unique reasoning pattern หรือ vertical domain expertise** จะโดนบีบ; sandbox startup ที่ไม่ได้เป็น 9 partner แรกต้องหา niche ก่อน consolidation; **hyperscaler ที่ไม่ใช่ Oracle** (AWS, Azure, GCP) จะโดน pressure ให้ประกาศ first-class integration ใน 30–60 วัน (Azure น่าจะเร็วสุดผ่าน Foundry); Thai cloud (True IDC, INET, CAT) ที่ทำ AI infra should consider เป็น "regional sandbox provider" ใน list — window เปิดช่วงนี้เท่านั้น

## Sources
- [InfoWorld — OpenAI launches managed Agents API to simplify enterprise AI agent development](https://www.infoworld.com/article/4221163/openai-launches-managed-agents-api-to-simplify-enterprise-ai-agent-development.html)
- [Seeking Alpha — OpenAI ups agentic game as it releases new Data agent and Agents API](https://seekingalpha.com/news/4641846-openai-ups-agentic-game-as-it-releases-new-data-agent-and-agents-api)
- [Digital Applied — OpenAI Agents API: What Moves Out of Your Application](https://www.digitalapplied.com/blog/openai-agents-api-managed-runtime-guide)
- [Blockchain.News — OpenAI Launches Agents API to Streamline AI-Powered Cloud Agents](https://blockchain.news/news/openai-agents-api-launch)
- [OpenAI — Release Notes](https://openai.com/products/release-notes/)

---

## Audio script
วันที่สิบกันยายน OpenAI ปล่อย Agents API เข้า public beta. ไม่มี event ใหญ่ ไม่มี DevDay stage. แค่ release note. signal ว่านี่คือ infrastructure release ปกติ ไม่ใช่ hype moment.

ตัว API แพ็ค 5 อย่างเข้าเป็นบริการเดียว. Managed Codex harness ที่รัน session ต่อเนื่องได้หลายวัน. automatic context compaction เมื่อใกล้ full. retry policy ต่อกลับให้เอง. sandbox orchestration. และ tool กับ MCP server binding โดยตรง.

quote ของ Amit Kumar Jena ที่ Kanerika frame ได้ดี. long running agent ที่ทำเองต้องมี job queue มี state database มี sandbox fleet มี compaction routine มี retry policy. Fewer moving parts. เดิม builder ที่จะทำ agent จริงต้อง compose 5 layer จาก 5 vendor คนละที่. ตอนนี้ OpenAI ยอมเก็บของ 5 อย่างไปวิ่งให้.

Sandbox partner first class มี 9 ค่าย. Blaxel Cloudflare Dev Daytona DigitalOcean E2B Modal Oracle Cloud Runloop Vercel. Deploy สามทางเลือก. OpenAI managed. sandbox partner. หรือ self VPC. beta ไม่มี additional fee. จ่ายเท่า token usage ปกติ.

pattern ที่เห็นชัดคือ OpenAI absorb orchestration layer เข้าเป็น native. เดิม LangChain LlamaIndex CrewAI Semantic Kernel AutoGen มีตลาดเพราะ OpenAI API แค่ให้ chat completion กับ tool call เดี่ยว ไม่มี state ไม่มี long running session ไม่มี sandbox. Agents API เก็บส่วนที่ orchestration framework ทำอยู่ให้เอง. framework เหลือคุณค่าสองอย่าง. agent design pattern และ portability layer.

signal ที่ควรอ่านคู่กันคือ Anthropic Claude Code update วันที่เก้ากันยายน. Google กำลังผลัก ADK 2.7 แต่ต้อง delay เพราะ CVE 2026 79696. สาม frontier lab กำลัง converge ที่จุดเดียว. agent runtime กลายเป็นบริการ. framework กลายเป็น glue.

จุดคมที่สามคือ sandbox industry กำลังโตขึ้น. E2B Modal Daytona Runloop สี่ค่ายในกลุ่ม first class เป็น sandbox pure play ที่ระดม funding รอบ 50 ถึง 200 ล้านมาแล้วในปีที่ผ่านมา. OpenAI ยอมกำหนดว่าเป็น official partner ทำให้ sandbox layer กลายเป็น commodity ที่ราคาแข่งกันหนัก. Vercel Cloudflare Dev ที่มี dev platform อยู่แล้วจะกินตลาดนี้เร็ว. ตลาด agent sandbox startup อาจ consolidate ภายใน 12 ถึง 18 เดือน.

สำหรับ builder ที่มี agent product อยู่แล้ว. ประเมิน migration cost จาก LangChain CrewAI ไป Agents API. ถ้ารันข้าม OpenAI Anthropic Gemini ให้ชะลอ. ถ้าล็อค OpenAI แล้วให้ย้ายเร็วเพื่อลด infrastructure ownership. MCP server จะกลายเป็น key differentiator เพราะ Agents API bind ตรง.

สำหรับ business ที่ deploy agent ในองค์กร ระวัง procurement risk. Agents API เป็น managed service. lock in สูงกว่า LangChain กับ own infrastructure. ประเมินก่อนย้าย. compliance question. session state OpenAI เก็บที่ไหน. retention เท่าไหร่. EU AI Act หรือ PDPA compliance. ถ้ายังไม่ชัดให้ใช้ self VPC sandbox.

ecosystem framework generic ที่ไม่มี reasoning pattern เฉพาะหรือ vertical domain จะโดนบีบ. hyperscaler ที่ไม่ใช่ Oracle จะต้องประกาศ first class integration ใน 30 ถึง 60 วัน. Azure น่าจะเร็วสุดผ่าน Foundry. Thai cloud อย่าง True IDC INET CAT ที่ทำ AI infra ควรพิจารณาเป็น regional sandbox provider. window เปิดช่วงนี้เท่านั้น.
