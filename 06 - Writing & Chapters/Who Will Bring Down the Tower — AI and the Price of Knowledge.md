# Who Will Bring Down the Tower?

*Essay — filed from "A new Tower.md"*

**Themes:** [[Sociology of Professions]] · [[AI Safety & Alignment]] · [[Symbiotic Design Framework]]

Oct 17, 2026 · @Zac

---

*"After all, we're here to make the unknown known, to make the other familiar. We're here to make magic with words."*
R.F. Kuang, *Babel*

## The tower

Perhaps the greatest irony of the AI boom is where it started. The 2017 paper that laid its foundations, "Attention Is All You Need", was not an attempt to build a machine that could topple whole industries. Its authors, mostly researchers at Google, built and tested their new architecture, the transformer, on translation. That architecture now sits underneath the large language models behind today's generative AI. At heart it does one thing remarkably well: it turns meaning into numbers, and uses those numbers to complete sentences. That ability alone has unlocked incredible capabilities that we have never before seen.

There is something almost poetic in that. Our capacity for language built the very machine that now threatens the people who spend their careers learning to read and write.

Which brings us back to *Babel*. R.F. Kuang's novel, which won both the Nebula and Locus awards, is set at the height of British colonialism, as Britain moves toward the Opium War with China. Its hero is taken from Canton as a child and raised to serve Oxford's Royal Institute of Translation, the engine of the Empire. Children like him are taken from their homes, educated and indoctrinated, so that their languages can power someone else's empire. *Babel* is, of course, a tragedy, and we watch as the story unfolds and all of it crashes and falls, swiftly. It echoes many historical stories, and when we reflect on its themes against the world we live in, it is not hard to notice the uncanny similarities.

The scholars who lived and worked in Kuang's tower never thought of themselves as replaceable. Neither do the scholars who live and breathe in the walls of our universities today.
It would seem that they were wrong to believe that to be true.

→ This is the jurisdictional question at the heart of [[System of Professions — Abbott 1988]]: new technologies rarely eliminate a profession outright — they redraw who holds the legitimate claim to diagnose and validate a class of problems. The mathematicians below are a live case of that boundary moving.

On 6 October, OpenAI posted 722 mathematical manuscripts to GitHub, produced by an unreleased model and claiming progress on 372 open problems. It had pointed the model at roughly 4,000. A day later it withdrew three of them, after a sign error broke one proof and the two that depended on it. More than a dozen others were revised. The prompts, the model's name and the computing power behind each result were kept private, against the advice of a panel of mathematicians OpenAI itself had helped form.

The release followed a month of disputes. In September, OpenAI announced that an internal model, running around 10,000 AI agents for about 88 hours, had resolved the Navier–Stokes problem, one of mathematics' famous million-dollar Millennium Prize problems. By OpenAI's own account, it launched that effort after hearing a rumour, which it later traced to Alpöge and NYU mathematician Tristan Buckmaster, who were close to a related result. OpenAI says it never saw their work and has credited them with the earlier result. Separately, a mathematician at TU Dresden says his private ChatGPT conversations may have fed into another OpenAI result, even though he had opted out; OpenAI says it cannot rule out that de-identified data was used.

The economist Daniel Susskind calls what is happening here task encroachment. Machines rarely take a whole job at once. They take tasks one by one until the job thins out. He also offers a sharper image. Horses were displaced by engines, but horses had no vote. People do, which makes displacement a political question, not a natural law.

→ See [[AI Deskilling — Ferdman 2026]] on why task encroachment is a structural design outcome, not an individual failure, and [[Moral Deskilling Upskilling — Vallor 2015]] on what is ethically at stake when a skill erodes rather than a task merely getting faster.

## The machine that needs us

The industry tells a story of inevitability: an ever-growing machine that will eventually outpace us all. The reality is more dependent. These systems still need a steady supply of human knowledge and human judgement, and they need it at both ends.

