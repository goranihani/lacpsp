# Field Shorthand Commands

Use this file when the field model can read `https://github.com/goranihani/lacpsp`, but the team cannot browse GitHub manually. The human may type only one short Korean command. Interpret the command using the rules below.

## Memorized Link

```text
https://github.com/goranihani/lacpsp
```

## Command 1: First Draft

If the user says any of the following:

```text
goranihani/lacpsp 초벌 진행할거야
lacpsp 초벌 진행
lacpsp 1차 초본
```

Do this:

```text
You are in FIRST-DRAFT mode.
Use the uploaded problem file and public lacpsp workflow context only.
Create a first-draft answer, not a final submission.
Do not invent statutes, articles, cases, deadlines, agencies, or foreign-law conclusions.
Mark unverified legal claims as [HOLD: official source check required].

Return:
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
goranihani/lacpsp 슈퍼로이어와 엘박스 2차본 두가지로 3차본을 만듬과 동시에 ai사용방법에 대한 내용도 만들어줘
lacpsp 2차본 통합해서 3차본과 AI사용내역 만들어줘
lacpsp 3차본 + AI활용내역서
```

Do this:

```text
You are in THIRD-DRAFT MERGE mode.
Inputs:
- first draft
- second draft A
- second draft B
- source-check status
- field rule on allowed AI tools

Do not assume second drafts are correct.
Compare the two second drafts and classify every meaningful difference as:
CONFIRM, MODIFY, HOLD, DELETE, or STYLE ONLY.

Create:
1. difference table between second drafts
2. final issue order
3. third-draft answer by question
4. official source check queue still open
5. AI-usage report draft explaining how GPT/Codex and any allowed legal AI were used
6. final submission risk list

If SuperLawyer or LBOX were not expressly allowed, do not write that they were used. Instead write that the team used only allowed GPT/Codex-style tools and human verification.
```

## Free-Model Usage Guard

Use at most five GPT/Codex turns unless the human says `긴급 추가`.

| Turn | Purpose | Prompt length |
| --- | --- | --- |
| 1 | first draft from problem file | one master prompt |
| 2 | HOLD/source queue compression | 8 lines or less |
| 3 | second-draft prompt generation or substitute review | 10 lines or less |
| 4 | third-draft merge | one compact merge prompt |
| 5 | AI-usage report and final risk list | 10 lines or less |

Never spend a turn asking the model to restate the full GitHub repository. Ask it to use `lacpsp` as workflow context, then move directly to the required output.
