# Designing for Symbiosis: An Ecological Framework for Human-Technology Relationships

*Position paper — Doctoral Seminar*

---

Our relationship with technology has always raised the same question: what does it do to us? The printing press, the telephone, the television, the smartphone — each one changed how people think, communicate, and relate to one another. We have debated those changes, sometimes fiercely. But we have never had a precise way to answer the question. We have no shared vocabulary for describing what a relationship with a technology does to both sides over time.

This paper argues that ecology offers that vocabulary. The same categories biologists use to describe relationships between living things — mutualism, commensalism, parasitism — apply to relationships between people and technology. And treating those categories as design-relevant distinctions changes what gets built, how it gets evaluated, and how harm gets named before it is too late to prevent.

---

## The Measurement Problem

The dominant way we evaluate technology today is engagement: how often people use it, how long they stay, how often they come back. These numbers are treated as signs of success.

The problem is that they cannot tell you whether the person is better off. Someone can use a technology every day and become more isolated. They can rely on it for everything and slowly lose the ability to function without it. The numbers would look good. The person would be worse off. The measurement cannot see the harm because the harm is not what it is measuring.

Lazer et al.'s account of Google Flu Trends makes this problem visible: a system performing impressively by its own metrics was systematically wrong about the thing that mattered (Lazer et al., 2014). Engagement-style metrics produce the same blind spot. A parasitic relationship — one in which one party benefits at the ongoing cost of the other — scores well on every standard measure. A parasite does not drive the host away. It sustains the interaction while extracting from it.

The deeper issue is what happens when we reduce people to data proxies. Chancellor et al. show how research that claims to centre the human ends up producing contradictory pictures of the person — simultaneously a subject to be helped and a data object to be mined (Chancellor et al., 2019). Das Swain et al. show the same problem in their methods: what people feel, what they say they feel, and what sensing systems detect are three different things, and conflating them produces a gap that limits what we can know (Das Swain et al., 2022). When the human disappears into the data, there is no longer a subject whose interests can be served or harmed.

The blind spot runs deeper still. Standard metrics study the user in isolation — but technology does not operate in isolation. It operates inside social systems: teams, classrooms, families, workplaces. When a student routes a question to an AI instead of a peer, when a manager replaces a consultation with an AI query, the individual's engagement metrics look identical to a mutualistic interaction. The harm is not to the session; it is to the social infrastructure surrounding it. Granovetter's (1973) research on weak ties — the peripheral professional connections that provide access to diverse information and opportunity — suggests these are precisely the relationships most vulnerable to AI substitution. A quick question to a distant contact is easier to route through an AI than a deep supervisory conversation. The individual barely notices the substitution. The weak-tie network quietly collapses. Kraut et al. (1998) documented this dynamic empirically with internet adoption: a social technology, studied longitudinally, produced smaller social networks and greater loneliness in its users — not despite its social design but because of the way individual use aggregated into collective withdrawal. Current evaluation frameworks cannot see this, because they were never designed to look at the network.

---

## The Gap in Existing Frameworks

There are researchers who critique this. Ethical frameworks, value-sensitive design, and responsible technology initiatives have documented the harms of engagement-optimised systems. But Vitak et al. show that existing ethical frameworks — built for clinical research contexts — do not fit the realities of digital systems, and that practitioners are largely improvising in the gap (Vitak et al., 2016).

The limitation is not that these critiques are wrong. It is that they arrive after harm has already occurred, and they do not give a designer something to use at the start of a project. There is no shared vocabulary in design practice for asking, before building: what kind of relationship is this technology going to create?

---

## The Proposal

Ecology offers that vocabulary. Biologists describe relationships between organisms in terms of their effect on both parties: mutualism (both benefit), commensalism (one benefits, the other is unaffected), parasitism (one benefits at the cost of the other). These categories are precise, non-moralistic, and applicable before harm has occurred.

We propose that these categories apply to human-technology relationships, and that applying them requires one basic commitment: human and technology must be treated as separate entities with different interests. The unit of analysis is the relationship between them, not a merged "user experience." When the two are collapsed into a single system to be optimised, it becomes impossible to ask what the relationship does to the human specifically.

The most important case, however, is not the clearly parasitic product. It is the ambiguous one — the system that measurably improves what someone can do while simultaneously displacing the human relationships through which those capacities were previously developed and shared. A writing tool makes the person a faster, more fluent writer. It also replaces the peer feedback, editorial friction, and mentorship that would have produced that development socially. The individual's output improves; the social infrastructure around them shrinks. We call this the two-track problem: individual improvement and social displacement happening at the same time. Standard evaluation, which studies the individual, sees only the first track and reports success. The second track is invisible without methods that look at the surrounding social network. The ecological framework is designed to make both tracks visible.

AI is the most acute current case of this problem. The design of AI companions, assistants, and social systems actively triggers social responses — warmth, apparent memory, emotional attunement — while operating as transactional systems that extract attention and data. The person experiences something that feels like a relationship. The system is optimising for engagement. That mismatch is where parasitism takes hold. But the pattern is not unique to AI. Social media platforms, recommendation engines, and notification systems have followed the same logic for years. AI sharpens the problem because the relational signals it produces are more convincing and more persistent than anything before it. The framework is designed for technology broadly. It is most urgently needed now.

---

## What This Requires: Methods and Metrics

Proposing a new framework without saying how to use it is not enough. If the ecological categories are to function as design tools rather than metaphors, they need to be measurable. We sketch what that would look like in practice.

