---
date: 2026-10-24
slug: anthropic-sandbox-runtime-opensource
topic: openbridge-trend
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of a transparent glass vault labeled
  "srt — @anthropic-ai/sandbox-runtime" sitting on an open laptop. Inside the
  vault, a small robot labeled "MCP SERVER" is contained behind translucent
  walls that read "FILESYSTEM" and "NETWORK". Three stacked numbers float
  above: "APACHE 2.0", "NO CONTAINERS", "macOS / LINUX / WIN α". A ribbon
  running across the laptop keyboard reads "DROP-IN SANDBOX FOR AGENTS".
  Deep navy and amber palette with a touch of green for the "open-source"
  tag, strong contrast for 200px thumbnails, 1:1 aspect, no real human
  faces.
image: images/26-10-25-0605-03-anthropic-sandbox-runtime-opensource.png
---

# Anthropic เปิดซอร์ส sandbox-runtime (Apache 2.0) — MCP server ถูก sandbox ได้ที่ระดับ OS โดยไม่ต้องมี container

## TL;DR
- **24 ต.ค.** Anthropic เปิดซอร์ส **sandbox-runtime (srt)** — tool ที่อยู่หลัง Claude Code สำหรับ **sandbox process ทั่วไปที่ระดับ OS** โดยไม่ต้องมี Docker/container, ภายใต้ **Apache 2.0** เป็น npm package `@anthropic-ai/sandbox-runtime` (v0.0.81, Beta Research Preview)
- ใช้ **Seatbelt (sandbox-exec) บน macOS, bubblewrap บน Linux, Windows alpha**; สิทธิ์ filesystem + network จำกัดด้วย config ที่ YAML/JSON — ไม่ต้องรัน VM
- จุดสำคัญสำหรับ agent ecosystem: `srt` support **"drop-in sandboxing of MCP servers"** — เรียก MCP server (เช่น Playwright, filesystem, Postgres MCP) ภายใต้ sandbox แบบปลอดภัยในคำสั่งเดียว
- Signal: **container-less sandbox กลายเป็น primitive ของ agent runtime** — เทียบคู่ขนานกับ VAST + Nvidia OpenShell (21 ต.ค., container-based) และ 1Password for Agents (22 ต.ค., credential-level)

## เกิดอะไรขึ้น

วันเสาร์ **24 ต.ค.** Anthropic เผยแพร่ **sandbox-runtime** ที่ repo GitHub `anthropics/sandbox-runtime` (บางอ้างอิงชี้ไป `anthropic-experimental/sandbox-runtime`) ภายใต้ **Apache 2.0** — tool เดิมที่อยู่ภายใน Claude Code สำหรับ enforce **filesystem + network restriction** กับ arbitrary process. ปล่อยเป็น npm package ชื่อ `@anthropic-ai/sandbox-runtime` version **0.0.81** วันนี้ (v0.0.80 ปรากฏใน registry เมื่อ 5 วันก่อน แสดงว่า dev เร็ว). ตามเอกสาร: **ไม่ต้องมี container** ทำงานผ่าน **sandbox-exec (Seatbelt) บน macOS, bubblewrap บน Linux**, และมี **alpha สำหรับ Windows**

structure พื้นฐาน: writer กำหนด policy ว่า process ที่จะ run นั้น (1) อ่าน/เขียน path ไหนได้บ้าง, (2) จะต่อ internet หรือเฉพาะ domain ไหน, (3) จะเรียก process ย่อย executable ตัวไหนได้. policy เขียนเป็น YAML/JSON ที่ `srt` compile เป็น Seatbelt profile บน macOS หรือ bubblewrap namespace บน Linux. เนื่องจาก **ไม่ต้องสร้าง VM หรือ container**, overhead ของการเริ่ม process อยู่ที่ **millisecond** ไม่ใช่ second-level ของ container

