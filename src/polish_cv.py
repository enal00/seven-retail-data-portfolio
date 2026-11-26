"""Final CV polish: fix PPROFESSIONAL typo at paragraph level, add portfolio link line in header."""
import docx
from pathlib import Path
from copy import deepcopy

ROOT = Path(__file__).resolve().parent.parent
CV = ROOT / "CV_M_Zainal_Salim_S.docx"
d = docx.Document(str(CV))

for p in d.paragraphs:
    # Fix the PROFESSIONAL EXPERIENCE heading regardless of split runs
    if "PROFESSIONAL EXPERIENCE" in p.text and "PROFESSIONAL EXPERIENCE" not in p.text.replace("PPROFESSIONAL", ""):
        pass
    if "PPROFESSIONAL" in p.text or ("ROFESSIONAL" in p.text and "PROFESSIONAL" not in p.text):
        # Rebuild the first line cleanly, keep the rest of the paragraph
        lines = p.text.split("\n")
        lines[0] = "PROFESSIONAL EXPERIENCE"
        # capture formatting of first run
        first_run = p.runs[0] if p.runs else None
        fmt = None
        if first_run is not None:
            fmt = (first_run.font.size, first_run.font.bold, first_run.font.name, first_run.font.color.rgb if first_run.font.color and first_run.font.color.type else None)
        for r in list(p.runs):
            r._element.getparent().remove(r._element)
        new_run = p.add_run("\n".join(lines))
        if fmt:
            new_run.font.size, new_run.font.bold, new_run.font.name = fmt[0], fmt[1], fmt[2]
            if fmt[3] is not None:
                new_run.font.color.rgb = fmt[3]

# Header: add explicit portfolio repo line after the github line
for p in d.paragraphs:
    if "Email:" in p.text and "github.com/enal00" in p.text and "seven-retail" not in p.text:
        r = p.add_run("\nData Portfolio Repo: https://github.com/enal00/seven-retail-data-portfolio")
        # copy size from an existing run if possible
        if p.runs:
            src = p.runs[0]
            r.font.size = src.font.size
            r.font.name = src.font.name

d.save(str(CV))
print("✅ polish done")
