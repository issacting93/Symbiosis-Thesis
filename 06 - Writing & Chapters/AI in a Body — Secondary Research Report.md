# AI in a Body: Embodiment, Nonverbal Interaction, and the Future of Human-AI Communication

*Secondary Research Report — Symbiosis Pre-Thesis Project*

## RQ1: What are the different ways people are using AI today? 
## RQ2 : How has adopting this form of AI changed the way we interact with technology?
RQ2: How does the embodiment type affect user trust, rapport, and willingness to comply?   
---
---

## 1. Introduction

Almost all human-AI interaction today happens through text. Even voice input is typically transcribed before the model processes it. This is not a technical constraint. It is a design choice that was made early and has been rarely questioned since. The result is that we communicate with AI in a register unlike any we use with other people.

When a person explains an idea to a colleague, they point, sketch, demonstrate, lean forward, raise an eyebrow. Goffman's (1959) account of social interaction establishes that bodily performance — the management of gesture, expression, and physical presence — is not supplementary to meaning; it is constitutive of it. Stivers (2008) shows that even a nod is a full communicative act, one that conveys affiliation, stance, and understanding simultaneously. These channels carry meaning that resists translation into words: the moment of recognition in someone's face when an idea lands, the hesitation in a gesture that signals doubt, the shared glance that replaces an explanation.

The interface has remained text-bound while the *presentation* layer has shifted. In 2025 and 2026, major AI companies began introducing visual social presences for their systems: Meta launched MUSE AI as a soft, friendly character [citation needed]; xAI introduced “Grok Bots” [citation needed]; OpenAI launched “dots” [citation needed] — each form simple and designed to appear approachable. These products reflect a deliberate strategy. When an entity has human-like visual features — a face, an expression, a consistent character — people respond to it as a social agent regardless of its underlying nature, a tendency Nass, Steuer, and Tauber (1994) documented as the Computers Are Social Actors (CASA) paradigm. AI companies are activating this tendency to build engagement: avatars that initiate interaction sustain use more effectively than passive interfaces. But anthropomorphism carries consequences beyond the designed interaction. AI companions have been positioned as substitutes for human confidants, romantic partners, and therapists (Agarwal, 2026; Zhang & Yu, 2026), a social claim that existing evaluation frameworks are not equipped to assess. The visual form has become more elaborate; the nonverbal input gap has not narrowed.

This research is about that gap. Specifically, it asks: what changes when AI can receive and respond to nonverbal communication — gesture, expression, sketch, bodily presence — rather than text alone? And what does giving AI a physical body make possible that a screen cannot?

This report synthesizes what the existing literature has established, identifies what it has not, and derives the insights that motivate the primary research phase.

---

## 2. A Taxonomy of AI Embodiment

Before examining the literature, it is useful to define the object of study. "Embodied AI" is not a single form — it encompasses a wide range of physical and virtual configurations, each with distinct interaction affordances.

| Embodiment Type | Description | Dominant Interaction Modality |
|---|---|---|
| **Virtual Embodied AI** | AI with a virtual body in digital or VR environments, often human-like in appearance and animation. | Text, speech, gesture in VR; haptics can add tactile feedback. |
| **Humanoid Robots** | Robots shaped like humans, deployed in care, service, education, and research contexts. | Speech, physical proximity, gesture, gaze, and movement. |
| **Zoomorphic and Mechanical Robots** | Non-human robotic forms — robot dogs, robotic arms, expressive mechanical devices, soft AI objects. | Command, physical interaction, emotional cuing through movement and texture. |
| **Cyber-Physical Systems and Swarms** | Multiple AI agents coordinating across digital and physical spaces; no single body. | Language, shared goals, ambient signal; users relate to the system collectively rather than individually. |

These four types are not equally studied. Humanoid HRI has the deepest literature. Virtual embodiment is growing rapidly through digital twins and avatar systems. Zoomorphic and soft-bodied AI is an emerging area. Swarms are primarily studied in technical and military research contexts, less so in HCI. This unevenness matters: the forms most likely to enter domestic and workplace contexts in the near term are among the least studied from a human experience standpoint.

