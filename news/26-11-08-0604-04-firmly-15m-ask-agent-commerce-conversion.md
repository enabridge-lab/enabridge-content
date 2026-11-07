---
date: 2026-11-07
slug: firmly-15m-ask-agent-commerce-conversion
topic: use-case
reading_time_min: 4
sources: 3
image_prompt: |
  An editorial isometric illustration of an e-commerce storefront on a
  laptop screen. A large chat bubble labeled "ASK AGENT" sits above the
  product grid. Two stacked numbers float beside it: "+18% CONVERSION"
  and "+23% AOV". A small tag reads "$15M SERIES A" and another says
  "1 LINE OF JS". Logos of J.P. Morgan Payments, Mastercard, and Samsung
  NEXT ride a small ribbon as co-investors. In the background a wide
  highway labeled "11M MERCHANTS" leads to a glowing agent hub. Clean
  editorial style, retail magenta and emerald palette, 1:1 aspect, high
  contrast for 200px thumbnail, no real human faces (silhouettes OK).
image: images/26-11-08-0604-04-firmly-15m-ask-agent-commerce-conversion.png
---

# firmly ปิด $15M + ปล่อย Ask Agent — ขาย agentic commerce เป็น "JS 1 บรรทัด" บวกตัวเลข conversion ที่น่าสนใจ

## TL;DR
- firmly ปิด Series A $15M (รายงานหลาย source นำโดย Squarepoint Capital, Axios Pro ระบุ J.P. Morgan Payments + Mastercard + Samsung NEXT ร่วมด้วย) — ยอด funding รวม ~$20M
- Launch **Ask Agent** — conversational shopping บนเว็บ merchant ติดด้วย JS 1 บรรทัด ใช้ catalog + pricing + inventory จริงเวลา
- Early deployment: conversion +18%, AOV +23% (company-reported, ยังไม่ 3rd party verify) — ซึ่งเป็น top-line number ที่ agentic commerce ขาดมาตลอด

## เกิดอะไรขึ้น
วันที่ 5 พฤศจิกายน firmly — startup agentic commerce ที่ Perplexity เคยใช้สร้าง merchant network — ประกาศปิด Series A $15M ทำให้ยอดสะสม ~$20M ตัว cap table น่าสนใจ: Squarepoint Capital lead (per หลาย source) + J.P. Morgan Payments + Mastercard + Samsung NEXT ร่วม — การที่ payment infrastructure giant 2 รายและ corporate venture ของ Samsung เข้าร่วม signal ชัดว่า agentic commerce กลายเป็นเกมของ incumbent payment rail ไม่ใช่ fringe play อีก

ของจริงคือ product ที่ launch คู่กัน — **Ask Agent**: merchant เอา JS 1 บรรทัดวางบนเว็บ แล้ว shopper พิมพ์ความต้องการแบบธรรมชาติ ("หารองเท้าวิ่งใต้ 3,000 บาท ที่ส่งถึงภายในวันพรุ่งนี้") agent ตอบ recommendation จาก catalog, pricing, และ inventory จริงเวลาของ merchant เอง ไม่ใช่ generic product search แบบ Google หรือ generic chatbot แบบ Shopify Magic — จุดสำคัญคือ **merchant ควบคุม catalog เอง** (ไม่มี marketplace commission, ไม่มี Perplexity/ChatGPT เป็นคนกลาง) และ **integration แค่ 1 บรรทัด** (ไม่มี implementation project 3 เดือน)

ตัวเลข early deployment ที่ firmly เผยคือ **conversion rate +18%** และ **AOV +23%** — ถ้าจริง เป็น proof point ที่หมวด agentic commerce รอมาทั้งปี (Shopify, Klarna, PayPal, Visa ต่างมี agentic commerce initiative แต่ไม่มีใครเคย publish conversion lift ที่ consistent ใน case study) Pattern คือ shopper ที่ "describe intent" ให้ agent conversion เร็วกว่า shopper ที่ browse facet filter แบบเดิม — เพราะ agent ตัด friction ของ "แปล query เป็น filter combination" และตัด fatigue ของการเลื่อนดูของ 20 หน้า

Positioning คู่กันคือ firmly Connect — "no-code connection to sell through new channels" ที่เชื่อม merchant เข้ากับ 11 ล้าน merchant network รวมถึง agent channel ภายนอก (Perplexity Shopping, ChatGPT commerce, Amazon Rufus) — ขายเป็น horizontal distribution layer

## ทำไมสำคัญ
2025-26 เต็มไปด้วย agentic commerce pitch แต่ metric ที่ CFO ของ retailer อยากเห็นคือ "conversion + AOV + customer acquisition cost" ไม่ใช่ demo cool การที่ firmly เผย +18% conversion / +23% AOV สองตัวพร้อมกัน (ถ้า hold up ภายใต้ analyst scrutiny) จะเป็น anchor number ที่หมวด agentic commerce ทั้งหมดต้อง benchmark ต่อ — ไม่ใช่เพราะ firmly ใหญ่ที่สุด แต่เพราะมันเป็น public data point แรกที่มีตัวเลขพร้อม

