# Third Draft And AI-Usage Report Prompt

Use this after the first draft and two second-draft reviews are ready. If SuperLawyer and LBOX were not expressly allowed by the organizer, replace them with two internal GPT/Codex review tracks and do not claim those legal AI services were used.

```text
You are helping merge a lawschool AI competition answer.
Use the first draft, second draft A, second draft B, and source-check status below.

This is a Lawschool AI Challenge main/final round work product.
Do not mention lacpsp, GitHub, or any repository name in the visible answer.
Do not explain the workflow source.
Do not use a command handle as a heading, tool name, prompt name, or evidence item.
Do not assume any second draft is correct.
Do not invent legal citations.
Do not say SuperLawyer or LBOX were used unless the official field rule expressly allowed them and the team actually used them.
Prioritize a timely submission-ready third draft over broad research.
Do not fake certainty: unverified law, dates, authorities, foreign-law claims, or tool-use claims must be marked HOLD or omitted.

Input:
First draft:
[paste]

Second draft A:
[paste]

Second draft B:
[paste]

Confirmed sources:
[paste]

Remaining HOLD sources:
[paste]

Return:
1. Difference table:
   - point
   - draft A position
   - draft B position
   - human decision: CONFIRM/MODIFY/HOLD/DELETE/STYLE ONLY
   - answer location

2. Third-draft answer:
   - direct conclusion first
   - legal standard only if confirmed or marked HOLD
   - application to facts
   - counterargument
   - mini-conclusion

3. AI-usage report draft:
   - tool used
   - purpose
   - human verification
   - adopted/modified/rejected/held output
   - limitation or hallucination risk
   - final human judgment

4. Open source queue:
   - what must be checked before final wording
   - fallback sentence if not checked

5. Submission risk list:
   - five items only
```
