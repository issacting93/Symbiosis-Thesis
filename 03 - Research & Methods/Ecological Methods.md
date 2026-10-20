# Ecological Methods

*Methods borrowed from ecology that can be adapted to study human-technology relationships as relational systems. Organised from most to least immediately applicable to the Symbiosis framework.*

---

## 1. Measuring the Relationship Itself

### Net effect measurement
The empirical core of symbiosis research. Ecologists determine whether a relationship is mutualistic or parasitic by measuring its net effect on each party: does the presence of the partner increase or decrease the host's fitness over time?

**Applied here:** Measure what the relationship does to each party over time.
- For the human: capacity retention, autonomy, skill development, social connection, emotional regulation
- For the technology/company: engagement, retention, revenue, data extraction

You cannot run a controlled experiment where one group never uses AI. But you can use quasi-experimental designs — compare users of a mutualistically-designed system against users of a parasitically-designed one, or track the same users before and after a major design change.

### Resilience measurement
Resilience is a system's capacity to absorb disturbance and reorganise while retaining its essential function. Ecologists measure two components: resistance (how much the system changes under disturbance) and recovery (how quickly it returns to baseline).

**Applied here:** Measure the resilience of a person's capacity to function without the technology. Apply a disturbance — a forced 48-hour break, a technical failure, a period without access — and measure how quickly and completely the person returns to their baseline performance. A mutualistic relationship leaves the person resilient. A parasitic one leaves them brittle. This is a concrete, testable operationalisation of the typology.

---

## 2. Tracking Change Over Time

### State-and-transition models
Ecosystems do not change gradually and continuously — they occupy discrete states (grassland, shrubland, forest) and transition between them when triggers accumulate past a threshold. Some transitions are reversible. Others are not.

**Applied here:** Model human-technology relationships as a state-and-transition system. Possible states:
- *Instrumental use* — the person uses the technology for a task and puts it down (commensal)
- *Relational engagement* — the person begins to relate to the technology as an entity (potentially mutualistic or parasitic)
- *Dependency* — the person cannot easily function without it (parasitic)
- *Withdrawal* — the person exits or significantly reduces use

Transitions are triggered by design features (a new notification, a memory update, a personalisation change) or life events (loneliness, stress, social isolation). The key insight: parasitic relationships often involve transitions that users do not notice until they are already in the new state. The model makes the thresholds visible before the shift occurs.

### Chronosequences and permanent plots
Two complementary approaches to studying change. A chronosequence substitutes space for time — study people at different stages of adoption (one month, six months, two years) and infer the trajectory. A permanent plot tracks the same people over time with repeated measures.

**Applied here:** Use chronosequences when longitudinal data is not yet available. Use permanent plots — diary studies, cohort tracking, repeated measures — as the methodological gold standard. The combination gives you both breadth and depth.

### Disturbance regime analysis
Ecologists study not just individual disturbances but disturbance regimes: the pattern, frequency, and intensity of disturbances over time. Changing regimes produce regime shifts — abrupt reorganisations of the ecosystem.

**Applied here:** Analyse the disturbance regime of a human-technology relationship. How often does the system introduce a new feature, notification, or personalisation update that changes the terms of the relationship? Small, frequent disturbances can gradually push a relationship from mutualistic toward parasitic without any single dramatic event. The framework makes cumulative drift visible.

---

## 3. Mapping Relational Structure

### Signed networks
Networks where edges carry a sign — positive (mutualistic, facilitative) or negative (parasitic, antagonistic). This allows both beneficial and harmful relationships to be represented in a single structure.

**Applied here:** Build a signed network of human-technology relationships in a specific context — a team, a classroom, a care home. Nodes are people and technology systems. Edges are relationships weighted by frequency, type of interaction, and net effect on each party. A mutualistic edge is positive for both. A parasitic edge is positive for the company and negative for the human. The network makes the typology quantitative and visual, and shows how individual relationships aggregate into system-level patterns.

