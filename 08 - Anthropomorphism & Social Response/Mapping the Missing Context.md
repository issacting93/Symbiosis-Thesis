# Mapping the Missing Context: Social Graphs as Design Probe and Data for Adaptive Support

*A Diary Study with Recently Relocated International Students*

Oct 12, 2026 · @Zac

## Position

The data we use to design for people's emotional and social lives is too thin. Surveys average a process that shifts from moment to moment (Wadley et al. 2020). Usage logs and engagement metrics record what people do but not why, so a system cannot tell relief from avoidance (Kleinberg, Mullainathan and Raghavan 2022; Milli et al. 2025). Both treat technology apart from the people it sits among. Generative interfaces inherit the same limit: an agent decides the interface from the request in front of it, with no model of the person's relationships or needs.

**We argue that a social graph the person builds and revisits, with people and technologies on the same map, can serve as both a design probe and a data tool.** Paired with a diary and reflection, it produces data that is closer to the moment, relational, and in the person's own words. That data can then give an adaptive interface the context it lacks: suggestions drawn from the person's own network rather than from what they last clicked.

Technology can either **scaffold** people's relationships, helping them reach and rebuild human ties, or **substitute** for them, standing in for the companionship it was meant to help them find. This tension runs through decades of work on displacement and stimulation (Kraut et al. 1998, 2002; Valkenburg and Peter 2007; Hall et al. 2019). We borrow "scaffolding" in its original sense of support that is meant to fall away once a skill is built (Wood, Bruner and Ross 1976), and "substitution" in the sense of practices that erode the skills they replace (Vallor 2015). People have long formed social bonds with media and machines (Horton and Wohl 1956; Reeves and Nass 1996), but AI is the first widely available technology designed to take a seat in someone's support network rather than connect them to the people in it. People now form relationships with AI companions (Skjuve et al. 2021; Brandtzaeg et al. 2022; Pentina et al. 2023), with mixed effects on loneliness and dependence (De Freitas et al.; Fang et al. 2025; Guingrich and Graziano 2025).

→ This is the vault's existing analytic core, not a new borrowing — see [[Instructional Scaffolding — Wood Bruner Ross 1976]] and [[Moral Deskilling Upskilling — Vallor 2015]] for the scaffolding/substitution pair, and [[Symbiotic Design Framework]] for the fuller bee/locust/wasp account this study specialises for one population. The parasocial and CASA citations in this paragraph already have full paper notes with DOIs — [[Parasocial Interaction — Horton Wohl 1956]], [[Media Equation — Reeves Nass 1996]], [[Computers as Social Actors — Nass 1994]] — so they can come out of the "to confirm" list at the end of this document.

→ Carried over from an earlier draft of this pitch (`DIS_Pitch.md`, now merged into this file): two sociological framings that sharpen "scaffold vs. substitute" without replacing it. Hochschild's *The Managed Heart* (1983) treats emotion regulation as social labour governed by feeling rules, so "who or what now does that work?" is the substitution question in its original sociological form. Domestication theory (Silverstone and colleagues) gives language for how a technology's role shifts as it's absorbed into someone's routines and relationships over time — relevant to how AI's position in a student's ecomap might move over the diary week, not just where it starts.

We study this through international students who have recently relocated for study. Moving countries ruptures their support network, so they are actively rebuilding it while keeping old ties alive at a distance (Diminescu 2008; Madianou and Miller 2012) and adapting to a new culture (Berry 1997), often with real loneliness along the way (Sawir et al. 2008). Infrastructure tends to become visible when it breaks down (Star 1999), and life disruptions have been shown to reveal the roles technology plays (Massimi, Dimond and Le Dantec 2012; Haimson et al. 2018). Relocation does the same for the technologies in a person's support network, making them easier to see than in a settled life.

