---
date: 2026-10-29
slug: google-jules-sunset-antigravity-plugin-marketplace
topic: agentic-ai
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a cartoonish asteroid labeled "JULES"
  being tractor-beamed into a glowing dome stamped "ANTIGRAVITY". Around the
  dome float stickers for third-party plugins: "ATLASSIAN", "STRIPE MCP",
  "DATABRICKS", "UNITY". Below, a terminal window shows the command
  "agy plugin install" in monospace. A countdown ribbon reads
  "READ-ONLY NOV 11 · OFFLINE DEC 31". Google blue, green and yellow
  palette on deep space background, 1:1 aspect, high contrast for 200px
  thumbnails, no real human faces.
image: images/26-11-02-0605-03-google-jules-sunset-antigravity-plugin-marketplace.png
---

# Google ปิด Jules → ย้าย learning เข้า Antigravity + เปิด Plugin Marketplace (Atlassian/Stripe MCP/Databricks)

## TL;DR
- 29 ต.ค. 2026 Google ประกาศปิด **Jules** async coding agent — read-only **11 พ.ย.**, offline สมบูรณ์ **31 ธ.ค.**
- Learnings ย้ายเข้า **Antigravity 2.0** (เปิดตัว I/O พ.ค. 2026) ที่ Google rebuild เป็น desktop app + CLI + SDK
- วันเดียวกัน Antigravity เปิด **Plugin Marketplace** — launch partner: **Atlassian Teamwork Graph CLI** (Jira/Confluence/Bitbucket), **Stripe MCP server**, **Databricks**, **Unity**
- Install plugin ผ่าน CLI: `agy plugin install <name>` — pattern เดียวกับ `npm`/`pip`
- Export จาก Jules ครอบ session history, memories, repo connection, แต่ **ไม่มี auto-migration** → ลูกค้าต้องย้ายมือ

## เกิดอะไรขึ้น

29 ต.ค. 2026 Google ประกาศปิด **Jules** — async coding agent ที่ Google เปิดตัวใน Labs เมื่อปลายปี 2024 (เริ่มเป็น experiment ก่อน Antigravity). Timeline: **11 พ.ย.** sessions หยุดรับ new work, product กลายเป็น read-only. **31 ธ.ค. 2026** service ปิดสมบูรณ์. Jules พยายามจะเป็น "coding agent ที่ background run" — ให้ developer โยนงานไปแล้วกลับมาดู PR ทีหลัง — แต่ Google ยอมรับโดยตรงใน announcement ว่า **"learnings ย้ายเข้า Antigravity"** ซึ่งคือ IDE/agent harness ที่ Google ลงทุนหนักกว่า

Antigravity 2.0 เปิดตัวที่ Google I/O พ.ค. 2026 เป็น **standalone desktop app** ที่ไม่มีความเกี่ยวข้องกับ Antigravity 1.0 (เขียนใหม่ 100%). มี desktop UI, CLI (`agy`), SDK. ตำแหน่งคือ **"full-stack platform for autonomous AI agent teams"** — ไม่ใช่แค่ coding agent แต่ครอบ product dev lifecycle. วันที่ประกาศปิด Jules — เป็นวันเดียวกันที่ Antigravity ประกาศ **Plugin Marketplace** ที่ Google blog อธิบายว่าเป็น "centralized directory for discovering and installing third-party and Google-built plugins across the Antigravity App and CLI"

Launch partner ที่น่าสนใจที่สุด:
- **Atlassian Teamwork Graph CLI** — "agent-first interface to your entire work context" ครอบ Jira + Confluence + Bitbucket (คือ MCP บน Atlassian suite)
- **Stripe MCP server** — ให้ agent query customer, payment, subscription ของ Stripe account โดยตรง
- **Databricks** + **Unity** (น่าจะเป็น game-engine Unity ไม่ใช่ Databricks Unity Catalog)
- Install pattern: `agy plugin install <plugin-name>` — เลียน `npm install` / `pip install` ตรงๆ

