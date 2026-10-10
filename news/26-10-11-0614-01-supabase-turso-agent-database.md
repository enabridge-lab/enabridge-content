---
date: 2026-10-10
slug: 26-10-11-0614
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: |
  Editorial isometric illustration of a central Supabase-green server tower absorbing a smaller
  Turso logo cube on its left, while on its right a swarm of tiny agent robots each carry their
  own glowing miniature database crate. Giant stacked labels in the sky: "+$150M FUNDING",
  "DATABASE PER AGENT", "600% GROWTH". Deep navy background, neon lime accents, strong contrast
  for 200px thumbnail. 1:1 aspect ratio, no real human faces.
image: images/26-10-11-0614-01-supabase-turso-agent-database.png
---

# Supabase ปิด $150M พร้อมซื้อ Turso — "ฐานข้อมูลหนึ่งอันต่อ agent หนึ่งตัว" กำลังกลายเป็น primitive ใหม่ของ runtime

## TL;DR
- 2 ต.ค. 2026 — Supabase ปิดดีลคู่ **$150M รอบใหม่ (นำโดย GIC จากสิงคโปร์, มี CapitalG/IronArc/SquarePeg ร่วม)** + ซื้อ Turso (SQLite-เบส) ไม่เปิดเผยมูลค่า — valuation ประเมิน ~$10.65B
- Pitch คือ **"database per agent task"** — agent ทุกตัวได้ DB ส่วนตัวที่เกิด-ตาย-เขียน-ลบในวินาที, Supabase อ้างว่าทราฟฟิกจาก agent โตขึ้น **600%** ในปีเดียว
- Glauber Costa ผู้ก่อตั้ง Turso ย้ายไปเป็น **Head of Agentic Services** ที่ Supabase — Turso แพลตฟอร์มเดิมยังรันต่อ แต่ลูกค้ามีทางย้ายเข้า Supabase ecosystem

## เกิดอะไรขึ้น
วันพฤหัสที่ 2 ต.ค. Supabase ประกาศปิดรอบใหม่ **$150M นำโดย GIC** กองทุนความมั่งคั่งแห่งชาติของสิงคโปร์ ควบด้วยการเข้าซื้อ **Turso** บริษัท SQLite สตาร์ทอัพที่ได้ YC Combinator ปั้นมา สัญญาซื้อขายไม่เปิดเผยมูลค่า แต่สื่อสายธุรกิจประเมิน valuation ของ Supabase ที่ **$10.65B** — ขยับขึ้นเล็กน้อยจาก Series F รอบเดือนมิถุนายน ($10.5B)

เรื่องสำคัญไม่ใช่ตัวเลข แต่คือ **เหตุผล** ที่ CEO Paul Copplestone ให้สัมภาษณ์กับ The Information: ปริมาณ API call จาก **AI agent** ที่ยิงเข้าฐานข้อมูล Supabase โตขึ้น **600%** ในช่วง 12 เดือน และรูปแบบการใช้งานผิดจาก SaaS app แบบคลาสสิก — agent ตัวหนึ่งขอ DB มาเล่นแป๊บเดียวแล้วทิ้ง, ตัวต่อไปขอใหม่ parallel สิบตัว การจัดการ connection pool แบบ Postgres เดิม**คุมไม่อยู่**

Turso เข้ามาตอบปัญหานี้ตรง ๆ — libSQL (fork ของ SQLite ที่ Turso maintain) **spin ฐานข้อมูลใหม่ได้ในหลักมิลลิวินาที**, คิดราคาต่อ query ไม่ใช่ต่อ connection, และรันทั้งในคลาวด์ของ Supabase หรือ **bring-your-own-cloud** ของลูกค้า เป้าหมายที่ Copplestone ตั้งคือ "agent หนึ่งตัว หนึ่ง task ได้ DB หนึ่ง instance" — ไม่ใช่ shared tenant, ไม่ใช่ schema per customer, แต่คือ **ephemeral database per execution**

Glauber Costa founder Turso ย้ายไปเป็น **Head of Agentic Services** ที่ Supabase — ตำแหน่งที่ไม่เคยมีก่อน บอก org chart ตัวนึงว่า agent infrastructure จะเป็น P&L แยกจาก developer platform เดิม

## ทำไมสำคัญ
นี่คือ **primitive change** ที่คนเล็ก ๆ ในวงการ cloud มองออกตั้งแต่ปี 2024 แล้วแต่คนใหญ่เพิ่งขยับ — ฐานข้อมูลสำหรับ agent **ต้อง scale ลงไปจน serverless ต่อการประมวลผล**, ไม่ใช่ scale ขึ้นต่อ workload Supabase เป็นเจ้าแรกใน OSS developer platform tier ที่ยอม shift การคิดราคาและ runtime ไปทางนี้แบบเต็มตัว

วาง pattern ปีนี้ไว้ข้าง ๆ กัน — Nous Research ขาย **"bring your own compute"** สำหรับ model inference, Netskope ขาย **"shared credit pool"** สำหรับ security agent, Supabase ขาย **"ephemeral DB per agent"** — ทั้งสามเลิก sell "seat/SKU per user" แล้วย้ายไปขายทรัพยากรที่ agent ใช้จริง สิ่งที่เคยเป็น developer tool กำลังกลายเป็น **agent runtime layer** และคนที่ครองเลเยอร์นี้จะได้ margin หนากว่า SaaS คลาสสิก

