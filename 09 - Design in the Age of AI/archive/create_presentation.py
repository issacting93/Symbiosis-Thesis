from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os

BASE = "/Users/zac/Documents/Symbiosis/09 - Design in the Age of AI"
CHARTS = os.path.join(BASE, "presentation", "charts")
ARCHIVE = os.path.join(BASE, "archive")

# ── Colour palette (drawn from Roots of UX dark theme + chart bg) ──
BG_DARK   = RGBColor(0x14, 0x14, 0x13)
BG_CREAM  = RGBColor(0xfa, 0xf9, 0xf5)
TXT_MAIN  = RGBColor(0x14, 0x14, 0x13)
TXT_BODY  = RGBColor(0x40, 0x40, 0x3e)
TXT_DIM   = RGBColor(0x8d, 0x8d, 0x8a)
TXT_DIM2  = RGBColor(0x55, 0x55, 0x53)
TXT_LIGHT = RGBColor(0xf2, 0xf2, 0xf0)
TXT_MID   = RGBColor(0xb0, 0xaf, 0xaa)
RULE_D    = RGBColor(0x26, 0x26, 0x26)
RULE_L    = RGBColor(0xd0, 0xce, 0xc8)
C_PSY     = RGBColor(0xb7, 0xad, 0xff)   # purple
C_ENG     = RGBColor(0x7f, 0xd9, 0xc4)   # teal
C_DES     = RGBColor(0xe8, 0xbd, 0x78)   # gold
C_SOC     = RGBColor(0xf2, 0x9d, 0xba)   # pink
C_CMP     = RGBColor(0x8d, 0xba, 0xf6)   # blue
C_UI      = RGBColor(0xcf, 0xe0, 0x7e)   # yellow-green
CALLOUT   = RGBColor(0xf0, 0xef, 0xea)

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

# ── Helpers ──────────────────────────────────────────────────────────

def slide():
    return prs.slides.add_slide(BLANK)

def bg(s, color):
    f = s.background.fill
    f.solid()
    f.fore_color.rgb = color

def tb(s, text, l, t, w, h, size=12, bold=False, color=None,
       align=PP_ALIGN.LEFT, italic=False, wrap=True, font="Helvetica Neue"):
    box = s.shapes.add_textbox(l, t, w, h)
    tf  = box.text_frame
    tf.word_wrap = wrap
    p   = tf.paragraphs[0]
    p.alignment = align
    r   = p.add_run()
    r.text = text
    r.font.name = font
    r.font.size = Pt(size)
    r.font.bold   = bold
    r.font.italic = italic
    if color:
        r.font.color.rgb = color
    return box

def mtb(s, items, l, t, w, h, font="Helvetica Neue"):
    """Multi-paragraph textbox. items = [(text,size,bold,color,space_before), ...]"""
    box = s.shapes.add_textbox(l, t, w, h)
    tf  = box.text_frame
    tf.word_wrap = True
    first = True
    for text, size, bold, color, spb in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        if spb:
            p.space_before = Pt(spb)
        r = p.add_run()
        r.text = text
        r.font.name = font
        r.font.size = Pt(size)
        r.font.bold = bold
        if color:
            r.font.color.rgb = color

def hline(s, y, color=RULE_D, x0=None, x1=None):
    x0 = x0 or Inches(0.75)
    x1 = x1 or (prs.slide_width - Inches(0.75))
    ln = s.shapes.add_connector(1, x0, y, x1, y)
    ln.line.color.rgb = color
    ln.line.width = Pt(0.5)

def vline(s, x, y0, y1, color=RULE_L):
    ln = s.shapes.add_connector(1, x, y0, x, y1)
    ln.line.color.rgb = color
    ln.line.width = Pt(0.5)

def rect(s, l, t, w, h, fill=None):
    sh = s.shapes.add_shape(1, l, t, w, h)
    if fill:
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
    else:
        sh.fill.background()
    sh.line.fill.background()
    return sh