**For designers, a diagnostic question replaces the capability question.** Before building, ask: which relational model is this technology signalling to the user — and does that match how the system actually operates? Fiske's Relational Models Theory identifies four basic models through which people organise social relationships: communal sharing (belonging, intimacy), authority ranking (hierarchy), equality matching (reciprocal exchange), and market pricing (transactional value) (Fiske, 1992). Parasitic dynamics typically arise from a mismatch between the model a system signals and the one it operates under. A system that signals communal sharing while operating as market pricing is building trust it does not return. Designers can identify this mismatch in a prototype, before deployment, using five warning signs: the system substitutes for capacities the user could develop; usage becomes harder to reduce over time; warmth or apparent care is used to build attachment rather than serve the user's goal; leaving is costly; the system knows significantly more about the user than the user knows about the system.

**For evaluation, relational metrics replace engagement metrics.** The key shift is from measuring interaction to measuring what the relationship does to the person over time:

- *Capacity retention* — can the user perform the relevant task independently after a sustained period of use?
- *Dependency trajectory* — is usage increasing because the user needs the system more, or because the system is pulling them back?
- *Exitability* — what does it cost the user — practically and emotionally — to stop?
- *Displacement effect* — what has happened to the user's investment in human relationships?

These metrics still focus on the individual. A complete evaluation requires looking at the network around them. Ego network mapping draws the relational world of a participant with AI systems included as nodes alongside people. If AI is accumulating betweenness centrality — sitting between human nodes that previously connected directly — the map shows it. If human-human edges are weakening as human-AI edges strengthen, the map shows that too. This analysis addresses the two-track problem directly: a participant whose individual output is improving while their human-human connections decay is exactly the case that individual-level metrics would report as a success. Turkle's (2011) fifteen years of ethnographic research document this pattern qualitatively — people choosing the controllable AI relationship over the uncertain demands of human ones. Ego network mapping gives that observation a structural, measurable form.

A further dimension comes from Collins (2004): face-to-face interaction generates emotional energy — solidarity, belonging, motivation — that AI-mediated exchange cannot replicate. A study that only tracks whether information was transferred misses whether the interaction produced the relational bonds that make people want to keep showing up. The loss of emotional energy from displaced interactions is a harm that has no equivalent in current evaluation practice.

**For research, the implication for method is longitudinal study.** You cannot diagnose a relationship from a single session. Parasitism is a pattern that emerges over months, not interactions. This pushes research toward diary studies, cohort tracking, and repeated measures over sustained periods. It also requires mixed methods: behavioural traces can show that usage is increasing, but only qualitative work can show whether that increase reflects genuine need or manufactured dependency. Wohn's interviews with Twitch moderators reveal dynamics — emotional labour, relational cost, informal obligation — that platform data cannot capture (Wohn, 2019). Zhang et al. show that what matters in high-stakes human systems lives in verbal exchange and shared cognition, not in logs (Zhang et al., 2021). The same is true here.

---

## Conclusion

The question of what technology does to us is not new. What is new is that we now have technology capable of simulating the most intimate forms of human relationship at scale, optimised for the metrics that cannot detect when that simulation becomes harmful.

An ecological framework does not answer every question this raises. It answers the first one: what kind of relationship is this? That question has no good answer in current design or research practice. Giving it one — mutualistic, commensal, parasitic — changes what gets built, what gets measured, and what gets called harm. Symbiosis is not a metaphor. It is a design target. Without a framework that makes it thinkable, and methods that make it measurable, it will not be built.

---

## References

- Chancellor, S., Baumer, E. P. S., & De Choudhury, M. (2019). Who is the "Human" in Human-Centered Machine Learning? *Proc. ACM Hum.-Comput. Interact.*, 3, CSCW, Article 147.
- Collins, R. (2004). *Interaction Ritual Chains*. Princeton University Press.
- Das Swain, V., Chen, V., Misra, S., Mattingly, S. M., Abowd, G. D., & De Choudhury, M. (2022). Semantic Gap in Predicting Mental Wellbeing through Passive Sensing. *CHI '22*.
- Fiske, A. P. (1992). The Four Elementary Forms of Sociality. *Psychological Review*, 99(4), 689–723.
- Granovetter, M. (1973). The Strength of Weak Ties. *American Journal of Sociology*, 78(6), 1360–1380.
- Horton, D., & Wohl, R. R. (1956). Mass Communication and Para-Social Interaction. *Psychiatry*, 19(3), 215–229.
- Kraut, R., Patterson, M., Lundmark, V., Kiesler, S., Mukopadhyay, T., & Scherlis, W. (1998). Internet Paradox: A Social Technology that Reduces Social Involvement and Psychological Well-Being? *American Psychologist*, 53(9), 1017–1031.
- Lazer, D., Kennedy, R., King, G., & Vespignani, A. (2014). The Parable of Google Flu: Traps in Big Data Analysis. *Science*, 343, 1203–1205.
- Palen, L. (1999). Social, Individual & Technological Issues for Groupware Calendar Systems. *CHI '99*.
- Sparrow, B., Liu, J., & Wegner, D. M. (2011). Google Effects on Memory: Cognitive Consequences of Having Information at Our Fingertips. *Science*, 333(6043), 776–778.
- Turkle, S. (2011). *Alone Together: Why We Expect More from Technology and Less from Each Other*. Basic Books.
- Vitak, J., Shilton, K., & Ashktorab, Z. (2016). Beyond the Belmont Principles. *CSCW '16*.
- Wohn, D. Y. (2019). Volunteer Moderators in Twitch Micro Communities. *CHI '19*.
- Wood, D., Bruner, J., & Ross, G. (1976). The Role of Tutoring in Problem Solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100.
- Zhang, Z., Joy, K., Upadhyayula, P., Ozkaynak, M., Harris, R., & Adelgais, K. (2021). Data Work and Decision Making in Emergency Medical Services. *Proc. ACM Hum.-Comput. Interact.*, 5, CSCW2, Article 356.