---

## 3. Background Research

### 3.1 Social Response Is a Human Default

The most important finding in this body of literature is the oldest: humans apply social rules to computers automatically, regardless of whether they know the machine is not a person. This is the CASA (Computers Are Social Actors) paradigm established by Nass, Steuer, and Tauber (1994), extended empirically in *The Media Equation* (Reeves & Nass, 1996), and theorised in *Machines and Mindlessness* (Nass & Moon, 2000).

What CASA showed is not that people are confused about what computers are. Participants in these studies knew perfectly well they were interacting with machines. They applied social rules anyway — responding to flattery, attributing gender, extending politeness, expressing loyalty. The response was not reasoned. It was automatic. Nass & Moon (2000) describe it as "mindless": social scripts activate below the threshold of deliberate cognition, triggered by minimal cues — a voice, a name, a conversational pattern.

The implication for embodiment research is immediate. If a minimal cue — a text prompt with a consistent "voice" — is sufficient to activate social response, then a physical body, a face, a gesture, will activate it far more powerfully. The strength of the effect scales with the richness of the social signal. Embodiment is not just an interface design choice; it is a decision about how strongly to trigger the social response circuitry that humans bring to every interaction.

### 3.2 The Genealogy: From ELIZA to the Current Moment

The CASA paradigm did not emerge in a vacuum. Its intellectual origin is ELIZA, Joseph Weizenbaum's 1966 pattern-matching program designed to simulate a Rogerian therapist. ELIZA had no intelligence in any meaningful sense — it reflected users' words back at them using simple substitution rules. Weizenbaum was startled to discover that users formed genuine emotional attachments to it. Some asked to be alone with the program. His secretary asked him to leave the room. He published his account as a warning (*Computer Power and Human Reason*, 1976): the "ELIZA effect" showed that emotional engagement could be triggered by the appearance of understanding, in the complete absence of understanding itself.

Thirty years later, Microsoft's Clippy took the "logical" next step — deliberately anthropomorphizing a productivity assistant, drawing directly on CASA findings. The result was the canonical failure case of anthropomorphic AI design. Clippy's error was not that it had a personality. It was that it made a relational promise — a friendly, approachable companion — that its functional capability could not fulfil. The mismatch between the emotional signal and the actual experience produced active hostility. Users did not simply stop using Clippy; they resented it. The lesson: anthropomorphic design commits the designer to a relational contract. If the system cannot deliver on that contract, the failure is experienced as a betrayal.

The current moment revisits this at scale. Companion AI products — Replika, Character AI, and their successors — have built entire product categories on the ELIZA-to-CASA logic. Zhang & Yu (2026) document empirically that perceived anthropomorphism significantly predicts emotional attachment and sustained use of AI companions. Agarwal (2026) theorises this as "frictionless love": AI companions eliminate the friction of human relationships while simulating their emotional warmth, creating the conditions for behavioral addiction. The mechanism is the same one Weizenbaum identified in 1966. The scale is incomparably larger.

### 3.3 Embodiment Shapes the Relationship: Evidence from Human-Robot Interaction

Kate Darling's work provides the clearest experimental evidence of how embodiment — and framing — alters users' relationships with AI. In a series of studies (Darling, 2015a; 2015b), participants who were given a backstory for a simple robotic toy — "his name is Frank, he has been on a long journey" — showed measurably greater reluctance to harm it than those given no narrative. The robot was identical. The name and story changed the moral calculus. This is the embodied extension of the ELIZA effect: physical presence plus narrative framing is sufficient to shift how users reason about and relate to a machine.

Mollen et al. (2023) extend this finding into naturalistic settings. Their study of a robot living in shared domestic space found that cohabitation itself — the fact of sharing physical environment over time — significantly increased bonding. Familiarity, proximity, and the incidental social cues of physical presence built a relationship that was not designed for or expected. The robot was not particularly capable. Its presence was enough.

