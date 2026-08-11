---
date: 2026-08-07
slug: anthropic-claude-code-self-hosted-runner-enterprise
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  A split enterprise diagram: on the left, a glowing cloud with an Anthropic
  mark labeled "AUTH + ROUTING"; on the right, a locked server rack inside
  a corporate boundary labeled "YOUR NETWORK · YOUR COMPUTE". A single
  arrow connects them with the tag "claude self-hosted-runner". Three
  chips under the rack read "FIN-SVCS", "HEALTHCARE", "GOV". Editorial
  isometric style, deep indigo and gold palette, 1:1 aspect, no real
  human faces.
image: images/26-08-12-0617-03-anthropic-claude-code-self-hosted-runner-enterprise.png
---

# Anthropic เปิด Claude Code แบบ self-hosted runner — agent session รันบน infra ลูกค้าเอง สำหรับ bank, hospital, gov contractor

## TL;DR
- Claude Code v2.1.224 (7 ส.ค.) เพิ่ม **self-hosted environments** — session รันบน compute ที่องค์กร provision เอง คำสั่งเดียว `claude self-hosted-runner` เปลี่ยนเครื่อง/container เป็น session compute
- Anthropic เก็บแค่ authentication + session routing; **repo checkout, build artifact, secret, และไฟล์ที่ session สร้าง/แก้ไข อยู่บน infra ลูกค้าทั้งหมด**
- Public beta เฉพาะ Team + Enterprise plan; off by default; ไม่ available สำหรับ ZDR account — target ชัด: financial services, healthcare, gov contractor, data-residency

## เกิดอะไรขึ้น
7 สิงหาคม Anthropic ปล่อย Claude Code v2.1.224 พร้อม feature ที่เปลี่ยน architecture ของ agent สำหรับ enterprise — **self-hosted environments** ปกติ Claude Code session รันบน infrastructure ของ Anthropic (หรือ sandbox provider ที่ Anthropic ควบคุม) ตอนนี้ทีม admin สามารถรัน `claude self-hosted-runner` บนเครื่องของตัวเอง — VM, bare metal, หรือ Kubernetes cluster — เปลี่ยนให้เครื่องนั้นเป็น compute layer ที่ session ของ Claude Code ทำงานจริง

โครงสร้างที่ Anthropic ออกแบบชัดเจน: **Anthropic เก็บแค่ auth + session routing** — คือทำ identity check, route session ไปหาเครื่องที่ถูกต้อง, และ handle model inference (เพราะ model ยังอยู่ที่ Anthropic) แต่ **ทุกอย่างที่ session touch — repo checkout, secret file, build artifact, ผลลัพธ์คำสั่ง, ไฟล์ที่แก้ — อยู่บนเครื่องขององค์กรทั้งหมด** ไม่มี copy กลับไปที่ Anthropic ถ้าองค์กรใช้ VPC หรือ air-gapped network session ก็รันข้าง internal service ตรงนั้นเลย ไม่ต้อง VPN ออก

Availability: **public beta เฉพาะ Team + Enterprise plan**, off by default (ต้อง admin เปิดเอง), และ **ไม่ available สำหรับ organization ที่ใช้ ZDR** (zero data retention) ซึ่งเป็น trade-off ที่น่าสังเกต — ZDR ปกติเป็นตัวเลือกของ compliance-heavy customer แต่ self-hosted บังคับให้ session state ต้อง flow ผ่าน routing layer ของ Anthropic Anthropic เตือนใน docs ว่าให้ staff engineering team เตรียม own setup + ongoing maintenance เพราะไม่มี managed upgrade

## ทำไมสำคัญ
ดีลนี้เป็น **pattern "hybrid frontier" ที่ frontier lab เริ่มยอมรับอย่างเป็นทางการ** — cloud brain (model + auth) กับ local body (execution + data) แยกกัน ปีที่แล้ว Anthropic กับ OpenAI ยังไม่ยอมเลยเพราะกลัวเสีย data flywheel และเสีย control ของ inference cost ตอนนี้ทั้งคู่รู้ว่าถ้าไม่ให้ enterprise เลือกที่จะ keep execution ในบ้านตัวเอง จะเสียดีล 8-9 หลักให้ Databricks, Snowflake, และ private hyperscaler ที่ pitch "your data never leaves"

