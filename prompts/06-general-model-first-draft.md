# General GPT First-Draft Prompt

Use this with an allowed basic GPT-style model after uploading the competition problem file. The model may be able to read public links, but it must not rely on private memory, prior chats, paid features, or unverified citations.

```text
You are helping a two-person lawschool AI competition team.
Use only the uploaded problem file and these two public GitHub links to create a first-draft answer:

1. https://github.com/goranihani/lacpsp
2. https://github.com/legalize-kr/legalize-pipeline

Important:
- This is a first draft for human revision, not a final submission answer.
- Do not invent statute numbers, article numbers, case names, case numbers, deadlines, agencies, or foreign-law conclusions from memory.
- Mark every unverified legal authority as [HOLD: official source check required].
- Treat legalize-pipeline as public context about Korean statute/case data collection and verification workflow, not as the official authority itself.
- Treat lacpsp as public context about two-person no-idle workflow, HOLD/DELETE, AI-usage reporting, and official-source verification.
- Do not reproduce the full problem text. Summarize only the facts needed for analysis.

First report only these four lines:
1. Problem file read: YES/NO
2. lacpsp accessed: YES/NO
3. legalize-pipeline accessed: YES/NO
4. Continue with a first draft even if public links are inaccessible: YES

Then create the first draft in this structure:

I. Problem Intake Table
Columns:
- Q-ID
- question demand
- key facts
- actors
- data/AI/contract/administrative/criminal/civil flow
- tentative conclusion
- official source to check
- status: CONFIRM/MODIFY/HOLD/DELETE

II. Issue Contract Table
Columns:
- Issue-ID
- priority A/B
- issue
- why it matters for scoring
- possible statute/case/guidance candidates
- official verification route
- answer location
- HOLD/DELETE reason

III. First-Draft Answer
For each question, begin with the direct conclusion.
Use this order:
1. conclusion
2. legal standard candidate
3. application to facts
4. counterargument or unfavorable fact
5. mini-conclusion

Add [HOLD: official source check required] to every unverified statute, case, guidance, deadline, agency, or foreign-law statement.

IV. Official Source Check Queue
Columns:
- priority
- source candidate
- why needed
- where to verify
- answer location if confirmed
- fallback sentence if not confirmed

V. AI-Usage Report Material
Columns:
- U-ID
- what GPT did
- what humans must verify
- adopt/modify/reject/hold candidate
- hallucination or limitation risk
- one sentence usable in the AI-usage report

VI. No-Idle A/B Next 15 Minutes
Columns:
- time
- Track A task
- Track B task
- five-minute handoff sentence
- stop line

VII. Final Human Warnings
List only five risks humans must check before submission.
```
