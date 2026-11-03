---
date: 2026-10-28
slug: android-studio-byoa-40-agents-acp
topic: agentic-ai
reading_time_min: 4
sources: 4
image_prompt: |
  An editorial isometric illustration of an Android Studio IDE window opened
  on a dark desk, its sidebar branching into forty tiny glowing agent
  silhouettes. Four large tiles stand in the front row stamped "CLAUDE",
  "CODEX", "ANTIGRAVITY", "JUNIE", each plugged into a translucent central
  socket labeled "AGENT CLIENT PROTOCOL". A bold counter above the IDE reads
  "40+ AGENTS", "77% FASTER", "3x FEWER TOKENS". Android-green and midnight
  navy palette with white accents, 1:1 aspect, strong contrast for 200px
  thumbnails, no real human faces.
image: images/26-11-04-0604-03-android-studio-byoa-40-agents-acp.png
---

# Android Studio เปิด BYOA — 40+ coding agent ต่อผ่าน Agent Client Protocol, IDE กลายเป็น neutral ground

## TL;DR
- 28 ต.ค. 2026 Google เปิด **"Bring Your Own Agent" (BYOA)** ใน Android Studio Rabbit 2 — รองรับ coding agent มากกว่า **40 ตัว** ผ่าน **Agent Client Protocol (ACP)**
- Agent ที่ list ชัด: **Claude Agent (Anthropic), Codex (OpenAI), Antigravity (Google), Junie (JetBrains)**
- ACP คือ standard สำหรับ IDE-agent communication แบบ **LSP สำหรับ agent** — IDE ไม่ต้อง custom integration ต่อตัว
- Google อ้างตัวเลข agent ทำงาน UI task ได้ **77% เร็วขึ้น** และใช้ **token น้อยลง 3 เท่า** ด้วยคำสั่ง Compose preview terminal ใหม่ (ยังไม่ third-party verify)
- Signal: IDE กำลังกลายเป็น **neutral runtime** — vendor lock-in ลดลง, ชั้นที่แข่งขันย้ายไปที่ตัว agent

## เกิดอะไรขึ้น

ใน Android Dev Summit 2026 Google ประกาศว่า Android Studio Rabbit 2 เปิด **Bring Your Own Agent (BYOA)** — developer เลือก coding agent ตัวใดก็ได้ใน list 40+ มา plug เข้า IDE ผ่าน **Agent Client Protocol (ACP)**. agent ที่ Google highlight คือ Claude Agent ของ Anthropic, Codex ของ OpenAI, Antigravity ของ Google เอง, และ Junie ของ JetBrains

ACP เป็น **protocol มาตรฐานสำหรับ editor-agent communication** — model mirror ของ Language Server Protocol (LSP) ที่ VS Code และ IDE ส่วนใหญ่ใช้สำหรับคุยกับ language server. ก่อน ACP: Android Studio ต้อง build integration custom ต่อ agent — ซึ่งทำให้ Google ต้องเลือกว่าจะ invest ใน agent ของใครก่อน. หลัง ACP: agent ตัวใดที่ speak protocol จะ plug ได้ทันที — เหมือนที่ language server ใด ๆ ก็ทำงานใน VS Code ได้ถ้า implement LSP

Agent ที่ต่อผ่าน ACP จะเข้าถึง IDE context สำคัญ: project structure, symbol resolution, emulator, Logcat log. Google เพิ่ม **Android CLI** ที่เป็น official agent plugin สำหรับ Claude Code, Codex, และ Antigravity ด้วย — agent รัน build/test/deploy จาก CLI ได้ตรง

ตัวเลขที่ Google claim: agent ทำงาน UI task **77% เร็วขึ้น** และใช้ **token น้อยลง 3 เท่า** ด้วยคำสั่ง Compose preview terminal ใหม่. Google ยังเปิด **Android Bench 2.0** benchmark สำหรับ agent บน multi-day Android task. ตัวเลขทั้งหมดมาจาก Google — ยังไม่มี third-party verify

ค่าใช้จ่าย: Google ไม่ bundle — pricing ขึ้นกับ agent provider แต่ละราย. ใช้ Claude Agent = จ่าย Anthropic, ใช้ Codex = จ่าย OpenAI, ใช้ Antigravity = จ่าย Google

## ทำไมสำคัญ

สิ่งที่น่าสนใจไม่ใช่ความสามารถใหม่ของ agent — แต่คือ **Google ยอมเปิด IDE ให้คู่แข่งเข้า**. ปี 2024-2025 Google plays catch-up ในเกม coding assistant — Copilot นำ, Cursor กำลังมา. การเลือก open กลางปี 2026 แทนที่จะ lock Antigravity ให้เป็น default = ยอมรับว่า IDE lock-in strategy แพ้แล้ว. เทียบกับ Microsoft ที่ยังพยายามให้ Copilot เป็น default ใน VS Code, Google เลือก position Android Studio เป็น **neutral runtime** — เหมือนที่ Android เองเคย beat iOS ด้วย openness

ACP เป็น protocol ที่สำคัญเกินกว่าแค่ Android Studio. ถ้า Jetbrains adopt (Junie ก็อยู่ใน list แล้ว), Zed หรือ Neovim ก็น่าจะ adopt ตาม — ซึ่งแปลว่าภายในปี 2027 น่าจะเห็น **"agent ตัวหนึ่ง, IDE หลายตัว"** เป็น default pattern. Agent vendor (Anthropic, OpenAI) มี surface เพิ่มโดยไม่ต้อง build plugin, แต่ก็จะเริ่มสูญ lock-in บน UI ของตัวเอง (Claude Code, OpenAI Codex CLI). Trade-off ที่ทั้งสองฝั่งต้องยอมรับ