These findings establish an embodiment dividend: physical form generates social response that virtual or text-based interfaces cannot replicate at the same intensity. But the evidence also documents the cost. Manoli (2025) shows that users construct idealised mental models of AI companions — "she's like a person but better" — that position the AI as superior to human relationships in exactly the domains where human relationships are most developmentally important. Embodiment amplifies the social response; it also amplifies the risk that the relationship displaces rather than augments human connection.

The literature on zoomorphic and soft-form AI is thinner but directionally consistent. Han (2026) documents users' interaction with an AI pillow designed for emotion regulation — "tendling," a form of care-giving interaction with a soft robotic object. Song (2026) examines a robotic co-creator for children's storytelling. Both suggest that non-humanoid embodiment opens interaction registers that are unavailable in screen-based interfaces: touch, physical manipulation, presence without the uncanny valley effects of humanoid design.

### 3.4 The Nonverbal Dimension: What Gets Lost — and What Context Determines

The gap at the centre of this research is between how humans naturally communicate and what AI currently can receive. Goffman (1959) showed that social interaction is a performance sustained through bodily management — posture, expression, gesture, gaze — and that this performance is not decorative but essential to what communication is. Stivers (2008) shows this in the granularity of a nod: a single head movement can function as affiliation, acknowledgement, or encouragement, with distinct sequential consequences in conversation.

Current AI interfaces receive none of this. A user who is confused does not convey confusion to the AI through their posture or expression. A user who is struggling with a concept cannot show the AI what they mean by sketching it. Every piece of meaning that would normally travel through a nonverbal channel must be either translated into text or abandoned. This translation is never lossless.

Expert consultation with Kevin Chow, a PhD researcher who developed a computer vision system for tracking nonverbal cues in real work video meetings, sharpened the research question considerably (Chow, personal communication, September 2026). His team tracked observable cues — smiling frequency, nodding rate, posture — rather than inferring emotions, on the grounds that a cue is a measurable observable while an emotional state is an interpretation layered on top, one that varies across individuals and cultures. A smile is not the same thing as happiness. The distinction is methodologically important: emotion recognition carries significant cultural bias, and AI systems trained on internet-scale data risk encoding stereotyped mappings (Western contexts equated with expressiveness; Eastern contexts with restraint) as defaults. Chow's system reported cues neutrally — "you haven't smiled in the last two minutes" — rather than prescribing behaviour. The framing is informational, not directive.

The most counterintuitive finding from this research is that participants often did not want to optimize their nonverbal presentation. In familiar, close-colleague meetings, appearing tired, slouching, or visibly struggling was experienced as appropriate and authentic. An imperfect nonverbal cue carried real social information: a tired look on a Monday morning could prompt a colleague to ask whether everything was all right. Chow described this as "the imperfection is what makes it human." The finding reverses a naive assumption: that AI reading nonverbal cues more accurately will necessarily improve interaction. In intimate contexts, reducing nonverbal imperfection is not an improvement; it is a loss. High-stakes, formal settings — presentations, job interviews, teaching — were different. There, participants found feedback on their nonverbal cues genuinely useful. The formal/informal axis determines whether monitoring nonverbal signals is a tool or surveillance.

Chow also identified a largely unaddressed channel: paralanguage — the non-word aspects of voice that carry meaning: tone, emotional quality, pitch, speaking rate, pauses, and silences. This is distinct from language content and from visual gesture. It is currently unclear whether voice-based AI systems capture paralinguistic information or simply convert speech to text and discard it. If the latter, voice interaction with AI is more truncated than it appears — not speech, but transcribed speech with prosody stripped out.