def img(s, name, l, t, w=None, h=None):
    path = os.path.join(CHARTS, name)
    if w and h:
        return s.shapes.add_picture(path, l, t, w, h)
    elif w:
        return s.shapes.add_picture(path, l, t, width=w)
    elif h:
        return s.shapes.add_picture(path, l, t, height=h)
    else:
        return s.shapes.add_picture(path, l, t)

def header_light(s, label, title, title_size=28):
    hline(s, Inches(1.2), RULE_L)
    tb(s, label, Inches(0.75), Inches(0.55), Inches(9), Inches(0.45),
       size=9, color=TXT_DIM2)
    tb(s, title, Inches(0.75), Inches(0.88), Inches(11.5), Inches(0.75),
       size=title_size, color=TXT_MAIN)

def header_dark(s, label, title, title_size=28):
    hline(s, Inches(1.2), RULE_D)
    tb(s, label, Inches(0.75), Inches(0.55), Inches(9), Inches(0.45),
       size=9, color=TXT_DIM)
    tb(s, title, Inches(0.75), Inches(0.88), Inches(11.5), Inches(1.5),
       size=title_size, color=TXT_LIGHT)

def footer_light(s, text, y=Inches(6.5)):
    hline(s, y, RULE_L)
    tb(s, text, Inches(0.75), y + Inches(0.18), Inches(11.5), Inches(0.4),
       size=9, color=TXT_DIM2)

def footer_dark(s, text, y=Inches(6.5)):
    hline(s, y, RULE_D)
    tb(s, text, Inches(0.75), y + Inches(0.18), Inches(11.5), Inches(0.4),
       size=10, color=C_DES)

def two_col(s, left_items, right_items, top=Inches(1.75), h=Inches(4.4)):
    mtb(s, left_items,  Inches(0.75), top, Inches(5.7), h)
    vline(s, Inches(6.9), top, top + h)
    mtb(s, right_items, Inches(7.2), top, Inches(5.7), h)

def callout(s, text, y=Inches(5.5)):
    rect(s, Inches(0.75), y, Inches(5.7), Inches(0.75), fill=CALLOUT)
    tb(s, text, Inches(0.9), y + Inches(0.1), Inches(5.4), Inches(0.6),
       size=11, color=TXT_MAIN)


# ════════════════════════════════════════════════════════════════════
# SLIDE 1 — Title
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_DARK)

hline(s, Inches(1.35), RULE_D)

tb(s, "Design Research\nin the Age of AI",
   Inches(0.75), Inches(1.55), Inches(10), Inches(3.5),
   size=60, bold=False, color=TXT_LIGHT)

hline(s, Inches(5.8), RULE_D)

tb(s, "2026",
   Inches(0.75), Inches(6.0), Inches(1.5), Inches(0.4),
   size=10, color=TXT_DIM)
tb(s, "Three observations  ·  Two problems  ·  One argument",
   Inches(2.5),  Inches(6.0), Inches(9.0), Inches(0.4),
   size=10, color=TXT_DIM)


# ════════════════════════════════════════════════════════════════════
# SLIDE 2 — Her (2013) / The Black Mirror Effect
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_CREAM)
header_light(s, "Opening", "Her  (2013)")