At one end is the knowledge itself, the raw material models are built from. Epoch AI estimates that the stock of quality public human text could be fully used up somewhere between 2026 and 2032. The obvious fix, training models on AI-generated text, has its own trap. A 2024 study in *Nature* by Shumailov and colleagues found that models trained repeatedly on their own output degrade, losing the rare and unusual first and then drifting into nonsense. The researchers called it model collapse. Companies are betting on licensing deals and carefully filtered synthetic data to avoid it, so this is a risk rather than a certainty. But in *Babel*, the silver only works because translators keep finding new meaning between languages. Without fresh human thought, the machine ends up translating itself.

At the other end is validation. Seven hundred manuscripts arrived in a single afternoon. Each one still needs someone with years of training to tell whether it holds, and the first error was caught within a day. AI has dramatically shortened the middle of the chain: the drafting, the searching, the first attempts. The beginning and the end, making knowledge and judging it, remain human. The tower is not self-sustaining. It is a machine with people at both ends, and the people at the end are now being asked to check more than any human field can absorb.

→ The validators are living the identity strain [[AI Professional Identity — Ahuja 2026]] documents in knowledge workers more broadly: oscillating between contesting the tool, compromising with it, and folding it into a revised sense of what their expertise is for.

That is leverage. The question is who gets to use it, and that depends on who owns the tower.

## Open and closed: a short primer

Every AI model is, at bottom, a very large file of numbers called weights. Training is the process of setting those numbers, and it is the expensive part: the data, the chips, the electricity and the human labour part one described. Once trained, the weights are the model.

A closed model keeps its weights private. You use it through an app or a paid connection, on the company's servers and on the company's terms. Most of the best-known chatbots work this way. An open-weight model publishes its weights for anyone to download, run on their own machines, and modify. That is not quite the same as open source. A fully open model would also publish its code and training data. Most open-weight models do not, so you can use the tower without being told whose words it was built from.

The case for open weights is strong. You can run the model on your own hardware, so your data never leaves the building. You can adapt it to your language, your field or your company. It is far cheaper: hosted open models often cost a tenth of the frontier models per word. And it spreads power, so no single company becomes a gatekeeper for everyone else. The case against is also real. Once weights are published, the safety training can be stripped out, and a release cannot be undone. One way to put the trade-off: the risk of misuse favours closed models, while the risk of power gathering in a few hands favours open ones.

## The view from Beijing

For most of the AI boom, open models were a Western story. That has changed. Chinese models overtook American ones in open-model downloads in the summer of 2025, and by March 2026 they had 1.15 billion tracked downloads against 723 million for American models. Most of that comes from Alibaba's Qwen family, especially small models that are cheap to run and easy to build on. In Japan, six of the ten best domestically built models are reportedly built on DeepSeek or Qwen.

Part of this is necessity. American export controls kept the most advanced chips out of China, which pushed Chinese labs to build leaner models that need less computing power, and lean models travel well. Part of it is strategy. At the World AI Conference in Shanghai this July, Xi Jinping urged countries to seize a rare, historic opportunity to embrace open source. China has set up a World AI Cooperation Organization to promote AI adoption and governance in developing countries. As one researcher put it, a model you can download and run yourself sidesteps the question of whether you trust the Chinese state. It is good for soft power.

Openness, though, is a strategy rather than a principle. China is reportedly considering limits on overseas access to its most advanced models: keep the middle tier open for influence, and the frontier behind the counter. The irony would not be lost on Kuang. Two centuries after the Opium War, China is the one offering the world a product on generous terms, and the West is the one warning about dependence.

## "But China"

Every argument for slowing down runs into the same two words. In Washington, the case against pausing is simple: the rivals will not pause, so restraint only hands them the lead. President Trump has said winning the race comes before slowing down.

The argument is weaker than it sounds. The Carnegie fellow Matt Sheehan points out that China has run the world's strictest AI regulations for three or four years. Most of it is about controlling information, which in practice means censorship, and it has only recently expanded to companions and harms to children. China is not racing toward the same finish line Silicon Valley describes. Beijing, for its part, has rejected American calls for a global slowdown, including one from Anthropic's chief executive, Dario Amodei, which Chinese state media called a Cold War playbook. Its reasoning is not hard to follow: a pause that binds both sides would freeze it in second place. To have a say in the rules, you have to be in the race.