We examine this question structurally because scaffolding and substitution are not properties of a technology but of its position among a person's ties. The same conversation with a chatbot substitutes for a person if it replaces a call home, and scaffolds if it leads to one; telling these apart requires seeing the ties around it. Usage measures and studies of the person–AI dyad cannot show this, and survey research on displacement reports averages rather than the seat a technology occupies in one person's network. A structural view also lets the map serve as both data and design probe. As data, it records where AI sits relative to human ties and how that shifts as a network is rebuilt after relocation. As a probe, it puts those positions in front of the student, prompting them to explain, question or revise them, so each position comes with the person's own account (Hogan, Carrasco and Wellman 2007; Herz, Peters and Truschkat 2015). We build on the social-work ecomap, which already places resources beside people (Hartman 1978), and on traditions that treat non-human things as part of a network (Latour 2005; Bødker and Klokmose 2012). Because a probe can change what it records, we treat students' responses to their own map as findings rather than noise. We design the ecomap app as a research-through-design artifact (Zimmerman, Forlizzi and Evenson 2007) and deploy it in a one-week diary study (Bolger, Davis and Rafaeli 2003).

## Problem

People use technology for two jobs that used to belong mostly to other people: managing how they feel, and finding and keeping relationships. The technologies doing this work pull in different directions.

| Kind of technology | Examples | Typical pull |
| --- | --- | --- |
| Connective | Messaging and calls home, event platforms (Luma, Partiful), dating apps, online communities | Toward people |
| Ambiguous | Social media, multiplayer and single-player games, streaming | Either way, depending on use |
| Companionate | AI chatbots and AI companions | Possibly away from people, by standing in for them |

AI is new in this lineup. It does not connect you to someone; it can be the someone. We do not yet know whether it takes over dynamics that used to run through connective technologies and through people, or whether it helps people reach them.

The question is hardest to see in a settled life, where networks change slowly. It is easiest to see where a network has been broken and has to be rebuilt. International students who have recently relocated for study are in exactly that position: they leave a dense support network, keep parts of it alive through technology, and must build a new one in an unfamiliar culture, often adapting how they speak, dress and socialise.

**What current data misses.** Three common sources each leave a gap a designer needs filled:

| Source | What it captures | What it misses |
| --- | --- | --- |
| Surveys and scales | How a person usually copes | The moment, the situation, and who else was involved |
| Usage logs and engagement metrics | What was opened, clicked or watched | Why, and whether it helped; relief and avoidance look the same |
| Studies of one user and one AI | How the person relates to that system | The human ties the system sits beside or stands in for |

By "better data" we mean data that is **close to the moment** (recorded the same day), **relational** (each technology placed among the people around it), and **in the person's own words** (their labels and accounts, not our categories).

## What we know

Six bodies of work frame the study. Each gives part of the picture; none puts the parts together.

**Digital emotion regulation.** People deliberately combine apps and devices to manage everyday emotions, and a large share of phone use may serve this purpose (Wadley et al. 2020; Smith et al., CHI 2022). Regulation research also finds no strategy is good or bad in itself: healthy regulation is a varied, flexible repertoire (Bonanno and Burton), and much of it happens through other people (Zaki and Williams).

**Displacement versus stimulation.** A forty-year debate asks whether technology displaces richer relationships (Kraut et al. 1998) or strengthens them (Valkenburg and Peter). Later work found the early displacement effects faded (Kraut et al. 2002) and that social media rarely displaces face-to-face time (Hall et al. 2019), while deactivation experiments show small gains in offline time and wellbeing (Allcott et al. 2020). The consistent lesson: effects are small on average and depend on who uses technology and why. Scaffold versus substitute is this debate, applied to individuals.

**AI and relationships.** AI companions reduce loneliness in the moment, about as much as talking to a person (De Freitas et al.). Longer randomised studies find no average effect of chatbot use on loneliness or socialising, but heavier voluntary use goes with more loneliness and dependence (Fang et al. 2025), and people who want more connection anthropomorphise chatbots more and report bigger effects on their human relationships (Guingrich and Graziano 2025). These studies examine the person–AI dyad in isolation from the rest of the person's network.

→ The vault's [[Social AI & Companionship]] theme already has paper notes this paragraph doesn't draw on: [[Companion AI Impacts — Malfacini 2025]] (systematic review of risks and benefits), [[Rise of AI Companions — Zhang 2026]] (longitudinal wellbeing data), [[AI Companion Addiction — Agarwal 2026]] ("frictionless love" and dependency), and [[Companion-Assistant Dynamics — Manoli 2025]]. Closest of all is [[Companionship to Mediationship — Wang 2025]], which names in a caregiving context exactly the distinction this study is probing — AI as companion (dyad-focused) versus AI as mediator (bridging human ties) — and is worth citing directly rather than re-deriving the same distinction from scratch.

