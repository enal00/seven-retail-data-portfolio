"""
Clean CV update script v2 — robust ordering.
- Fix typos ROFESSIONAL / SELECTED DATA ANALYTICS  PROJECT
- Add Apache Superset to Technical Skills
- Replace Project 3 (E-Commerce) with Seven Retail Multi-Store Analytics Portfolio
- Add repo links to projects 1 & 2, clarify header GitHub link

Usage:
    python src/update_cv.py
"""

import docx
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CV = ROOT / "CV_M_Zainal_Salim_S.docx"

d = docx.Document(str(CV))

# ---------- 1. Fix typos ----------
for p in d.paragraphs:
    if "ROFESSIONAL" in p.text:
        for r in p.runs:
            if "ROFESSIONAL" in r.text:
                r.text = r.text.replace("ROFESSIONAL", "PROFESSIONAL")
    if "PPROFESSIONAL" in p.text:
        for r in p.runs:
            if "PPROFESSIONAL" in r.text:
                r.text = r.text.replace("PPROFESSIONAL", "PROFESSIONAL")
    if "SELECTED DATA ANALYTICS  PROJECT" in p.text:
        for r in p.runs:
            r.text = r.text.replace("SELECTED DATA ANALYTICS  PROJECT", "SELECTED DATA ANALYTICS PROJECT")

# ---------- 2. Add Apache Superset to Technical Skills ----------
for p in d.paragraphs:
    if "Dashboard & Data Visualization" in p.text and "Superset" not in p.text:
        for r in p.runs:
            if "Power BI" in r.text:
                r.text = r.text.replace("Power BI, Tableau, Looker Studio", "Power BI, Apache Superset, Tableau, Looker Studio")
        if "Superset" not in p.text:
            p.add_run(" | Apache Superset (Docker, REST API)")

# ---------- 3. Replace Project 3 ----------
start_idx = end_idx = None
for i, p in enumerate(d.paragraphs):
    if "E-Commerce Customer Behavior" in p.text:
        start_idx = i
    if start_idx is not None and "TECHNICAL SKILLS" in p.text:
        end_idx = i
        break

assert start_idx is not None and end_idx is not None, f"range not found {start_idx},{end_idx}"
print(f"Project 3 range: {start_idx}..{end_idx}")

ref_p = d.paragraphs[end_idx]  # TECHNICAL SKILLS paragraph — insert before it

new_items = [
    ("Seven Retail Multi-Store Analytics Portfolio", "Normal"),
    ("Tools: Python (Pandas, NumPy), SQL / SQLite, Apache Superset, REST API Automation, GitHub", "Normal"),
    ("Business Case: Support decision-making for a 200+ center retail group (F&B, Education, Healthcare, Lifestyle) — identify top-margin categories, operational bottlenecks (returns, complaints), and track AOV, gross profit, and churn risk across all store locations.", "Normal"),
    ("Key Contributions", "Normal"),
    ("Built an end-to-end pipeline on 120,000 transactions x 325 columns: automated EDA, data cleaning with dtype enforcement, and feature engineering (calculated_profit, profit margin %).", "List Paragraph"),
    ("Loaded cleaned data into a queryable relational layer (SQLite) and built a 6-chart executive dashboard in Apache Superset, created programmatically via the Superset REST API.", "List Paragraph"),
    ("Computed aggregated profit margin per category (SUM profit / SUM revenue) — Supplements (51.87%), First Aid (50.38%), Batteries (48.50%) are the true margin leaders.", "List Paragraph"),
    ("Identified operational bottlenecks: Vegetables & Fruits lead returns (191 & 165) and complaints (overall return rate 3.06%) — cold-chain logistics issue at branch level.", "List Paragraph"),
    ("Tracked customer health: 2,721 customers (2.3%) flagged HIGH churn risk (>0.7), with segment LTV ranking across locations.", "List Paragraph"),
    ("Verified every chart via /api/v1/chart/data; all claims in reports traceable to a dashboard chart.", "List Paragraph"),
    ("Business Impact", "Normal"),
    ("Actionable decisions: reallocate shelf-space toward high-margin categories, cold-chain audit for top-10 branches (-15% waste target), weekly AOV alerts for stores below Q1, CRM re-engagement for high-churn customers.", "List Paragraph"),
    ("Delivered a reproducible package: GitHub repo with scripts + 6 PNG charts + Markdown reports; live dashboard at Apache Superset (localhost:8088, slug: seven-retail-executive-dashboard).", "List Paragraph"),
    ("Project Repository: https://github.com/enal00/seven-retail-data-portfolio", "Normal"),
]

# Insert in FORWARD order — each insert lands directly before ref_p,
# so later inserts push earlier ones up. Forward iteration gives correct order.
for text, style in new_items:
    ref_p.insert_paragraph_before(text, style=style)

# Remove old project 3 paragraphs (elements still in doc between start and end)
for _ in range(start_idx, end_idx):
    p = d.paragraphs[start_idx]
    p._element.getparent().remove(p._element)

# ---------- 4. Repo links for projects 1 & 2 + header ----------
seen_supply = seen_furniture = False
for p in list(d.paragraphs):
    if "Supply Chain & Sales Performance Analytics" in p.text and not seen_supply:
        p.insert_paragraph_before("Project Repository: https://github.com/enal00/", style="Normal")
        seen_supply = True
    if "Furniture Sales Performance Analytics" in p.text and not seen_furniture:
        p.insert_paragraph_before("Project Repository: https://github.com/enal00/", style="Normal")
        seen_furniture = True

# Header: clarify the GitHub line
for p in d.paragraphs:
    if "Email:" in p.text and "github.com/enal00" in p.text:
        for r in p.runs:
            if "github.com/enal00" in r.text and "Portfolios" not in r.text:
                r.text = "GitHub (Data Portfolio): https://github.com/enal00/seven-retail-data-portfolio | Profile: https://github.com/enal00/"

d.save(str(CV))
print("✅ CV updated cleanly (v2)")
