"""
Restructures 'Design Research in the Age of AI.pptx':
  1. Reorders slides so all three observations come before the pivot
  2. Moves Roots of UX inside the knowledge-problem section
  3. Puts Field Notes adjacent to Human Framework
  4. Updates XX / 19 slide numbers throughout
"""

import re
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

PATH = "/Users/zac/Documents/Symbiosis/09 - Design in the Age of AI/presentation/Design Research in the Age of AI.pptx"
prs = Presentation(PATH)

# ── Verify current order before touching anything ───────────────────
print("BEFORE:")
for i, slide in enumerate(prs.slides):
    texts = [s.text_frame.text.strip() for s in slide.shapes
             if s.has_text_frame and s.text_frame.text.strip()]
    print(f"  {i:02d} → {texts[:2]}")

# ── Reorder ─────────────────────────────────────────────────────────
#
#  old index  content
#  ─────────  ──────────────────────────────────────────
#  0          Title
#  1          Her (2013)
#  2          Black Mirror Effect
#  3          Three Observations overview
#  4          01 Anthropomorphism — observation
#  5          PIVOT "None of this is new"          ← was too early
#  6          01 Research (ELIZA, CASA, Clippy)
#  7          02 Conversational UX — observation
#  8          02 Research (direct manip vs NL)
#  9          03 Design Tools — observation
#  10         Field Notes
#  11         03 Social Contracts — research
#  12         UX Knowledge Problem
#  13         UX Knowledge Lineage (chart)
#  14         Reconnect to Science
#  15         Roots of UX reference               ← move inside knowledge section
#  16         Human Framework
#  17         Closing
#  18         Final question
#  19         References
#
#  Target order (by old index):
#  ── HOOK ──────────────────────────────────────────
#  0   Title
#  1   Her
#  2   Black Mirror Effect
#  ── THREE OBSERVATIONS ────────────────────────────
#  3   Overview
#  4   01 Anthropomorphism — observation
#  7   02 Conversational UX — observation
#  9   03 Design Tools — observation
#  ── PIVOT ─────────────────────────────────────────
#  5   "None of this is new"
#  ── WHAT THE RESEARCH SAYS ────────────────────────
#  6   01 Research
#  8   02 Research
#  11  03 Social Contracts
#  ── THE KNOWLEDGE PROBLEM ─────────────────────────
#  12  UX Knowledge Problem
#  15  Roots of UX               ← moved here as evidence
#  13  UX Knowledge Lineage
#  ── WHAT WE NEED ──────────────────────────────────
#  14  Reconnect to Science
#  10  Field Notes               ← reunited with Human Framework
#  16  Human Framework
#  ── CLOSING ───────────────────────────────────────
#  17  Closing
#  18  Final question
#  19  References

NEW_ORDER = [0, 1, 2, 3, 4, 7, 9, 5, 6, 8, 11, 12, 15, 13, 14, 10, 16, 17, 18, 19]

xml_slides = prs.slides._sldIdLst
refs = list(xml_slides)
for ref in refs:
    xml_slides.remove(ref)
for old_idx in NEW_ORDER:
    xml_slides.append(refs[old_idx])

# ── Update XX / 19 slide numbers ────────────────────────────────────
number_pattern = re.compile(r'^\d{2} / 19$')
updated = 0
for new_pos, slide in enumerate(prs.slides):
    new_label = f'{new_pos + 1:02d} / 19'
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for para in shape.text_frame.paragraphs:
            for run in para.runs:
                if number_pattern.match(run.text.strip()):
                    old_label = run.text.strip()
                    run.text = new_label
                    if old_label != new_label:
                        updated += 1

print(f"\n{updated} slide-number labels updated")

# ── Verify new order ────────────────────────────────────────────────
print("\nAFTER:")
for i, slide in enumerate(prs.slides):
    texts = [s.text_frame.text.strip() for s in slide.shapes
             if s.has_text_frame and s.text_frame.text.strip()]
    print(f"  {i+1:02d} → {texts[:2]}")

# ── Save ─────────────────────────────────────────────────────────────
prs.save(PATH)
print(f"\nSaved: {PATH}")
