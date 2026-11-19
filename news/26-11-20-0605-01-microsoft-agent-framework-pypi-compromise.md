---
date: 2026-11-19
slug: microsoft-agent-framework-pypi-compromise
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  An editorial isometric illustration of a dark server room with a glowing
  Python package box labeled "agent-framework 1.26.1" cracked open; a shadowy
  hand lifts out golden keys tagged "AZURE", "AWS", "GITHUB", "OPENAI". A
  giant red stamp overlays the box reading "HIJACKED", and a smaller banner
  says "192,534 DOWNLOADS/MONTH". Clean editorial style, deep navy and red
  alert palette, 1:1 aspect, no real human faces (silhouette hand only),
  high contrast so numbers stay readable at 200px.
image: images/26-11-20-0605-01-microsoft-agent-framework-pypi-compromise.png
---

# Microsoft agent-framework ถูก hijack บน PyPI — คนสร้าง agent คือ attack surface ใหม่

## TL;DR
- Microsoft agent-framework เวอร์ชัน 1.26.1 และ 1.26.2 ถูกดันขึ้น PyPI วันที่ 17 พฤศจิกายน ฝัง credential stealer ที่รันผ่าน `.pth` ตอน Python start — ไม่ต้อง import ก็โดน
- ขโมย secret ของ Azure, AWS, GitHub, Docker, Hugging Face และ OpenAI พร้อม environment + cloud identity token ส่งเข้า webhook
- Wiz ชี้ว่าผู้โจมตีอาจได้ client certificate ของ Microsoft ESRP (Engineering System Release Pipeline) — แปลว่าไม่ใช่ typosquat แต่เป็น supply-chain ของ Microsoft เอง

## เกิดอะไรขึ้น
เย็นวันอังคารที่ 17 พฤศจิกายน มี package `agent-framework` สองเวอร์ชันถูกดันขึ้น PyPI ห่างกัน 33 นาที ภายใต้บัญชี Microsoft อย่างเป็นทางการ ทั้ง 1.26.1 และ 1.26.2 ยังคง dependency `agent-framework-core 1.26.0` ตัวจริงไว้ — ทำให้ framework ทำงานตามปกติ ไม่มีสัญญาณผิดสังเกต ผู้ใช้ที่ `pip install` ตามปกติจึงได้ทั้งของจริงและ payload พร้อมกัน

สิ่งที่อยู่ข้างในคือ Python startup hook ผ่าน `.pth` file — เทคนิคที่ทำให้ malware รันทุกครั้งที่ Python interpreter เริ่ม process ใน environment นั้น ไม่จำเป็นต้องมี code ไหน `import agent_framework` เลย Help Net Security รายงานว่า stealer เก็บ environment variables, cloud identity token, credentials ของ Azure/AWS/GitHub/Docker/Hugging Face/OpenAI แล้ว exfiltrate ไปยัง webhook ที่ attacker ควบคุม — crosswall ไปทั้ง developer workstation, CI runner และ production container ที่โหลด package นี้

Wiz ขุดต่อแล้วชี้ว่าการที่ attacker สามารถ publish เวอร์ชันใหม่ภายใต้บัญชี Microsoft ได้ น่าจะมาจากการ compromise client certificate และ private key ของ Microsoft ESRP ซึ่งเป็น release pipeline ภายในที่ Microsoft ใช้ sign package ของตัวเอง PyPI ได้ quarantine ทั้งสองเวอร์ชันแล้ว แต่ Help Net Security ยก OX data ที่บอกว่า `agent-framework` มียอด download เฉลี่ย 192,534 ครั้งต่อเดือน TechRadar ประมาณ actual malicious download ที่ประมาณ 150 ครั้ง — ตัวเลขน้อยแต่กลุ่มเป้าหมายคือ builder ของ agent ที่เก็บ key ของทุก cloud ไว้ใน environment

## ทำไมสำคัญ
นี่คือการโจมตีครั้งแรกที่ pitch ตัวเองชัดเจนว่า "attack surface ใหม่ของยุค agent คือคนที่กำลัง build agent" ปีที่แล้วเรายังคุยกันว่า prompt injection กับ tool misuse เป็น risk หลักของ agentic AI ตอนนี้ risk จริงอยู่ที่ layer ต่ำกว่านั้น — supply chain ของ framework ที่คุณ pip install เพื่อสร้าง agent คือ single point of compromise ที่กินทั้ง key ของ model provider, cloud, source control และ container registry ในคำสั่งเดียว

จังหวะก็เจ็บเป็นพิเศษ — Microsoft Agent Framework (ตัว successor ของ AutoGen) กำลัง gain momentum ในกลุ่ม enterprise ที่ต้องการ MCP + A2A native support โดยไม่ต้องไปที่ Python SDK ของ OpenAI หรือ Anthropic การที่ ESRP cert น่าจะโดน compromise เล่าเรื่องใหญ่กว่านั้น — ถ้า attack vector เป็น Microsoft's own release pipeline ไม่ใช่ typosquat คำถามคือมี package อื่นใต้บัญชี Microsoft ที่โดนเหมือนกันไหม และ hooks แบบนี้ pivot ง่ายไปที่ `openai-python`, `langchain`, `anthropic` SDK ของจริงได้แค่ไหน

