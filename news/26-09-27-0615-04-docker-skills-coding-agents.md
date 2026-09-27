---
date: 2026-09-24
slug: docker-skills-coding-agents
topic: openbridge-trend
reading_time_min: 3
sources: 2
image_prompt: |
  Editorial isometric illustration of a Docker whale carrying a stack of glowing
  "SKILL CARDS" over a container yard; three floating cards labeled
  "BUILD", "TEST", "OPTIMIZE" hover above four robot mascots tagged "CLAUDE
  CODE", "CODEX", "COPILOT", "CURSOR". A green banner reads "APACHE 2.0 —
  ONE COLLECTION, EVERY AGENT". Cinematic navy-and-cyan palette, high contrast
  for 200px thumbnails, editorial illustration style, 1:1 aspect, no real human
  faces.
image: images/26-09-27-0615-04-docker-skills-coding-agents.png
---

# Docker เปิด Skills official ให้ agent 4 เจ้า — สงคราม "skill catalog" เริ่มต้นแล้ว

## TL;DR
- Docker ปล่อย **docker/skills** บน GitHub เมื่อ 24 ก.ย. — collection ของ reusable workflow ให้ coding agent build/test/debug/optimize containerized app
- ใช้ได้กับ Claude Code, Codex, GitHub Copilot, Cursor — Apache License 2.0
- นี่คือครั้งแรกที่ platform ใหญ่ปล่อย "skill catalog" อย่างเป็นทางการ — แปลว่า agent skills กำลังกลายเป็น distribution channel ใหม่ที่ vendor ต้องแย่งกัน publish

## เกิดอะไรขึ้น
วันที่ 24 ก.ย. Docker ประกาศ **Docker Skills** — collection ของ skill สำหรับ AI coding agent ให้ทำงานกับ Dockerfile และ multi-container application ตาม Docker's official guidelines. Arnaud Héritier จาก Docker ประกาศบนทั้ง X และ Bluesky, repo อยู่ที่ github.com/docker/skills, สัญญาอนุญาต Apache 2.0.

จุดที่น่าสังเกต: Docker ระบุ compatibility กับ **Claude Code, Codex, GitHub Copilot, Cursor** ทั้งสี่เจ้าในประกาศเดียว. นี่เป็น pattern ที่ยังใหม่มาก — vendor ที่ผลิต **domain expertise** (Docker เชี่ยวชาญ container) ปล่อย skill spec ที่ agent หลายเจ้าใช้ได้เหมือนกัน แทนที่จะ integrate เจ้าใดเจ้าหนึ่งเป็น flagship. แนวคิด **skill** ตัวนี้อิงกับ Anthropic ที่เปิด skills format ให้ Claude Code เมื่อต้นปี — file-level, prompt-based, versioned — และตอนนี้ agent เจ้าอื่นก็อ่าน format ใกล้เคียงกันได้เกือบทั้งหมด.

ก่อนหน้านี้ OpenAI เปิด Agents SDK พร้อม sandbox กับ MCP foundation, Nvidia เปิด Agent Toolkit + OpenShell, Cloudflare เปิด MCP reference architecture สำหรับ enterprise. Docker Skills เข้ามาต่อชั้นบนสุด — เลเยอร์ที่ **แต่ละ vendor domain publish know-how ของตัวเอง** ให้ agent เอาไปทำงานตามได้เลย ไม่ต้องรู้เอง.

## ทำไมสำคัญ
ปี 2024 คำถามคือ "agent ตัวไหนเก่งที่สุด". ปี 2025 คำถามคือ "agent ใช้ tool อะไรได้บ้าง". ปี 2026 คำถามใหม่กำลังโผล่ — "agent มี **skill catalog** ที่กว้างแค่ไหน". Docker เพิ่งแสดงให้เห็นว่า skill catalog จะเป็น distribution channel ใหม่ที่ vendor domain อย่าง Docker, GitHub, HashiCorp, Datadog, Snowflake, Databricks จะแย่งกัน publish — เพราะ agent ที่ code แล้วเปิด Dockerfile เจอ error จะ auto-invoke skill ของ Docker ทันที ไม่ต้องผ่าน tutorial บน docs.docker.com เลย.

