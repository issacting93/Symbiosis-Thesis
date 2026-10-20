# Script — Design Research in the Age of AI


Talk outline 
- We are being told that things are changing, and there are many different views of where UX should go, or what designers must do.
-  Design research needs ways of understanding problems in a deeper level to evaluate harm, to measure impact and to learn how we can better integrate these technologies_
- the way I think we should do it is by understanding the lineage of UX and reconnect with the fields that developed the rigour and methods that helped build the knowledge that grounds UX.
- These methods have evolved, and by talking to HCI researchers we can reconnect with the part of our lineage that we have lost, and find ways to integrate those ideas. Our lineage provides us a shallow understanding of many fields, but that is also our strength. It means that as UX or product designers or researchers, we have different wells of knowledge to tap into to redefine our field.
- And we do need to redefine our field, because the methods we use today do not understand the complex nature of how technology has shifted, and with that shift, how it has affected our social dynamics and relationships.

---

Hi everyone. Today I'll be talking about design research in the age of AI. I want to start with a clip from a 2013 film.

The film is *Her*, directed by Spike Jonze. It follows a character named Theodore who falls in love with an AI operating system. Looking at it from 2026, the film feels uncanny — it managed to predict something about the present with surprising accuracy. It resonated widely, winning an Oscar and earning a place as a landmark in cinema.

One of the more interesting footnotes to the film: Scarlett Johansson voiced Samantha, the AI. Years later, Sam Altman approached her to voice a version of ChatGPT. She declined. The controversy that followed made it clear how much the people building this technology had been shaped by the film. This wasn't coincidental. The people building AI were clearly aware of *Her*, and aware of the role that Samantha occupied in people's imaginations — this very conscious, relational dimension of what AI could be.

Art and Society has always been in conversation. Art reflect society, society takes inspiration from art. This recursive pattern is what helped us learn more about who we are and helps u understand where we might be going, or in some cases where we shouldn't go. 
This is part of a broader pattern. We keep seeing what might be called a Black Mirror effect — fiction articulates something, and technology builds toward it.  



---

## Three Observations

So, what are we actually observing in the current age of AI?

**The first is the rise of anthropomorphism.** It's not just that AI systems can now hold conversations. There's a deliberate effort to make them feel like living creatures — to give them physical presence, personality, and embodiment. Meta AI uses a soft, cute character — deliberately harmless-looking — and lets users customise its appearance. Replika, Character AI, and others have built entire products around AI companionship. In China, this reached a point where the government moved to restrict companion AI outright. 

These are engineering decisions to change how you feel about AI, designed to make 

This is worth examining, because LLMs entering the design space means that someone made active decisions — about shape, form, character, and emotional register. None of this is incidental. It's all designed. The design question is: why give AI a body? Why does embodiment matter? The short answer is obvious — it looks friendly, it looks trustworthy. We've seen this trend develop progressively: from the Rabbit R1 as one of the first physical AI devices, to Microsoft giving Copilot a visual identity and presence. Embodiment is clearly important to these companies as a mechanism for building trust and connection with users.

**The second trend is that conversation has become the dominant UX paradigm.** A lot of products now embed their entire user flow inside a conversational interface. We see this with government websites, for example — what appears to be a large RAG system embedded into a chat interface to handle queries. The implication is that the user experience is no longer deterministic. Responses are probabilistic rather than fixed, which creates new design challenges: not just in how we design, but in how we diagnose failure and measure success. In the past, we could track success through click-through rates and defined completion flows. That's no longer the case. The metrics have changed. The design process has changed.

**The third is that design tools and collaboration are changing.** Companies are bringing AI in at the research stage, using it to reduce the time it takes to run studies and synthesise insights. Product managers are giving designers AI-generated briefs, which then get fed into Figma, Make, or Lovable to produce initial flows. The problem is that different disciplines are now working across different tools. It used to be easier when everyone was on the same platform. Now designers are increasingly expected to work in code environments that aren't native or intuitive to design practice. This has fundamentally changed how teams collaborate. And researchers are using these same tools to transcribe and synthesise insights at a scale that wasn't possible before — which has its own implications for rigour.

---

## These Trends Are Not New

I want to go a bit deeper into all three — but before I do, I want to flag something: none of this is actually new. The underlying research already exists.

Take anthropomorphism. We have known for a long time that people treat computers as social actors — as though they are people. This was formalised as the CASA paradigm (Computers Are Social Actors) by Nass and Reeves in the early 1990s ([[Media Equation — Reeves Nass 1996|Reeves & Nass, 1996]]; [[Machines and Mindlessness — Nass 2000|Nass & Moon, 2000]]). One of the pivotal case studies is ELIZA — a chatbot that used simple rule-based replies to simulate a therapeutic conversation ([[Computer Power and Human Reason — Weizenbaum 1976|Weizenbaum, 1976]]). Users responded to it as though it were a genuine therapist. Even with that level of simplicity — just pattern-matching and reflecting language back — users formed real emotional responses.

So we've moved from understanding that people treat computers as social actors, to deliberately designing for that tendency. We give tools mascots and personalities not because the functionality requires it, but because emotional investment drives engagement. If users form a bond with a tool, they're more likely to keep using it. And this means complex interactions that might otherwise be handled through a well-structured form are now being wrapped inside a conversational avatar — and users tolerate them more because the avatar feels approachable. Emotional design as a substitute for interaction design.

