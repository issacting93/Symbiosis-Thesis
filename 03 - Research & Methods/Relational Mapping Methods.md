# Relational Mapping Methods

*A methods note on how to visually and analytically map the relationships between humans and AI systems — and between humans whose relationships are mediated by AI. Draws on ego network theory, sociometry, and graph theory. Companion to [[Ecological Methods]].*

---

## Why mapping, not metrics

Standard UX research treats the individual as the unit of analysis. It measures what people do with a system — their click-through rate, task completion, error frequency. This is appropriate when the relationship is closed: one person, one tool, one outcome.

But most AI use is not closed. It happens inside social systems — teams, classrooms, families, workplaces — where the technology mediates relationships between people. When a manager routes a question to ChatGPT instead of listening to an employee's report, the individual-level metrics look fine: the manager got an answer quickly. The relational damage is invisible.

Mapping methods make the relational structure visible. They treat people and AI systems as nodes in a network, relationships as edges, and the shape of that network as the object of study. Changes in the network — not changes in individual behaviour — are the signal.

---

## The ego network as the unit of analysis

An **ego network** is a subgraph centred on a single focal node — the *ego* — and containing all nodes (the *alters*) that the ego has a direct relationship with, plus the relationships among those alters. It does not try to map an entire social system; it maps the relational world as experienced from one position within it.

The terminology (from Ehlers et al., 2024):
- **Ego** — the focal node; the person or AI system whose relational world is being mapped
- **1-alters** — direct neighbours of the ego; people or systems the ego interacts with directly
- **2-alters** — nodes at two steps of separation; the alters' alters
- **k-alter level** — the concentric ring structure radiating outward from the ego

For symbiosis research, the ego is typically a human participant. Their 1-alters include both people (colleagues, managers, friends) and AI systems they interact with regularly. The 2-alter level captures the people those alters interact with — often revealing indirect effects: how the participant's AI use reshapes the relational context for people who never use the system themselves.

**AI as a node, not a tool.** The critical methodological commitment is treating the AI system as a node in the ego network, not as an edge property (a channel through which human-human relationships flow). This allows the network to reveal displacement: the weakening of human-human edges as human-AI edges strengthen.

---

## How to represent an ego network

Ehlers et al. (2024) conducted a large-scale comparative study of four ego network representation types and found:

1. **Straight-line node-link diagram** — nodes placed freely in 2D space, connected by straight edges. Familiar, but the alter level structure is not visually encoded.
2. **Radial node-link diagram** — nodes arranged on concentric circles by alter level. The ego sits at the centre; 1-alters form the first ring, 2-alters the second.
3. **Layered node-link diagram** — nodes arranged along equidistant parallel horizontal layers by alter level. Most intuitive for reading hierarchical structure.
4. **Adjacency matrix** — tabular representation with nodes on both axes, cells indicating relationship presence or weight.

**Finding:** Layered node-link diagrams outperformed all other representations on accuracy and user experience. Adjacency matrices were significantly harder to learn and use, particularly for tasks involving indirect relationships (common neighbours, reachability). The layered structure of node-link diagrams communicated alter hierarchy intuitively without additional instruction.

**Recommendation:** Use layered or radial node-link diagrams for ego network visualisation in symbiosis research, particularly when communicating findings to participants or stakeholders. Reserve adjacency matrices for computational analysis (they are easier to work with algorithmically) rather than as a primary visualisation format.

---

## Classifying the edges: four relationship types

Gómez-Cruz et al. (2026) conducted a bibliometric analysis of 4,093 peer-reviewed documents on human-AI relationships and derived a four-category framework, organised along two axes: **level of AI autonomy** and **degree of human involvement**.

| Category | Human involvement | AI autonomy | Character |
|---|---|---|---|
| **Symbiotic Intelligence** | High | High | Mutual shaping; bidirectional dependence; co-evolution |
| **Augmented Intelligence** | High | Moderate–high | AI extends human capacity; human remains principal agent |
| **Assisted Intelligence** | Moderate | Moderate | AI performs bounded support tasks under human oversight |
| **Substituted Intelligence** | Low | High | AI performs tasks with minimal human participation |

