#!/usr/bin/env python3
"""
charts.py — Design in the Age of AI
Four concept maps and diagrams for the presentation.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Palette ────────────────────────────────────────────────────────────────────

C = {
    'bg':       '#F7F6F2',
    'ink':      '#1C1C1E',
    'muted':    '#8E8E93',
    'rule':     '#C8C8C4',

    'blue':     '#1D6EAC',
    'blue_lt':  '#C3DCF5',

    'red':      '#B83532',
    'red_lt':   '#FAD5D4',

    'grn':      '#1E6B42',
    'grn_lt':   '#C1EDD6',

    'pur':      '#5B3E9E',
    'pur_lt':   '#DDD1F8',

    'ctr_lt':   '#E8E7E3',
}

plt.rcParams.update({
    'font.family':      'sans-serif',
    'font.sans-serif':  ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'figure.facecolor': C['bg'],
    'axes.facecolor':   C['bg'],
    'text.color':       C['ink'],
})

OUT = '/Users/zac/Documents/Symbiosis/09 - Design in the Age of AI/presentation/charts/'

# ── Helpers ────────────────────────────────────────────────────────────────────

def circle(ax, x, y, r, face, edge, lbl, fsize=9, lw=1.8, zbase=2):
    c = plt.Circle((x, y), r, facecolor=face, edgecolor=edge, linewidth=lw, zorder=zbase)
    ax.add_patch(c)
    ax.text(x, y, lbl, ha='center', va='center', fontsize=fsize,
            color=edge, fontweight='bold', zorder=zbase + 1,
            multialignment='center', linespacing=1.35)


def arrow(ax, x0, y0, x1, y1, color=None, dashed=False, lw=1.4, rad=0.0):
    color = color or C['rule']
    ls = '--' if dashed else '-'
    ax.annotate(
        '', xy=(x1, y1), xytext=(x0, y0),
        arrowprops=dict(
            arrowstyle='->', color=color, lw=lw,
            mutation_scale=14, linestyle=ls,
            connectionstyle=f'arc3,rad={rad}',
        ),
        zorder=1,
    )


def title_block(ax, main, sub=None):
    ax.text(0.01, 0.99, main, transform=ax.transAxes,
            fontsize=13, fontweight='bold', va='top', color=C['ink'])
    if sub:
        ax.text(0.01, 0.92, sub, transform=ax.transAxes,
                fontsize=8.5, va='top', color=C['muted'])


# ── Chart 1: The Human Framework ───────────────────────────────────────────────

def chart1_human_framework():
    fig, ax = plt.subplots(figsize=(15, 4.8), facecolor=C['bg'])
    ax.set_facecolor(C['bg'])
    ax.axis('off')
    ax.set_xlim(-0.2, 10.2)
    ax.set_ylim(-2.2, 3.8)

    questions = [
        ('What do we\nvalue?',        1.0, C['blue'],  C['blue_lt'],  'Companionship\nSafety · Agency'),
        ('How do we\nfeel?',          3.0, C['red'],   C['red_lt'],   'Alone\nAnxious · Curious'),
        ('How do we\nact?',           5.0, C['grn'],   C['grn_lt'],   'Seek connection\nComplain · Improve'),
        ('What enables\nus to act?',  7.0, C['pur'],   C['pur_lt'],   'Tools · Language\nCommunity'),
        ('Who do we\naffect?',        9.0, C['ink'],   C['ctr_lt'],   'Users · Designers\nSociety'),
    ]

    R = 0.68

    for i, (lbl, x, dark, light, sub) in enumerate(questions):
        circle(ax, x, 1.5, R, light, dark, lbl, fsize=8.5)
        ax.text(x, 1.5 - R - 0.22, sub,
                ha='center', va='top', fontsize=7, color=C['muted'],
                linespacing=1.4, multialignment='center')

        if i < len(questions) - 1:
            nx_x = questions[i + 1][1]
            arrow(ax, x + R + 0.08, 1.5, nx_x - R - 0.08, 1.5,
                  color=C['rule'], lw=1.5)

    # Bracket annotation above nodes 3 & 4
    ax.annotate(
        '', xy=(7.0 + R + 0.05, 2.4), xytext=(5.0 - R - 0.05, 2.4),
        arrowprops=dict(arrowstyle='<->', color=C['muted'], lw=1.0),
    )
    ax.text(6.0, 2.55, 'tools shape action', ha='center', fontsize=7,
            color=C['muted'], style='italic')

    title_block(ax, 'The Human Framework',
                'Five questions design must hold simultaneously  ·  from fieldwork sketch')

    plt.tight_layout(pad=0.6)
    fig.savefig(OUT + 'chart1_human_framework.png',
                dpi=180, bbox_inches='tight', facecolor=C['bg'])
    plt.close()
    print('Saved  chart1_human_framework.png')


# ── Chart 2: Main Concept Map ──────────────────────────────────────────────────

def chart2_concept_map():
    fig, ax = plt.subplots(figsize=(16, 14), facecolor=C['bg'])
    ax.set_facecolor(C['bg'])
    ax.axis('off')
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlim(-9, 9)
    ax.set_ylim(-8, 8.5)

    # ── Node definitions: (key, label, x, y, dark, light, r) ──────────────────

    N = {
        # Central
        'ctr':  ('Design in the\nAge of AI',            0.0,   0.0,  C['ink'],  C['ctr_lt'],  0.9),

        # Four main themes
        'ant':  ('Anthropo-\nmorphism',                 -4.2,  1.8,  C['blue'], C['blue_lt'], 0.72),
        'cnv':  ('Conversational\nUX',                   0.0,  4.0,  C['red'],  C['red_lt'],  0.72),
        'tls':  ('Design Tools\n& Collaboration',        4.2,  1.8,  C['grn'],  C['grn_lt'],  0.72),
        'uxg':  ('UX Knowledge\nGap',                    0.0, -4.0,  C['pur'],  C['pur_lt'],  0.72),

        # Anthropomorphism sub-nodes
        'casa': ('CASA Paradigm\nReeves & Nass 1990s',  -7.5,  3.2,  C['blue'], C['blue_lt'], 0.52),
        'eli':  ('ELIZA Effect\nWeizenbaum 1966',        -7.5,  1.8,  C['blue'], C['blue_lt'], 0.52),
        'clp':  ('Clippy\nDouble-edged',                -7.5,  0.4,  C['blue'], C['blue_lt'], 0.52),
        'emb':  ('Embodied AI\nRabbit R1 · Meta AI',    -6.0, -1.2,  C['blue'], C['blue_lt'], 0.52),

        # Conversational UX sub-nodes
        'prb':  ('Probabilistic\nResponses',             -2.4,  6.5,  C['red'],  C['red_lt'],  0.52),
        'dm':   ('Direct Manip.\nvs NLI',                 0.0,  7.2,  C['red'],  C['red_lt'],  0.52),
        'pmt':  ('Prompt Eng.\nas Design',                2.4,  6.5,  C['red'],  C['red_lt'],  0.52),

        # Design Tools sub-nodes
        'dif':  ('Differential\nAdoption',               7.5,  3.2,  C['grn'],  C['grn_lt'],  0.52),
        'soc':  ('Social Contracts\naround AI',           7.5,  1.8,  C['grn'],  C['grn_lt'],  0.52),
        'rsc':  ('Research\nat Scale',                   7.5,  0.4,  C['grn'],  C['grn_lt'],  0.52),

        # UX Knowledge sub-nodes
        'hci':  ('HCI Lineage\n1980s–2000s',            -2.4, -6.5,  C['pur'],  C['pur_lt'],  0.52),
        'rcn':  ('Reconnect\nto Science',                 2.4, -6.5,  C['pur'],  C['pur_lt'],  0.52),

        # Cross-cutting
        'bmr':  ('Black Mirror\nEffect',                -1.6,  1.8,  C['muted'], '#E0E0DC',   0.44),
        'vis':  ('Craft\na Vision',                      1.6,  1.8,  C['muted'], '#E0E0DC',   0.44),
    }

    # ── Edges: (src, dst, color, dashed, rad) ─────────────────────────────────

    E = [
        # Center → main themes
        ('ctr', 'ant', C['blue'], False, 0.0),
        ('ctr', 'cnv', C['red'],  False, 0.0),
        ('ctr', 'tls', C['grn'],  False, 0.0),
        ('ctr', 'uxg', C['pur'],  False, 0.0),
        ('ctr', 'bmr', C['muted'], True, 0.0),
        ('ctr', 'vis', C['muted'], True, 0.0),

        # Anthropomorphism
        ('ant', 'casa', C['blue'], False, 0.0),
        ('ant', 'eli',  C['blue'], False, 0.0),
        ('ant', 'clp',  C['blue'], False, 0.0),
        ('ant', 'emb',  C['blue'], False, 0.0),

        # Conversational UX
        ('cnv', 'prb', C['red'], False, 0.0),
        ('cnv', 'dm',  C['red'], False, 0.0),
        ('cnv', 'pmt', C['red'], False, 0.0),

        # Design Tools
        ('tls', 'dif', C['grn'], False, 0.0),
        ('tls', 'soc', C['grn'], False, 0.0),
        ('tls', 'rsc', C['grn'], False, 0.0),

        # UX Knowledge Gap
        ('uxg', 'hci', C['pur'], False, 0.0),
        ('uxg', 'rcn', C['pur'], False, 0.0),

        # Cross-links (dashed)
        ('casa', 'uxg', C['muted'], True,  0.2),
        ('soc',  'uxg', C['muted'], True,  0.15),
        ('bmr',  'ant', C['muted'], True,  0.2),
        ('vis',  'cnv', C['muted'], True,  0.2),
    ]

    # Draw edges first (underneath nodes)
    for src, dst, col, dsh, rad in E:
        x0, y0, r0 = N[src][1], N[src][2], N[src][5]
        x1, y1, r1 = N[dst][1], N[dst][2], N[dst][5]
        # Trim to node edges
        dx, dy = x1 - x0, y1 - y0
        dist = np.hypot(dx, dy)
        if dist == 0:
            continue
        ux, uy = dx / dist, dy / dist
        arrow(ax, x0 + ux * r0, y0 + uy * r0,
                  x1 - ux * r1, y1 - uy * r1,
              color=col, dashed=dsh, lw=1.2, rad=rad)

    # Draw nodes
    for key, (lbl, x, y, dark, light, r) in N.items():
        sz = 9 if r > 0.65 else (7.5 if r > 0.5 else 6.5)
        circle(ax, x, y, r, light, dark, lbl, fsize=sz, lw=1.6)

    # Legend
    legend_items = [
        mpatches.Patch(facecolor=C['blue_lt'], edgecolor=C['blue'],   label='Anthropomorphism'),
        mpatches.Patch(facecolor=C['red_lt'],  edgecolor=C['red'],    label='Conversational UX'),
        mpatches.Patch(facecolor=C['grn_lt'],  edgecolor=C['grn'],    label='Design Tools & Collab'),
        mpatches.Patch(facecolor=C['pur_lt'],  edgecolor=C['pur'],    label='UX Knowledge Gap'),
    ]
    ax.legend(handles=legend_items, loc='lower left', fontsize=8,
              framealpha=0.9, edgecolor=C['rule'], facecolor=C['bg'],
              bbox_to_anchor=(0.01, 0.01))

    title_block(ax, 'Design in the Age of AI — Concept Map',
                'Core themes and their sub-concepts  ·  dashed lines = cross-cutting links')

    plt.tight_layout(pad=0.3)
    fig.savefig(OUT + 'chart2_concept_map.png',
                dpi=180, bbox_inches='tight', facecolor=C['bg'])
    plt.close()
    print('Saved  chart2_concept_map.png')


# ── Chart 3: UX Knowledge Lineage ─────────────────────────────────────────────

def chart3_ux_lineage():
    fig, ax = plt.subplots(figsize=(15, 6), facecolor=C['bg'])
    ax.set_facecolor(C['bg'])
    ax.axis('off')
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-2.8, 5.2)

    R = 0.70
    Y = 1.8

    stages = [
        ('Academic\nDisciplines',  'Psychology · CS\nSocial Sciences',         1.0, C['ink'], C['ctr_lt']),
        ('HCI',                    '1980s – 2000s\nRigour + method\nNIST · CHI', 3.3, C['grn'], C['grn_lt']),
        ('UX',                     '2000s – 2020s\nMethods adopted\nrigour lost', 5.6, C['red'], C['red_lt']),
        ('AI-era\nDesign',         '2020s –\nNew challenges\nold answers exist', 7.9, C['blue'], C['blue_lt']),
        ('Reconnect\nto Science',  'HCI · AI Safety\nAlignment · Values',      10.2, C['pur'], C['pur_lt']),
    ]

    for i, (lbl, sub, x, dark, light) in enumerate(stages):
        circle(ax, x, Y, R, light, dark, lbl, fsize=8.5)
        ax.text(x, Y - R - 0.22, sub,
                ha='center', va='top', fontsize=7, color=C['muted'],
                linespacing=1.4, multialignment='center')

        if i < len(stages) - 1:
            nx_x = stages[i + 1][2]
            arrow(ax, x + R + 0.08, Y, nx_x - R - 0.08, Y,
                  color=C['rule'], lw=1.5)

    # Dashed arc: HCI → UX (knowledge gap / rigour skipped)
    x0, x1 = 3.3, 5.6
    theta = np.linspace(0, np.pi, 60)
    arc_x = (x0 + x1) / 2 + (x1 - x0) / 2 * np.cos(np.pi - theta)
    arc_y = Y + 1.5 * np.sin(theta)
    ax.plot(arc_x, arc_y, '--', color=C['red'], lw=1.4, alpha=0.7)
    ax.annotate('', xy=(x1 - R - 0.05, Y + 0.3),
                xytext=(arc_x[-2], arc_y[-2]),
                arrowprops=dict(arrowstyle='->', color=C['red'], lw=1.4))
    ax.text((x0 + x1) / 2, Y + 1.8, 'rigour skipped', ha='center',
            fontsize=7.5, color=C['red'], style='italic')

    # Dashed arc: AI-era → Reconnect (the needed step)
    x2, x3 = 7.9, 10.2
    theta2 = np.linspace(0, np.pi, 60)
    arc2_x = (x2 + x3) / 2 + (x3 - x2) / 2 * np.cos(np.pi - theta2)
    arc2_y = Y + 1.5 * np.sin(theta2)
    ax.plot(arc2_x, arc2_y, '--', color=C['pur'], lw=1.4, alpha=0.7)
    ax.annotate('', xy=(x3 - R - 0.05, Y + 0.3),
                xytext=(arc2_x[-2], arc2_y[-2]),
                arrowprops=dict(arrowstyle='->', color=C['pur'], lw=1.4))
    ax.text((x2 + x3) / 2, Y + 1.8, 'reconnection needed', ha='center',
            fontsize=7.5, color=C['pur'], style='italic')

    # Shneiderman & Gabriel annotation
    ax.text(10.2, Y - R - 1.6,
            'Shneiderman (2022)\nHuman-Centered AI\n\nGabriel (2020)\nValue alignment\n= normative problem',
            ha='center', va='top', fontsize=6.5, color=C['pur'],
            linespacing=1.4, style='italic')

    title_block(ax, 'The UX Knowledge Lineage',
                'How UX inherited HCI methods without its research rigour — and what AI design demands now')

    plt.tight_layout(pad=0.6)
    fig.savefig(OUT + 'chart3_ux_lineage.png',
                dpi=180, bbox_inches='tight', facecolor=C['bg'])
    plt.close()
    print('Saved  chart3_ux_lineage.png')


# ── Chart 4: Designer–User–AI Ecosystem ───────────────────────────────────────

def chart4_ecosystem():
    fig, ax = plt.subplots(figsize=(11, 9), facecolor=C['bg'])
    ax.set_facecolor(C['bg'])
    ax.axis('off')
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-4.8, 4.8)

    # Nodes: (key, label, x, y, dark, light, r)
    N = {
        'usr': ('User',             0.0,  0.0, C['ink'],  C['ctr_lt'], 0.75),
        'des': ('Designer',        -3.2,  2.2, C['blue'], C['blue_lt'], 0.65),
        'res': ('Researcher',      -3.2, -2.2, C['grn'],  C['grn_lt'],  0.65),
        'ai':  ('AI Tool',          3.2,  2.2, C['red'],  C['red_lt'],  0.65),
        'soc': ('Society /\nOthers', 3.2, -2.2, C['pur'], C['pur_lt'],  0.65),
        'org': ('Organisation',     0.0,  3.8, C['muted'], '#E2E2DE',   0.55),
    }

    # Edges: (src, dst, label, dashed, rad)
    E = [
        ('des', 'usr', 'designs for',       False,  0.05),
        ('des', 'ai',  'uses / delegates',  False,  0.15),
        ('res', 'usr', 'studies',           False,  0.05),
        ('res', 'des', 'informs',           False,  0.0),
        ('ai',  'usr', 'serves',            False,  0.05),
        ('ai',  'des', 'augments',          True,   0.15),
        ('usr', 'soc', 'part of',           False,  0.05),
        ('org', 'des', 'commissions',       False,  0.05),
        ('org', 'res', 'commissions',       False, -0.05),
        ('soc', 'usr', 'shapes values',     True,   0.2),
        ('res', 'ai',  'evaluates',         True,   0.25),
    ]

    for src, dst, lbl, dsh, rad in E:
        x0, y0, r0 = N[src][1], N[src][2], N[src][5]
        x1, y1, r1 = N[dst][1], N[dst][2], N[dst][5]
        dx, dy = x1 - x0, y1 - y0
        dist = np.hypot(dx, dy)
        if dist == 0:
            continue
        ux, uy = dx / dist, dy / dist
        ax0, ay0 = x0 + ux * r0, y0 + uy * r0
        ax1, ay1 = x1 - ux * r1, y1 - uy * r1
        arrow(ax, ax0, ay0, ax1, ay1, color=C['rule'], dashed=dsh, lw=1.2, rad=rad)

        # Edge label at midpoint
        mx = (ax0 + ax1) / 2 + (-uy * 0.2 if rad != 0 else 0)
        my = (ay0 + ay1) / 2 + (ux * 0.2 if rad != 0 else 0)
        ax.text(mx, my, lbl, ha='center', va='center', fontsize=6.2,
                color=C['muted'],
                bbox=dict(boxstyle='round,pad=0.12', facecolor=C['bg'],
                          edgecolor='none', alpha=0.88))

    for key, (lbl, x, y, dark, light, r) in N.items():
        circle(ax, x, y, r, light, dark, lbl, fsize=9.5, lw=1.8)

    # Dashed = AI mediated / indirect
    legend_items = [
        mpatches.Patch(facecolor='none', edgecolor='none',
                       label='── direct relationship'),
        mpatches.Patch(facecolor='none', edgecolor='none',
                       label='- - AI-mediated / indirect'),
    ]
    ax.legend(handles=legend_items, loc='lower right', fontsize=7.5,
              framealpha=0.9, edgecolor=C['rule'], facecolor=C['bg'],
              bbox_to_anchor=(0.99, 0.01))

    title_block(ax, 'The Designer–User Ecosystem',
                'How AI reshapes roles and relationships within design practice')

    plt.tight_layout(pad=0.3)
    fig.savefig(OUT + 'chart4_ecosystem.png',
                dpi=180, bbox_inches='tight', facecolor=C['bg'])
    plt.close()
    print('Saved  chart4_ecosystem.png')


# ── Run ────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    chart1_human_framework()
    chart2_concept_map()
    chart3_ux_lineage()
    chart4_ecosystem()
    print('\nAll charts saved to', OUT)