two_col(s,
    left_items=[
        ("Spike Jonze's film follows Theodore, who falls in love with an AI operating system. Looking from 2026, it predicted the present with uncanny accuracy — winning an Oscar and shaping imaginations across the industry.", 12, False, TXT_BODY, 0),
        ("", 6, False, None, 0),
        ("Scarlett Johansson voiced Samantha. Years later, Sam Altman approached her to voice a version of ChatGPT. She declined. The controversy made one thing clear: the people building AI had been shaped by the film.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("This wasn't coincidental. The film captured a very conscious, relational dimension of what AI could be — and engineers built toward it.", 12, False, TXT_MAIN, 0),
    ],
    right_items=[
        ("The Black Mirror Effect", 14, True, TXT_MAIN, 0),
        ("", 4, False, None, 0),
        ("Fiction articulates something, and technology builds toward it.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("We keep seeing this pattern: a story captures a feeling about the present, it resonates widely, and then engineers use it as a north star. The narrative precedes the technology.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("Design can play the same role. Observing, articulating, giving language to what hasn't been named yet.", 12, False, TXT_MAIN, 0),
    ]
)
footer_light(s, "Opening")


# ════════════════════════════════════════════════════════════════════
# SLIDE 3 — Three Observations (overview)
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_DARK)
header_dark(s, "Observations", "Three things we are\nobserving right now", title_size=36)

observations = [
    ("01", "The Rise of Anthropomorphism", C_PSY,
     "AI is being given physical presence, personality, and embodiment. Meta AI, Replika, Character AI. None of this is incidental — it's all designed."),
    ("02", "Conversation as UX Paradigm", C_CMP,
     "Conversational interfaces are now dominant. Responses are probabilistic. The metrics for success have changed."),
    ("03", "Design Tools & Collaboration", C_ENG,
     "AI is entering the research stage. Teams are fragmenting across tools. Different disciplines work in incompatible environments."),
]

for i, (num, title, color, desc) in enumerate(observations):
    x = Inches(0.75 + i * 4.15)
    y = Inches(2.7)
    w = Inches(3.9)
    tb(s, num,   x, y,                   w, Inches(0.45), size=11, color=color)
    tb(s, title, x, y + Inches(0.38), w, Inches(0.85), size=15, bold=True, color=TXT_LIGHT)
    hline(s, y + Inches(1.3), RULE_D, x0=x, x1=x + w - Inches(0.3))
    tb(s, desc,  x, y + Inches(1.42), w, Inches(1.9), size=11, color=TXT_MID)

footer_dark(s, "None of this is new — the research already exists")


# ════════════════════════════════════════════════════════════════════
# SLIDE 4 — Trend 1: Anthropomorphism
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_CREAM)
header_light(s, "01 — Anthropomorphism", "The Rise of Anthropomorphism")