ตัวเลขที่น่าสนใจไม่ใช่ downloads (ยังไม่ทันนับ) แต่ **coverage ของ agent** — ประกาศเดียวรองรับ 4 เจ้าใหญ่. Anthropic Skill format กลายเป็น **de facto standard** ที่ agent เจ้าอื่นตามหลังโดย compat — เช่นเดียวกับที่ MCP กลายเป็น de facto tool protocol เมื่อปีที่แล้ว. Anthropic ผลักดันมาเงียบ ๆ ประมาณ 8 เดือน — และตอนนี้ ecosystem ก็เริ่มขยับด้วยตัวเอง.

ที่น่าตามต่อคือ **skill governance**. ถ้า Docker publish skill แล้ว agent เอาไปใช้ผิด — เช่น skill บอกให้ chmod 777 dir ที่ไม่ควร — ใครรับผิด? Docker หรือ vendor agent? Anthropic ตอบเรื่องนี้ผ่าน skill sandbox กับ scope, แต่ Docker Skills ตอนนี้ยังไม่ระบุชัด. คาดว่า 6 เดือนข้างหน้าจะเห็น "skill signing" + registry แบบ MCP registry ตอนต้นปีนี้.

## มุม AI Agent Platform
**Builders** — ถ้าคุณสร้าง developer tool ให้ agent ใช้ ให้เขียน skill spec ของตัวเองแล้ว publish บน GitHub เลย. อย่ารอ platform เชิญ. Docker เพิ่ง set pattern ให้ — file-based, Apache 2.0, multi-agent compat. **Users / business** — ทีม engineering ที่ใช้ Claude Code / Copilot / Cursor เต็มตัว ให้ import Docker Skills เลย free, license Apache — ROI คือ mistake รอบ Dockerfile misconfiguration ที่ทีมทำอยู่ทุก sprint. **Ecosystem** — เกิด land grab ใหม่ที่ vendor **infrastructure** จะแข่งกัน publish skill official แข่งกัน. คนที่จะเจ็บคือ SaaS docs site แบบเดิม (readthedocs, GitBook) — เพราะ agent ไม่อ่าน docs อีกต่อไป มันอ่าน skill. traffic docs.docker.com ปีหน้าน่าจะลดลง 30-50%. คนที่ควบคุม **skill registry** จะควบคุม developer distribution ทั้งชั้น.

## Sources
- [docker/skills GitHub repository](https://github.com/docker/skills)
- [Docker、AIコーディングエージェント向けの公式スキル「Docker Skills」を公開 — gihyo.jp](https://gihyo.jp/article/2026/09/docker-skills)

---

## Audio script
เรื่องนี้เล็กแต่สำคัญมากครับ. Docker เพิ่งปล่อย Docker Skills — collection ของ skill สำหรับ AI coding agent — บน GitHub เมื่อวันที่ 24 ก.ย. Apache 2.0 open source. จุดที่สำคัญ คือ ประกาศเดียวรองรับ Claude Code Codex GitHub Copilot กับ Cursor พร้อมกัน 4 เจ้าใหญ่. นี่เป็นครั้งแรกที่ vendor domain — คนที่เชี่ยวชาญ container จริง — ปล่อย skill spec สำหรับให้ agent เอาไปใช้ได้ทันที ไม่ต้องอ่าน docs. Pattern นี้จะเป็น land grab ใหม่. ปี 2024 เราถามว่า agent ตัวไหนเก่งสุด. ปี 2025 เราถามว่า agent ใช้ tool อะไรได้บ้าง. ปี 2026 เริ่มถามว่า agent มี skill catalog กว้างแค่ไหน. Anthropic ผลักดัน skill format มา 8 เดือนแบบเงียบ ๆ ตอนนี้กลายเป็น de facto standard ที่ agent เจ้าอื่นตามหลังโดย compat — เหมือน MCP เมื่อปีที่แล้ว. Signal ที่ต้องดูต่อ คือ vendor infrastructure ทั้งวงการ GitHub HashiCorp Datadog Snowflake Databricks จะแข่งกัน publish skill ในอีก 6 เดือน. คนที่คุมได้คือคุม developer distribution ทั้งชั้น. Traffic docs SaaS แบบเดิมจะลดลงชัดเจน. ถ้าคุณทำ developer tool อย่ารอ platform เชิญ เขียน skill แล้ว publish เลยครับ.