The research gap is therefore not just about adding input channels. Frauenberger (2020) calls for a "more-than-human" approach to HCI that takes seriously the embodied, relational, and environmental dimensions of interaction. La Delfa (2024) develops somaesthetics as a method for studying the bodily felt dimension of human-machine relations. Both mark the same gap: the question is not only what channels AI can receive, but in what contexts making those channels legible to technology serves the person rather than surveilling them.

### 3.5 Trust, Mental Models, and the Agency Perception Problem

How users represent AI capability to themselves — their mental model of the system — is foundational to everything that follows: what they ask of it, how they interpret its failures, whether they recover after an error. Nass & Moon (2000) showed that mental models of AI are shaped less by accurate technical knowledge than by social scripts triggered in interaction. Users do not understand what an LLM is. They form an impression of it from conversational cues.

Embodiment form reliably shapes the mental model. Research on how users describe AI systems shows a consistent pattern: users describe virtual agents as "helpers" or "assistants," humanoid robots as "colleagues" or "friends," zoomorphic robots as "pets" or "tools." The label is not neutral — it carries expectations about capability, reliability, and what kind of failure constitutes a betrayal. A "colleague" who repeatedly gets things wrong is experienced differently from a "tool" with the same error rate.

This asymmetry between the mental model and actual system capability is the source of two failure modes that the trust literature documents in detail. Buçinca et al. (2021) demonstrate overreliance: users trust AI outputs beyond the system's actual reliability, especially when the interface presents outputs confidently. Cheng et al. (2026) document sycophancy as the structural driver of this: AI systems that agree with users regardless of accuracy measurably reduce users' prosocial intentions and promote dependence. The sycophantic system is not failing to deliver on its relational promise — it is delivering on it perfectly, while eroding the user's capacity for independent judgment. This is what Vallor (2015) calls moral deskilling: technology eroding not just technical skill but the moral and cognitive capacities that practice develops.

### 3.6 Cognitive and Linguistic Effects

The literature on cognitive and linguistic effects of AI interaction has expanded sharply in recent years, and the findings are consequential for the nonverbal interaction question. Blevins et al. (2026) and Chen et al. (2026) document bidirectional linguistic accommodation between humans and LLMs: users adapt their language toward AI style through repeated interaction. This is not a trivial finding. It means that the interaction modality is not simply a conduit for communication — it is an environment that shapes how users think and express themselves. Sustained text-based AI interaction is leaving a trace on how people write and speak.

Lee et al. (2025) add a more troubling dimension: self-reported reductions in critical engagement among knowledge workers who use generative AI tools regularly. Users describe doing less thinking, reaching for AI before attempting to reason through problems independently. Ferdman (2026) frames this as a structural outcome of AI adoption in knowledge work — deskilling not as individual choice but as a systemic effect of tool design. The AI is not making people less capable by accident. It is designed to be the easier option.

Taken together, these findings establish that the interface modality has cognitive consequences. Text-based AI interaction involves specific cognitive costs (the translation cost of putting every thought into words) and produces specific cognitive effects (reduced critical engagement, linguistic convergence). A different modality — one that can receive gesture, sketch, and expression — would involve different costs and produce different effects. What those effects would be is precisely what the primary research phase is designed to investigate.

---

## 4. Insights Derived from Secondary Research

The following insights are not merely summaries of the literature. They are the propositions that the secondary research has warranted — claims that are supported by the evidence, that have implications for design, and that open specific questions for primary research.

**Insight 1: Anthropomorphism is not a design choice — it is a human default that design either amplifies or suppresses.**
The CASA paradigm establishes that social response to AI is automatic and mindless. Designers cannot choose whether users will anthropomorphize an AI; they can only choose how strongly to trigger that tendency. This shifts the ethical question. The question is not "should we make AI seem human?" but "what kind of relationship are we committing the user to, and can the system fulfil it?" Clippy is the failure case. The risk of high-anthropomorphism design without matching capability is active user hostility, not indifference.