two_col(s,
    left_items=[
        ("What we observe", 9, False, TXT_DIM2, 0),
        ("", 4, False, None, 0),
        ("Meta AI uses a soft, cute character — deliberately harmless-looking. Replika, Character AI, and others have built products around AI companionship. In China, the government moved to restrict companion AI outright.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("Rabbit R1, Microsoft Copilot — embodiment is a deliberate trust and connection mechanism, not a functional requirement.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("Why give AI a body? The short answer: it looks friendly, it looks trustworthy. Emotional design as a mechanism for engagement.", 12, False, TXT_MAIN, 0),
    ],
    right_items=[
        ("Research context", 9, False, TXT_DIM2, 0),
        ("", 4, False, None, 0),
        ("CASA — Computers Are Social Actors", 13, True, TXT_MAIN, 0),
        ("Reeves & Nass (1996)  ·  Nass & Moon (2000)", 10, False, TXT_DIM, 4),
        ("", 6, False, None, 0),
        ("People treat computers as social actors even with the simplest prompts — just pattern-matching and reflected language. This was formalised in the 1990s.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("ELIZA (Weizenbaum, 1976)", 13, True, TXT_MAIN, 0),
        ("A rule-based chatbot whose users formed genuine emotional responses. The tendency is deep and well-documented.", 11, False, TXT_BODY, 4),
        ("", 8, False, None, 0),
        ("Clippy: personality without capability erodes trust. It became a double-edged sword. Not every tool benefits from a personality.", 12, False, TXT_MAIN, 0),
    ]
)
callout(s, "Design question: why give AI a body? Embodiment is a trust mechanism — and it can mislead when capability doesn't match the emotional promise.")
footer_light(s, "Trend 01 of 03")


# ════════════════════════════════════════════════════════════════════
# SLIDE 5 — Trend 2: Conversational UX
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_CREAM)
header_light(s, "02 — Conversational UX", "Conversation as the Dominant UX Paradigm")

two_col(s,
    left_items=[
        ("What we observe", 9, False, TXT_DIM2, 0),
        ("", 4, False, None, 0),
        ("Products now embed their entire user flow inside a conversational interface — government websites, customer support, utilities. The UX is no longer deterministic.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("Responses are probabilistic rather than fixed. We can no longer track success through click-through rates and defined completion flows. The metrics have changed. The design process has changed.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("When responses are probabilistic and require engineering to shape, design decisions become engineering decisions.", 12, False, TXT_MAIN, 0),
    ],
    right_items=[
        ("An old debate, newly relevant", 9, False, TXT_DIM2, 0),
        ("", 4, False, None, 0),
        ("Direct Manipulation vs. Natural Language", 13, True, TXT_MAIN, 0),
        ("Jönsson et al. (2005)  ·  DirectGPT, CHI 2024", 10, False, TXT_DIM, 4),
        ("", 6, False, None, 0),
        ("Research consistently shows users prefer direct manipulation when they can use it effectively: faster, greater sense of control. Natural language is reached for when objects are hard to describe precisely.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("This debate played out between key figures in HCI in the 1990s. It is relevant again. Designers should know the lineage.", 12, False, TXT_MAIN, 0),
    ]
)
callout(s, "Better solution: give users a structured menu of intentions — let people select what they want, rather than expecting inference from open-ended input.")
footer_light(s, "Trend 02 of 03")


# ════════════════════════════════════════════════════════════════════
# SLIDE 6 — Trend 3: Design Tools & Collaboration
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_CREAM)
header_light(s, "03 — Design Tools & Collaboration", "How Design Work and Collaboration Are Changing")

two_col(s,
    left_items=[
        ("What we observe", 9, False, TXT_DIM2, 0),
        ("", 4, False, None, 0),
        ("Companies are using AI at the research stage to reduce time in studies and synthesis. PM briefs — AI-generated — feed into Figma, Make, or Lovable to produce initial flows.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("Different disciplines now work across incompatible tools. Designers are expected to work in code environments not native to design practice. Researchers transcribe and synthesise at a scale not possible before.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("This has fundamentally changed how teams collaborate — with implications for rigour.", 12, False, TXT_MAIN, 0),
    ],
    right_items=[
        ("Social contracts around AI", 9, False, TXT_DIM2, 0),
        ("", 4, False, None, 0),
        ("Society-in-the-Loop  (Rahwan, 2018)", 13, True, TXT_MAIN, 0),
        ("AI Professional Identity  (Ahuja et al., 2026)", 11, False, TXT_DIM, 4),
        ("", 6, False, None, 0),
        ("A writer may be pressured by a manager to use AI while being judged by peers for doing so. For engineers, using AI to write code is socially expected. These contracts vary enormously by discipline.", 12, False, TXT_BODY, 0),
        ("", 8, False, None, 0),
        ("Workers simultaneously fear being seen as cheaters for using AI and as incompetent for not using it — and those pressures fall unevenly across roles.", 12, False, TXT_MAIN, 0),
    ]
)
callout(s, "Abbott (1988): AI is redrawing lines of professional jurisdiction. The social norms haven't caught up with the technical change.")
footer_light(s, "Trend 03 of 03")


# ════════════════════════════════════════════════════════════════════
# SLIDE 7 — The UX Knowledge Problem
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_DARK)
header_dark(s, "The UX Knowledge Problem", "Why does it feel like\nwe're starting from scratch?", title_size=34)

two_col(s,
    left_items=[
        ("UX as an industry is at most 20 years old. It spent a long time as a subset of HCI.", 12, False, TXT_MID, 0),
        ("", 8, False, None, 0),
        ("HCI accumulated psychology, social sciences, engineering, and computer science — a group of people from those disciplines who brought their rigour to construct a new field.", 12, False, TXT_MID, 0),
        ("", 8, False, None, 0),
        ("When UX emerged, bootcamps taught the methods — but not the discipline and rigour needed to create new knowledge, share it, or retain it within the community.", 12, False, TXT_LIGHT, 0),
        ("", 8, False, None, 0),
        ("We adopted the knowledge without acquiring the skills to generate new knowledge.", 12, False, TXT_LIGHT, 0),
    ],
    right_items=[
        ("What we need to reconnect with", 9, False, TXT_DIM, 0),
        ("", 4, False, None, 0),
        ("Shneiderman (2022) — Human-Centered AI", 13, True, TXT_LIGHT, 0),
        ("A vocabulary for arguing against maximum automation — and for placing humans in the loop.", 11, False, TXT_MID, 4),
        ("", 8, False, None, 0),
        ("Gabriel (2020) — Value Alignment", 13, True, TXT_LIGHT, 0),
        ("Value alignment is not an engineering problem. It is a normative one — requiring exactly the stakeholder deliberation that design research is built to support.", 11, False, TXT_MID, 4),
        ("", 8, False, None, 0),
        ("The problem: we don't yet have the language to discuss ideas with these fields.", 12, False, C_DES, 0),
    ],
    top=Inches(2.5), h=Inches(3.9)
)
footer_dark(s, "The answer is not more AI — it is going back to the scientific community")


# ════════════════════════════════════════════════════════════════════
# SLIDE 8 — Concept Map (full image)
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_CREAM)
hline(s, Inches(0.85), RULE_L)
tb(s, "Concept Map — Design in the Age of AI",
   Inches(0.75), Inches(0.22), Inches(10), Inches(0.5), size=9, color=TXT_DIM2)
img(s, "chart2_concept_map.png", Inches(1.8), Inches(0.95), h=Inches(6.35))
hline(s, Inches(7.4), RULE_L)


# ════════════════════════════════════════════════════════════════════
# SLIDE 9 — UX Knowledge Lineage (full image)
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_CREAM)
hline(s, Inches(0.85), RULE_L)
tb(s, "The UX Knowledge Lineage — how UX inherited HCI methods without its research rigour",
   Inches(0.75), Inches(0.22), Inches(11), Inches(0.5), size=9, color=TXT_DIM2)