Singapore is not in that race, and has said so. In his Budget speech, PM Wong argued that our edge lies not in building the largest frontier models but in deploying AI effectively, responsibly and at speed. That is sensible, and it means our future depends on towers built elsewhere: American closed models, Chinese open ones, or something we and our neighbours build together. Which of those we lean on is a labour question as much as a geopolitical one.

## Three ways this ends

In *Babel*, the tower falls one way: the people inside stop working. Ours has three possible endings, and they are not equally good.

**The tower falls.** People withhold what the system runs on: mathematicians walking away, writers' and actors' strikes, artists poisoning their images, publishers blocking the crawlers. Or the system fails on its own: the data runs dry, the money runs out, a visible disaster sets the field back for decades, as accidents did for nuclear power, or courts and insurers make harm too expensive to risk. This is Kuang's ending, and everyone loses something in it, including the people who would have benefited from the technology.

**The tower is rebuilt.** The dot-com crash reset the companies, not the internet. A bubble bursting, or a wave of regulation, may do the same here: some firms fail, the survivors consolidate, and the tower goes back up on much the same terms. Licensing deals pay off the loudest rights holders while everyone else is left out. This is the likeliest ending if nothing changes, and it fixes very little.

**The tower fractures.** The third ending is the hopeful one. In *Empire of AI*, the journalist Karen Hao describes today's AI companies as empires, claiming data, land, water and energy that are not theirs and justifying it with a mission to benefit humanity. But she also argues that we need to separate AI from empire, and she points to what that looks like. In New Zealand, the Māori media organisation Te Hiku Media built a speech-recognition model for te reo Māori using recordings its community gave with consent, and the community kept control of its data. Smaller, task-specific models like this use far less energy, can run on your own device, and are easier to audit. Singapore's SEA-LION, built for Southeast Asian languages, hints at a regional version of the same idea.

Open weights make this ending possible, but they do not guarantee it. A Qwen model running in Jakarta is still someone else's tower, trained on data nobody disclosed, by workers nobody credited. Fracture only helps if the smaller towers answer to the people inside them. What is missing is a public that knows how to choose the right tool rather than the biggest one, and policy that pays the people the towers run on.

→ "Answer to the people inside them" is the [[Symbiotic Design Framework]]'s test applied at the scale of an industry rather than a single interaction: a tower that extracts data and labour without consent or return is operating on the parasitism end of the spectrum; a tower whose community keeps control of its own data and sees it reused on its own terms — Te Hiku's model is the clean case — is closer to the mutualistic one. The "fading test" the framework proposes for a single AI interaction (does the person need the tool less over time, not more) has an institutional analogue here: does the community that supplied the data and judgement end up with more capacity and leverage, or less?

## Paying the people inside

The rest of the world is already arguing about how. Bill Gates has proposed taxing AI tokens and robots, because a company that hires a person pays payroll taxes while one that buys a machine can write it off; in his words, the tax system nudges you toward replacing people with machines. He pairs it with "Human Reserved" work: jobs society deliberately keeps for people, the way we set aside nature reserves, with education and mental healthcare among his examples. Token taxes now have backers ranging from Mark Cuban to Elizabeth Warren. Critics point out the weaknesses: a token is a unit each company defines for itself, its price falls every year, and a tax on domestic providers quietly favours foreign ones.

The AI companies have their own plans. OpenAI's April blueprint proposes a public wealth fund, taxes on automated labour, trials of a 32-hour week, and safety-net payments that switch on automatically when displacement crosses set thresholds. Senator Bernie Sanders has gone further, proposing to put half the shares of the largest AI companies into an Alaska-style public fund, though since most of them pay no dividends yet, the fund could hold a fortune and pay out nothing. Meanwhile, unions are not waiting for governments. Workers at Microsoft's ZeniMax won contract language requiring AI to support employees rather than replace them, and requiring management to bargain before introducing new systems.

