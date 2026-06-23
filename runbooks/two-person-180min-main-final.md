# Two-Person 180-Minute Main/Final Runbook

Use this as a rehearsal sheet. On site, follow organizer instructions first.

## Roles

| Role | Owner | Mission |
| --- | --- | --- |
| Track A | answer lead | conclusions, issue priority, application, counterarguments, final wording |
| Track B | verification lead | AI operation, source verification, AI-usage report, format and submission safety |

## Free-Model Usage Control

Track B owns the model budget. The normal plan is 5 turns maximum; the emergency plan is 3 turns.

| Budget item | Rule |
| --- | --- |
| Essential turns | `1` first draft, `3` third-draft merge, `ai` AI-use report |
| Optional turns | HOLD/source compression and adversarial/substitute review |
| Stop trigger | limit warning, file-read failure after one retry, weak-model fallback, or 12:25 clock line |
| Codex free use | optional only; use for short checklist, consistency scan, or formatting, not long research |

Visible note for B:

```text
Model budget: turn __ / 5, file access YES/NO, warning YES/NO, fallback at __:__.
```

## No-Idle Rule

A and B should never wait for the other person to finish a broad task. Every block has a primary task, a secondary task, and a handoff sentence. If one track finishes early, that person immediately moves to the matching standby task.

| Situation | Track A standby task | Track B standby task |
| --- | --- | --- |
| Waiting for AI output | write direct conclusion and fact hooks | fill AI-usage ledger shell and verification status |
| Waiting for source check | tighten issue priority and page budget | mark source as CONFIRM, MODIFY, HOLD, or DELETE |
| Waiting for draft paragraph | prepare counterargument and fallback conclusion | check citation/source risk and report material |
| Waiting for final wording | scan answer for question-by-question directness | scan metadata, anonymity, file name, and tool-use consistency |
| Conflict between A and B | state answer impact in one sentence | state rule/source/submission risk in one sentence |

Use this micro-loop every 5 minutes:

```text
A: I am locking ___ / I need ___ / I am dropping ___.
B: I confirmed ___ / I hold or delete ___ / I need ___.
Next 5 minutes: A ___, B ___.
```

## Time Plan

| Time | Track A | Track B | Locked Output |
| --- | --- | --- | --- |
| 09:00-09:30 | review official instructions and write allowed/forbidden list | account/device smoke test and new-account baseline prompt | allowed-tool status |
| 10:00-10:10 | read problem, mark questions, draft direct conclusions | log official instructions, facts, deadlines, file rules | intake |
| 10:10-10:25 | lock direct conclusions, issue priority, page budget | run turn 1 if allowed; choose 3-5 verification targets | issue contract |
| 10:25-10:45 | build answer skeleton and first application bullets | verify top sources; use optional turn 2 only for source/HOLD compression | source status table |
| 10:45-11:05 | convert skeleton into headings and paragraph order | mark CONFIRM/MODIFY/HOLD/DELETE risks | answer skeleton |
| 11:05-11:35 | write core application for strongest issues | use optional turn 3 only for adversarial/substitute review; update source ledger | draft block 1 |
| 11:35-12:05 | write counterarguments, fallback conclusions, remedies | verify remaining sources and collect AI-usage report material | draft block 2 |
| 12:05-12:25 | refine conclusions and remove weak overclaims | use turn 4 for third-draft merge only if the draft inputs are ready | report draft |
| 12:25-12:40 | judge-style attack and final legal corrections | consistency, metadata, anonymity, tool-use report check | submit candidate |
| 12:40-12:45 | read final answer aloud by headings | use turn 5 only for AI-use report material or skip AI entirely | final review |
| 12:45-12:50 | no new content; only fatal issue notes | file, format, and venue-approved transfer readiness | final file |
| 12:50-13:00 | no edits except fatal issue; confirm final version | submit or assist submission and confirm receipt | submission evidence |

## Parallel Work Diagram

```text
09:00  A rules intake + allowed/forbidden list
       B account/device/tool smoke test

10:00  A questions -> direct conclusions -> issue priority
       B facts/rules log -> verification targets -> AI queue

10:25  A answer skeleton -> application bullets
       B official sources -> foreign-law signals -> HOLD/DELETE list

11:05  A core drafting
       B AI/source cross-check + AI-usage ledger

12:05  A conclusion tightening + overclaim removal
       B AI-usage report + answer/report consistency

12:25  A judge-style attack corrections
       B metadata/anonymity/file/tool-use safety

12:50  A final version freeze
       B submission execution/confirmation
```

No blank cell means no spectator mode. If A is typing, B is verifying or recording. If B is operating AI, A is writing or narrowing. If either person is blocked for more than 90 seconds, call the 5-minute micro-loop early.

## First 25-Minute Lock

By 10:25, stop expanding and lock:

- questions
- direct conclusion for each question
- 3-5 A-level issues
- 3 official source checks
- any foreign-law signal
- page budget
- AI-usage ledger IDs

## Stop Lines

| Time | Stop |
| --- | --- |
| 10:25 | stop rereading the whole problem |
| 10:45 | stop open-ended source searching |
| 12:05 | stop broad answer expansion |
| 12:25 | stop new issues, new cases, new foreign law |
| 12:45 | stop content additions |
| 12:50 | stop editing and submit |

## 15-Minute Handoff

```text
Locked judgment:
Newly verified source:
HOLD/DELETE:
Next 15 minutes:
Stop doing:
```
