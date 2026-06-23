# Free/Basic GPT Operating Model

The live pack assumes only a free/basic GPT-style model may be available. It must work without long context, custom instructions, advanced file upload, persistent memory, browsing guarantees, or paid model reliability.

## Operating Rules

- Use short prompts.
- Ask for tables, not long memos.
- Split tasks into intake, candidate search, verification, critique, and report.
- Never ask the model to decide final law from memory.
- Treat every statute, case, deadline, regulator name, and translation as `HOLD` until checked against an official source.
- Keep a human-owned ledger of what was adopted, modified, rejected, or held.

## Public Link Intake

If the venue allows a basic GPT-style model and allows public links, give the model only public preparation links first. Do not give it real competition facts until it has confirmed what it can and cannot access.

Recommended order:

1. Send the two public links and ask for an access report.
2. If access works, ask for a short no-idle A/B operating table.
3. If access fails, paste only a public excerpt from the README or runbook.
4. After the workflow is loaded, send the real problem only in short chunks allowed by the organizer.
5. Keep all final legal judgments human-owned.

Access check prompt:

```text
I gave you two public preparation links.
Before using them, tell me:
1. which pages you actually accessed
2. which headings you saw
3. which parts you could not access
4. what public excerpt I should paste if access failed

Do not summarize anything you did not actually access.
```

No-idle conversion prompt:

```text
Using only the public workflow context you can access, convert the two-person plan into a no-idle plan.
A must always be drafting, narrowing, attacking, or freezing answer content.
B must always be verifying, operating allowed AI, logging AI use, checking source risk, or preparing submission safety.

Return a table with:
time, A active task, B active task, if-finished-early task, 5-minute handoff, locked output.
```

If the model cannot access links:

```text
You cannot access the links. Use only the public excerpt below.
Do not infer missing rules.
Return a no-idle A/B plan and short prompts for the next 15 minutes.

[paste public excerpt]
```

## Prompt Budget

| Stage | Prompt Size | Output Target |
| --- | --- | --- |
| Intake | 10-15 lines | questions, facts, issue candidates |
| Candidate search | 8-12 lines | statutes/cases/source candidates only |
| Foreign law | 8-12 lines | source IDs and risk expressions |
| Critic | 8-12 lines | missing issues and overclaims |
| AI usage | 8-12 lines | report material, not transcripts |

## Five-Turn Field Budget

Assume the free/basic model may run out of turns. Do not spend turns asking it to summarize the whole repository. Move directly to the output needed for the round.

| Turn | Use | Stop after |
| --- | --- | --- |
| 1 | first draft from uploaded problem and `lacpsp` context | first-draft answer plus HOLD queue |
| 2 | compress HOLD/source queue | top 10 checks only |
| 3 | second-draft split or substitute review | differences and risks only |
| 4 | third-draft merge | answer plus CONFIRM/MODIFY/HOLD/DELETE table |
| 5 | AI-usage report and final risk list | report material plus five submission risks |

If the model cannot access GitHub, paste the short command from `prompts/07-field-shorthand-commands.md` instead of the full repository.

## Avoid

- "Write the final answer from scratch."
- "Find every legal issue."
- "Give me all relevant foreign law."
- "Cite cases with exact numbers from memory."
- "Use previous chats or uploaded repository context."

These prompts are too broad for a basic model and invite hallucinated citations.

## Prefer

```text
Return only a table with: claim, source candidate, official source to verify, risk if unverified, status.
```

```text
Do not create statute numbers or case numbers. If you are not certain, mark HOLD.
```

```text
Give me three strongest counterarguments and the fact that would decide each.
```

## Human Lock

The model can propose. Humans lock:

- direct conclusion for each question
- legal issue priority
- whether a source is verified
- whether a foreign-law issue changes the answer or only adds practical risk
- final wording
- submission approval