Jules export ครอบ session history, memories, repository connection แต่ Google **ยืนยันว่า ไม่มี automatic migration** — ลูกค้า Jules ต้อง export + reconnect ใน Antigravity (หรือ Codex / Claude Code / Cursor) เอง

## ทำไมสำคัญ

ปี 2025–2026 เราเห็น pattern ชัด: **ยักษ์ใหญ่ "consolidate" coding agent ของตัวเอง**. Google เพิ่งปิด Gemini CLI + Code Assist ไปเมื่อ มิ.ย. 2026, ปิด Jules วันนี้. **ที่เหลือมี Antigravity 2.0 เป็น flagship เดียว**. ก่อนหน้านี้ GitHub ปิด Copilot Workspace แล้วรวมเข้า Copilot Agent. Microsoft ก็ทยอยปิด product ซ้ำซ้อน. OpenAI ก็เพิ่งประกาศปิด AgentKit **30 พ.ย. 2026** (ที่เรารายงานเมื่อวาน) แล้วเหลือ Agents SDK + Codex เป็น primitive. แปลว่าทุกเจ้ากำลัง**บีบ product mix เหลือ coding agent 1 ตัว + agent SDK 1 ตัว** — เพราะพื้นที่โฆษณาและ dev relations ไม่พอโฆษณา 3–4 product แข่งกันเอง

ประเด็นที่สอง: **Plugin Marketplace ของ Antigravity สะท้อนว่า Google ไม่ปิด MCP**. ตรงกันข้าม — launch partner (Stripe MCP, Atlassian) ยืนยันว่า Antigravity ใช้ MCP เป็น protocol ร่วม. นี่คือจุดสำคัญเพราะหลายคนกังวลว่า Google จะดัน A2A (Agent-to-Agent) ของตัวเองจน MCP ตาย. ตัว marketplace บอกว่า Google **รับ MCP เป็น protocol มาตรฐานของ plugin layer** — A2A เป็น protocol สำหรับ agent คุยกับ agent, MCP เป็น protocol สำหรับ agent คุยกับ tool. สองเลเยอร์ไม่ชนกัน

ประเด็นที่สาม — **การไม่มี auto-migration คือ signal เชิง strategy**. Google ยอมเสียลูกค้า Jules บางคนที่ไม่อยากย้ายมือ เพื่อให้ Antigravity ไม่ต้อง compromise architecture. Jules เป็น async-first (session รัน background), Antigravity 2.0 เป็น interactive-first (dev สั่งงาน agent ใน IDE context). สองโมเดลคนละแบบ auto-migrate ไม่ได้จริง. การเลือก **"แยกให้ขาด"** คือการยอมรับว่า Jules experiment ล้มเหลวแค่ส่วนหนึ่ง — Google ไม่ใช่ GitHub Copilot ที่พยายามรักษาตลาด

## มุม AI Agent Platform

สำหรับ **builders**: Antigravity Plugin Marketplace คือ distribution channel ที่สดใหม่ที่สุดในตลาด coding agent — ถ้าคุณสร้าง MCP server อยู่แล้ว (เรื่อง Mintive, Persona, Sweep) การ list บน Antigravity marketplace แปลว่าได้ reach developer base ของ Google. แต่ต้องระวัง: Google ก็มี Google-built plugin ที่แข่งใน marketplace เดียวกัน (ลูกเล่น store-of-store ที่ Apple ใช้กับ Store = เสี่ยงถูก squeeze). ถ้าทีมอยาก publish — ควรเริ่ม design plugin ของตัวเองให้ **cross-IDE** (install ได้ใน Antigravity + Claude Code + Cursor + Codex) ไม่ใช่ Antigravity-only

