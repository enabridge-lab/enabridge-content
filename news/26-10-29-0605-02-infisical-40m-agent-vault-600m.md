---
date: 2026-10-29
slug: infisical-40m-agent-vault-600m
topic: agentic-ai
reading_time_min: 5
sources: 2
image_prompt: |
  An editorial isometric illustration of a glowing orange AI agent reaching
  through a slot of a dark steel vault to receive a key card, with the vault
  marked "AGENT VAULT". Credentials and API keys locked inside the vault behind
  a wall of code. Bold floating numbers: "$40M SERIES B", "$600M VALUATION",
  "10B SECRETS / DAY", "1,300 CUSTOMERS", "300K DEVELOPERS". Logos of Airbus,
  Volkswagen and Hugging Face stacked as small ribbons at the bottom. Deep navy
  and amber Kodak-film grade, strong contrast for 200px thumbnails, 1:1 aspect,
  no real human faces.
image: images/26-10-29-0605-02-infisical-40m-agent-vault-600m.png
---

# Infisical ปิด $40M Series B ที่ valuation $600M — "Agent Vault" กลายเป็น primitive ที่ Fortune 500 ซื้อ

## TL;DR
- **Infisical** (open-source secrets management) ปิด **Series B $40M** ที่ valuation **$600M** นำโดย **Elad Gil** (ลงต่อจาก Series A) พร้อม Gradient + Y Combinator
- **Scale ปัจจุบัน:** 1,300+ customer, 300,000+ developer, GitHub stars **30,000+**, secrets ที่ platform secure **10 billion per day**
- **Named customer:** Airbus, Volkswagen, Hugging Face, OpenRouter, Lucid, First American Financial, Wise, Clay
- **Agent angle:** ผลิตภัณฑ์ใหม่ชื่อ **Agent Vault** — ให้ AI agent เข้าใช้ sensitive system ได้โดย **ไม่เห็น credential จริง**, แต่ละ agent มี access boundary ของตัวเอง → ปิด risk ของ "LLM provider เห็น API key"
- Signal: **Credential layer สำหรับ non-human identity** กลายเป็น enterprise-ready category — pair กับ SailPoint Agentic Fabric (brief รอบที่แล้ว) + Microsoft Entra Agent ID; nice-to-know ขั้น proto-protocol กำลังเป็น paid product tier

## เกิดอะไรขึ้น

27 ตุลาคม 2026, **Infisical** ประกาศ Series B $40M ที่ valuation $600M. Elad Gil (angel investor ชื่อดัง + ex-Twitter/Mixer Labs) นำ round นี้ — เขาเป็นคนเดียวกับที่ lead Series A $16M เมื่อ มิ.ย. 2025. Gradient (venture fund ของ Google) และ Y Combinator เข้า round ด้วย. Infisical เริ่มต้นที่ YC W23 แล้วโตเร็ว — Series A valuation ที่เคยเป็น ~$80-100M (private estimate) ขยับ **6-7x ภายใน 16 เดือน**

Business number ที่เปิดเผย:
- **1,300+ customer** — รวม Fortune 500 หลายราย
- **300,000+ developer** ใช้ platform (self-hosted + cloud)
- **10 billion secrets per day** ที่ platform encrypt + rotate + distribute (= scale ของ Vault ของ HashiCorp หรือ AWS Secrets Manager ขนาดเล็ก)
- GitHub repo **30,000+ stars** (open-source core, enterprise feature ขายแยก)
- Named enterprise customer: **Airbus, Volkswagen Group, Hugging Face, OpenRouter, Lucid, First American Financial Corporation, Wise, Clay**

ผลิตภัณฑ์ที่ชี้ชัดการใช้เงิน round นี้คือ **Agent Vault** — มิติที่ Infisical พัฒนาเพื่อรองรับ AI agent ที่ต้องเข้าใช้ **database credential, API key, cloud resource access**. Pain point ที่ Infisical ชี้: **"Credential ที่ agent ต้องใช้มีมูลค่าสูงเกินกว่าจะส่งเป็น plain-text ให้ LLM เห็น"** — ถ้า agent ที่รัน บน OpenAI/Anthropic API โยน DB credential เข้า prompt, LLM provider เห็นหมด; prompt-injection attack เห็นหมด; model fine-tune เห็นหมด. Agent Vault ทำหน้าที่เป็น **proxy layer** — agent request action, Infisical execute credential-bound operation แล้วส่ง result กลับ, credential ไม่เคยออกจาก vault