img(s, "chart3_ux_lineage.png", Inches(0.4), Inches(0.95), w=Inches(12.5))
hline(s, Inches(7.4), RULE_L)


# ════════════════════════════════════════════════════════════════════
# SLIDE 10 — Designer–User Ecosystem (full image)
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_CREAM)
hline(s, Inches(0.85), RULE_L)
tb(s, "The Designer–User Ecosystem — how AI reshapes roles and relationships within design practice",
   Inches(0.75), Inches(0.22), Inches(11), Inches(0.5), size=9, color=TXT_DIM2)
img(s, "chart4_ecosystem.png", Inches(3.5), Inches(0.9), h=Inches(6.2))
hline(s, Inches(7.4), RULE_L)


# ════════════════════════════════════════════════════════════════════
# SLIDE 11 — The Human Framework (full image)
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_CREAM)
hline(s, Inches(0.85), RULE_L)
tb(s, "The Human Framework — five questions design must hold simultaneously  ·  from fieldwork sketch",
   Inches(0.75), Inches(0.22), Inches(11), Inches(0.5), size=9, color=TXT_DIM2)
img(s, "chart1_human_framework.png", Inches(0.4), Inches(0.95), w=Inches(12.5))
hline(s, Inches(7.4), RULE_L)


# ════════════════════════════════════════════════════════════════════
# SLIDE 12 — Roots of UX
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_DARK)
header_dark(s, "Reference", "Roots of UX\n1911 → 2023", title_size=44)

tb(s, "An interactive swimlane timeline of the seven disciplines that shaped UX — Psychology, Human factors, Design, Social science, Computing, Interfaces, UX practice.",
   Inches(0.75), Inches(2.9), Inches(5.9), Inches(1.0), size=12, color=TXT_MID)

tb(s, "Open Roots of UX (2).html in a browser to explore the full interactive graph.",
   Inches(0.75), Inches(4.1), Inches(5.9), Inches(0.6), size=11, color=C_DES)

# Threads panel
tb(s, "THREADS", Inches(7.2), Inches(1.55), Inches(5.5), Inches(0.45), size=9, color=TXT_DIM)