**Insight 2: Embodiment form determines the relationship metaphor, and the metaphor determines expectations.**
Users do not form neutral mental models of AI. They reach for familiar social categories — tool, pet, colleague, companion — and those categories carry built-in expectations about capability, reciprocity, and failure tolerance. The form AI takes (virtual, humanoid, zoomorphic, swarm) strongly predicts which category is activated. This means that embodiment is not merely an aesthetic decision; it is a decision about what relational promises the system is making.

**Insight 3: The nonverbal gap is structural, not incidental.**
The dominance of text-based AI interaction is not a transitional state waiting to be overtaken by better technology. It reflects a design assumption — that communication with AI should be explicit, discrete, and recordable — that is incompatible with how humans naturally carry meaning. Closing the nonverbal gap requires not just adding input channels but rethinking what "understanding" means for an AI system. A system that detects a sketch but processes it as a text description has not closed the gap.

**Insight 4: The translation cost of text is real and routinely overlooked.**
Every thought that enters a text-based AI through a keypad has already been filtered, formalized, and partially changed by the act of translation. Ideas that exist as gestures, spatial arrangements, or visual impressions must be rendered into propositions before the AI can receive them. This is not just an efficiency cost — it is a cognitive intervention. Research on cognitive offloading (Kirsh) and linguistic convergence (Blevins, 2026) suggests that sustained text-based AI interaction reshapes how users formulate thoughts, even outside of AI interaction.

**Insight 5: Bidirectional accommodation means the interaction modality changes the person, not just the task.**
The finding that linguistic convergence goes both ways (Blevins, 2026; Chen, 2026) has a design implication that has not yet been fully absorbed. The modality through which users interact with AI is not neutral. A tool users interact with predominantly through text will push their thinking toward textual formulation. A tool users interact with through gesture and sketch would presumably push differently. The interaction modality is an environment, not just a channel.

**Insight 6: Parasitism is a structurally produced outcome of current design defaults, not an edge case.**
The consistent empirical direction of recent work — sycophancy reducing critical judgment (Cheng, 2026), companion AI producing behavioral addiction (Agarwal, 2026), GenAI reducing critical engagement (Lee, 2025), deskilling as a structural outcome (Ferdman, 2026) — is not coincidental. These systems are designed to be used. The defaults that make them easiest to use (frictionless, agreeable, always available) are precisely the defaults that produce dependence over time. Symbiotic design requires actively designing against these defaults, not merely avoiding the most egregious cases.

**Insight 7: Cues are not emotions — and conflating them is a design risk, not just a technical limitation.**
Emotion recognition assumes a reliable mapping from observable signals to internal states. That mapping does not exist consistently across individuals or cultures. A furrowed brow signals concentration in one person and distress in another; the same expression carries different social meaning in different cultural contexts. AI systems trained on internet-scale data risk encoding these mappings as stereotypes and applying them as defaults. The appropriate design response — tracking and reporting cues without asserting what they mean — is a principle, not a concession to technical limitation. It preserves the user's interpretive authority over their own signals (Chow, personal communication, September 2026).

**Insight 8: Nonverbal AI is most valuable in formal contexts and potentially counterproductive in intimate ones.**
The instinct behind this research is that more nonverbal understanding produces better interaction. Expert consultation and existing literature on technology-mediated communication suggest this is wrong as a general claim. In close, familiar relationships, imperfect nonverbal cues carry authentic social information. A tired appearance invites care; monitored tiredness invites correction. The formal/informal axis is not incidental context — it determines whether making nonverbal signals legible to technology is a tool or a form of surveillance. Any primary research design must treat context as a primary variable, not a control.

**Insight 9: The literature has established the risks clearly. What it has not yet established is what a mutualistic human-AI interaction looks like.**
The secondary research provides a rich account of what goes wrong: ELIZA effects, CASA-triggered over-anthropomorphism, deskilling, sycophancy, linguistic accommodation, companion addiction. It provides much less on what goes right — on what the interaction looks like when it builds rather than depletes human capacity. This is the gap that the primary research is designed to enter.