สำหรับ Postgres hosting incumbents (Neon, Crunchy, Supabase เอง, และ RDS/Cloud SQL) นี่คือ **shot across the bow** — Neon ที่ขาย "database branching for Copilot" ตอบ pattern นี้ได้บางส่วน แต่ Supabase + Turso ตอบได้ครบตั้งแต่ connection pooling ลงไปจน storage engine หวัง Cloud SQL จะเป็นเจ้าถัดไปที่ขยับ

## มุม AI Agent Platform
**Builders** ที่ขาย agent framework (CrewAI, AutoGen, LangGraph, Mastra) ต้องรู้ว่าสถาปัตยกรรม "ให้ agent ทุกตัวแชร์ Postgres เดียวกัน" กำลัง**หมดอายุ** — ลูกค้า enterprise จะเริ่มขอ data isolation ระดับ task, ไม่ใช่แค่ระดับ tenant วาง data layer ของ framework ให้รองรับ libSQL หรือ Turso-style ephemeral DB ตั้งแต่ตอนนี้

**Users / business** ที่ deploy agent ใน workflow ควรถามเวนเดอร์: "เมื่อ agent ของฉันเก็บ context ใน DB, มันแชร์กับ tenant อื่นหรือเปล่า? เมื่อฉันลบ agent, data หายจริงหรือเพียงแค่ unmap?" — คำตอบจะชี้ว่าเวนเดอร์พร้อม compliance ปีหน้าหรือไม่

**Ecosystem** — GIC นำ (ไม่ใช่ Sequoia/a16z) เป็น signal — sovereign wealth fund เริ่มเห็น agent infra เป็น strategic asset ที่ยาวพอจะถือ 10 ปี บวกกับ Turso ที่รองรับ BYOC (bring-your-own-cloud) — pitch สำหรับรัฐบาลและ regulated industry ที่ต้องเก็บข้อมูลใน sovereign cloud ง่ายขึ้นมาก; SaaS ไทยที่ขาย GovTech/BankingTech ควรเพิ่ม BYOC + database isolation เป็น default สิ่งที่เคยเป็น "nice to have" ปี 2024 กำลังจะเป็น **table stakes สำหรับ RFP ปี 2027**

## Sources
- [Supabase raises $150M and acquires Turso to scale agentic databases — Verdict](https://www.verdict.co.uk/supabase-150m-funding-turso-acquisition/)
- [Supabase Raises $150M and Acquires Turso — SaaS Rise](https://www.saasrise.com/deals/database-startup-supabase-raises-150m-acquires-turso-1ff0d608-c05d-4c67-bdb7-96fa74a3916a)
- [Supabase Raises $150 Million And Acquires Turso As AI Agents Drive 600% Database Growth — Ventureburn](https://ventureburn.com/supabase-raises-150-million-acquires-turso-for-agentic-ai/)
- [Supabase Acquires Turso: A Database Per Agent Task — ChatPicture](https://www.chatpicture.com/en/blog/supabase-bought-turso-because-agents-need-a-database-per-task)
- [Supabase raises $150M led by GIC — Source Trail](https://www.sourcetrail.com/sql/supabase-raises-150m-led-by-gic-and-acquires-turso-to-serve-ai-agents/)

---

## Audio script
สวัสดีครับ วันเสาร์ที่ 11 ตุลาคม 2026 ครับ ข่าวแรกวันนี้คือดีลที่น่าสนใจมากในวงการ developer platform — Supabase เจ้าของฐานข้อมูล Postgres แบบ open source ที่หลายคนใช้กัน ปิดรอบใหม่ 150 ล้านดอลลาร์ นำโดย GIC ซึ่งเป็นกองทุนความมั่งคั่งของสิงคโปร์ และพร้อมกันนั้นก็ซื้อสตาร์ทอัพชื่อ Turso ที่ทำ SQLite แบบ serverless ด้วย — มูลค่าดีลไม่เปิดเผย แต่ valuation รวมของ Supabase ขยับไปที่ประมาณ 10 point 65 billion ครับ

เหตุผลที่น่าสนใจคือ Supabase บอกว่าทราฟฟิกจาก AI agent ที่ยิงเข้า DB โตขึ้น 600 เปอร์เซ็นต์ในปีเดียว และ pattern การใช้งานผิดจาก SaaS app ปกติ agent ตัวหนึ่งขอฐานข้อมูลมาเล่นแป๊บเดียวแล้วทิ้ง ตัวต่อไปขอใหม่ขนานสิบตัว การจัดการ connection แบบ Postgres เดิมคุมไม่อยู่ Turso เลยเข้ามาตอบ — spin ฐานข้อมูลใหม่ได้ใน มิลลิวินาที คิดราคาต่อ query ไม่ใช่ต่อ connection รันในคลาวด์ Supabase หรือ bring-your-own-cloud ก็ได้ Glauber Costa founder Turso ย้ายไปเป็น Head of Agentic Services ที่ Supabase ตำแหน่งใหม่ที่ไม่เคยมีก่อน

สำหรับทีมในไทยที่กำลังสร้าง agent หรือ framework ประเด็นที่ต้องคิดคือ สถาปัตยกรรมแบบที่ agent ทุกตัวแชร์ Postgres เดียวกำลังหมดอายุ ลูกค้า enterprise จะเริ่มขอ data isolation ระดับ task ไม่ใช่แค่ระดับ tenant และสำหรับ SaaS ที่ขาย GovTech หรือ BankingTech ควรเพิ่ม BYOC และ database isolation เป็น default ตั้งแต่ตอนนี้ สิ่งที่เคยเป็น nice to have ปี 2024 กำลังจะเป็น table stakes สำหรับ RFP ปี 2027 ครับ
