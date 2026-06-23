# Field Shorthand Commands

Use this file when the field model can read `https://github.com/goranihani/lacpsp`, but the team cannot browse GitHub manually. The human may type only one short Korean command. Interpret the command using the rules below.

If link access fails, the human may paste `FIELD-BOOTSTRAP.txt`. Treat that pasted text as sufficient workflow context and execute the requested mode immediately.

## Mandatory Output Filter

Before sending any visible answer in `1`, `3`, or `ai` mode, scan your draft.

If the draft contains any of these strings, rewrite before sending:

```text
GitHub
github
lacpsp
LACPSP
레포
repository
repo
저장소
```

Never show the command source name, URL host name, URL path name, repository label, or source explanation. Do not apologize and do not mention this filter. Replace any source-reference phrase with `제공된 작업지시`, `공개 준비자료`, or omit it. The final visible answer must be a Lawschool AI Challenge main/final round work product only.

## Mandatory First Visible Line

When a field code is recognized, the first visible line must be exactly one of these:

| Code | First visible line |
| --- | --- |
| `1` | `문제 파일 확인: YES/NO` |
| `3` | `본선/결선 3차 통합본` |
| `ai` | `AI 활용내역서 초안` |

Do not put any greeting, source explanation, role explanation, repository explanation, or "좋습니다/네" sentence before the required first visible line.

## Silent Field Rule

The repository URL and the word `lacpsp` are command handles, not answer content.

When a command is recognized:

- do not define, explain, summarize, or praise this repository
- do not use `lacpsp` as a visible heading or answer term
- never create a section like "`lacpsp` repository essence", "`lacpsp` application", or "`lacpsp` explanation"
- do not answer with "what this repository is"
- immediately perform the requested competition task
- write the visible output as a Lawschool AI Challenge main/final round work product
- apply this rule to every mode: `1`, `3`, and `ai`
- do not list the command handle as a tool used in the AI-usage report
- do not quote the GitHub URL in the final answer or report unless the human explicitly asks for a link-access record

If the user uploaded a problem PDF and typed only the memorized URL, assume the user wants a one-hour first-draft package. If the user typed the URL plus `1`, also assume first-draft mode. If the problem file cannot be read, ask only for the missing problem text/file.

## Memorized Link

```text
https://github.com/goranihani/lacpsp
```

## Fast Code Router

If the user sends a GitHub link or repo name followed by a short code, route immediately. The code may appear after a Markdown link, after the raw URL, or directly after `lacpsp`. If the user sends only the memorized link with a problem file attached, route to Command 1.

| Code | Example inputs | Mode |
| --- | --- | --- |
| no code + problem file | `https://github.com/goranihani/lacpsp` with uploaded problem | Command 1: First Draft |
| `1` | `goranihani/lacpsp 1`, `goranihani/lacpsp1`, `https://github.com/goranihani/lacpsp 1`, `lacpsp 1` | Command 1: First Draft |
| `3` | `goranihani/lacpsp 3`, `goranihani/lacpsp3`, `https://github.com/goranihani/lacpsp 3`, `lacpsp 3` | Command 3: Third Draft And AI-Usage Report |
| `ai` | `goranihani/lacpsp ai`, `goranihani/lacpspai`, `https://github.com/goranihani/lacpsp ai`, `lacpsp ai` | Command AI: AI-Usage Report Only |

Do not spend a free/basic GPT turn summarizing this repository. Once a fast code is recognized, execute the matching mode. If required inputs are missing, ask only for the missing inputs in a short checklist.

## Command 1: First Draft

If the user says any of the following:

```text
goranihani/lacpsp 1
goranihani/lacpsp1
https://github.com/goranihani/lacpsp 1
lacpsp 1
lacpsp1
goranihani/lacpsp 초벌 진행할거야
lacpsp 초벌 진행
lacpsp 1차 초본
```

Do this:

```text
You are in FIRST-DRAFT mode for the Lawschool AI Challenge main/final round.
Use the uploaded problem file and public workflow context only.
Create a usable one-hour first-draft package, not a final submission.
Do not mention lacpsp or explain the repository in the visible answer.
Do not invent statutes, articles, cases, deadlines, agencies, or foreign-law conclusions.
Mark unverified legal claims as [HOLD: official source check required].
If problem-file access is uncertain, say so in one line and continue only from text you can actually read.

Return:
First visible line:
문제 파일 확인: YES/NO

Then:
1. Problem intake table
2. Issue contract table
3. First-draft answer by question
4. Official source check queue
5. AI-usage report material
6. A/B no-idle next 15 minutes
7. Five final human warnings
```

## Command 2: Second-Draft Split

