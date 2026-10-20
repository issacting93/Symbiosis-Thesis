# Symbiotic Design Framework

We live in an age where our relationship with technology feels like it is a form of parasitism. What we need instead is to construct technology in a way where we can co-exist, where the benefits are mutually beneficial, and where it is not a zero-sum game type of situation. What we need to move towards is a symbiotic relationship.

A symbiote is different from a cyborg or transhumanism. A cyborg looks at technology as a way to replace parts of the human, while transhumanism explores the idea of the human going beyond the physical and entering into the digital. Both dissolve the boundary between human and machine — the merger is the point.

Symbiosis works differently. It requires two distinct entities. In ecology, a symbiotic relationship does not mean two organisms become one — it means two organisms remain separate while their relationship shapes both of them. That distinction is foundational here.

This framework keeps human and technology as separate entities. The human is not enhanced by merging with technology. The technology is not humanised by absorbing human qualities. What is studied is the *relationship* between them: what it asks of each party, what each party gets in return, and whether that exchange is balanced or exploitative over time.

This matters because it preserves the question that the cyborg and centaur metaphors foreclose: *is this good for the human?* You can only ask that if there is still a human — separate, intact, with interests of their own — to ask it about.

In this essay, I will go in-depth and look at how designers and researchers are exploring this, and through a review of different ways of thinking about symbiosis, articulate the implications and principles of a symbiotic design.

### Rethinking design methods beyond a "user-centric lens"

Now more than ever, our relationship with technology is no longer something that exists in a closed system. Our relationship with technology is shaped by a network of interconnected systems, and how we understand technology is no longer just by how we interact with it, but how we interact with other people.

Current research methods for user experience design looks at the user as the subject to be studied. Current metrics look at individuals' click through rate, retention rates and completion to understand an individual behavior. But as our relationship with technology becomes even more complex and intertwined, so does the social interaction that emerges as a result.

3 case studies to think about:

1. Employee A needs to present a report to their boss, boss chooses to ask chatgpt for an answer instead of listening to the report
2. Designer A uses vibe coding tools but other designers are still on figma. This creates multiple sources of truth that makes collaboration impossible

### Ecology & Swarms

Symbiosis design aims to look at our relationship with technology and help us to better categorize it to understand what we can change or what needs to be fixed.

I start with looking at the ethnographic and ecology lens to understand the relation we have with technology. A broad category to examine is the Swarm. A swarm describes multiple actors, working together in a hive-mind like manner. When we read about 100 agents hacking a website, that describes what we would call a swarm behavior. When multiple agents act together with a similar goal, it mimics the behavior of animals like bees, locust and wasps.

Bees are the most essential out of the 3. Bees provide honey, they pollinate and they are a vital part of the environment. Bees work in a swarm, listening to the queen bee and working together to make honey. [ insert bee research I haven't fully done].

Locusts on the other hand have been a symbol of plagues, famine and suffering. Locusts also work in swarms, but their actions exploit, extract and eradicate farmlands. They are highly invasive and create catastrophic levels of damages. Wasps on the other hand have been known to create more localised dangers. Wasps are angry, their strings inflict pain. They create damage on a smaller level but can also be dangerous.

AI systems do not have physical forms unless we give it to them. They don't actually live in a machine, they are mostly just API calls from our computers to a data center. But by understanding how they behave, we can draw parallels between the morphology of nature to better understand.

### From Ecology to Interaction: Scaffolding and Substitution

The ecological lens gives us categories — locust, bee, wasp — to describe *what kind* of relationship exists between human and technology at the macro level. But it does not yet tell us *how* a relationship becomes parasitic, or *what* makes an individual interaction mutualistic. For that, we need a theory that operates at the level of the single exchange.

Wood, Bruner, and Ross (1976) provide exactly this. Their concept of instructional scaffolding, built on Vygotsky's Zone of Proximal Development, describes the difference between support that builds capacity and support that replaces it. A scaffold is temporary — it is calibrated to what the learner cannot yet do, helps them do it, and is gradually withdrawn as they develop the ability to do it independently. The goal of a scaffold is always its own disappearance.

The alternative — substitution — looks identical in the short term. The person gets the outcome they wanted. But the underlying capacity is never developed, and the support is never withdrawn. Over time, they need the tool more, not less.

This distinction gives the Symbiosis framework its smallest unit of analysis. Every interaction with a technology is either scaffolding or substitution. And a parasitic relationship is not one dramatic event — it is an accumulation of substitution interactions that, individually, feel helpful and, collectively, erode independent capacity. This is why the ecological metaphor holds: the locust swarm does not destroy the farmland all at once. It passes through repeatedly, each time extracting a little more.

**The fading test.** This gives the framework a concrete, testable design criterion. A mutualistic technology should become less necessary as the person's capacity grows. If, after extended use, the person needs the tool just as much — or more — than when they started, the interaction pattern has been substitutive. The tool has not scaffolded; it has replaced. Fading is not a feature to be added — it is the diagnostic.

**The contingency requirement.** Scaffolding works because it is responsive to the learner's current state. Support increases when the learner struggles; it decreases when they succeed. For AI systems, this translates into a design requirement: a mutualistic AI does not answer every question at the same level of completeness. It calibrates its response to what the person can do themselves, and adjusts as their capacity changes. Non-contingent support — fixed, regardless of user state — is more likely to drift toward substitution precisely because it cannot tell the difference between a person who needs help and a person who is developing the capacity not to.

**The two-track problem.** Scaffolding at the task level does not guarantee scaffolding at the social level. An AI can help a person become a better writer while substituting for the peer feedback, editorial friction, and mentorship relationships that would have produced that development socially. The task capacity grows; the relational capacity atrophies. This is why the framework's insistence on studying the relationship network — not just the individual user — matters. A system that improves individual output while degrading the social infrastructure around that output is still operating parasitically, just on a different host.