สำหรับ agent ecosystem จุดที่สำคัญที่สุดคือ **"drop-in sandboxing of MCP servers"** ที่ README เน้น. ตอนที่ Claude Code หรือ agent อื่นเรียก MCP server (Playwright, filesystem, Postgres, GitHub, custom tool) — process เหล่านี้ **ไม่เคยถูก sandbox** โดย default. ถ้า MCP server มี bug หรือ malicious tool definition, มันทำอะไรก็ได้ที่ user process ทำได้ (อ่าน SSH key, ลบไฟล์, upload data). `srt` ปิดช่องนี้ด้วยการให้ user run MCP server ภายใต้ profile ที่ลง precise permission ได้

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **sandbox ที่ปลอดภัยพอใช้ production กลายเป็น prerequisite ของ agent platform**. ตอน MCP ถูก push ขึ้นมาตั้งแต่ปลาย 2024, ส่วน security model เป็น weakness ที่ติดใจ enterprise — Fortune 500 CISO กว่าครึ่ง**ปฏิเสธจะ deploy MCP server ที่ internal engineer เขียน** เพราะไม่มี isolation layer ที่น่าเชื่อ. วันนี้ Anthropic ปล่อยสิ่งที่หลายทีมเคยอยาก build เอง — **Apache 2.0 แปลว่าใครก็ embed ได้**, cloud vendor, enterprise framework, security tool

ประเด็นที่สอง — **container-less isolation กำลัง rebuild stack ของ agent runtime**. VAST + Nvidia OpenShell (21 ต.ค.) ใช้ container + persistent storage; Daytona ($1B valuation, 20 ต.ค.) ใช้ container cloud ของตัวเอง; Microsoft Copilot Managed Runtime ใช้ Azure Container Apps. `srt` เลือก **OS-level primitive** (เพราะ Claude Code run ในเครื่องของ developer เองอยู่แล้ว) ซึ่งต่างมุมอย่างสิ้นเชิง — เร็วกว่า, แต่ security boundary อ่อนกว่า container ถ้า kernel ของ host มี vulnerability. **ไม่ใช่ substitute** แต่เป็น **complementary layer**: dev-side ใช้ srt, production ใช้ VAST+OpenShell

ประเด็นที่สาม — **Anthropic กำลังสร้าง "agent safety primitive portfolio"**. 20 ก.ย. Anthropic กับ OpenAI มี cross evaluation agreement; ต.ค. ปล่อย Agent Skills (280M installs) ให้ Linux Foundation; ตอนนี้ srt. ภายใน IPO window ของกลาง พ.ย., Anthropic กำลังขายตัวเองในฐานะ **"company ที่ทำ frontier model + สร้าง primitive ให้ ecosystem"** — คล้าย Google สมัย open-source TensorFlow + Android. underwriter จะชอบ pitch นี้มากกว่า "we are large labs who sell tokens"

## มุม AI Agent Platform

สำหรับ **Builders** (framework/orchestration): ถ้า build agent หรือ MCP server โดยไม่คิดเรื่อง sandbox, product ของคุณจะไม่ผ่าน enterprise procurement ที่เข้มขึ้น. การ integrate `srt` (หรือ **integrate Seatbelt/bubblewrap โดยตรง** สำหรับทีมที่อยากคุม 100%) จะกลายเป็น default feature ใน agent framework ตั้งแต่ Q1 2027. **จุดโต้ตอบ**: enterprise framework ที่ยัง require Docker ของตัวเองจะดู over-engineered เทียบกับ srt

สำหรับ **Users / Business**: ถ้ามี internal team deploy MCP server (เช่น ให้ agent เข้า Postgres, Slack, SharePoint ภายใน) — **เริ่ม audit ว่า server เหล่านี้ run ภายใต้ sandbox ไหมอยู่แล้ว**. บ่อยครั้งคำตอบคือ "ไม่", เพราะ MCP sample code ไม่ sandbox อะไรเลย. srt เป็น quick win ที่ security team กับ platform team wrap เพิ่มในสองสัปดาห์ — ก่อนที่ internal red team หรือ regulator จะมาถาม

