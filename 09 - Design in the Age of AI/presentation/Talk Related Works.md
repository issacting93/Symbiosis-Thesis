# Related Works — Design Research in the Age of AI

*Supporting literature for the talk. Organised by theme, with connection notes.*

---

## Anthropomorphism & the CASA Paradigm

The foundational work here is Nass and Reeves' **CASA (Computers Are Social Actors) paradigm**, which established that people apply human social rules to computers even when they know the machine is not human. Their experiments showed that users respond to computers with gender, personality, and flattery cues in ways that mirror human–human interaction — and that these responses can be triggered by very crude representations of agentness. The "mindless" application of social scripts, rather than conscious anthropomorphizing, is what drives the effect. This is the empirical backbone for the claim that emotional design can substitute for interaction design.

- Nass, C., & Moon, Y. (2000). Machines and mindlessness: Social responses to computers. *Journal of Social Issues*, 56(1), 81–103.
- Reeves, B., & Nass, C. (1996). *The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places*. Cambridge University Press.

The **ELIZA effect** is the historical case study for the pre-LLM genealogy of anthropomorphism. Weizenbaum built ELIZA as a Rogerian therapy simulation using simple pattern-matching, and was startled when users formed genuine emotional attachments — some asked to be alone with the program. The ELIZA effect is now a named phenomenon in HCI, and it directly parallels what has since emerged with Replika and Character AI at scale.

- Weizenbaum, J. (1976). *Computer Power and Human Reason: From Judgment to Calculation*. W.H. Freeman.
- Wardrip-Fruin, N., & Montfort, N. (Eds.). (2026). *Inventing ELIZA*. MIT Press. [Scholarly reconstruction of the original source code with annotation.]

**Clippy** is the canonical failure case, and the research literature supports this reading precisely. The design was inspired by CASA findings — Microsoft took the "logical" next step of anthropomorphizing the assistant — but the mismatch between Clippy's emotional promise and its limited functionality turned users against it. The lesson: anthropomorphic design is a double-edged sword, and the boundary condition is whether the system can deliver on the relational promise it makes.

- Analysis in *Metaphors in Voice User Interfaces*, ACM TOCHI (2023), which frames Clippy as "pesky and meddlesome due to its anthropomorphic design and intrusive nature."
- "What can we learn from Clippy about AI?" SAS Blogs (2019) — identifies the specific design violations: gendered agent design, intrusive interruption, and mismatch between personality and capability.

Recent empirical work on **AI companions** provides contemporary evidence for the first observation. A 2026 study in *Scientific Reports* found that perceived anthropomorphism has significant positive effects on perceived ease of use, perceived usefulness, and behavioural intention — mediated by emotional attachment. The mechanism (emotional investment drives engagement) is now empirically validated.

- Zhang & Yu (2026). Exploring the attraction of AI companions. *Scientific Reports*.
- Longitudinal RCT on companion chatbot use and social impacts. AAAI (2025).

---

## Conversation as Dominant UX Paradigm & Probabilistic Design

The shift from deterministic to **probabilistic interfaces** is one of the central problems of current design practice. The risk is not the probabilistic system itself — it is probabilistic systems wrapped in deterministic interfaces, where the AI offers a guess and the interface presents it as truth.

- "Designing With Uncertainty: How AI Supercharges Probabilistic Thinking," *Smashing Magazine* (June 2026). Practical guide for designers working with probabilistic outputs, including the Air Canada chatbot case as a cautionary example.
- On **probabilistic UX** as an emerging approach: zeroheight's analysis of generative UI (2026) defines it as "less an architecture and more an approach: one that accepts and communicates uncertainty and variability."

The **direct manipulation vs. natural language debate** has a rich HCI lineage. The key paper directly compared a conversational agent (CA) metaphor against direct manipulation (DM) for the same task. The finding is nuanced: task completion rate was higher for the CA system, but users who could use DM effectively preferred it because it was faster and gave a greater sense of control. This supports the argument that a structured menu of intentions is often the better design solution.

- Jönsson, A., et al. (2005). Conversational agent or direct manipulation in human–system interaction. *Speech Communication*, 47(1–2), 194–207.
- DirectGPT, ACM CHI (2024): users prefer a combination of direct manipulation and natural language, especially when objects are hard to describe — consistent with Wizard-of-Oz findings from the 1990s.

---

## Design Tools, Collaboration & Differential AI Adoption

On **AI-assisted design workflows**, emerging qualitative research documents how designers are actually using these tools. A 2026 study of AI-assisted UX/UI design processes found that participants used ChatGPT primarily for research and chat, while Lovable and Figma Make provided support in design production and prototyping — the divided-toolchain problem.

- Qualitative study of AI-assisted UX/UI design processes, Istanbul Technical University (2026).
- On prompt-to-prototype generators (Figma Make, Bolt, Lovable) enabling researchers to generate working prototypes in hours rather than weeks.