We've seen where this goes wrong. Clippy — Microsoft's Office Assistant from the late 90s — is the canonical example. Clippy had a personality but very limited functionality, and the mismatch between the emotional promise of a friendly character and the frustration of its actual capabilities turned users against it. It became a double-edged sword. There are cases where relational design is appropriate, and cases where it isn't. Not every tool benefits from a personality.

---

## The Conversation Design Problem

The problem with conversational UX goes deeper than the interface. We don't have good tools for designing conversations. The most common approach is prompt engineering — structuring what the model knows and how it should respond. But when responses are probabilistic and require engineering to shape, a lot of what should be a design decision becomes an engineering decision. The designer's influence moves upstream, into the architecture and the prompts, while the actual response is something that emerges rather than something that is designed.

The easier solution — arguably the better design solution — is to give users a structured menu of intentions. Let people select what they want to do, rather than expecting the model to infer intent from open-ended input. This connects to a very old debate in HCI — the debate between direct manipulation and natural language interaction, which played out between key figures in the field in the 1990s ([[Conversational Agent vs Direct Manipulation — Jönsson 2005|Jönsson et al., 2005]]). Research consistently shows that users prefer direct manipulation when they can use it effectively — it's faster and gives a greater sense of control — and that they reach for natural language mainly when objects are hard to describe precisely (cf. DirectGPT, CHI 2024). That debate is relevant again, and it's a lineage designers should be aware of.

---

## Social Contracts Around AI

The trend of designers adopting new tools at different rates is a symptom of a much larger problem: people don't adopt new software or workflows at the same pace, and they have fundamentally different preferences for how they work. From a design perspective, differential adoption creates friction within teams. From a research perspective — and drawing on Abbott's theory of professional jurisdictions (1988) — it's also a boundary problem: AI is redrawing the lines of who legitimately owns what kind of work, and the social norms haven't caught up.

This isn't unique to design. In the workplace more broadly, people have very different attitudes toward AI adoption — shaped by their role, their community, and the social norms of their field. A writer might be pressured by a manager to use AI, while simultaneously being judged by peers for doing so. That social pressure is largely absent for software engineers, where using AI to write code is socially acceptable — expected, even. The issue arises when AI-generated code is low quality and that becomes someone else's problem. But the broader point is that there are social contracts around how we use AI that vary enormously by discipline and context ([[Society-in-the-Loop — Rahwan 2018|Rahwan, 2018]]). Recent empirical work documents this precisely: workers simultaneously fear being seen as cheaters for using AI and as incompetent for not using it — and those pressures fall very unevenly across roles and fields ([[AI Professional Identity — Ahuja 2026|Ahuja et al., 2026]]).

We don't yet understand how the integration of AI into work culture is reshaping social dynamics — or what its true impact on the social fabric at large looks like. That's a relatively new area of inquiry, and it will require rigorous study.

---

## The UX Knowledge Problem

So those are three observations shaping the conversation right now. But here's what I think matters most: a lot of these changes are not new. The research already exists. So why does it feel like we're starting from scratch?

UX as an industry is at most 20 years old. And its history is that it spent a long time as a subset of HCI. HCI itself was an accumulation of psychology, social sciences, engineering, and computer science — a group of people from those disciplines who came together and said: we need to study this specifically. They brought the rigour of their home disciplines and used it to construct an entirely new field.

The problem is that when UX emerged from HCI, it adopted the techniques and methods — but not the discipline and rigour needed to create new knowledge, share it, and retain it within the community. We saw bootcamps emerge that taught specific UX methods, focused on usability and heuristics. And that worked well — it created a new generation of designers at a moment when we badly needed them, particularly during COVID. But it left a vacuum: we adopted the knowledge without acquiring the skills to generate new knowledge.

This is one of the biggest problems in the UX community. Research occupies a very different position within design than it does in the disciplines HCI drew from. We need to go back to the study of research — to analysis, to the underlying sciences — to understand why we do what we do, and to develop the skills to make sense of the observations and insights that are emerging.

The methods we have today are outdated. The way to update them isn't to adopt more AI. It's to go back to the scientific community, to re-engage with HCI, AI safety, and alignment research, and to understand how those fields are thinking about these changes. Many of the things we're struggling with have already been worked through in those spaces — from [[Human-Centered AI — Shneiderman 2020|Shneiderman's human-centered AI framework (2022)]], which gives designers a vocabulary for arguing against maximum automation, to [[AI Values and Alignment — Gabriel 2020|Gabriel's work (2020)]] establishing that value alignment is not an engineering problem but a normative one requiring exactly the kind of stakeholder deliberation that design research is built to support. The problem is that we don't yet have the language to discuss ideas with them.

---

## Closing — Craft a Vision

Going back to Spike Jonze: why did he make *Her*? I think he observed something personal enough that it became universal. And he translated it into something intentional — a film that resonated, and that resonance then reached engineers and technologists and captured their imaginations. From that vision, engineers had something worth building toward, because it spoke to a bigger problem. What films like *Her* are doing isn't predicting the future. They're articulating how we feel in the present — giving language to something nobody has named yet.

When we think about design, we're describing the same process: observing, generating insights, inspiring, visualising, building, and observing again. That cycle — through research, design, and engineering — is something we have to keep crafting and holding onto.

We know we're going to keep building. We need to craft a vision first. What kind of future do we want to see? How do we get there?