threads = [
    ("Affordance",    "1966 → 2004", C_PSY),
    ("Design systems","1919 → 2013", C_DES),
    ("Social turn",   "1930 → 2017", C_SOC),
    ("Behaviorism",   "1938 → 2017", C_PSY),
    ("UI ↔ UX",      "1981 → 2016", C_CMP),
    ("Human factors", "1911 → 1990", C_ENG),
]
for i, (name, dates, color) in enumerate(threads):
    y = Inches(2.05 + i * 0.72)
    hline(s, y, RULE_D, x0=Inches(7.2), x1=Inches(12.6))
    tb(s, name,  Inches(7.2),  y + Inches(0.08), Inches(3.2), Inches(0.55), size=13, bold=True, color=TXT_LIGHT)
    tb(s, dates, Inches(10.5), y + Inches(0.08), Inches(2.1), Inches(0.55), size=11, color=TXT_DIM, align=PP_ALIGN.RIGHT)

# Lane colours
lanes = [
    ("Psychology", C_PSY), ("Human factors", C_ENG), ("Design", C_DES),
    ("Social science", C_SOC), ("Computing", C_CMP), ("Interfaces", C_UI), ("UX practice", TXT_LIGHT),
]
hline(s, Inches(5.75), RULE_D)
tb(s, "LANES", Inches(0.75), Inches(5.9), Inches(2), Inches(0.4), size=9, color=TXT_DIM)
for i, (name, color) in enumerate(lanes):
    x = Inches(0.75 + (i % 4) * 3.0)
    y = Inches(6.35 + (i // 4) * 0.5)
    tb(s, "● " + name, x, y, Inches(2.8), Inches(0.45), size=10, color=color)

footer_dark(s, "Roots of UX (2).html — interactive visualisation, open in browser")


# ════════════════════════════════════════════════════════════════════
# SLIDE 13 — Closing: Craft a Vision
# ════════════════════════════════════════════════════════════════════
s = slide()
bg(s, BG_DARK)
header_dark(s, "Closing", "Craft a Vision", title_size=52)

tb(s,
   "Spike Jonze observed something personal enough that it became universal — and translated it into something intentional. That resonance reached engineers and captured their imaginations. What Her is doing isn't predicting the future. It's articulating how we feel in the present — giving language to something nobody has named yet.",
   Inches(0.75), Inches(2.1), Inches(6.0), Inches(1.8),
   size=12, color=TXT_MID)

tb(s,
   "Design describes the same process: observing, generating insights, inspiring, visualising, building, observing again.",
   Inches(0.75), Inches(4.05), Inches(6.0), Inches(0.9),
   size=13, color=TXT_LIGHT)

# Design cycle
cycle = [
    ("Observe",    C_PSY),
    ("Insights",   C_ENG),
    ("Inspire",    C_DES),
    ("Visualise",  C_SOC),
    ("Build",      C_CMP),
    ("Observe →",  C_UI),
]
tb(s, "THE DESIGN CYCLE", Inches(7.5), Inches(1.9), Inches(5), Inches(0.45), size=9, color=TXT_DIM)
for i, (step, color) in enumerate(cycle):
    y = Inches(2.45 + i * 0.65)
    dot = s.shapes.add_shape(9, Inches(7.5), y + Inches(0.1), Inches(0.11), Inches(0.11))
    dot.fill.solid(); dot.fill.fore_color.rgb = color; dot.line.fill.background()
    tb(s, step, Inches(7.72), y, Inches(4.5), Inches(0.55), size=14, color=TXT_LIGHT)
    if i < len(cycle) - 1:
        ln = s.shapes.add_connector(1, Inches(7.555), y + Inches(0.21), Inches(7.555), y + Inches(0.65))
        ln.line.color.rgb = RULE_D; ln.line.width = Pt(0.5)

hline(s, Inches(6.35), RULE_D)
tb(s, "We know we're going to keep building. We need to craft a vision first.",
   Inches(0.75), Inches(6.5), Inches(8), Inches(0.65),
   size=13, bold=True, color=C_DES)
tb(s, "What kind of future do we want to see?",
   Inches(9.0), Inches(6.5), Inches(4.0), Inches(0.65),
   size=13, color=TXT_DIM, align=PP_ALIGN.RIGHT)


# ════════════════════════════════════════════════════════════════════
# Save
# ════════════════════════════════════════════════════════════════════
out = os.path.join(ARCHIVE, "Design in the Age of AI.pptx")
prs.save(out)
print(f"Saved: {out}")