On **social contracts around AI adoption**, the most directly relevant recent work documents exactly the disciplinary divide described in the talk: leadership evaluates AI by efficiency metrics while workers see deskilling and diminished craft; adoption reshapes interpersonal relationships; and workers face "fear of being seen as a cheater, fear of being perceived as incompetent, and fear of deviating from workplace norms."

- "AI Adoption as a Mirror of Organizational Culture," arXiv (2026).
- 2025 latent profile analysis finding that the "Anxious but Disciplined" group reports the highest AI usage at work.

On **social contract theory applied to AI design**, the foundational move is Rahwan's Society-in-the-Loop (SITL) framework, which uses social contract theory to embed societal values into AI development.

- Rahwan, I. (2018). Society-in-the-loop: Programming the algorithmic social contract. *Ethics and Information Technology*, 20, 5–14.

---

## The UX Knowledge Problem & HCI Rigor

The field of HCI grew through the 1980s and 1990s by assimilating scientific rigor from cognitive science, sociology, and engineering — combining quantitative and qualitative methods, hypothesis testing with case-study methods. The early empirical tradition was forged by Shackel (1959) and Shneiderman (1980), who advocated user testing as the primary means of improving usability.

- "Revisiting the Astonishing Growth of Human–Computer Interaction Research," *Computer* (2017) — on how HCI researchers adopted new methods that blended quantitative and qualitative approaches.

On the **research–practice gap** in UX specifically, there is recent empirical work documenting how practitioners navigate pre-production through "adaptive strategies rather than direct application of academic frameworks." Practitioners extract core concepts from academic work and reframe them for local contexts — they treat scholarship as a resource for collaborative sense-making rather than a rigid blueprint. The gap is not that practitioners ignore research; it is that the research is not designed with sensitivity to industry timelines and constraints.

- "Within these teams, experts emphasized that minimal friction is not always beneficial," ACM (2025).
- Tang & Herrli (2025). "Where to Go from Here: Bridging the Gaps." In *The Domain of UX in Information Studies*, Springer. Establishes a framework for bridging academic UX research and industry practice.

---

## The Black Mirror Effect & *Her* as Design Fiction

On **design fiction** as a method, Mark Blythe's work on Research through Design Fiction is particularly relevant. It theorizes how fiction can be used as an empirical method to gain knowledge rather than merely as inspiration.

- Blythe, M. (2014). Research through design fiction: Narrative in real and imaginary abstracts. *Proceedings of CHI 2014*.
- "Designing for an AI Future: Avoiding the Dystopia," Association of Professional Futurists (2024) — explicitly frames *Black Mirror* as a cautionary tale and asks whether it serves as "a warning or an inspiration."

On ***Her*** **as a design text**, there is a growing scholarly literature. Useful for grounding the Spike Jonze opening beyond anecdote:

- "A Feminist-Rights Reassessment of Spike Jonze's *Her* and Its Influence on Real-World Companion AI Design" (2025).
- "From Natural Selection to Digital Transcendence: Re-thinking Evolution and the Possibility of AI Supremacy in Spike Jonze's *Her* (2013)," *Semantic Scholar* (2026).
- "AI, Body, Emotion and Ethical Subject in Spike Jonze's *Her*," KCI (2026).

---

## AI Safety & Alignment

*This section provides language for engaging with technical audiences on the connection between design practice and the AI safety/alignment research agenda.*

The foundation for the technical vocabulary is the **Concrete Problems in AI Safety** paper, which decomposed AI safety into five sub-problems — avoiding negative side effects, reward hacking, scalable oversight, safe exploration, and distributional robustness. For designers, it provides a taxonomy of ways AI systems fail relative to intent that maps directly onto failure modes observable at the interface level (e.g., a model optimizing a measurable proxy rather than the user's actual goal).

- Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). Concrete problems in AI safety. arXiv:1606.06565.

A critical sociotechnical revisitation extends the original framework, arguing it was framed too narrowly around technical robustness and missed the social and organizational conditions that produce AI harm in deployment — reframing safety in terms that map onto design research methods (contextual inquiry, deployment research, stakeholder analysis).

- Raji, I. D., & Dobbe, R. (2024). Concrete problems in AI safety, revisited. arXiv:2401.10899 (ICLR workshop).

**Gabriel (2020)** is the key philosophical bridge. Writing from DeepMind, Gabriel argues that value alignment is not merely a technical problem but an irreducibly normative one: the question is not which "true" moral principles AI should follow, but which principles are fair under conditions of widespread moral disagreement. This shifts alignment from an engineering specification problem toward a participatory design problem — one that requires stakeholder deliberation, not just annotation and RLHF pipelines.

