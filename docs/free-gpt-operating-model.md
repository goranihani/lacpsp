# Free/Basic GPT Operating Model

The live pack assumes only a free/basic GPT-style model may be available. It must work without long context, custom instructions, advanced file upload, persistent memory, browsing guarantees, or paid model reliability.

## Operating Rules

- Use short prompts.
- Ask for tables, not long memos.
- Split tasks into intake, candidate search, verification, critique, and report.
- Never ask the model to decide final law from memory.
- Treat every statute, case, deadline, regulator name, and translation as `HOLD` until checked against an official source.
- Keep a human-owned ledger of what was adopted, modified, rejected, or held.

## Prompt Budget

| Stage | Prompt Size | Output Target |
| --- | --- | --- |
| Intake | 10-15 lines | questions, facts, issue candidates |
| Candidate search | 8-12 lines | statutes/cases/source candidates only |
| Foreign law | 8-12 lines | source IDs and risk expressions |
| Critic | 8-12 lines | missing issues and overclaims |
| AI usage | 8-12 lines | report material, not transcripts |

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