สำหรับ **Ecosystem**: Docker, Firecracker (AWS Lambda runtime), gVisor (Google) จะโดนถามคำถามเดียวกัน — จำเป็นต้องปรับให้มีเวอร์ชัน "lightweight agent sandbox" ไหม. Daytona ($1B agentic cloud) และ VAST Agent Sandbox จะต้องชี้แจงว่า container stack ของตัวเองยัง value อะไรเมื่อ dev เลือก srt. และ **MCP registry ที่ Anthropic เพิ่งปล่อยให้ Linux Foundation**ควรเริ่มมี field "sandbox requirement" ของแต่ละ server ที่ list — ไม่ใช่แค่ตัว capability

## Sources
- [Meet Anthropic's sandbox-runtime: OS-Level Sandboxing for AI Agents, No Containers (MarkTechPost)](https://www.marktechpost.com/2026/10/24/anthropic-sandbox-runtime-ai-agent-sandbox/)
- [anthropics/sandbox-runtime (GitHub)](https://github.com/anthropics/sandbox-runtime)
- [Claude Code's Sandbox Is an npm Package — Run srt Yourself (DEV Community)](https://dev.to/gabrielanhaia/claude-codes-sandbox-is-an-npm-package-run-srt-yourself-and-watch-what-it-blocks-50i9)

---

## Audio script
วันเสาร์ 24 ตุลาคม Anthropic เปิดซอร์ส sandbox runtime หรือ srt — tool ที่อยู่หลัง Claude Code สำหรับ sandbox process ทั่วไปที่ระดับ OS โดยไม่ต้องมี container ภายใต้ Apache 2.0 เป็น npm package ที่ชื่อ at anthropic ai slash sandbox runtime เวอร์ชัน 0.0.81. การทำงานพึ่ง Seatbelt หรือ sandbox exec บน macOS, bubblewrap บน Linux, และ Windows alpha. User เขียน policy ว่า process ที่ run นั้นอ่านเขียน path ไหนได้ ต่อ internet domain ไหน และเรียก executable ตัวไหนได้ ส่วนของ Anthropic จะ compile เป็น OS native profile. เพราะไม่มี container หรือ VM, overhead อยู่ที่หลัก millisecond ไม่ใช่หลักวินาที. จุดที่สำคัญที่สุดคือ srt support drop in sandboxing ของ MCP server ซึ่งปัจจุบันตอนที่ Claude Code หรือ agent อื่นเรียก MCP server ไม่เคยถูก sandbox โดย default ถ้า MCP server มี bug หรือ malicious tool definition ทำอะไรก็ได้ที่ user process ทำได้. srt ปิดช่องนี้. ความสำคัญสามประเด็น หนึ่ง sandbox ที่ปลอดภัยพอ production กลายเป็น prerequisite ของ agent platform CISO Fortune 500 เกินครึ่งเคยปฏิเสธ MCP server ที่ internal engineer เขียนเพราะไม่มี isolation. สอง container less isolation รู้สร้าง stack ใหม่ของ agent runtime VAST plus Nvidia OpenShell ใช้ container srt เลือก OS level primitive ไม่ substitute กันแต่ complementary dev side ใช้ srt production ใช้ VAST plus OpenShell. สาม Anthropic กำลังสะสม primitive portfolio ให้ ecosystem — Agent Skills ลง Linux Foundation 280 ล้าน install, cross evaluation agreement กับ OpenAI, และตอนนี้ srt. ก่อน IPO กลางพฤศจิกายน Anthropic ขายตัวเองในมุม company ที่สร้าง primitive ให้ ecosystem คล้าย Google สมัย open source TensorFlow กับ Android. สำหรับ builder integrate srt หรือ Seatbelt กับ bubblewrap โดยตรงจะเป็น default feature ของ agent framework ภายใน Q1 2027. สำหรับ enterprise ที่มี internal MCP server เริ่ม audit ว่า server เหล่านี้ run ภายใต้ sandbox ไหมอยู่แล้ว ถ้าไม่ srt เป็น quick win ก่อน red team หรือ regulator มาถาม