จังหวะที่ตามมาชัด: หลัง [MCP 2026-07-28 spec](https://www.anthropic.com/news/mcp-2026-07-28) ที่ทำให้ connection เป็น stateless + versioned, self-hosted runner คือ**ชิ้นสุดท้ายที่ทำให้ Claude Code deploy ได้ใน bank ที่กฎ compliance ไม่ให้ code หรือ secret ออกไปนอก network** ก่อนหน้านี้ทีม security ของ Goldman Sachs, JPMorgan, HSBC ต้อง block Claude Code ที่ firewall level ตอนนี้เปิดได้ (พร้อม audit control ที่เขากำหนดเอง)

Signal สำหรับ market: OpenAI ต้องตอบภายในไม่กี่สัปดาห์ — Codex/GPT-5.6-Code ยังรันบน OpenAI-managed sandbox เท่านั้น Google Gemini Enterprise มี private VPC deployment แต่ยังไม่ถึง code-agent tier ทำนายได้ว่าเราจะเห็น GitHub Copilot Workspace + Cursor ปล่อย self-hosted mode ในไตรมาสหน้าเพื่อป้องไม่ให้ enterprise ย้ายไป Claude ทั้งกระดาน

## มุม AI Agent Platform
สำหรับ **builders** ที่ทำ agent framework/orchestration: self-hosted runner ของ Anthropic เป็น reference architecture สำหรับ "cloud auth + local execution" pattern — ทีมที่สร้าง agent platform ควรออกแบบ execution layer ให้แยกจาก control plane ตั้งแต่แรก ไม่อย่างนั้นจะ retrofit ยากตอน enterprise customer มา ask compliance สำหรับ **users/business** ที่ deploy agent: compliance officer ของ regulated industry ตอนนี้มี**สินค้าจริงที่ตอบโจทย์ 3 ข้อ**พร้อมกัน — code stays in network, secrets stay in vault, audit log stays in enterprise SIEM — Claude Code จึงเข้า POC ที่เคย blocked ได้

สำหรับ **ecosystem/vendor**: GitHub, GitLab, JetBrains, Sourcegraph, Cursor, และ Windsurf ต้องอ่าน move นี้ว่าเป็น**การเปลี่ยน rule ของตลาด code agent** — pricing per-seat + cloud-only ที่ครองตลาดมา 2 ปีกำลังถูก challenge ด้วย hybrid deployment ที่มี premium tier ชัด Snowflake/Databricks จะเข้ามาแข่งในชั้นเดียวกันด้วย reason ว่า data + code + agent ควรอยู่ compute เดียวกันเพื่อลด egress cost + latency — ยุค "agent runs where the model lives" กำลังจะจบ

## Sources
- [Self-hosted environments for Claude Code — Anthropic](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute)
- [Self-hosted environments — Claude Code Docs](https://code.claude.com/docs/en/self-hosted-environments)
- [Claude Code Sessions Can Now Run on Infrastructure Your Team Controls — Unite.AI](https://www.unite.ai/claude-code-sessions-can-now-run-on-infrastructure-your-team-controls/)

---

## Audio script
สัปดาห์ที่แล้ววันที่ 7 สิงหาคม Anthropic ปล่อย Claude Code เวอร์ชัน 2.1.224 พร้อม feature สำคัญมากสำหรับ enterprise คือ self-hosted environments เดิมที Claude Code session รันบน infrastructure ของ Anthropic เอง ตอนนี้ทีม admin สามารถรันคำสั่ง claude self-hosted-runner บนเครื่องของตัวเอง — VM, bare metal, หรือ Kubernetes — แล้วเปลี่ยนเครื่องนั้นเป็น compute layer ที่ session รันจริง Anthropic เก็บแค่ authentication กับ session routing ส่วนทุกอย่างที่ session touch ตั้งแต่ code checkout, secret, build artifact, ไฟล์ที่แก้ อยู่บนเครื่องขององค์กรทั้งหมด ไม่มี copy กลับไปที่ Anthropic เปิด public beta เฉพาะ Team กับ Enterprise plan target ชัดเจนคือ financial services, healthcare, government contractor และองค์กรที่มี data residency requirement นี่คือ pattern hybrid frontier ที่ frontier lab เริ่มยอมรับ — cloud brain ควบคู่ local body หลังจาก MCP 2026-07-28 spec ทำให้ connection เป็น stateless self-hosted runner คือชิ้นสุดท้ายที่ทำให้ Claude Code deploy ได้ใน bank ที่กฎ compliance เดิม block ไว้ทั้งหมด OpenAI Codex กับ Google Gemini ต้องรีบตามภายในไม่กี่สัปดาห์ สำหรับคนสร้าง agent platform นี่คือ reference architecture ที่ว่า execution layer ควรแยกจาก control plane ตั้งแต่แรก ไม่อย่างนั้น retrofit ยากตอน enterprise customer ถามเรื่อง compliance ครับ