Pattern ที่ชัดใน 3 เรื่องแรกของวันนี้: **Uber (เรื่อง 01) เปิด internal MCP distribution, GitHub (เรื่อง 02) เปิด external MCP distribution, Google (เรื่อง 03) เปิด IDE distribution**. ทั้งสามชี้ไปทิศเดียวกัน — **ชั้นที่ profit ไม่ใช่ distribution แต่คือ agent-level capability**. Vendor ที่แพ้ race ของ distribution จะต้องสู้กลับที่ model quality + reasoning + agentic skill — ซึ่งเป็นที่ที่ Anthropic และ OpenAI สบายใจกว่า Google

Caveat: ตัวเลข 77% faster และ 3x fewer tokens มาจาก Google เอง — ขาด third-party benchmark. Android Bench 2.0 จะเป็น reference ที่ Anthropic และ OpenAI น่าจะ gaming ได้ง่ายถ้ามันโหลดไปที่ Compose task specific. ขอดู third-party result ก่อนเชื่อตัวเลข

## มุม AI Agent Platform

สำหรับ **builders** ที่สร้าง coding agent หรือ IDE plugin: เรียน ACP spec ให้ไว. ถ้าสร้าง agent ที่ speak ACP ได้, คุณจะ plug เข้า Android Studio, Jetbrains (น่าจะตามมา), และ IDE ตัวอื่น ๆ ได้โดยไม่ต้อง rebuild integration. นี่คือการประหยัด engineering effort มหาศาล

สำหรับ **users / business** ที่ build Android (fintech, e-commerce ไทยหลายเจ้ายังพัฒนา Android native): ถ้าทีมใช้ Claude Code หรือ Copilot อยู่แล้ว, การย้ายเข้า Android Studio BYOA หมายถึง developer ใช้ agent เดียวกันทั้ง desktop/web/mobile stack ได้ — productivity consistency ที่ก่อนหน้านี้แทบไม่มี. CTO ควรให้ทีม Android experiment Rabbit 2 กับ agent ของตัวเองใน sprint นี้

สำหรับ **ecosystem**: JetBrains, Microsoft VS Code, Zed, Cursor ต้องเลือกว่าจะ adopt ACP หรือสร้าง protocol ของตัวเอง. VS Code น่าจะยากที่สุด (Microsoft มี political incentive push Copilot ก่อน), แต่ pressure จาก community ผู้ใช้ Claude/Cursor จะดันให้ VS Code ต้อง support อย่างน้อย partial. ภายในปี 2027 พน่าจะเห็น ACP (หรือ fork ของมัน) เป็น de-facto standard สำหรับ IDE-agent communication เหมือน LSP

## Sources
- [Google opens Android development to third-party AI agents (The Decoder)](https://the-decoder.com/google-opens-android-development-to-third-party-ai-agents-and-unveils-new-gemini-apis/)
- [Google opens Android Studio to more than 40 coding agents (SuperpowerDaily)](https://superpowerdaily.com/posts/google-opens-android-studio-to-more-than-40-coding-agents-including-claude-and-codex)
- [Agent Client Protocol spec (agentclientprotocol.com)](https://agentclientprotocol.com)
- [Android Studio BYOA explained honestly (Dev.to)](https://dev.to/paullovelace/android-studio-just-opened-to-40-ai-agents-claude-codex-and-antigravity-in-one-ide-explained-28gb)

---

## Audio script
ข่าวที่สามน่าสนใจมากครับ ที่ Android Dev Summit 2026 Google ประกาศว่า Android Studio Rabbit 2 เปิด Bring Your Own Agent หรือ BYOA แปลว่า developer เลือก coding agent ตัวใดก็ได้ใน list สี่สิบกว่าตัวมาเสียบเข้า IDE ผ่าน protocol ใหม่ชื่อ Agent Client Protocol หรือ ACP agent ที่ Google highlight คือ Claude Agent ของ Anthropic, Codex ของ OpenAI, Antigravity ของ Google เอง และ Junie ของ JetBrains ACP เป็น model mirror ของ Language Server Protocol ที่ VS Code ใช้สำหรับคุยกับ language server ก่อน ACP: Android Studio ต้อง custom build integration ต่อ agent หลัง ACP: agent ตัวใดก็ plug ได้ถ้า speak protocol Google ยัง claim ด้วยว่า agent ทำงาน UI task ได้ 77% เร็วขึ้นและใช้ token น้อยลง 3 เท่า ด้วยคำสั่ง Compose preview terminal ใหม่ ตัวเลขยังมาจาก Google ขอดู third party verify ก่อนเชื่อ จุดที่น่าคิดคือ Google ยอมเปิด IDE ให้คู่แข่งเข้า ซึ่งแปลว่า Google ยอมรับแล้วว่า IDE lock-in strategy แพ้ Copilot และ Cursor การ position Android Studio เป็น neutral runtime ก็เหมือนที่ Android เองเคย beat iOS ด้วย openness Pattern ที่ชัดในวันนี้ Uber เปิด internal MCP distribution, GitHub เปิด external MCP distribution, Google เปิด IDE distribution ทั้งสามชี้ไปทิศเดียวกัน ชั้นที่ profit ไม่ใช่ distribution แต่คือ agent-level capability ทีม Android ไทยควร experiment Rabbit 2 ใน sprint นี้ถ้ายังใช้ Claude Code หรือ Copilot อยู่ครับ