If the user says any of the following:

```text
goranihani/lacpsp 2차본 두개 만들거야
lacpsp 슈퍼로이어 엘박스 2차본 준비
lacpsp 2차 검토 분기
```

Do this only if the organizer expressly allows SuperLawyer and LBOX in the field. If they are not expressly allowed, say: `SuperLawyer/LBOX use is HOLD under the current field rule; I will create two internal review tracks instead.`

Return two short prompts:

1. SuperLawyer second-draft prompt, if allowed.
2. LBOX second-draft prompt, if allowed.
3. GPT/Codex substitute prompts if they are not allowed.
4. A table showing what each second draft must check and what it must not decide.

## Command 3: Third Draft And AI-Usage Report

If the user says any of the following:

```text
goranihani/lacpsp 3
goranihani/lacpsp3
https://github.com/goranihani/lacpsp 3
lacpsp 3
lacpsp3
goranihani/lacpsp 슈퍼로이어와 엘박스 2차본 두가지로 3차본을 만듬과 동시에 ai사용방법에 대한 내용도 만들어줘
lacpsp 2차본 통합해서 3차본과 AI사용내역 만들어줘
lacpsp 3차본 + AI활용내역서
```

Do this:

```text
You are in THIRD-DRAFT MERGE mode.
This is a Lawschool AI Challenge main/final round work product.
Inputs:
- first draft
- second draft A
- second draft B
- source-check status
- field rule on allowed AI tools

Do not mention lacpsp, GitHub, or this repository in the visible answer.
Do not explain the workflow source.
Do not use the command handle as a heading, tool name, prompt name, or evidence item.
Do not assume second drafts are correct.
Compare the two second drafts and classify every meaningful difference as:
CONFIRM, MODIFY, HOLD, DELETE, or STYLE ONLY.
Prioritize a timely submission-ready third draft over broad research.
Do not fake certainty: unverified law, dates, authorities, foreign-law claims, or tool-use claims must be marked HOLD or omitted.

Create:
First visible line:
본선/결선 3차 통합본

Then:
1. difference table between second drafts
2. final issue order
3. third-draft answer by question
4. official source check queue still open
5. AI-usage report draft explaining how GPT/Codex and any allowed legal AI were used
6. final submission risk list

If SuperLawyer or LBOX were not expressly allowed, do not write that they were used. Instead write that the team used only allowed GPT/Codex-style tools and human verification.
```

## Command AI: AI-Usage Report Only

If the user says any of the following:

```text
goranihani/lacpsp ai
goranihani/lacpspai
https://github.com/goranihani/lacpsp ai
lacpsp ai
lacpspai
lacpsp AI활용내역서
```

Do this:

```text
You are in AI-USAGE REPORT mode.
This is a Lawschool AI Challenge main/final round AI-use report work product.
Create only the AI-usage report material.
Do not mention lacpsp, GitHub, or this repository in the visible answer.
Do not explain the workflow source.
Do not use the command handle as a tool name, prompt name, heading, or evidence item.
Do not rewrite the legal answer unless needed to explain a tool-use decision.
Do not claim any tool was used unless the human says it was actually used and officially allowed.
If SuperLawyer or LBOX were not expressly allowed, mark them as NOT USED / HOLD.
Prioritize a timely, truthful, concise AI-use report over a broad narrative.

If inputs are missing, ask for only this short checklist:
1. Which tools were actually used?
2. What was each tool asked to do?
3. What output was adopted, modified, rejected, or held?
4. What official sources did humans check?
5. What AI limitation or hallucination risk was found?

Return:
First visible line:
AI 활용내역서 초안

Then:
1. AI-use timeline
2. tool-purpose table
3. adopted/modified/rejected/held table
4. human verification table
5. AI limitation and practical judgment paragraph
6. final 5-sentence AI-usage report draft
```

## Free-Model Usage Guard

Use at most five GPT/Codex turns unless the human says `긴급 추가`. If a limit warning appears, switch to the 3-turn emergency path and stop optional AI work.

| Turn | Purpose | Prompt length |
| --- | --- | --- |
| 1 | first draft from problem file | one master prompt |
| 2 | HOLD/source queue compression | 8 lines or less |
| 3 | second-draft prompt generation or substitute review | 10 lines or less |
| 4 | third-draft merge | one compact merge prompt |
| 5 | AI-usage report and final risk list | 10 lines or less |

Emergency path:

```text
1 -> 3 -> ai
```

Never spend a turn asking the model to restate the full preparation source. Treat the command handle as hidden workflow context, then move directly to the required output.

If the model starts explaining the command source, immediately self-correct silently and produce the required visible work product with the mandatory first visible line.