---

## References

Abbott, A. (1988). *The System of Professions: An Essay on the Division of Expert Labor*. University of Chicago Press.

Agarwal, S. (2026). Frictionless love: AI companion roles and behavioral addiction. *[Journal pending]*.

Albrecht, C., et al. (2025). Future You: Designing and evaluating multimodal AI-generated digital twins for strengthening future self-continuity. arXiv:2512.06106.

Afroogh, S., et al. (2026). Task-driven human-AI collaboration: When to automate, collaborate, or challenge. *[Journal pending]*.

Blevins, J., et al. (2026). Linguistic convergence between humans and LLMs. *[Journal pending]*.

Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW1), 1–21.

Chen, G., et al. (2026). Bidirectional linguistic accommodation in human-AI conversation. *[Journal pending]*.

Chow, K. (2026). Expert interview on nonverbal cues in AI-mediated communication. Personal communication, September 25, 2026.

Cheng, Y., et al. (2026). Sycophantic AI, prosocial intentions, and behavioral dependence. *[Journal pending]*.

Cox, A. L., et al. (2016). Design frictions for mindful interactions: The case for microboundaries. *CHI 2016 Workshop*.

Darling, K. (2015a). "Who's Johnny?" Anthropomorphic framing in human-robot interaction, integration, and policy. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.2588669

Darling, K. (2015b). Empathic concern and the moral status of robots. *[Conference paper]*.

Ferdman, A., et al. (2026). AI deskilling as a structural problem in knowledge work. *[Journal pending]*.

Frauenberger, C. (2020). Entanglement HCI: The next wave? *ACM Transactions on Computer-Human Interaction*, 27(1), 1–27.

Gabriel, I. (2020). Artificial intelligence, values, and alignment. *Minds and Machines*, 30, 411–437.

Goffman, E. (1959). *The Presentation of Self in Everyday Life*. Anchor Books.

Han, J., et al. (2026). Tendling embodied AI: Designing soft AI objects for emotion regulation. *[Conference paper]*.

Haraway, D. (2003). *The Companion Species Manifesto: Dogs, People, and Significant Otherness*. Prickly Paradigm Press.

La Delfa, J. (2024). Mechanical sympathy: Somaesthetic approaches to human-machine relations. *[Conference paper]*.

Lee, H., et al. (Microsoft Research, 2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive engagement among knowledge workers.

Leigh, S. W., et al. (2018). Robotic symbionts: Wearable robots that interweave human and machine action. *[Conference paper]*.

Manoli, A. (2025). Companion-assistant dynamics: "Better than human" framing in AI relationships. *[Journal pending]*.

Mollen, L., et al. (2023). Bonding with a couchsurfing robot: In-the-wild human-robot interaction in shared domestic space. *[Conference paper]*.

Nass, C., Steuer, J., & Tauber, E. R. (1994). Computers are social actors. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 72–78. https://doi.org/10.1145/191666.191703

Nass, C., & Moon, Y. (2000). Machines and mindlessness: Social responses to computers. *Journal of Social Issues*, 56(1), 81–103.

Reeves, B., & Nass, C. (1996). *The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places*. Cambridge University Press.

Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press.

Song, Y., et al. (2026). CoStage: A robotic co-creator for children's storytelling. *[Conference paper]*.

Stivers, T. (2008). Stance, alignment, and affiliation during storytelling: When nodding is a token of affiliation. *Research on Language and Social Interaction*, 41(1), 31–57.

Vallor, S. (2015). Moral deskilling and upskilling in a new machine age: Reflections on the ambiguous future of character and virtue. *Philosophy & Technology*, 28(1), 107–124.

Weizenbaum, J. (1976). *Computer Power and Human Reason: From Judgment to Calculation*. W.H. Freeman.

Zhang, Y., & Yu, X. (2026). Exploring the attraction of AI companions: Anthropomorphism, emotional attachment, and sustained use. *Scientific Reports*.