**International students.** Research on international and transnational students, mostly survey-based in communication and psychology, documents the same tension: social media relieves homesickness by keeping home ties alive, while heavy reliance on it can go with fewer host-country ties. A CHI 2020 extended abstract found international graduate students preferred technology for informational support but wanted emotional support in person. (Exact references to confirm.)

**Mapping networks as method.** Sociology and social work have long used participant-drawn network maps as both data and interview prompt: participant-aided sociograms (Hogan et al. 2007), qualitative structural analysis (Herz et al. 2015), and egocentric maps with international students' support networks (Altissimo 2016). Social work's ecomap (Hartman 1978) already places institutions and resources beside people. Maps prompt stories and reveal gaps, but can feel exposing (Ryan et al. 2014).

→ This paragraph cites the qualitative sociogram tradition but not the vault's existing social-network-analysis grounding: [[Strength of Weak Ties — Granovetter 1973]] and [[Structural Holes — Burt 1992]] for why *which* tie gets displaced matters, and [[Social Network Analysis — Wasserman Faust 1994]] / [[Egocentric and Sociocentric Measures — Marsden 2002]] for the ego-network method itself. [[Relational Mapping Methods]] already works out a fuller protocol for this exact kind of map, including a finding that answers an open design question for the app: Ehlers et al. (2024) found layered node-link diagrams outperform radial layouts and adjacency matrices for ego-network legibility — directly relevant to how the ecomap should actually render people, technologies, and distance-from-centre.

→ One more method precedent, carried over from the merged `DIS_Pitch.md`: Hoefer & Voida (DIS 2023) ran a one-week probe followed by a think-aloud session over the participant's own collected data — structurally close to this study's diary week + exit interview walking back through the student's own ecomap. Worth citing alongside Hogan, Carrasco & Wellman 2007 as a design-venue precedent for the method, not just a sociology one.

**Engagement metrics and generative interfaces.** Platforms adapt to what people click, watch and share. Kleinberg, Mullainathan and Raghavan (2022) show that engagement can diverge from what users actually want, so optimising it misreads them. On Twitter, engagement-ranked content left users feeling worse than content they said they valued (Milli et al. 2025). Generative UI now lets an agent build the interface itself (Google Research 2025; Cao, Jiang and Xia 2025), but these systems adapt to the current request, not to a model of the person's life or relationships.

## The gap

No work we found places AI and other technologies on the same map as the people someone relies on, and asks where they sit and how that changes. Each strand stops short:

- Network maps treat people as the nodes; the ecomap admits institutions but not technologies or AI.
- AI-companion studies examine the person–AI dyad, not the AI's position among human ties.
- Displacement research measures average effects at scale and cannot show what substitution looks like inside one person's network.
- International-student research is largely survey-based and outside design venues, and does not consider AI.
- Adaptive and generative interfaces learn from clicks or the current request, with no model of the person's support network to draw on.

The claim we can defend is therefore narrow and specific: **not** that people use AI for emotion regulation (already established), but that placing AI inside a person's whole support map shows whether it is bridging them toward people or taking a seat a person could have filled.

## Research questions

Each question asks one thing, matches a kind of evidence the study produces, and leaves open whether substitution happens.

| RQ | Type | Question | Answered by |
| --- | --- | --- | --- |
| RQ1 | Structural | When recently relocated international students place people and technologies on the same ecomap, where does AI sit relative to their human ties? | Baseline and end-of-week ecomaps |
| RQ2 | Processual | How do students account for the roles technologies play as they maintain distant ties and build local ones? | Intake and exit interviews, voice notes |
| RQ3 | Conditional | Under what conditions do students experience a technology as bridging them toward people rather than standing in for them? | Variation across participants and across days of the diary week |
| RQ4 | Design (pilot) | When an agent offers suggestions drawn from a student's own graph, which do students take up, and do they turn toward people or toward activities on their own? | Suggestion log, what students did next, exit interview |

RQ3 can only be answered if the data contains variation. The daily check-in therefore pairs mood with the people and technologies used that day, so harder and easier days can be compared, alongside differences between participants. The study does not claim to measure long-term change in reliance; the longer arc comes from what students recount in the interviews.

## Approach

A research-through-design study: we design an ecomap app and deploy it in a one-week diary study with up to 12 international students at a US university who have recently relocated for study (window to confirm, e.g. within the past 12 months).

