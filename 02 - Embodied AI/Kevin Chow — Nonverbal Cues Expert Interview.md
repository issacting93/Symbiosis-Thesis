# Kevin Chow — Expert Interview: Nonverbal Cues in Human-AI Interaction

**Date:** September 25, 2026
**Interviewer:** Issac Ting
**Participant:** Kevin Chow (PhD researcher, human-computer interaction)
**Context:** Pre-thesis expert consultation on nonverbal communication and AI. Non-IRB exercise interview.

---

## Kevin's Research: Nonverbal Cues in Video Meetings

Kevin developed a probe system using computer vision to track body language and facial expressions in real work video meetings — inspired by Zoom's push to integrate emotion AI during the pandemic.

**Core methodological decision — cues, not emotions:**
The team tracked observable cues (smiling frequency, nodding rate, posture) rather than inferring emotions. The distinction mattered: a smile is a measurable observable; "happiness" is an interpretation layered on top of it, one that varies across individuals and cultures. Tracking the cue without asserting what it means keeps the system honest.

**Design principle — neutral reporting, not prescription:**
The system was deliberately kept neutral. It would say "you haven't smiled in the last two minutes" — not "you should smile more." The framing is informational, not directive. Users own their data and decide what to do with it.

**The mirror effect:**
People overcompensate on Zoom because they see their own image during the call. Constant self-observation leads to over-smiling, over-nodding — performative emotion rather than authentic expression. This is a documented driver of Zoom fatigue.

---

## Key Findings

**1. People often didn't want ideal nonverbal cues.**
After weeks of use, participants found many situations where they actively didn't care about performing "good" body language. This was not laziness — it was relational appropriateness.

**2. Imperfect cues in close relationships felt authentic and important.**
In familiar, intimate meetings with trusted colleagues, appearing tired, slouching, or visibly struggling was valued as authentic. It could prompt a colleague to notice and check in. The imperfection is functional: it carries real social information. Kevin's phrase: *"the imperfection is what makes it human."*

**3. Formal contexts were the exception.**
In high-stakes, structured settings — job interviews, presentations, teaching — people wanted to manage their nonverbal presentation and found the tool genuinely helpful. They needed to "put on a mask" and the system supported that.

**4. The formal/informal axis is well-validated.**
Kevin noted this is consistent across technology-mediated communication research broadly. Tools that formalize interaction are more useful and acceptable in formal, high-stakes contexts. AI-mediated communication is more acceptable in the workplace than in close personal relationships because context norms already lean formal.

---

## On Nonverbal AI More Broadly

**Context and task determine whether gesture/expression input is valuable:**
For simple text-editing tasks, gesture reading is overkill — extra tokens, slower, risk of misinterpretation, and probably irrelevant. Kevin's framing: *"scope tightly to a specific context and specific goal. Broad claims are unlikely to hold."*

**Computer vision misinterpretation:**
Concentration and frustration look the same from the outside. A furrowed brow means focus for one person and distress for another. Idiosyncratic expressions (tongue out while focusing) could be misread. The AI risks acting on noise.

**Cultural bias is structural:**
AI trained on internet data risks encoding cultural stereotypes — e.g., Western context = more expressive; Eastern context = less expressive. Applying these norms as defaults would be actively harmful and would encode existing power imbalances into the system's interpretation logic.

**Paralinguistic cues: an underexplored category:**
Kevin introduced the term *paralanguage* — the non-word aspects of voice that carry meaning: tone, emotional quality, pitch, speaking rate, pauses, silences. This is distinct from language content and distinct from visual nonverbal cues (gestures, expressions). It is underexplored. Kevin was uncertain whether current voice AI captures paralinguistic information or simply converts speech to text and discards it.

**High-value contexts (with significant caveats):**
- *Therapy:* potentially useful but risky; chatbot therapy research broadly shows short-term benefits and long-term risks; adding emotion/expression reading would amplify both the potential and the risk
- *Customer service / help desk:* detecting frustration could help calibrate AI response — but acting on that detection is still unsolved
- Both contexts require caution and very specific scoping

---

## How This Informs the Research

- The hypothesis "more nonverbal data = better AI interaction" is too simple. Value is context-dependent.
- The most important design question is not *can AI read nonverbal cues* but *in what context does reading them serve the user rather than surveilling them*
- Kevin's cues-not-emotions distinction is a design principle directly relevant to the symbiosis framework: a symbiotic tool reports; a parasitic tool prescribes
- Paralinguistic cues (prosody, pauses, pitch) are a gap in the current research scope — a channel neither text-based nor visual-gesture-based AI is currently processing
- Cultural bias in nonverbal interpretation is a structural problem, not an edge case — any nonverbal AI system needs explicit attention to this from the outset
- The formal/informal axis should be a design variable in the primary research protocol, not just a contextual note
