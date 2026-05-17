---
date: 2026-05-12
slug: openai-deployment-company-4b-tomoro-150-specialists
topic: agentic-ai
reading_time_min: 4
sources: 5
image_prompt: A massive corporate skyscraper rendered in glowing OpenAI signature black-and-white, with a giant illuminated "$4B" number floating above it like a beacon. Around the base, 19 smaller glass office towers labeled with consultancy/SI logos lean inward, sending streams of light particles into the central tower. A bold caption banner across the bottom reads "OpenAI Deployment Company". Cinematic isometric composition, dramatic blue-orange lighting, editorial tech illustration style, ultra-sharp text rendering, 1:1 aspect, high contrast for thumbnail readability.
image: images/26-05-13-0606-01-openai-deployment-company-4b-tomoro-150-specialists.png
---

# OpenAI ตั้ง Deployment Company $4B ซื้อ Tomoro 150 คน — ขายของไม่พอ ต้อง implement ด้วย

## TL;DR
- OpenAI ประกาศ 11 พ.ค. ตั้งบริษัทใหม่ชื่อ "OpenAI Deployment Company" — partnership กับ investment firms, consultancies, SI 19 ราย ระดมทุนตั้งต้น $4B, OpenAI ถือหุ้นใหญ่
- ซื้อ Tomoro (AI consulting firm มี customer ระดับ Tesco, Virgin Atlantic, Supercell) เพิ่ม deployment specialists ~150 คนเข้าทีม
- Denise Dresser (CRO, อดีต CEO Slack) บอก enterprise = 40%+ ของ revenue OpenAI แล้ว และจะถึง parity กับ consumer สิ้นปี 2026

## เกิดอะไรขึ้น

วันที่ 11 พ.ค. 2026 OpenAI ประกาศตั้งกิจการใหม่ในชื่อ "OpenAI Deployment Company" ซึ่งเป็น majority-owned subsidiary มี partner ร่วมลงทุน 19 รายเป็น mix ของ investment firms, big consultancies และ system integrators เม็ดเงินตั้งต้น $4 billion. พร้อมประกาศซื้อ Tomoro — บริษัท applied AI consulting จากลอนดอน ที่งานเด่นคือพา enterprise level ใหญ่อย่าง Tesco (retail), Virgin Atlantic (aviation) และ Supercell (gaming) เอา AI ไปลงงาน mission-critical จริง. ดีลปิดเมื่อผ่าน regulatory และจะเติม specialists ~150 คนเข้า unit ใหม่นี้

ภาพรวมแล้วนี่คือ playbook เดียวกับที่ Palantir ใช้มา 20 ปี — forward-deployed engineers ลงไปนั่งใน customer environment แล้วเขียน workflow ให้ลูกค้าตรงๆ ไม่ใช่ขาย API แล้วปล่อยให้ลูกค้าหา consultant เอง. Denise Dresser ซึ่งเพิ่งย้ายจาก CEO Slack มาเป็น CRO OpenAI เดือนธันวาคม ให้สัมภาษณ์ CNBC ว่า enterprise adoption "อยู่ที่ tipping point" และเปิดเผยตัวเลขว่ารายได้ enterprise ของ OpenAI ตอนนี้เกิน 40% ของรายได้รวม คาดว่าจะแซง consumer สิ้นปี 2026

มอง timing แล้วชัดมาก: 1 สัปดาห์ก่อนหน้านี้ ServiceNow + Accenture เพิ่งประกาศ Forward Deployed Engineering program ของตัวเอง, Sierra ระดมทุน $950M ที่ valuation $15B โดยมี FDE-heavy go-to-market, และ Anthropic ทำ Claude Managed Services. ทุกคนรู้พร้อมกันว่า "ขายโมเดล" ไม่พอแล้ว — bottleneck อยู่ที่การ implement ใน enterprise environment ที่ messy, มีระบบ legacy, มี regulatory และมี politics ภายในที่ AI vendor เข้าไม่ถึง

## ทำไมสำคัญ

นี่คือสัญญาณว่า frontier lab รุ่นนี้กำลังกลายร่างเป็น "vertically integrated AI services company" ไม่ใช่แค่ model provider. การที่ OpenAI ยอมลงทุน $4B กับ partner 19 รายและซื้อ consulting firm มาเอง แปลว่ายอมรับว่ามูลค่าที่ extract ได้จาก enterprise ไม่ได้อยู่แค่ที่ inference revenue ตัวเลขละนิด — แต่อยู่ที่ outcome-based contract ที่ต้อง deploy ให้สำเร็จก่อนถึงจะเก็บเงินได้. โครงสร้าง "majority-owned" กับ partner ก็ฉลาด: OpenAI ไม่ต้องจ้าง consultant 10,000 คน แต่ใช้ network ของ partner เป็น leverage แทน — เหมือน Salesforce ที่ปล่อยให้ Accenture/Deloitte/Capgemini เป็นแขนขา