**The ecomap app.** The student sits at the centre. People and technologies are both nodes on the same map. Edges are typed to describe the relationship, for example whether a tie scaffolds, substitutes for, or augments other ties. Distance from the centre shows closeness. The map is the research instrument and also the design artifact under study.

*Open design question, carried over from the merged `DIS_Pitch.md`:* should the map the student sees be precise (weighted edges, exact distances) or deliberately ambiguous? Affective Diary (Lindström et al.) made the opposite choice on purpose — ambiguous visual representations that invite the participant's own interpretation rather than a precise read-out. A precise map is easier to code consistently; an ambiguous one may elicit richer reflection and avoid the map feeling like a score. Not yet resolved — worth deciding before the app is built, not after.

**Study arc**

1. **Intake interview (remote).** Briefing, then the student's story of leaving home and rebuilding. Together we build the baseline ecomap.
2. **Diary week (7 days).** A daily check-in of about two minutes: which technologies they used, which people they remember interacting with, and a quick mood rating. Each check-in updates the map. An optional voice-note button lets students record a moment in their own words whenever it feels worth capturing.
3. **Exit interview (remote).** We walk back through how the map changed across the week and connect it to the longer story of the move.

**Analysis.** Map and narrative are analysed together, following qualitative structural analysis. Interviews and voice notes are coded inductively, with scaffolding, substitution and augmentation, drawn from the displacement–stimulation debate, as declared sensitising concepts. Daily check-ins are summarised descriptively, never as outcome metrics.

**What counts as evidence.** Codes are applied to ties, using these working definitions:

- **Scaffolding:** a tie through which the student reaches, maintains or builds a human tie ("I used Luma to find the event where I met them").
- **Substitution:** a tie the student uses in place of a human contact they say they would otherwise have reached ("I talked to the chatbot instead of calling home").
- **Augmentation:** a tie that adds to a human tie without replacing it or leading to it.

**Pilot: graph-informed suggestions (RQ4).** The graph also feeds an adaptive interface. When a student reports how they feel (for example "overwhelmed", "numb" or "just scrolling"), an agent offers suggestion cards of two kinds:

- **On your own:** a breathing exercise, a stretch, a short workout, a walk, or a brief meditation.
- **With people:** drawn from the student's own map, such as messaging a named friend, calling home, or going to a place they added.

We compare suggestions drawn from the graph with generic suggestions and with no suggestion, and record what the student did next. Mixing solo and social options shows when students turn to people and when they turn to themselves, which links the pilot back to scaffolding and substitution.

States are self-reported in this pilot. The agent does not infer states such as dissociation or overwhelm; passive detection is clinical territory and out of scope. Still to decide: whether the agent offers one suggestion or a small choice of two, and whether the pilot runs in the second half of the diary week or as a follow-on study.

## Contributions and scope

**Contributions**

1. **A research instrument (method contribution):** an ecomap that places technologies, including AI, beside people as nodes with typed relationships, serving both as data and as a design probe. This contribution comes from building and deploying the app, independent of how the research questions are answered.
2. **Empirical account (RQ1, RQ2):** where AI and other technologies sit in recently relocated students' support networks, and how students explain the roles those technologies play.
3. **Design knowledge (RQ3):** the conditions under which technology bridges people toward others rather than standing in for them, and a pilot of graph-informed suggestions (RQ4) showing how relational data can give generative interfaces the context they lack.

**Scope and limits**

- The study captures how students experience and describe scaffolding and substitution; it does not measure whether regulation skills or relationships grow or decline. The pilot relies on self-reported states and makes no clinical inferences.
- One week shows short-term movement; the longer arc relies on retrospective accounts in the interviews.
- A single group of recently relocated students, with no domestic comparison. A comparison would confound relocation with cultural background, so we leave it out deliberately.
- Up to 12 participants, expecting 8–10 complete datasets after attrition.

## Venue and timeline

Primary target is DIS 2027 papers (abstract 11 January, paper 18 January 2027), under the Research through Design subcommittee with Design Methods and Processes as second choice. If the timeline slips, the fallback is CHI 2028 (deadline expected around September 2027, to confirm).

&#91;embedded content: proposed plan · November 2026 to January 2027\]

