# Free ChatGPT/Codex Usage Limits And Field Plan

Last checked against official OpenAI pages: 2026-06-23.

This document is a field rule for the Lawschool AI Challenge main/final rounds when the team may use only free GPT/Codex-style tools. It records what is official, what is not numerically promised, and how the team should avoid running out of model access during a 3-hour round.

## Official Limit Snapshot

| Tool/model surface | Free-plan status | Field assumption |
| --- | --- | --- |
| GPT-5.5 Instant | Available to all users. Free access is limited within a 5-hour window and resets after that window. The limit can vary with system conditions, and the chat may move to a smaller model after the limit. | Treat the whole 3-hour round as one no-reset window. Use 3 essential turns, 5 maximum turns. |
| GPT-5.5 Instant context | OpenAI release notes state a 16k context window for free users. The pricing page separately lists GPT Instant at 27K. | Plan for the smaller 16k window. Do not paste long background material. |
| GPT-5.5 Thinking | Not included in the Free plan on the pricing page. | Do not build the plan around it. |
| GPT-5.5 Pro | Not included in the Free plan on the pricing page. | Do not rely on it. |
| GPT-5 Thinking Mini | Listed as available on the Free plan on the pricing page. | Use only if it appears in the venue account, mainly for short review or formatting. |
| File upload, data analysis, image generation, voice | Limited access on the Free plan. | Upload the problem once. If upload fails, paste only short permitted excerpts. |
| Deep research, Codex agent, Codex CLI | Limited access on the Free plan. | Use as optional support only. Do not assign a mission-critical long task to it. |

OpenAI does not publish a fixed free-message number for GPT-5.5 Instant. The reliable rule is the 5-hour reset window plus dynamic limits. The competition plan therefore controls the number of model interactions instead of trying to predict the hidden cap.

## Best Field Plan

Use one chat for the main answer flow unless it becomes unusable. Starting many fresh chats wastes setup turns and can lose the problem context.

| Budget | When to use | Turns |
| --- | --- | --- |
| Emergency budget | Limit warning, upload problem is long, or model is slow | `1` -> `3` -> `ai` |
| Normal budget | Model works and outputs are useful | `1` -> source/HOLD compression -> substitute review -> `3` -> `ai` |
| No more AI | Model moves to a weaker model, refuses files, or limit is reached | Humans finish from locked outputs and source table |

## Five-Turn Maximum

| Turn | Purpose | Hard stop |
| --- | --- | --- |
| 1 | First-draft package from the problem file | Stop after issue contract, draft, HOLD queue, A/B next 15 minutes |
| 2 | Compress source/HOLD queue | Top 10 checks only |
| 3 | Adversarial review or substitute second review | Missing issues, overclaims, and decisive facts only |
| 4 | Third-draft merge | Main/final-round draft plus difference table |
| 5 | AI-use report material | Tool-purpose table, verification table, limitation paragraph |

Do not spend any turn asking the model to summarize the preparation material. The short field codes already tell the model what to do.

## B Owns The Usage Budget

Track B is the usage controller. B should keep a visible line in the working notes:

```text
Model budget: turn __ / 5, file access YES/NO, warning YES/NO, fallback at __:__.
```

B stops new AI requests when:

- the model warns that a limit is near
- the file cannot be read after one retry
- the answer begins explaining the source material instead of doing the competition task
- an output creates too many unchecked legal claims
- the clock passes 12:25 in a 10:00-13:00 round

## What To Do If Limited

1. Do not ask a broad follow-up.
2. Save the latest useful output in the venue-approved workspace.
3. A locks the legal issue order and writes from the source table.
4. B completes the AI-use ledger from actual interactions only.
5. If another allowed model surface is still available, use it only for a 10-line checklist or consistency scan.

## Prompt Compression Rules

- Put the problem file first, then the short code.
- Ask for tables before prose.
- Ask for `HOLD` instead of uncertain citations.
- Limit follow-ups to one question per turn.
- Never ask for "all possible law" or "all possible issues."
- Never paste the whole preparation pack into chat.

## Official Source Links

- OpenAI ChatGPT release notes: https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- OpenAI ChatGPT pricing: https://openai.com/chatgpt/pricing/
- OpenAI Codex pricing: https://developers.openai.com/codex/pricing
