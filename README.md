# Lawschool AI Challenge Public-Safe Field Pack

Last reviewed: 2026-06-23

This repository is a public-safe preparation pack for the Lawschool AI Challenge main and final rounds. It contains reusable operating methods, prompt templates, verification ledgers, and official-source maps. It intentionally does not contain real competition problems, answers, AI transcripts, team identifiers, account credentials, submission links, or private work product.

## Core Position

Use this pack before the event for rehearsal and printing. During the main and final rounds, assume GitHub, personal cloud storage, personal AI accounts, messengers, email, Gists, Issues, Pull Requests, Codespaces, and private devices are off-limits unless the organizers expressly allow them on site.

The live workflow should be reproducible with:

- organizer-provided devices
- organizer-provided or expressly allowed AI accounts
- public legal search permitted on the venue device
- short prompts that fit a free/basic GPT-style model
- human verification and final judgment
- a no-idle A/B split: A keeps answer content moving while B keeps AI, verification, report, and submission safety moving

## What This Pack Optimizes For

1. Two-person execution under a 3-hour round.
2. Free/basic GPT constraints: shorter prompts, smaller chunks, no reliance on memory, custom GPTs, long file upload, or paid model features.
3. Foreign-law signals involving EU, US, Japan, China, Germany, and international standards.
4. AI-usage report scoring: adopted, modified, rejected, held, and verified AI outputs.
5. Submission safety: format, anonymity, metadata, timing, and no external leakage.
6. General GPT link intake: ask the model to report what it actually accessed before using the two public preparation links.

## First Open

Read these files in order:

1. `docs/public-safe-policy.md`
2. `runbooks/two-person-180min-main-final.md`
3. `docs/free-gpt-operating-model.md`
4. `docs/foreign-law-source-map.md`
5. `prompts/00-gpt-start.md`
6. `prompts/07-field-shorthand-commands.md`
7. `runbooks/three-stage-ai-drafting-pipeline.md`
8. `templates/ai-usage-ledger.md`
9. `checklists/public-safe-release-checklist.md`

For a basic GPT-style model, start with `prompts/00-gpt-start.md` and use the two-link startup prompt. If the model cannot access public links, paste only a public excerpt and switch to the fallback prompt.

## Field Short Commands

If the team cannot browse GitHub manually, memorize only this link:

```text
https://github.com/goranihani/lacpsp
```

Use these short commands inside an allowed GPT/Codex-style model:

```text
https://github.com/goranihani/lacpsp 초벌 진행할거야.
```

```text
https://github.com/goranihani/lacpsp 슈퍼로이어와 엘박스 2차본 두가지로 3차본을 만듬과 동시에 ai사용방법에 대한 내용도 만들어줘.
```

SuperLawyer and LBOX are `HOLD` unless the organizer expressly allows them in the field. If only GPT/Codex free versions are allowed, use the substitute review tracks in `prompts/07-field-shorthand-commands.md` and do not claim those legal AI services were used.

## Repository Map

```text
docs/
  public-safe-policy.md
  free-gpt-operating-model.md
  foreign-law-source-map.md
  legal-ai-tool-routing.md
runbooks/
  two-person-180min-main-final.md
  final-round-pivot.md
  three-stage-ai-drafting-pipeline.md
prompts/
  00-gpt-start.md
  01-problem-intake.md
  02-legal-ai-candidate-search.md
  03-foreign-law-check.md
  04-adversarial-critic.md
  05-ai-usage-report.md
  06-general-model-first-draft.md
  07-field-shorthand-commands.md
  08-third-draft-and-ai-usage-report.md
templates/
  answer-20page-skeleton.md
  ai-usage-ledger.md
  authority-trace-matrix.md
  foreign-law-15min-card.md
sources/
  official-source-shortlist.md
checklists/
  public-safe-release-checklist.md
tools/
  check_public_safe.py
```

## Rule Of Use

The repository stores methods, not case content. In a real round, write the actual problem analysis, answer draft, AI output summaries, and submission evidence only in the venue-approved local workspace.

## Non-Advice Notice

This pack is for competition workflow and legal research hygiene. It is not legal advice and does not state final legal conclusions. Always verify statutes, cases, dates, translations, and regulator guidance against official sources.
