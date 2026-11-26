"""
Seven Retail Analytics - PowerPoint Deck Generator
==================================================
Builds a professional 16:9 PPTX presentation embedding the generated
PNG charts from reports/charts/.

Usage:
    python src/make_pptx.py
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pathlib import Path

# ---------- Paths ----------
ROOT = Path(__file__).resolve().parent.parent
CHARTS = ROOT / "reports" / "charts"
OUT = ROOT / "reports" / "Seven_Retail_Analytics_Presentation.pptx"

# ---------- Palette ----------
NAVY = RGBColor(0x1B, 0x2A, 0x4A)
BLUE = RGBColor(0x2E, 0x86, 0xAB)
ORANGE = RGBColor(0xF1, 0x8F, 0x01)
RED = RGBColor(0xC7, 0x3E, 0x1D)
GREEN = RGBColor(0x4C, 0xAF, 0x50)
GREY = RGBColor(0x5A, 0x5A, 0x5A)
LIGHT = RGBColor(0xF4, 0xF6, 0xF9)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

SW, SH = 13.333, 7.5

def add_slide():
    return prs.slides.add_slide(BLANK)

def rect(slide, x, y, w, h, fill, line=None):
    from pptx.enum.shapes import MSO_SHAPE
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    if line:
        sh.line.color.rgb = line
    else:
        sh.line.fill.background()
    sh.shadow.inherit = False
    return sh

def textbox(slide, x, y, w, h, text, size=18, color=NAVY, bold=False, align=PP_ALIGN.LEFT, font="Calibri", anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.bold = bold
    r.font.name = font
    return tb

def bullets(slide, x, y, w, h, items, size=16, color=NAVY, gap=6):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        if isinstance(item, tuple):
            txt, lvl, bold = item
        else:
            txt, lvl, bold = item, 0, False
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.level = lvl
        p.space_after = Pt(gap)
        r = p.add_run()
        r.text = ("• " if lvl == 0 else "– ") + txt
        r.font.size = Pt(size if lvl == 0 else size - 2)
        r.font.color.rgb = color
        r.font.bold = bold
        r.font.name = "Calibri"
    return tb

def header(slide, title, subtitle=None):
    rect(slide, 0, 0, SW, 1.15, NAVY)
    rect(slide, 0, 1.15, SW, 0.06, ORANGE)
    textbox(slide, 0.6, 0.18, 12, 0.7, title, size=30, color=WHITE, bold=True)
    if subtitle:
        textbox(slide, 0.6, 0.72, 12, 0.4, subtitle, size=14, color=RGBColor(0xBB, 0xCC, 0xDD))

def footer(slide, n):
    textbox(slide, 0.6, 7.05, 8, 0.35, "Seven Retail — Multi-Store Data Analytics Portfolio", size=10, color=GREY)
    textbox(slide, 12.3, 7.05, 0.8, 0.35, str(n), size=10, color=GREY, align=PP_ALIGN.RIGHT)

def pic(slide, path, x, y, w=None, h=None):
    kw = {}
    if w: kw["width"] = Inches(w)
    if h: kw["height"] = Inches(h)
    return slide.shapes.add_picture(str(path), Inches(x), Inches(y), **kw)

def kpi_card(slide, x, y, w, h, value, label, accent=BLUE):
    rect(slide, x, y, w, h, LIGHT)
    rect(slide, x, y, 0.08, h, accent)
    textbox(slide, x + 0.25, y + 0.18, w - 0.4, 0.6, value, size=28, color=accent, bold=True)
    textbox(slide, x + 0.25, y + 0.85, w - 0.4, 0.4, label, size=13, color=GREY)

# =========================================================
# SLIDE 1 — TITLE
# =========================================================
s = add_slide()
rect(s, 0, 0, SW, SH, NAVY)
rect(s, 0, 4.9, SW, 0.08, ORANGE)
textbox(s, 1, 2.0, 11.3, 1.2, "Seven Retail", size=54, color=WHITE, bold=True)
textbox(s, 1, 3.1, 11.3, 0.9, "Multi-Store Data Analytics: From Raw Data to Executive Decisions", size=28, color=RGBColor(0xBB, 0xCC, 0xDD))
textbox(s, 1, 5.2, 11.3, 0.5, "End-to-End Data Analyst Portfolio  •  120,000 Transactions  •  Apache Superset Dashboard", size=16, color=ORANGE, bold=True)
textbox(s, 1, 6.3, 11.3, 0.4, "Prepared as a capability case study for the Data Analyst Associate (Group Service) role", size=13, color=RGBColor(0x99, 0xAA, 0xBB))

# =========================================================
# SLIDE 2 — BUSINESS CONTEXT & DATASET
# =========================================================
s = add_slide()
header(s, "Business Context & Dataset", "Why this analysis matters for a 200+ center retail group")
bullets(s, 0.6, 1.5, 6.2, 5.2, [
    ("Seven Retail operates 200+ centers across F&B, Education, Healthcare, Lifestyle", 0, True),
    ("Daily decisions needed: which categories to promote, which stores need intervention, which customers are at churn risk", 0, False),
    ("Dataset: Supermarket Large Dataset as a proxy for multi-store retail operations", 0, False),
    ("120,000 transactions × 325 columns (customer, product, store, payment, logistics)", 1, False),
    ("Two core business questions (from the JD):", 0, True),
    ("Q1: Which categories & segments drive the highest profit margins, and where are the operational bottlenecks (returns, complaints)?", 1, False),
    ("Q2: How do we track AOV, Gross Profit, and churn risk across stores to trigger corrective actions?", 1, False),
], size=15)
rect(s, 7.2, 1.6, 5.5, 5.0, LIGHT)
textbox(s, 7.5, 1.8, 5, 0.4, "Dataset Snapshot", size=18, color=NAVY, bold=True)
bullets(s, 7.5, 2.4, 5.0, 4.0, [
    "120,000 unique transactions",
    "325 engineered + raw columns",
    "Multiple store locations (store_id)",
    "Product categories: Grocery, Supplements, Bakery, Electronics-type taxonomy…",
    "Customer segments & churn risk scores",
    "Payment methods, returns, complaints flags",
], size=14)
footer(s, 2)

# =========================================================
# SLIDE 3 — PIPELINE
# =========================================================
s = add_slide()
header(s, "End-to-End Data Pipeline", "Clean → Analyze → Visualize → Decide")
steps = [
    ("1. EDA", "Automated profiling of 323 columns; nulls, dtypes, distributions (src/eda_analysis.py)", BLUE),
    ("2. CLEANING", "Median imputation, datetime typing, feature engineering: calculated_profit, margins (src/data_cleaning.py)", GREEN),
    ("3. WAREHOUSE", "Cleaned data loaded into a queryable relational layer (SQLite) behind Superset", ORANGE),
    ("4. DASHBOARD", "6 interactive charts in Apache Superset via REST API automation (src/superset_automation.py)", RED),
    ("5. DECISIONS", "Every claim traceable to a chart; actionable recommendations documented", NAVY),
]
x = 0.5
for title, desc, color in steps:
    rect(s, x, 2.2, 2.35, 3.4, LIGHT)
    rect(s, x, 2.2, 2.35, 0.6, color)
    textbox(s, x + 0.1, 2.3, 2.15, 0.45, title, size=16, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    textbox(s, x + 0.15, 3.0, 2.05, 2.4, desc, size=11.5, color=NAVY)
    x += 2.52
textbox(s, 0.6, 6.0, 12, 0.6, "Rule followed: data is always profiled and cleaned BEFORE it reaches the BI tool — no raw data in dashboards.", size=14, color=GREY)
footer(s, 3)

# =========================================================
# SLIDE 4 — EXECUTIVE KPI SUMMARY
# =========================================================
s = add_slide()
header(s, "Executive Summary — Key Numbers", "Audited directly from the cleaned dataset (120,000 transactions)")
kpi_card(s, 0.6, 1.6, 2.9, 1.5, "11.29M", "Total Revenue", BLUE)
kpi_card(s, 3.75, 1.6, 2.9, 1.5, "5.07M", "Total Profit", GREEN)
kpi_card(s, 6.9, 1.6, 2.9, 1.5, "44.9%", "Overall Profit Margin", ORANGE)
kpi_card(s, 10.05, 1.6, 2.7, 1.5, "94.09", "Avg Order Value (AOV)", RED)
bullets(s, 0.6, 3.5, 12.2, 3.2, [
    ("Top margin category: Supplements (51.87%), followed by First Aid (50.38%) and Batteries (48.50%)", 0, True),
    ("Top profit (nominal) category: Grocery — highest volume, thinner per-unit margin", 0, False),
    ("Operational bottleneck: Vegetables & Fruits lead returns (191 & 165) and complaints — cold-chain logistics issue", 0, False),
    ("Customer health: 2,721 customers (2.3%) flagged HIGH churn risk (>0.7 score)", 0, False),
    ("Payment mix dominated by Credit Card (30.2%) and Debit Card (25.1%) of revenue", 0, False),
], size=16)
footer(s, 4)

# =========================================================
# SLIDE 5 — PROFIT MARGIN CHART
# =========================================================
s = add_slide()
header(s, "Q1 — Profitability Drivers", "Which categories earn the most per unit of revenue?")
pic(s, CHARTS / "profit_margin_by_category.png", 0.5, 1.5, w=7.6)
bullets(s, 8.4, 1.7, 4.4, 5.0, [
    ("Supplements wins on margin (51.87%) despite lower volume", 0, True),
    ("High-volume categories (Grocery, Bakery) sit lower on margin", 0, False),
    ("Decision: shift shelf-space & cross-sell campaigns toward Supplements / First Aid / Batteries in top stores", 0, True),
], size=14)
footer(s, 5)

# =========================================================
# SLIDE 6 — PROFIT VALUE CHART
# =========================================================
s = add_slide()
header(s, "Q1 — Where the Money Actually Is", "Nominal profit vs margin — two different stories")
pic(s, CHARTS / "profit_by_category.png", 0.5, 1.5, w=7.6)
bullets(s, 8.4, 1.7, 4.4, 5.0, [
    ("Grocery delivers the highest absolute profit (volume play)", 0, True),
    ("Margin leaders (Supplements) are smaller in total — a growth opportunity, not the base", 0, False),
    ("Balanced portfolio: defend Grocery volume, grow high-margin niches", 0, True),
], size=14)
footer(s, 6)

# =========================================================
# SLIDE 7 — RETURNS / BOTTLENECK
# =========================================================
s = add_slide()
header(s, "Q1 — Operational Bottlenecks", "Returns & complaints concentrated in fresh produce")
pic(s, CHARTS / "returns_by_category.png", 0.5, 1.5, w=7.6)
bullets(s, 8.4, 1.7, 4.4, 5.0, [
    ("Vegetables (191) & Fruits (165) top the return list; overall return rate 3.06%", 0, True),
    ("Root cause hypothesis: cold-chain / shelf-life mismanagement at branch level", 0, False),
    ("Decision: cold-chain audit for top-10 branches with highest fresh-produce returns → target 15% waste reduction", 0, True),
], size=14)
footer(s, 7)

# =========================================================
# SLIDE 8 — REVENUE TREND
# =========================================================
s = add_slide()
header(s, "Q2 — Tracking Performance Over Time", "Monthly revenue & profit trend (Superset time-grain P1M)")
pic(s, CHARTS / "revenue_profit_trend.png", 0.7, 1.5, w=9.0)
bullets(s, 10.0, 1.8, 3.0, 4.5, [
    ("Stable monthly revenue with profit tracking at ~44.9% margin", 0, False),
    ("Drill-down enabled: daily → weekly → monthly → yearly", 0, False),
    ("Decision: automated weekly AOV alerts when a store drops below Q1", 0, True),
], size=13)
footer(s, 8)

# =========================================================
# SLIDE 9 — PAYMENT & CHURN
# =========================================================
s = add_slide()
header(s, "Q2 — Payment Mix & Customer Churn Risk", "Where revenue comes from, and who might leave")
pic(s, CHARTS / "payment_method_mix.png", 0.4, 1.5, h=4.6)
pic(s, CHARTS / "churn_risk_distribution.png", 6.9, 1.5, w=6.0)
bullets(s, 0.6, 6.25, 12.2, 0.9, [
    ("Credit Card + Debit Card = 55% of revenue → prioritize card payment UX & fraud monitoring", 0, False),
    ("2.3% of customers at HIGH churn risk → trigger automated CRM re-engagement vouchers before they leave", 0, True),
], size=13)
footer(s, 9)

# =========================================================
# SLIDE 10 — DECISIONS
# =========================================================
s = add_slide()
header(s, "Actionable Decisions", "Every recommendation is backed by a chart in the dashboard")
rows = [
    ("Finding", "Decision / Action", "Dashboard evidence"),
    ("Supplements & First Aid have the highest margins (51.9% / 50.4%)", "Reallocate shelf-space & run cross-sell campaigns in top-10 stores", "Chart 105 — Profit Margin by Category"),
    ("Vegetables/Fruits drive the most returns & complaints", "Cold-chain logistics audit in top-10 branches; target −15% waste", "Chart 108 — Returns & Complaints"),
    ("Store AOV disparity across 200+ locations", "Weekly automated AOV alerts to Area Managers below Q1", "Chart 106 — Top Stores by Revenue & AOV"),
    ("2,721 customers (2.3%) at high churn risk", "CRM re-engagement campaign with personalized vouchers", "Chart 107 — Segment LTV + churn flags"),
]
tbl_shape = s.shapes.add_table(len(rows), 3, Inches(0.5), Inches(1.5), Inches(12.3), Inches(4.8))
tbl = tbl_shape.table
tbl.columns[0].width = Inches(4.6)
tbl.columns[1].width = Inches(4.6)
tbl.columns[2].width = Inches(3.1)
for ri, row in enumerate(rows):
    for ci, val in enumerate(row):
        cell = tbl.cell(ri, ci)
        cell.text = val
        for p in cell.text_frame.paragraphs:
            for r in p.runs:
                r.font.size = Pt(13 if ri else 14)
                r.font.bold = (ri == 0)
                r.font.color.rgb = WHITE if ri == 0 else NAVY
        if ri == 0:
            cell.fill.solid()
            cell.fill.fore_color.rgb = NAVY
        else:
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT if ri % 2 else WHITE
footer(s, 10)

# =========================================================
# SLIDE 11 — TECH STACK
# =========================================================
s = add_slide()
header(s, "Tech Stack & Reproducibility", "Everything is scripted — run it, don't click it")
bullets(s, 0.6, 1.5, 6.2, 5.2, [
    ("Python / Pandas / NumPy — automated EDA, cleaning, feature engineering", 0, False),
    ("SQLite + SQL modeling — queryable analytical layer", 0, False),
    ("Apache Superset (Docker, localhost:8088) — 6-chart executive dashboard", 0, False),
    ("Superset REST API — charts & dashboard created programmatically (src/superset_automation.py)", 0, False),
    ("GitHub — full code + reports + charts versioned", 0, False),
], size=15)
rect(s, 7.2, 1.6, 5.5, 5.0, LIGHT)
textbox(s, 7.5, 1.8, 5, 0.4, "Reproduce in 3 commands", size=18, color=NAVY, bold=True)
bullets(s, 7.5, 2.4, 5.0, 4.0, [
    "python src/eda_analysis.py",
    "python src/data_cleaning.py",
    "python src/generate_charts.py",
    "→ Dashboard: http://localhost:8088 (dashboard: seven-retail-executive-dashboard)",
    "→ Repo: github.com/enal00/seven-retail-data-portfolio",
], size=14)
footer(s, 11)

# =========================================================
# SLIDE 12 — CLOSING
# =========================================================
s = add_slide()
rect(s, 0, 0, SW, SH, NAVY)
rect(s, 0, 3.4, SW, 0.08, ORANGE)
textbox(s, 1, 1.8, 11.3, 1.0, "Thank You", size=54, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
textbox(s, 1, 3.8, 11.3, 0.8, "Questions & Discussion", size=26, color=RGBColor(0xBB, 0xCC, 0xDD), align=PP_ALIGN.CENTER)
textbox(s, 1, 5.2, 11.3, 1.2, "Dashboard: http://localhost:8088/superset/dashboard/seven-retail-executive-dashboard/\nRepo: github.com/enal00/seven-retail-data-portfolio", size=15, color=ORANGE, align=PP_ALIGN.CENTER)

# ---------- Save ----------
OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(f"✅ Presentation saved: {OUT}")
print(f"   Slides: {len(prs.slides.__iter__.__self__._sldIdLst)}")