Economic model ก็สะอาด — merchant จ่าย firmly แบบ subscription หรือ transaction, ไม่มี marketplace commission layer เพิ่ม, และ merchant **ไม่สูญเสีย ownership ของ customer data** แบบที่ marketplace route ทำ — นี่คือ wedge ที่ shopify/BigCommerce merchant กำลังต้องการ ขณะที่ Perplexity/ChatGPT commerce ยัง route traffic ผ่านตัวเอง

Caveat ต้องชัด — ตัวเลขเป็น company-reported, early deployment sample size เล็ก และ selection bias เยอะ (early customer ของ firmly อาจเป็น merchant ที่ product page ไม่ดีมาก่อน ดังนั้น lift ย่อมสูง) ต้องรอ independent case study กับ merchant ขนาดใหญ่ 6-12 เดือนข้างหน้าถึงจะ confirm ได้ว่าเป็น real lift

## มุม AI Agent Platform
**Builders** — architecture ของ Ask Agent น่าสนใจ: agent runtime อยู่ข้าง merchant catalog โดยตรง ไม่ใช่ model-centric ที่ pull data ผ่าน RAG — ข้อดีคือ latency ต่ำและ data freshness ดี (shopper เห็น inventory จริงเวลา) ข้อเสียคือ agent personality ลบ model-dependent ถ้าคุณกำลัง build agent commerce layer ของตัวเอง อย่า copy Shopify Magic pattern (chatbot generic) — ให้ copy firmly pattern (agent + catalog เป็น unit เดียวกัน) แทน

**Users / business** — retailer ไทยที่มีเว็บ D2C (fashion, beauty, home, electronics) ควร trial agentic conversational layer ภายใน 6-12 เดือนข้างหน้า — ไม่ใช่เพราะต้องรีบ แต่เพราะ customer habit กำลังเปลี่ยน shopper Gen Z คุ้นกับการ "ถาม" ChatGPT ก่อนตัดสินใจซื้อ ถ้า merchant ไม่มี agent ของตัวเองบนเว็บ customer จะเดินผ่าน generic agent ซึ่ง merchant สูญเสีย personalization

**Ecosystem** — Shopify มี Magic และ Oberlo; BigCommerce มี Catalyst; Salesforce Commerce Cloud มี Einstein — ทุกคนจะเห็นตัวเลข +18/+23 ของ firmly แล้วรีบปล่อย feature คล้าย ๆ ใน Q1-Q2 2027 ราคาที่ firmly ตั้ง (subscription-based, no commission) จะเป็น anchor ที่ dictate market pricing

## Sources
- [firmly Raises $15 Million Series A and Launches Ask Agent (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/11/05/3396499/0/en/firmly-raises-15-million-series-a-and-launches-ask-agent-to-help-merchants-more-easily-adopt-agentic-commerce.html)
- [Agent-Shopping Firms Raise $30M as Uber Logs 4 Agent Rides (FourWeekMBA)](https://fourweekmba.com/ai-agent-shopping-firms-raise-30m-as-uber-logs-4-agent-rides/)
- [firmly launches firmly connect, the first agentic commerce platform (Agile Brand Guide)](https://agilebrandguide.com/firmly-launches-firmly-connect-the-first-agentic-commerce-platform-that-allows-merchants-to-directly-connect-to-any-agent-or-agentic-marketing-channel-without-deploying-any-code/)

---

## Audio script
firmly ซึ่งเป็น startup agentic commerce ประกาศปิด Series A 15 ล้านเหรียญเมื่อวันที่ 5 พฤศจิกายน ทำให้ยอดสะสม 20 ล้านเหรียญ ตัวที่น่าสนใจคือ cap table Squarepoint Capital เป็น lead J.P. Morgan Payments Mastercard และ Samsung NEXT เข้าร่วม การที่ payment infrastructure giant สองรายเข้ามา signal ชัดว่า agentic commerce ไม่ใช่ fringe play แล้ว firmly launch product ชื่อ Ask Agent ซึ่ง merchant เอา JavaScript บรรทัดเดียววางบนเว็บ แล้ว shopper พิมพ์ความต้องการแบบธรรมชาติ agent ตอบ recommendation จาก catalog pricing และ inventory จริงเวลาของ merchant เอง จุดสำคัญคือ merchant ควบคุม catalog เอง ไม่มี marketplace commission ไม่มี agent คนกลาง และ integration แค่บรรทัดเดียว ตัวเลข early deployment conversion rate เพิ่ม 18 เปอร์เซ็นต์ AOV เพิ่ม 23 เปอร์เซ็นต์ ถ้าจริงเป็น proof point ที่หมวด agentic commerce รอมาทั้งปี caveat คือตัวเลขเป็น company-reported sample เล็ก selection bias เยอะ ต้องรอ independent case study 6 ถึง 12 เดือนข้างหน้า สำหรับ retailer ไทยที่มีเว็บ D2C ควร trial agentic conversational layer ภายในปีหน้า ไม่ใช่เพราะต้องรีบ แต่เพราะ customer habit กำลังเปลี่ยน shopper Gen Z คุ้นกับการถาม ChatGPT ก่อนตัดสินใจซื้อ ถ้าร้านไม่มี agent ของตัวเอง customer จะเดินผ่าน generic agent แล้วร้านเสีย personalization สำหรับ Shopify BigCommerce Salesforce Commerce Cloud ทุกคนจะปล่อย feature คล้ายๆกันใน Q1-Q2 2027