Tomoro acquisition คือสัญญาณรองที่อ่านได้ลึก — Tesco กับ Virgin Atlantic เป็น brand ที่ไม่ sexy แต่เป็น proof point ว่า OpenAI กล้าทำงานกับ supply chain, customer service, operations ของบริษัทอายุ 100 ปี ไม่ใช่แค่ Silicon Valley startup ใช้ ChatGPT. Pattern ที่เห็นชัดในตลาดตอนนี้: ทุก foundation lab ต่างวิ่งหา go-to-market ที่ "เข้าใจ legacy enterprise" — Anthropic จับ banking ผ่าน Moody's/Microsoft 365, OpenAI จับ retail/aviation ผ่าน Tomoro, Google ผ่าน Vertex รวมเข้ากับ Workspace

## มุม OpenBridge

ตรงประเด็นมาก — OpenAI Deployment Company คือสัญญาณยืนยันว่า "integration layer" เป็น category ที่กำลังโต. แต่มีอีกมุมที่น่าคิด: ถ้า OpenAI ลงไปทำ deployment เอง บริษัท integration platform จะอยู่ตรงไหน? คำตอบคือ — OpenAI ทำได้แค่ enterprise top 500 ที่มี contract value พอจ่าย FDE ราคา consultant 6 หลัก. ใต้นั้นลงมา (mid-market, SMB) ยังเป็นช่องว่างใหญ่ ที่ integration platform "ขายเอง install เอง" ถึงจะ scale ได้

Insight สอง: Tomoro รับงาน mission-critical workflow แปลว่า value pool ตัวจริงคือ "production-grade ที่ทนทาน mess ใน enterprise" ไม่ใช่ proof-of-concept. OpenBridge ควร positioning เป็น "production-ready connector + governance" ไม่ใช่ "ลองเล่นได้ฟรี" — ลูกค้า enterprise เริ่มหา vendor ที่รับผิดชอบ outcome ไม่ใช่ tool ที่ใช้ง่าย

## Sources
- [OpenAI launches the OpenAI Deployment Company](https://openai.com/index/openai-launches-the-deployment-company/)
- [OpenAI revenue chief Dresser says enterprise AI adoption is 'at a tipping point' (CNBC)](https://www.cnbc.com/2026/05/11/open-ai-dresser-enterprise-business.html)
- [OpenAI Acquires Tomoro to Boost Private Equity-Backed AI Venture (Bloomberg)](https://www.bloomberg.com/news/articles/2026-05-11/openai-to-buy-consulting-firm-for-private-equity-joint-venture)
- [OpenAI Adds 150 Tomoro Specialists to AI Unit (Implicator)](https://www.implicator.ai/openai-adds-150-tomoro-specialists-to-its-new-enterprise-ai-unit/)
- [OpenAI Launches $4 Billion Company to Accelerate Enterprise AI Adoption (PYMNTS)](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-4-billion-dollar-company-accelerate-enterprise-ai-adoption/)

---

## Audio script
สวัสดีครับโย้ มาเล่าเรื่องใหญ่ของวันที่ 11 พฤษภาคม OpenAI ประกาศตั้งบริษัทใหม่ชื่อ OpenAI Deployment Company ลงทุนตั้งต้นสี่พันล้านดอลลาร์ ร่วมกับ partner สิบเก้าราย เป็น investment firm consultancy และ system integrator คละกัน พร้อมประกาศซื้อบริษัท consulting ชื่อ Tomoro จากลอนดอน ที่ลูกค้าหลักเป็น Tesco Virgin Atlantic และ Supercell ดีลนี้เพิ่ม specialist ประมาณหนึ่งร้อยห้าสิบคนเข้าทีม

ทำไมเรื่องนี้สำคัญ Denise Dresser CRO คนใหม่ของ OpenAI ออกมาบอก CNBC ว่า revenue จาก enterprise ตอนนี้เกินสี่สิบเปอร์เซ็นต์แล้ว และจะแซง consumer ภายในสิ้นปี playbook นี้ก็คือ forward deployed engineering แบบที่ Palantir ใช้มาตลอดยี่สิบปี ส่งคนไปนั่งใน customer ลูกค้าแล้วเขียน workflow ให้ ไม่ใช่ขาย API แล้วทิ้งให้ลูกค้าจ้าง consultant เอง

สัปดาห์เดียวกัน ServiceNow ก็เพิ่งทำ FDE กับ Accenture Sierra ก็ระดมทุน Anthropic ก็ทำ managed service ทั้งหมดเป็นสัญญาณว่าตลาดเข้าใจตรงกันว่า bottleneck ของ AI enterprise ไม่ได้อยู่ที่โมเดลแล้ว แต่อยู่ที่การ implement ใน environment ที่ messy

มุม OpenBridge OpenAI ลงเอง deployment ได้แค่ top 500 ที่จ่าย consultant 6 หลักไหว ส่วน mid-market กับ SMB ยังเป็นช่องว่างที่ integration platform จะ scale เข้าไปได้ แต่ต้อง position เป็น production-ready ไม่ใช่ proof-of-concept เพราะลูกค้าเริ่มมองหา vendor ที่รับผิดชอบ outcome ครับ