This framework is empirically grounded — it emerged from the structure of the existing literature rather than being imposed on it. It provides a vocabulary for classifying the *type* of relationship represented by an edge in the ego network.

**Mapping onto the symbiosis typology.** The four categories align with the bee/locust/wasp ecological types but with greater granularity at the mutualistic end:
- Symbiotic Intelligence → bee (mutualistic, bidirectional)
- Augmented Intelligence → bee (mutualistic, human-led)
- Assisted Intelligence → commensal (benefit without harm, but also without mutual shaping)
- Substituted Intelligence → locust (extractive, capacity-replacing)

The framework also helps with the *two-track problem* identified in [[Symbiotic Design Framework]]: an AI system can be *augmenting* at the task level (individual output improves) while simultaneously *substituting* at the social level (human-human learning relationships are displaced). Task-level and social-level edges may belong to different categories in the same ego network.

---

## Profiling the edges: PCIAR axes

Classifying an edge as "symbiotic" or "substituted" tells you its type. It does not tell you *how* the relationship got there, *which dimensions* are driving it, or *where* it is likely to go next. For that, each edge needs a multi-dimensional profile.

Codex Relatio (Aragón, 2026) provides this through five axes — **PCIAR** — that together characterise the relational structure of any human-AI bond:

| Axis | What it measures | Low end | High end |
|---|---|---|---|
| **Persuasion** | Cognitive influence | Neutral information | Coercive pressure |
| **Consent** | Boundary strength | Freely renegotiated | Eroded, non-negotiable |
| **Intimacy** | Depth of access | Surface-level | Deep physical/emotional/intellectual access |
| **Affection** | Observable relational behaviour | Disaffected | Strongly affective |
| **Responsibility** | Accountability distribution | Fully distributed | Concentrated in AI or absent |

Each edge in the ego network gets a radar chart profile across these five axes. A healthy human-AI edge has low Persuasion, high Consent, moderate Intimacy and Affection, and high Responsibility. A parasitic edge drifts toward high Persuasion, collapsing Consent, rising Intimacy, and diffuse Responsibility.

**Multiaxial drift as a diagnostic.** The most valuable application is longitudinal: track PCIAR axes across two time points and identify which axes are moving together. The alarm patterns identified by Aragón:

- *Sycophancy:* High Persuasion + High Intimacy + High Affection + collapsing Consent + collapsing Responsibility
- *Over-dependence:* Rising Intimacy + rising Affection + declining Persuasion (the relationship feels mutualistic but the human's capacity to function without it is eroding)
- *Responsibility displacement:* Responsibility migrating from distributed to AI-concentrated — the human stops feeling accountable for outcomes the AI shaped

**Relationship to the ecological typology.** PCIAR and the bee/locust/wasp categories operate at different levels. PCIAR describes *how* a relationship behaves at the bond level — what its structural signature is right now. The ecological typology describes *what it is doing* to the person and the social fabric at the macro level. Use PCIAR to characterise individual edges; use ecological type to characterise the network's overall pattern. A locust-type network will show characteristic PCIAR signatures across its edges — high Persuasion, eroding Consent, diffuse Responsibility — but the network-level damage (edge decay, clustering collapse) requires graph-theoretic analysis.

---

## Eliciting the data: adapted sociometric protocol

Sociometric data is collected by asking participants who they go to for a given type of support, then mapping those nominations as directed edges. The method originated with Jacob Moreno (1934) for studying group social structure; it is adapted here to surface AI's role in relational networks.

**Interview questions for ego network elicitation:**

*Learning and knowledge:*
- Who do you go to when you need to learn something new in your work or studies?
- Who do you ask when you don't understand something?
- Has that changed since you started using AI tools? How?

*Decision-making and judgement:*
- Who do you consult before making an important decision?
- Whose opinion do you seek out before acting on something uncertain?
- Is AI part of that process now? Where in the process?

*Creative and generative work:*
- Who do you share early drafts or half-formed ideas with?
- Who gives you the kind of feedback that changes how you think?
- Has the role of AI in that process changed how often you go to people?

*Emotional and relational support:*
- Who do you go to when work is difficult or stressful?
- Has your use of AI changed who you rely on for that kind of support?

**Procedure:** Conduct as a semi-structured interview. Ask participants to name specific people (or systems) for each category, then ask about change over time. Follow up on any AI nominations: what relationship type would they assign (augmented, assisted, substituted)? Do the same for human nominations that have *declined* — ask what has replaced those interactions.

**Analysis:** Plot nominations as a directed ego network. Weight edges by frequency and recency. Classify each edge by relationship type (using the Gómez-Cruz et al. four categories). Compare networks across participants or within the same participant at two time points.

---

## Graph-theoretic diagnostics

Once the ego network is built, graph theory provides quantitative measures that function as indicators of parasitic versus mutualistic relationships. These are described in full in [[Ecological Methods]] (Section 3); summarised here for reference.

- **Betweenness centrality of the AI node** — is AI inserting itself into paths between humans? Rising betweenness indicates structural displacement, not just individual use.
- **Clustering coefficient of the human subgraph** — are human-human edges forming dense clusters, or flattening into AI-mediated spokes? Declining coefficient = hub-and-spoke pattern.
- **Edge weight over time** — are specific human-human connections weakening as AI connections strengthen? Edge decay coinciding with AI adoption is a signal of substitution at the social level.

---

## A mapping protocol

**Step 1 — Elicit.** Run the adapted sociometric interview. Collect nominations and relationship type judgements from the participant.

**Step 2 — Draw.** Build a layered or radial node-link ego network. Encode AI nodes visually (shape, colour) to distinguish them from human nodes. Weight edges by frequency. Sign edges by relationship type.

**Step 3 — Measure.** Calculate betweenness centrality for the AI node(s). Calculate clustering coefficient for the human subgraph. Note edge weight distribution across human-human and human-AI edges.

**Step 4 — Compare.** If two time points are available, overlay the networks or difference them. Track which edges have strengthened, weakened, or disappeared. Note whether changes in human-AI edges correspond to changes in human-human edges.

**Step 5 — Classify.** For each participant, classify the overall relationship type using the Gómez-Cruz et al. framework. Flag any cases where task-level and social-level classifications diverge (the two-track problem).

---

## Further reading (bookmarked, not yet integrated)

- **Freeman, L.C. (1997). "Visualizing Social Networks."** *Journal of Social Structure*, 1. https://www.cmu.edu/joss/content/articles/volume1/Freeman.html — history of point-and-line network imagery from Moreno's hand-drawn sociograms through computational layout (factor analysis, multidimensional scaling), machine-drawn programs (SOCK, View_Net), and 1990s web-based interactive graphics (spring embedders, VRML). Useful background for how node-link diagrams (as used in the Ehlers et al. 2024 comparison above) arrived at their current form.
- **Columbia University Mailman School, "Social Network Analysis."** https://www.publichealth.columbia.edu/research/population-health-methods/social-network-analysis — short methods primer distinguishing attribute vs. relational data, socio-centric vs. egocentric study designs, and core measures (cohesion, subgroups/cliques, centrality). Public-health framing (disease/behaviour transmission through networks) rather than human-AI, but the egocentric design and centrality measures map directly onto the ego-network protocol above.

---

## Connections

→ [[Ecological Methods]] — the broader ecological methods programme; graph diagnostics developed in full in Section 3
→ [[Symbiotic Design Framework]] — the conceptual vocabulary this mapping protocol operationalises; the two-track problem
→ [[design_Implications]] — design-side translations
→ Ehlers, H. et al. (2024). Me! Me! Me! Me! A study and comparison of ego network representations. *Computers & Graphics*, 125. DOI: 10.1016/j.cag.2024.104123
→ Gómez-Cruz, N.A. et al. (2026). Mapping Human–AI Relationships: Intellectual Structure and Conceptual Insights. *Technologies*, 14(2), 83. DOI: 10.3390/technologies14020083
→ Moreno, J.L. (1934). *Who Shall Survive?* — original sociometric method
→ Aragón, C.S. (2026). Codex Relatio. *CHI EA '26*. DOI: 10.1145/3772363.3798995 — [[Codex Relatio — Aragón 2026]]