Infisical ครอบ 4 ชั้น identity: secret, certificate, encryption key, privileged access. ชั้นสุดท้ายคือ **เพิ่ม AI agent เข้ามาเป็น class เดียวกับ developer + machine** โดยมี **access boundary** ที่ granular — เช่น agent A access ได้แค่ production DB read-only, agent B access ได้ staging + sandbox เท่านั้น, agent C access production write แต่ต้อง HITL approve ก่อน execute

## ทำไมสำคัญ

ประเด็นที่หนึ่ง — **Valuation 6-7x ภายใน 16 เดือน ของ secrets management ที่ pivot เข้า agent คือ signal ชัดสุดของ 2026**. HashiCorp Vault (ก่อน IBM buy ที่ $6.4B ปี 2024) ใช้ 11 ปี toll เพื่อถึง $500M run rate; Infisical ทำ 3 ปี YC-start ถึง $600M valuation. ความต่าง = **"non-human identity scale".** Developer count ของทุก platform ค่อนข้าง flat (~27M worldwide), แต่ **agent count โตแบบ exponential**. ถ้า agent เฉลี่ย 10 ตัวต่อ developer ภายใน 2027 (sensible lower bound เพราะ Copilot/Claude Code แต่ละตัวสร้าง sub-agent หลายตัว), nhIdentity ทั้งหมดจะโต 10-20x; **vendor ที่ครอง layer นี้ก่อนจะเก็บ TAM กลุ่มใหม่**

ประเด็นที่สอง — **Named customer list ของ Infisical มี 2 ส่วนที่สำคัญ**. Airbus + Volkswagen = **safety-critical industrial** (ไม่ใช่ tech-first); Hugging Face + OpenRouter = **AI inference platform** ที่ secure มากที่สุดในโลก (ถ้า HF/OR ไม่ trust Infisical ก็ไม่ใช้). การที่ทั้งสองประเภทใช้ Infisical ก่อน Fortune 500 bank adopt เต็มที่ บอกว่า technical quality ผ่านทั้ง compliance + security review ของ enterprise ที่เข้มที่สุด — **vendor evaluation playbook ของ CISO กลาง 2027 จะมี Agent Vault เป็น checklist item เหมือน SSO + MFA**

ประเด็นที่สาม — **Elad Gil ลงต่อ 2 round ติดคือ pattern angel ที่สำคัญ**. Elad angel 400+ startup, lead round เองไม่กี่ตัว; เขา lead Infisical Series A ที่ไม่มี VC firm คู่, แล้ว **lead Series B อีก round หนึ่งหลัง 16 เดือน** = conviction extreme. Pattern นี้ซ้ำกับ Perplexity, Harvey, Loom (ยุคก่อน) ที่ Elad แยกจาก consensus VC thesis ก่อน 12-18 เดือน. ถ้าดูแผน Infisical trajectory, **Series C ปี 2027 ที่ $1.5-2B valuation ไม่ไกล** (เทียบ 1Password $8.6B หลัง Series C ปี 2023)

## มุม AI Agent Platform

สำหรับ **Builders**: ถ้าคุณสร้าง agent framework (LangGraph, CrewAI, Vercel AI SDK, Claude Agent SDK), **integrate Infisical Agent Vault เป็น first-party connector** = selling point ชัดต่อ enterprise. ปัจจุบัน agent framework ส่วนใหญ่ให้ developer จัดการ secret เอง (`.env file`, OS keyring) — ไม่ pass enterprise CISO review. Framework ที่ซัพพอร์ต Agent Vault + Entra Agent ID + SailPoint Agentic Fabric out-of-the-box จะ win enterprise contract. ทางเลือก alternate stack: HashiCorp Vault + Microsoft Entra Agent ID (ที่ Microsoft push หนัก), AWS Secrets Manager + IAM for Agents (คาด ประกาศ reinvent ธ.ค. 2026)