Many international students travel home over winter break, which would interrupt the relocation context the study depends on. The diary week therefore has to finish by about 20 December, which means IRB approval by early December and an app ready to pilot before then.

**Timeline** (carried over and adapted from the merged `DIS_Pitch.md`):

| When | Milestone |
| --- | --- |
| Mid-Oct 2026 | Agree scope with advisor; draft ethics application |
| Late Oct – Nov 2026 | Ethics approval; pilot the intake interview and ecomap on 2–3 people |
| Nov – ~20 Dec 2026 | Run the diary week and exit interviews (up to 12 participants) |
| Dec 2026 | Analyse |
| 11 Jan 2027 | Abstract due |
| 18 Jan 2027 | Full paper due |

Ethics approval is the main schedule risk. If it slips past early December, the diary week can't finish before winter break — the fallback is CHI 2028 (deadline expected ~September 2027, to confirm) with a longer probe.

## Connections to the vault

This pitch is a focused instance of a larger research programme already built out elsewhere in the vault, not a standalone idea. Reading it alongside that material changes what still needs inventing versus what can simply be reused.

**It has a sibling proposal with the same architecture.** [[Research Proposal — Social Dynamics of AI]] proposes the same core instrument — people and AI as nodes on one ego network, diary plus interview, scaffolding versus substitution as the individual-level test — for a broader population (learners, peer collaborators, independent knowledge workers) rather than recently relocated international students specifically. It is more fully grounded: it already cites [[Strength of Weak Ties — Granovetter 1973]], [[Structural Holes — Burt 1992]], [[Social Network Analysis — Wasserman Faust 1994]], [[Relational Models Theory — Fiske 1992]], [[Communal and Exchange Relationships — Clark Mills 1979]], [[Interaction Ritual Chains — Collins 2004]], [[Presentation of Self — Goffman 1959]], [[Longitudinal Qualitative Research — Saldaña 2003]], [[Interpretative Phenomenological Analysis — Smith Flowers Larkin 2009]], and [[Construct Validity — Cronbach Meehl 1955]] for the exact method moves this pitch still has to justify from scratch (diary design, interview coding, validity across triangulated measures). This DIS pitch should either cite the proposal directly as the broader framework it specialises, or pull in its missing citations wholesale rather than re-deriving them under deadline pressure.

**The coding scheme can borrow a sharper vocabulary.** "Scaffolding / substitution / augmentation" is a workable three-way code, but the vault already has two more precise alternatives built for the identical problem: [[Relational Models Theory — Fiske 1992]] (four relational models — Communal Sharing, Authority Ranking, Equality Matching, Market Pricing — with the parasitism signature being specifically Communal Sharing *signalled* over Market Pricing *operated*) and [[Communal and Exchange Relationships — Clark Mills 1979]] (the simpler two-category version of the same distinction). [[Codex Relatio — Aragón 2026]] goes further, scoring each edge across five axes (Persuasion, Consent, Intimacy, Affection, Responsibility) instead of a single label — worth having in reserve if a reviewer asks for more granularity than three mutually exclusive codes.

**Macro framing is available if the paper needs to justify why this matters beyond one diary week.** [[Bowling Alone — Putnam 2000]] gives the social-capital stakes at population scale; [[Strength of Weak Ties — Granovetter 1973]] narrows it to the specific claim that weak, peripheral ties — exactly the ones international students are rebuilding — are both the most socially valuable and the easiest for AI to quietly absorb.

**What's lost has a name.** [[Interaction Ritual Chains — Collins 2004]] names the mechanism directly: co-presence generates emotional energy that informational equivalence cannot replicate. That is why "the same conversation" with a chatbot and a phone call home are not interchangeable even when the content matches — the point the Position section makes informally without yet citing the theory that makes it precise.

**Genuinely missing from the vault — worth proper paper notes if this pitch firms up.** These are load-bearing in the draft but have no corresponding note in `05 - References & Reading/Papers/`: Wadley et al. 2020 and Smith et al. 2022 (the core digital-emotion-regulation lineage this paper extends — its closest precedent), Hogan, Carrasco & Wellman 2007 (participant-aided sociograms — the direct method precedent), Hartman 1978 (the ecomap itself), Zimmerman, Forlizzi & Evenson 2007 (the foundational research-through-design citation — [[Research-through-Design GenAI — Benjamin 2024]] is the vault's closest existing RtD note but doesn't substitute for it), De Freitas et al., Fang et al. 2025, and Guingrich & Graziano 2025 (the three AI-companion studies the draft leans on most heavily), and Berry 1997 / Diminescu 2008 / Madianou and Miller 2012 (the acculturation and transnationalism literature specific to the international-student framing, which nothing else in the vault covers).

