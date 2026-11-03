---
date: 2026-10-28
slug: github-copilot-26-mcp-connectors-preview
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a bright GitHub-octocat silhouette at
  the center of a hub-and-spoke diagram. Twenty-six glossy app tiles — stamped
  with "SLACK", "FIGMA", "NOTION", "SENTRY", "LINEAR", "ATLASSIAN", "CLOUDFLARE",
  "VERCEL", "WORK IQ" and more — snap into radial sockets through a translucent
  ring labeled "MCP". A bold banner across the top reads "26 CONNECTORS",
  "PUBLIC PREVIEW", "ONE SIGN-IN". Deep charcoal background with GitHub-purple
  highlights and warm orange glow lines, 1:1 aspect, strong contrast for 200px
  thumbnails, no real human faces.
image: images/26-11-04-0604-02-github-copilot-26-mcp-connectors-preview.png
---

# GitHub Copilot เปิด MCP connector 26 ตัวพร้อม public preview — distribution layer ของ agent-tool กำลังถูก lock

## TL;DR
- 28 ต.ค. 2026 GitHub ประกาศ public preview ของ **GitHub-verified MCP connector** ครอบคลุม **26 service**: Slack, Figma, Notion, Sentry, Linear, Atlassian Rovo, Cloudflare, Vercel, Work IQ ฯลฯ
- ใช้ได้กับ Copilot ทุกแพลน — enterprise ต้องเปิด "Editor preview features policy" และเพิ่ม server ใน allowlist
- Signal: GitHub เลือก position ตัวเองเป็น **distribution layer** ของ MCP ไม่ใช่แค่ consumer — ชน Microsoft's Copilot Studio, Cloudflare's AI Gateway, และ Anthropic's Claude Desktop head-to-head
- Connector เป็น "connect-once" — authenticate ครั้งเดียวแล้วใช้ได้ข้ามทุก Copilot surface (IDE, PR review, chat)

## เกิดอะไรขึ้น

28 ต.ค. 2026 GitHub changelog ประกาศว่า **GitHub-verified MCP server** กำลังเปิด public preview — รายการแรก 26 service ครอบคลุมทั้ง productivity (Notion, Linear, Atlassian Rovo), design (Figma), infra (Cloudflare, Vercel, Sentry), และ collaboration (Slack). ทั้งหมดผ่านชั้น verification ของ GitHub และเข้าถึงผ่าน Copilot ได้ทุก surface ตั้งแต่ IDE, PR review, ไปถึง chat

จุดที่สำคัญคือ **"connect once"** — developer authenticate เข้า Slack หรือ Figma ครั้งเดียว แล้วใช้ได้ข้าม Copilot surface ทั้งหมด. ปกติเวลา integrate MCP server เข้า Claude Desktop หรือ Cursor ต้อง config credential แต่ละเครื่องแต่ละ workspace — GitHub ตัด friction ตรงนั้นด้วย centralized identity ที่ผูกกับ GitHub account

เงื่อนไข enterprise: admin ต้องเปิด "Editor preview features policy" ให้ organization, และถ้าใช้ MCP allowlist (control feature ที่ GitHub ปล่อยเมื่อต้นปี) ต้อง explicit เพิ่ม server แต่ละตัวเข้า list. Docs บอกชัดว่า "subject to change" — public preview, ไม่ใช่ GA

Partner list ไม่ใช่ random — ตั้งใจเลือกคู่ที่ compete กับ Microsoft stack: **Figma** (vs Microsoft Designer), **Linear** (vs Azure DevOps), **Notion** (vs OneNote), **Cloudflare** (vs Azure). แสดง positioning ของ GitHub ว่าเป็น neutral hub, ไม่ใช่ Microsoft wing

## ทำไมสำคัญ

ตลอดปี 2026 ตลาด MCP เถียงกันเรื่อง "layer ไหนจะ monetize ได้". คำตอบเริ่มชัดในสัปดาห์นี้: ชั้น **distribution + identity** จะเป็น war zone หลัก ไม่ใช่ชั้น protocol (MCP เอง open), ไม่ใช่ชั้น runtime (containerize ได้). ใครมี developer จำนวนล้านอยู่ในมือ + ระบบ identity พร้อม — คนนั้นได้ default position

GitHub มีข้อได้เปรียบที่คู่แข่งแทบไม่มี: **developer identity ของคน 100+ ล้านคน** ที่ผูกกับ repo, action, package. ตอนนี้ connector 26 ตัวคือจุดเริ่ม — ปีหน้าตัวเลขนี้จะเป็นหลักร้อย และทุกคนที่ build MCP server จะต้องถาม "เราต้อง verified บน GitHub ไหม" คล้ายกับที่ developer ปี 2015 ถาม "เราต้องอยู่บน npm/PyPI ไหม"