สำหรับ **Users / Business**: ก่อน deploy agent ใน production, พูดคุยกับ CISO ให้ **list "agent credential path"** — ปัจจุบันของทุกองค์กรคือเละ: dev เอา API key เข้า Slack, agent prompt ส่ง DB password ไป OpenAI, log file เก็บ Bearer token. ให้ Infisical/Entra Agent ID/Vault ครอบ ก่อน agent ขึ้น production. ไม่ใช่ "future problem" — เป็น "ภายใน 30 วัน" ก่อน audit หน้างาน. Enterprise ไทย (SCB, Krungsri, PTT, True) ที่พูด "AI agent in production" คาดว่าตอนนี้มี **vulnerability ที่ credential ของ agent รั่วหรือถูก inject** — audit urgent

สำหรับ **Ecosystem**: การแยกชั้น "secrets vendor" กับ "identity vendor" กำลังเริ่มเลือน. **Infisical** ขยับ secrets → agent identity, **SailPoint** ขยับ identity → agent fabric, **Microsoft Entra** ขยับ IDP → agent ID. ชั้นที่ convergence นี้คือ **"non-human workforce identity provider"** — category ใหม่ที่ 2027 น่าจะมี 3-5 vendor เท่านั้น เพราะ CISO ไม่ชอบ switch vendor layer. ถ้าใครยังไม่มีจุดยืน พลาด window ภายใน 12 เดือน

## Sources
- [Infisical Raises $40 Million at $600 Million Valuation to Secure the AI Agent Economy (PR Newswire)](https://prnewswire.com/news-releases/infisical-raises-40-million-at-600-million-valuation-to-secure-the-ai-agent-economy-302920994.html)
- [Infisical: $16 Million Series A Raised (Pulse2)](https://pulse2.com/infisical-16-million-series-a-raised-for-transforming-enterprise-secrets-identity-and-access-management/amp/)

---

## Audio script
Infisical บริษัท open-source secrets management ปิด Series B 40 ล้านดอลลาร์ ที่ valuation 600 ล้าน Elad Gil นำ round เป็นรอบที่สองติด ตัวเลขที่สะท้อน scale ปัจจุบัน ลูกค้า 1,300 ราย developer ใช้ platform 300,000 คน secrets ที่ encrypt กับ rotate วันละ 10,000 ล้านชิ้น customer ที่เปิดชื่อรวม Airbus, Volkswagen, Hugging Face, OpenRouter, Wise ประเด็นที่สำคัญคือผลิตภัณฑ์ใหม่ที่เรียกว่า Agent Vault — ให้ AI agent เข้า database กับ API ได้โดยไม่เห็น credential จริง ที่ Infisical ชี้คือ credential ที่ agent ต้องใช้มีมูลค่าสูงเกินกว่าจะส่งเป็น plain text ให้ LLM เห็น ถ้า agent รันบน OpenAI หรือ Anthropic API ส่ง DB password เข้า prompt provider เห็นหมด prompt injection เห็นหมด model fine-tune เห็นหมด Agent Vault ทำหน้าที่เป็น proxy layer agent request action Infisical execute operation แล้วส่ง result กลับ credential ไม่เคยออกจาก vault Signal ที่น่าสังเกตคือ valuation โต 6-7 เท่าภายใน 16 เดือน สำหรับ secrets management ที่ pivot เข้า agent HashiCorp Vault ใช้ 11 ปีถึง 500 ล้าน run rate Infisical ทำ 3 ปีถึง 600 ล้าน valuation ความต่างคือ non-human identity scale สำหรับทีมที่กำลัง deploy agent ใน production คุยกับ CISO ให้ list credential path ของ agent วันนี้ก่อน audit หน้างาน บริษัทไทยที่พูด AI agent in production น่าจะมี vulnerability ที่ credential รั่ว audit urgent