→ See also [[Position Paper — Designing for Symbiosis]] and [[Ecological Methods]] for the wider argument and method set this pitch sits inside, and [[The Metrics Problem]] for the engagement-metrics critique this document's "What current data misses" table restates in its own terms.

## Sources

Opened during research:

- [DIS 2027 call for papers](https://dis.acm.org/2027/call-for-papers/) and [subcommittees](https://dis.acm.org/2027/selecting-a-subcommittee/)
- [Wadley et al., Digital Emotion Regulation (2020)](https://findanexpert.unimelb.edu.au/scholarlywork/1440648-digital%20emotion%20regulation)
- [Smith et al., Digital Emotion Regulation in Everyday Life (CHI 2022)](https://findanexpert.unimelb.edu.au/scholarlywork/1677372-digital-emotion-regulation-in-everyday-life)
- [De Freitas et al., AI Companions Reduce Loneliness](https://commbox.org/document/ai-companions-reduce-loneliness)
- [Fang et al., Psychosocial Effects of Chatbot Use (2025)](https://arxiv.org/abs/2503.17473v1)
- [Guingrich & Graziano, Longitudinal RCT of Companion Chatbot Use (2025)](https://arxiv.org/abs/2509.19515v1)
- [Ryan, Mulholland & Agoston, Talking Ties (2014)](https://www.socresonline.org.uk/19/2/16.html)
- [Altissimo, Combining Egocentric Network Maps and Narratives (2016)](https://socresonline.org.uk/21/2/14.html)
- [Herz, Peters & Truschkat, Qualitative Structural Analysis (2015)](https://www.qualitative-research.net/index.php/fqs/article/view/2092)
- [Hogan et al., participant-aided sociograms and netCanvas](https://pmc.ncbi.nlm.nih.gov/articles/PMC5176260)
- [Rind & Boeck, Visual Tools for Input and Reflection in Social Work](https://arxiv.org/html/2509.20307v1)

Added for the data and generative-interface argument:

- [Kleinberg, Mullainathan & Raghavan, The Challenge of Understanding What Users Want (2022)](https://arxiv.org/abs/2202.11776v1)
- [Milli et al., Engagement, User Satisfaction, and the Amplification of Divisive Content on Social Media (PNAS Nexus 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11894805/)
- [Google Research, Generative UI (2025)](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)
- [Cao, Jiang & Xia, Generative and Malleable User Interfaces (CHI 2025)](https://dl.acm.org/doi/10.1145/3706598.3713285)

**Confirmed via the vault** (full paper notes with DOIs — see Connections to the vault above): [[Instructional Scaffolding — Wood Bruner Ross 1976]], [[Moral Deskilling Upskilling — Vallor 2015]], [[Parasocial Interaction — Horton Wohl 1956]], [[Media Equation — Reeves Nass 1996]], [[Diary Methods — Bolger Davis Rafaeli 2003]]. Kraut et al. 1998 is confirmed as [[Internet Paradox — Kraut et al 1998]]; the 2002 follow-up is not separately noted and stays in the unconfirmed list below.

Still cited from memory, references to confirm: Berry 1997; Bonanno and Burton; Brandtzaeg et al. 2022; Bødker and Klokmose 2012; Diminescu 2008; Haimson et al. 2018; Hall et al. 2019; Hartman 1978; Kraut et al. 2002 (follow-up); Latour 2005; Madianou and Miller 2012; Massimi, Dimond and Le Dantec 2012; Pentina et al. 2023; Sawir et al. 2008; Skjuve et al. 2021; Star 1999; Valkenburg and Peter 2007; Zaki and Williams; Zimmerman, Forlizzi and Evenson 2007; the CHI 2020 extended abstract on international graduate students; survey studies of international students' social media use; Hochschild, *The Managed Heart* (1983); domestication theory (Silverstone and colleagues); Hoefer & Voida (DIS 2023); Lindström et al., *Affective Diary* — all four carried over from the merged `DIS_Pitch.md` and not yet verified.