- Gabriel, I. (2020). Artificial intelligence, values, and alignment. *Minds and Machines*, 30, 411–437.

**Shneiderman's HCAI framework** proposes a two-dimensional design space — degree of human control versus degree of automation — and argues that safety and trustworthiness require designers to deliberately locate systems within that space rather than defaulting to maximum automation. It is explicitly addressed to designers, engineers, and policymakers together, making it the most accessible bridge between HCI design practice and AI governance.

- Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press.

On **explainability as a user requirements problem**: drawing on interviews with 20 UX practitioners building AI products, Liao et al. developed an XAI Question Bank — a taxonomy of nine categories of questions users actually ask about AI behaviour (Why? Why not? What if? etc.) — and showed that existing interpretability techniques map poorly onto user needs. It establishes that designers are the appropriate professionals to specify what kind of explanation is needed before any technical approach is selected.

- Liao, Q. V., Gruen, D., & Miller, S. (2020). Questioning the AI: Informing design practices for explainable AI user experiences. *CHI 2020*.

On **automation bias as a UI-level safety problem**: a convergent cluster of 2024–2025 empirical work establishes that overreliance is significantly modulated by interface design decisions (ordering of information, confidence display, cognitive forcing functions). The Microsoft Critical Thinking study is especially relevant: it shows knowledge workers self-reporting reduced cognitive engagement when using AI tools, implicating interface design directly in the cognitive offloading that safety researchers flag as alignment-adjacent risk.

- Lee et al. (Microsoft Research, 2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive engagement.
- "Exploring automation bias in human–AI collaboration: A review and implications for explainable AI." *AI & Society* (2025).
- "To rely or not to rely? Evaluating interventions for appropriate reliance on large language models." arXiv:2412.15584 (2024).

---

## Sociology of Professions

*This section supports the argument that differential AI adoption is not just a tooling problem — it is a jurisdictional and professional identity problem with deep theoretical roots.*

**Abbott's system of professions** is the essential theoretical frame. Abbott argues that professions are best understood not as fixed occupational groups but as competitors in an interdependent system, where "jurisdiction" — the legitimate claim to define, diagnose, and treat a class of problems — is always contestable and never permanently settled. New technologies don't simply eliminate professions; they redraw jurisdictional boundaries, creating vacancies that adjacent groups rush to occupy. When AI absorbs certain diagnostic or generative tasks, the question is not whether designers are displaced but which aspects of the work remain theirs and who else is now making a credible claim on the rest.

- Abbott, A. (1988). *The System of Professions: An Essay on the Division of Expert Labor*. University of Chicago Press.

**Braverman's deskilling thesis** holds that management systematically separates conception from execution — centralizing knowledge and judgment in processes or technologies while reducing workers to the performance of fragmented, routinized steps. The framework remains the baseline for every subsequent debate about craft identity and what is lost when tools absorb previously skilled judgment. In UX contexts, the deskilling/upskilling tension is live: generative AI tools simultaneously promise to amplify creative capacity and threaten to hollow out the tacit, judgment-heavy work that practitioners use to define professional worth.

- Braverman, H. (1974). *Labor and Monopoly Capital: The Degradation of Work in the Twentieth Century*. Monthly Review Press.

**Autor, Levy, and Murnane's task-based model** distinguishes between routine cognitive/manual tasks (codifiable, automation-substitutable) and nonroutine analytical and interpersonal tasks (complemented by technology). Applied to design work: it predicts that AI tools will absorb layout generation, pattern-matching, and basic prototyping while intensifying the premium on contextual judgment, stakeholder negotiation, and ethical framing — precisely the tasks that are hardest to codify and most central to professional identity claims.

- Autor, D. H., Levy, F., & Murnane, R. J. (2003). The skill content of recent technological change: An empirical exploration. *Quarterly Journal of Economics*, 118(4), 1279–1333.

The most current empirical entry tracks how AI implementation destabilises professional identity among knowledge workers, identifying three enacted strategies — Contesting, Compromising, and Connecting — and finding that professionals do not progressively stabilize around a revised self-understanding but oscillate between strategies. This is theorized as constitutive of early AI adoption rather than transitional — the sharpest recent evidence that jurisdictional and identity disruption is an ongoing, uneven process, not a problem being resolved.

- Ahuja, S., Pemer, F., & Mastio, E. (2026). AI and identity work: A case of AI implementation and the fragmentation of professional identity. *Information and Organization*, 36(3).

For an accessible mid-range text bridging foundational theory and current empirics, Susskind and Susskind argue that technology will "decompose" professional work into constituent tasks, many of which will be automated or commoditized, and that the parts requiring genuine human judgment will shrink rather than expand.

- Susskind, R., & Susskind, D. (2022). *The Future of the Professions: How Technology Will Transform the Work of Human Experts* (updated ed.). Oxford University Press.