Caveat สำคัญ — Microsoft ยังไม่ confirm ว่า ESRP ถูก compromise จริง (Wiz พูดในฐานะ hypothesis จากการ reverse) และ Neowin เขียนชัดว่า "it is not yet known how the threat actor was able to publish" ต้องรอ post-mortem อย่างเป็นทางการก่อน blame infrastructure อย่างไรก็ตาม Help Net Security ยืนยันว่า quarantine + forced rotation เป็น standard response และควรเริ่มทันที

## มุม AI Agent Platform
Builders — ถ้าคุณกำลังสร้าง agent framework ด้วย Microsoft agent-framework บน Python ให้ pin version กลับไปที่ 1.26.0 ทันที scan environment ด้วย `pip show agent-framework` และ rotate ทุก cloud credential ที่เคย reach ได้จาก dev หรือ CI machine ที่ touch package นี้ ใช้ `pip install --require-hashes` กับ lockfile ที่ sign แล้วเป็น mandatory ไม่ใช่ optional อีกต่อไป และคิดเรื่อง ephemeral credential (short-lived token + OIDC) แทน long-lived API key ใน environment variables

Users/business — enterprise ที่กำลัง deploy agent บน Microsoft stack ต้องถาม vendor ทันทีว่า package version ไหนที่อยู่ใน production environment ก่อน 17 พฤศจิกายน ถ้าเป็น managed service (Azure AI Foundry, Copilot Studio) ควรขอ incident report ภายใน 48 ชั่วโมง สำหรับ Enabridge และบริษัทไทยที่กำลัง pilot agent — supply chain ของ framework จะกลายเป็น vendor-selection criteria ระดับเดียวกับ model choice

Ecosystem — PyPI, npm และ Hugging Face Hub จะเจอ pressure หนักขึ้นเรื่องการ sign + verify maintainer identity ถ้า Microsoft's ESRP ซึ่งเป็น gold standard ของ code signing ยัง compromise ได้ ecosystem ต้องย้ายไปที่ attestation model ที่ hardware-rooted (sigstore + TPM) ไม่ใช่แค่ cert-based เพียงอย่างเดียว เราน่าจะเห็น PEP ใหม่เกี่ยวกับ mandatory provenance ภายใน Q1 2027

## Sources
- [Attackers Compromise Microsoft's Agent Framework PyPI Package to Steal Cloud Credentials (The Hacker News)](https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html)
- [Microsoft agent-framework Compromised: Credential Stealer Targets Azure and CI Pipelines (Wiz)](https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi)
- [Credential stealer slipped into Microsoft's official Python agent framework (Help Net Security)](https://www.helpnetsecurity.com/2026/11/19/microsoft-agent-framework-package-pypi-compromised/)
- [Microsoft Agent Framework PyPI Supply-Chain Attack: Versions 1.26.1 and 1.26.2 Steal Cloud Credentials (Orca Security)](https://orca.security/resources/research/microsoft-agent-framework-pypi-supply-chain-attack-versions-1-26-1-and-1-26-2-steal-cloud-credentials/)
- [Microsoft's agent-framework PyPI package Compromised with Credential Stealer (Socket)](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer)

---

## Audio script
เรื่องใหญ่วันนี้ Microsoft agent-framework แพ็กเกจที่ builder ใช้สร้าง agent บน Python ถูก hijack บน PyPI เมื่อวันที่ 17 พฤศจิกายนที่ผ่านมา เวอร์ชัน 1.26.1 กับ 1.26.2 ถูกดันขึ้นห่างกันแค่ 33 นาที ภายใต้บัญชี Microsoft ของจริง ข้างในฝัง credential stealer ที่รันผ่าน Python startup hook — แปลว่าไม่ต้อง import ก็โดน ขโมยทั้ง key ของ Azure AWS GitHub Docker Hugging Face และ OpenAI ส่งเข้า webhook ของ attacker

Wiz วิเคราะห์ว่าผู้โจมตีน่าจะได้ client certificate ของ Microsoft ESRP ซึ่งเป็น release pipeline ภายในของ Microsoft เอง นี่ไม่ใช่ typosquat — มันคือ supply chain attack ของจริง package นี้มียอด download เดือนละเกือบสองแสนครั้ง กลุ่มเป้าหมายคือคนสร้าง agent ที่เก็บ key ทุก cloud ไว้ใน environment

ประเด็นที่ควรเก็บ — นี่คือครั้งแรกที่ attack surface ใหม่ของยุค agent ชัดเจนว่าอยู่ที่ "คนที่กำลัง build agent" ไม่ใช่ agent ที่ run แล้ว ถ้าทีมใช้ Microsoft agent framework ให้ pin version กลับไป 1.26.0 ทันที scan environment แล้ว rotate credential ทุกตัว บริษัทไทยที่ deploy agent บน Microsoft stack ควรถาม vendor ภายใน 48 ชั่วโมงว่า version ไหนอยู่ใน production ก่อนวันที่ 17 ครับ