สำหรับ **business users**: ถ้าทีม engineering ของคุณใช้ Jules อยู่ มี deadline 11 พ.ย. (read-only) + 31 ธ.ค. (ปิด). ควร: (a) export session history ทันที, (b) ประเมิน Antigravity 2.0 vs Claude Code vs Codex ว่าเจ้าไหนตรง workflow มากกว่า, (c) **อย่า wait-and-see** เพราะ 2 เดือนไม่พอทำ full migration ของทีมใหญ่. โดยเฉพาะ enterprise ที่ใช้ Jules สำหรับ async refactor / dependency upgrade — pattern นี้ Antigravity ยังไม่ชัดเจนว่า support ดีเท่า

สำหรับ **ecosystem**: Marketplace ของ Antigravity + MCP marketplace ของ OpenAI (เรื่อง Mintive, OpenAI × ServiceNow) + Anthropic MCP server directory = **3 plugin marketplace สำหรับ agent ที่กำลัง battle**. ปี 2027 เราจะเห็น plugin developer ที่ list บน 1–2 marketplace โตเร็ว, คนที่ไม่ list ตายช้าๆ. แยกจาก ad-tech ตรงที่ marketplace คือ distribution + billing + review — คน build vertical agent (Sweep model, Cresta model) จะได้ประโยชน์

## Sources
- [Antigravity Plugin Marketplace launch (antigravity.google blog)](https://antigravity.google/blog/plugin-marketplace-in-antigravity/)
- [Google launches Antigravity 2.0 at I/O 2026 (The Next Web)](https://thenextweb.com/news/google-antigravity-2-desktop-cli-sdk-io-2026)
- [AI Daily Digest November 1, 2026 — Google folds Jules into Antigravity (DEV)](https://dev.to/hiroki-ii-ai/ai-daily-digest-november-1-2026-google-folds-jules-into-antigravity-claude-ultra-drops-the-3e5e)

---

## Audio script
สองข่าวสำคัญจาก Google ที่คน build coding agent ต้องรู้ 29 ตุลาคม Google ประกาศปิด Jules async coding agent ของ Labs 11 พฤศจิกายน sessions จะกลายเป็น read-only 31 ธันวาคม service ปิดสมบูรณ์ Google ย้าย learning ทั้งหมดเข้า Antigravity 2.0 ซึ่งคือ IDE agent platform ที่ Google เปิดตัวที่ I/O พฤษภาคมปี 2026 สร้างใหม่ 100% เป็น desktop app CLI และ SDK ที่น่าสนใจมากกว่าการปิด Jules คือ Google เปิด Antigravity Plugin Marketplace ในวันเดียวกัน launch partner คือ Atlassian Teamwork Graph CLI ซึ่งคือ MCP สำหรับ Jira Confluence Bitbucket Stripe MCP server ให้ agent query customer payment subscription ของ Stripe โดยตรง Databricks และ Unity install plugin ด้วย CLI command agy plugin install ที่เลียน npm install pip install ตรงๆ pattern ที่เห็นชัดคือ ยักษ์ใหญ่กำลัง consolidate coding agent ของตัวเองเหลือ product เดียว Google ปิด Gemini CLI มิถุนายน ปิด Jules วันนี้ GitHub ปิด Copilot Workspace OpenAI ปิด AgentKit 30 พฤศจิกายน ทุกเจ้าเหลือ coding agent 1 ตัว agent SDK 1 ตัว เพราะพื้นที่ dev relations ไม่พอดูแล 3-4 product ซ้ำกันเอง จุดที่ต้องสังเกต Google ไม่ปิด MCP ตรงกันข้าม launch partner ของ Marketplace ยืนยันว่าใช้ MCP เป็น protocol มาตรฐาน Google รับว่า A2A เป็น protocol agent คุยกับ agent MCP เป็น protocol agent คุยกับ tool สองเลเยอร์ไม่ชนกัน สำหรับทีมที่ใช้ Jules อยู่ตอนนี้ควรเริ่ม export session ทันที อย่า wait-and-see เพราะสองเดือนไม่พอ migrate workflow ของทีมใหญ่ครับ