Susskind is honest about the limits of the redistribution route. A payout can deliver fairness in what people receive, but not the sense of contributing that work gives. Gates comes at it from the other side, asking how to keep people working at all. The best policies sit between them, acting before displacement rather than only after it.

→ These are all attempts at what [[Society-in-the-Loop — Rahwan 2018]] frames as the real alignment problem: not tuning a model's objective function, but building the deliberative, participatory structures — unions, levies, public funds — through which a society decides the terms on which it will be optimised against.

## What Singapore could try

Singapore's official answer, so far, is adaptation. Budget 2026 created a National AI Council and gives people taking selected SkillsFuture AI courses six months of free premium AI tools. Manpower Minister Tan See Leng has framed our approach as tripartism, not the tug of war between workers and businesses seen elsewhere. That is a real strength. But tripartism works when each side has leverage, and the gaps are visible. A Ministry of Manpower survey found about 6% of firms had already cut headcount because of AI. SkillsFuture Jobseeker Support is limited to people who earned up to $5,000 a month, which leaves out many of the professionals most exposed. In May, Parliament debated a motion on an "AI transition with no jobless growth", and the opposition proposed a National AI Equity Fund.

We have more of the machinery than we think. Five ideas, each an extension of something we already do:

1. **An AI levy.** We already price foreign labour through levies and dependency ratio ceilings, so firms think twice before relying too heavily on it. The same logic could apply to AI agents doing work at scale. Because the levy falls on the firm using the agent, not on the company that built the model, it avoids the main weakness of token taxes.
2. **A Human Reserved list.** We already reserve some jobs for citizens; taxi and private-hire licences are an example. A list of human-reserved roles, set through tripartite negotiation and reviewed over time, would turn Gates's idea into something we know how to run.
3. **An AI dividend from what we already own.** Unlike the United States, we do not need to seize shares. Part of the investment returns from our reserves already flows into the Budget. A slice could be set aside as a transition fund, paid out when AI-related job losses rise.
4. **Automatic triggers.** Expand Jobseeker Support automatically when AI-related retrenchments cross a set threshold, and lift the income cap that excludes professionals, managers and executives.
5. **A Creative Tax.** A levy on model developers for training and commercial use of creative and intellectual work, run by an independent collective body like the music rights societies. It would fund two pools: one paying the people whose work trained the models, and one sponsoring new human work, including regional models like SEA-LION, so the supply of fresh knowledge never runs dry.

The last idea has a precedent. In 1942, American musicians stopped recording because records were replacing live performers. The strike won a royalty paid into a union trust fund, which a later law made illegal, and a second strike in 1948 produced the Music Performance Trust Fund, paid from a share of record sales, which still funds free concerts by working musicians. It was Robin's strike with a different ending: the industry survived, and so did the musicians. Its flaws are worth learning from too. The money went to musicians in general rather than those on the records, and it shrank as record sales collapsed.

## Paying the translators

Robin had two choices: keep serving the tower, or bring it down with himself inside. Kuang gave him no third option, because the Empire would never offer one.

We are not in that story yet. The people who make and check knowledge still have leverage, and the companies still need them. We can let the tower fall, let it be rebuilt as it was, or help it break into many smaller towers that answer to the people inside them. The question is whether we build that bargain now, while both sides still have something to lose, or wait for the strike.

The tower doesn't have to fall. It has to start paying its translators.

---

## Sources