เทียบกับ Uber MCP Gateway (เรื่อง 01): Uber ทำ **internal gateway**, GitHub ทำ **external distribution**. สองรูปแบบนี้จะอยู่ข้างกันในทุกองค์กรเร็ว ๆ นี้ — internal MCP server (service ภายใน) ผ่าน gateway แบบ Uber, external MCP server (SaaS vendor) ผ่าน verified hub แบบ GitHub. ที่น่าจับตา: Anthropic และ OpenAI ไม่มี developer identity layer ของตัวเองขนาดนั้น — จะต้องเลือกระหว่าง (a) ผูกกับ GitHub, (b) สร้าง identity hub ของตัวเอง (OpenAI Workspaces?), หรือ (c) เลี่ยงชั้นนี้โดย push MCP registry ที่ decentralized

Caveat: ชื่อ "GitHub-verified" ปัจจุบันไม่มี SLA หรือ security standard สาธารณะ — เรายังไม่รู้ว่า verification ครอบคลุมอะไรบ้าง (code review? runtime audit? ข้อตกลง incident response?). CISO ควรเก็บ connector ทั้งหมดใน allowlist mode จนกว่า docs จะชัดกว่านี้

## มุม AI Agent Platform

สำหรับ **builders** ที่สร้าง MCP server เป็น product: ถ้ายังไม่ได้ส่ง application เข้า GitHub verification program ควรรีบ. ตำแหน่ง default ใน connector list = distribution ที่แทบไม่ต้องจ่าย. ข้อเสีย: GitHub คุม gating — เงื่อนไข, revenue share, และ branding เขียนโดย GitHub

สำหรับ **users / business**: อย่า deploy MCP server แบบ ad-hoc ต่อ developer เครื่องแต่ละเครื่อง — ดู verified hub ของ Copilot ก่อนเสมอ. ประหยัดเวลาตั้งค่าและได้ security verification ฟรี. ที่ไทยและ SEA: บริษัทที่ใช้ Copilot Business/Enterprise อยู่แล้ว ควรให้ CISO audit allowlist policy ใหม่ภายในเดือนนี้ — connector ใหม่ 26 ตัวจะเริ่มถูก developer เปิดใช้โดยอัตโนมัติถ้าไม่ล็อก policy

สำหรับ **ecosystem**: Cloudflare AI Gateway, Vercel's AI SDK, และ Apigee MCP แต่ละรายจะพยายามเป็น "distribution hub" คู่แข่ง. ปีหน้าเราน่าจะเห็น hyperscaler เปิด verified-connector program ของตัวเอง — AWS Bedrock Marketplace, Azure Marketplace for Agents. การ fragmentation ของ distribution layer = งานเพิ่มสำหรับ builder, แต่ก็หมายความว่าไม่มีใคร lock-in ได้แบบเด็ดขาด. นี่คือข่าวดีของ open ecosystem

## Sources
- [Connect your tools to Copilot without all the setup (GitHub Changelog)](https://github.blog/changelog/2026-10-28-connect-your-tools-to-copilot-without-all-the-setup/)
- [Supported Copilot connectors (GitHub Docs)](https://docs.github.com/en/copilot/reference/supported-connectors)
- [GitHub previews single-sign-on connectors across Copilot surfaces (Rise Productive)](https://www.riseproductive.com/news/github-copilot-verified-mcp-connectors-preview-20261028)

---

## Audio script
ข่าวที่สองวันนี้ครับ GitHub ประกาศ public preview ของ MCP connector ที่ verify โดย GitHub เอง รายการแรก 26 service ครอบคลุมทั้ง Slack, Figma, Notion, Sentry, Linear, Atlassian Rovo, Cloudflare, Vercel จุดสำคัญคือ connect once — developer authenticate เข้า Slack หรือ Figma แค่ครั้งเดียว แล้วใช้ได้ข้ามทุก Copilot surface ทั้ง IDE, PR review, chat ไม่ต้องตั้ง credential ใหม่ทุกเครื่องเหมือนที่ Claude Desktop หรือ Cursor ต้องทำ เงื่อนไข enterprise admin ต้องเปิด policy ให้ก่อนและถ้าใช้ allowlist ก็ต้อง explicit เพิ่ม server แต่ละตัว Partner list ไม่ใช่ random GitHub ตั้งใจเลือกคู่ที่ไม่ใช่ Microsoft stack เช่น Figma แข่ง Microsoft Designer, Linear แข่ง Azure DevOps, Notion แข่ง OneNote — แสดงว่า GitHub positioning ตัวเองเป็น neutral hub ไม่ใช่ Microsoft wing ที่สำคัญคือ GitHub มี developer identity ของคนร้อยล้านอยู่ในมือ ไม่มีคู่แข่งคนไหนมีขนาดนั้น ปีหน้าตัวเลข connector นี้น่าจะกลายเป็นหลักร้อย และทุกคนที่สร้าง MCP server จะเริ่มถามว่าต้อง verified บน GitHub ไหม เหมือนที่ developer ปี 2015 ถามว่าต้องอยู่บน npm หรือ PyPI ไหม สำหรับทีมไทยที่ใช้ Copilot Business อยู่แล้ว ควรให้ CISO review allowlist ภายในเดือนนี้ครับ ไม่งั้น connector 26 ตัวจะเริ่มถูก developer เปิดใช้โดยอัตโนมัติ
