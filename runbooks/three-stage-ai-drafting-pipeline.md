# Three-Stage AI Drafting Pipeline

This runbook assumes the team can remember one public link and type short commands into an allowed GPT/Codex-style model.

Memorize:

```text
https://github.com/goranihani/lacpsp
```

## Rule Gate

Before using any tool, lock the field rule:

| Tool | Status | Action |
| --- | --- | --- |
| GPT or Codex free/basic | allowed only if organizer permits | use short prompts |
| SuperLawyer | HOLD unless expressly allowed | do not use if not listed |
| LBOX | HOLD unless expressly allowed | do not use if not listed |
| GitHub website browsing by humans | avoid unless expressly allowed | type the remembered link into GPT/Codex instead |

If the official rule says only GPT/Codex free versions are allowed, skip SuperLawyer/LBOX and use the substitute review prompts in `prompts/07-field-shorthand-commands.md`.

## 3-Hour Flow

| Time | Track A | Track B | AI turn |
| --- | --- | --- | --- |
| 09:00-09:10 | read official rule and problem instructions | check allowed tools and file rules | none |
| 09:10-09:25 | mark questions and tentative conclusions | upload problem to allowed GPT/Codex | Turn 1: `lacpsp 초벌 진행` |
| 09:25-09:45 | turn first draft into answer skeleton | make HOLD/source queue | Turn 2: compress HOLD queue |
| 09:45-10:20 | draft core answer paragraphs | if allowed, run SuperLawyer and LBOX second-draft prompts; if not allowed, run GPT/Codex substitute reviews | Turn 3: second-draft split |
| 10:20-11:10 | write answer from strongest confirmed points | compare second drafts and mark CONFIRM/MODIFY/HOLD/DELETE | none unless necessary |
| 11:10-11:45 | revise weak issues and counterarguments | prepare two second-draft summaries for merge | Turn 4: `3차본 + AI활용내역서` |
| 11:45-12:20 | final third-draft answer editing | AI-usage report, source queue, tool-use truthfulness | Turn 5: AI-usage report |
| 12:20-12:45 | final legal read | metadata, anonymity, file format, remaining HOLD removal | no new broad AI |
| 12:45-13:00 | freeze answer | submit and confirm | no new AI except fatal formatting issue |

## First-Draft Command

```text
https://github.com/goranihani/lacpsp 초벌 진행할거야.
업로드한 문제 파일을 기준으로 1차 초본, 쟁점 계약표, 공식근거 확인 큐, AI활용내역서 소재, A/B 다음 15분 작업을 만들어줘.
검증 전 근거는 전부 HOLD로 표시해줘.
```

## Second-Draft Prompts

Use only if SuperLawyer and LBOX are expressly allowed.

SuperLawyer:

```text
아래 1차 초본을 검토해서 법적 쟁점 누락, 판례/조문 후보, 반론, 결론 위험만 표로 정리해줘.
제출본 문장은 쓰지 말고, 검증 전 근거는 HOLD로 표시해줘.
[1차 초본 붙여넣기]
```

LBOX:

```text
아래 1차 초본을 검토해서 법령·판례 후보, 반대논거, 문장 구조상 약점을 표로 정리해줘.
제출본 문장은 쓰지 말고, 검증 전 근거는 HOLD로 표시해줘.
[1차 초본 붙여넣기]
```

Substitute if legal AI is not allowed:

```text
SuperLawyer/LBOX는 현장 허용 도구가 아니므로 사용하지 않는다.
대신 아래 1차 초본을 검토자 A 관점과 검토자 B 관점으로 나누어, 누락 쟁점·반론·HOLD 근거만 표로 정리해줘.
새 법령번호나 판례명은 만들지 마라.
[1차 초본 붙여넣기]
```

## Third-Draft Merge Command

```text
https://github.com/goranihani/lacpsp 슈퍼로이어와 엘박스 2차본 두가지로 3차본을 만듬과 동시에 ai사용방법에 대한 내용도 만들어줘.

입력:
1차 초본:
[붙여넣기]

2차본 A:
[붙여넣기]

2차본 B:
[붙여넣기]

공식 확인된 근거:
[붙여넣기]

아직 HOLD인 근거:
[붙여넣기]

요구:
1. 두 2차본 차이표
2. CONFIRM/MODIFY/HOLD/DELETE 판정
3. 질문별 3차본 답안
4. AI활용내역서 초안
5. 제출 전 위험 5개

만약 SuperLawyer/LBOX가 공식 허용 도구가 아니라면, 그 도구를 사용했다고 쓰지 말고 GPT/Codex와 사람 검증만 사용한 것으로 정리해줘.
```