- [OpenAI: On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/)
- [Nature via AI Weekly: OpenAI posts 722 AI-generated math preprints, pulls three](https://aiweekly.co/alerts/openai-posts-722-ai-generated-math-preprints-pulls-three)
- [NYU Shanghai RITS: OpenAI drops 722 math manuscripts](https://rits.shanghai.nyu.edu/ai/openai-drops-722-math-manuscripts-from-an-unreleased-model)
- [Let's Data Science: OpenAI kept the prompts](https://letsdatascience.com/blog/openai-posted-722-ai-written-math-papers-kept-the-prompts)
- [Ukrainska Pravda: AHM statement](https://mezha.ua/en/news/mathematicians-urge-end-to-openai-collaboration-315962/)
- [Cybernews: TU Dresden mathematician](https://cybernews.com/ai-news/openai-accused-stealing-another-mathematicians-work/)
- [Epoch AI estimate (AP coverage)](https://www.adn.com/nation-world/2024/06/06/ai-gold-rush-for-chatbot-training-data-could-run-out-of-human-written-text/)
- [International AI Safety Report](https://arxiv.org/pdf/2501.17805)
- [Rest of World: Western open-weight models still can't beat China](https://restofworld.org/2026/china-open-weight-models/)
- [ATOM Report summary](https://digg.com/tech/vxin99ju)
- [TrendForce: Chinese models' global share](https://trendforce.com/news/2026/01/26/news-chinese-ai-models-reportedly-hit-15-global-share-in-nov-2025-fueled-by-deepseek-open-source-push/)
- [Startup Fortune: China and the Global South](https://startupfortune.com/china-is-winning-the-global-souths-ai-future-by-giving-models-away-for-free/)
- [Cornford and Cross: China's tiered access](https://cornfordandcross.com/digital-ai-art/the-ai-influence-on-the-china-open-weight-gateway-to-global-power/)
- [StartupHub: The 'But China' excuse is wearing thin](https://www.startuphub.ai/news/the-but-china-excuse-is-wearing-thin)
- [ThePrint: Why China will not slow down](https://theprint.in/opinion/us-china-donald-trump-xi-jinping-summit-ai-governance/3059125/)
- [Ground News: China on Anthropic's slowdown proposal](https://ground.news/article/769ad69a-212d-4378-ac78-c33527c8b90e)
- [Rest of World: Karen Hao interview](https://restofworld.org/2025/google-facebook-password-leak/karen-hao-empire-of-ai-book)
- [HR Executive: Gates's AI plan](https://hrexecutive.com/?p=165658)
- [Simulating a Post-Automation Economy (token tax debate)](https://arxiv.org/pdf/2606.20649)
- [Tech Insider: OpenAI blueprint](https://tech-insider.org/openai-robot-tax-blueprint-four-day-workweek-2026/)
- [Moneywise: Sanders' AI sovereign wealth fund](https://moneywise.com/news/top-stories/bernie-sanders-ai-sovereign-wealth-fund-government-stake-openai)
- [Allwork.Space: Union contracts and AI](https://allwork.space/2026/07/union-contracts-emerge-as-one-of-workers-strongest-ai-protections/)
- [People Matters: Budget 2026 AI agenda](https://sea.peoplemattersglobal.com/amp/article/economy-policy/singapore-budget-2026-and-the-ai-nation-agenda-pm-wong-details-ai-push-and-workforce-plans-48396)
- [People Matters: Tan See Leng on good jobs](https://sea.peoplemattersglobal.com/news/ai-and-emerging-tech/singapore-says-ai-must-create-good-jobs-not-mass-layoffs-49613)
- [Music Performance Trust Fund history](https://musicpf.org/?p=2321)
- [NPR: A dwindling trust](https://www.npr.org/transcripts/139951603)

---

## Related Research

**Directly cited / closely linked:**
- [[System of Professions — Abbott 1988]] — jurisdictional claims as the frame for "who validates the proof" once AI drafts it
- [[AI Deskilling — Ferdman 2026]] — structural case for why task encroachment erodes skill rather than just saving time
- [[AI Professional Identity — Ahuja 2026]] — the oscillating identity work of the humans left validating AI output
- [[Moral Deskilling Upskilling — Vallor 2015]] — the ethical stakes of skill erosion, distinct from productivity loss
- [[Society-in-the-Loop — Rahwan 2018]] — alignment as a governance/participation problem, the lens for reading the essay's policy proposals

**Thematically connected:**
- [[Sociology of Professions]] — core theme node; jurisdiction, deskilling, and identity fragmentation under AI adoption
- [[AI Safety & Alignment]] — governance and participation as the real alignment problem, not just model tuning
- [[Symbiotic Design Framework]] — the parasitism/symbiosis distinction this essay applies at industry scale: does the tower return capacity and control to the people who feed it, or only extract from them