### Indirect effects analysis
Ecologists distinguish direct effects (A eats B) from indirect effects (A eats B, which reduces predation on C, which increases C's population). Indirect effects are often the most consequential and the hardest to see.

**Applied here:** Trace the indirect effect chains in human-technology systems. A uses AI heavily → A's productivity rises → manager raises expectations → B feels pressure to adopt → B's relationship with AI changes → the team's social dynamics change. This framework makes visible the effects on people who are not the primary user — the co-worker, the student, the family member who adapts to someone else's AI use.

### Sociometry and sociograms
Sociometry, developed by Jacob Moreno in the 1930s, is a method for making invisible social structure visible. Participants are asked who they would choose to work with, learn from, or turn to in a given situation. The results are plotted as a sociogram — a directed graph in which nodes are people and edges are relational choices. The sociogram reveals who is central, who is peripheral, who bridges otherwise separate groups, and who is excluded.

The technique was designed for human groups. Extended to human-technology systems, AI becomes a node — not merely a tool, but a relational actor. The sociogram then captures something standard UX methods cannot: whether AI is *augmenting* human relationships or *displacing* them.

**Applied here:** Ask participants not only *who* they go to for a given kind of support, but whether that has changed since adopting an AI system. If the manager who once listened to the employee's report now routes that question to ChatGPT, the human-human edge has weakened and a human-AI edge has formed in its place. The sociogram makes this substitution structural and visible. Run it at two time points and the displacement becomes a longitudinal finding.

The adapted sociometric questions for this context:
- *Who do you go to when you need to learn something new in your work?*
- *Who do you consult before making an important decision?*
- *Who would you ask to review your work before submitting it?*
- *Has that changed since you started using AI tools? How?*

### Graph-theoretic diagnostics
Graph theory provides the mathematical vocabulary to move from visual sociograms to quantitative measures of relational change. Three metrics are particularly relevant to the symbiosis framework.

**Betweenness centrality** measures how often a node sits on the shortest path between other nodes. A node with high betweenness is a broker — information and influence route through it. For AI systems, rising betweenness centrality is a structural signal of parasitism: the AI is inserting itself into paths that previously connected humans directly. In a mutualistic relationship, the AI's betweenness is high but *passes through* — it facilitates connection without terminating it. In a parasitic one, it becomes the endpoint — the human-human connection is never completed.

**Clustering coefficient** measures how densely connected a node's neighbours are to each other. In a healthy human social graph, people form clusters — teams, friendships, peer groups where members interact with each other directly. A declining clustering coefficient, coinciding with increased AI adoption, indicates that the dense local structure is flattening into a hub-and-spoke pattern: each person connects to AI rather than to each other.

**Edge weight over time** — tracking the strength of specific human-human connections as AI use intensifies. Mutualistic AI should leave edge weight stable or increase it (by facilitating collaboration). Parasitic AI creates a pattern of edge decay: the human-human connections weaken precisely as the human-AI connections strengthen.

**Ecological types as graph structures.** The three ecological archetypes map onto recognisable graph patterns:
- *Bee-like AI* — bridges; creates new edges, increases clustering, betweenness is high but transitional
- *Locust-like AI* — hub-and-spoke; human-human edges atrophy, AI becomes the dominant node, clustering coefficient falls
- *Wasp-like AI* — disrupts local clusters without integrating; damages specific edges without forming stable alternatives

---

## 4. System-Level Dynamics

### Keystone actors
A keystone species is one whose effect on the ecosystem is disproportionate to its abundance. Remove it and the community restructures entirely.

**Applied here:** Analyse whether a technology platform functions as a keystone actor in a social system. Does its presence restructure how people interact with each other? Does removing it change the social fabric? In workplaces and schools, the dominant AI platform may be a keystone: it shapes the terms of interaction for everyone, including people who barely use it.

### Niche construction
Organisms do not just adapt to their environments — they modify them. This modification changes the conditions for everyone else.

**Applied here:** Heavy technology users construct a niche — a workflow, a set of expectations, a norm — that changes the environment for others. The co-worker who uses AI for everything constructs a niche in which colleagues must either adapt or fall behind. Niche construction theory names this dynamic and makes it a research object.

---

## 5. A Research Programme

If you were to build a study from these methods:

**Map** — Build a signed network of human-technology relationships in a target context. Use indirect effects analysis to identify who is affected beyond the primary user.

**Measure** — Apply net effect measurement to assess the relationship's impact on each party. Run resilience measurement to test how brittle the human's capacity becomes under disturbance.

**Track** — Use state-and-transition models to identify relational states and the triggers that move between them. Use chronosequences and permanent plots to study how relationships evolve over months and years.

**Monitor** — Build a long-term monitoring system that tracks relational quality alongside usage. Define the variables, collect data consistently, and flag when relationships drift toward parasitism.

---

## Connections

→ [[Symbiotic Design Framework]] — the conceptual vocabulary this methods programme operationalises
→ [[design_Implications]] — the design-side translation of these methods
→ [[Sociocultural Theory — Vygotsky 1934]] — scaffold vs. substitute as the individual-level equivalent of net effect measurement
→ [[Relational Models Theory — Fiske 1992]] — the relational model diagnostic that precedes network analysis
→ Moreno, J.L. (1934). *Who Shall Survive?* — original sociometric method
→ graph theory diagnostics (betweenness centrality, clustering coefficient, edge decay) as quantitative operationalisations of the bee/locust/wasp typology
→ [[Position Paper — Designing for Symbiosis]] — the academic argument these methods support
