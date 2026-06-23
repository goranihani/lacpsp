# Foreign-Law Source Map

Last reviewed: 2026-06-23. Verify against official sources before use.

Purpose: help a two-person team handle foreign-law signals that Korean legal AI may miss. This is a source map, not a legal conclusion memo.

## Status Codes

| Code | Meaning | Answer Treatment |
| --- | --- | --- |
| CONFIRM | official source confirms the proposition | may use narrowly |
| MODIFY | direction is right but jurisdiction, date, scope, or wording needs correction | use corrected wording |
| HOLD | not verified, translation-limited, time-limited, or fact-limited | do not use as final authority |
| DELETE | hallucinated, irrelevant, or outside the problem | exclude |
| GENERAL | useful as soft governance/risk framework, not binding law | use only as practical standard |

## EU / Germany

| ID | Official Source | Use When |
| --- | --- | --- |
| EU-GDPR | EUR-Lex GDPR, Regulation (EU) 2016/679 | territorial scope, lawful basis, transparency, security, breach notification, transfer |
| EU-PSD2 | EUR-Lex PSD2, Directive (EU) 2015/2366 | payment services, account information, payment initiation, money remittance |
| EU-DORA | EUR-Lex DORA, Regulation (EU) 2022/2554 | financial ICT risk and ICT incident reporting |
| EU-AI-ACT | EUR-Lex AI Act, Regulation (EU) 2024/1689 | AI classification, high-risk issues, application timeline |
| EU-KR-ADEQ | Commission Implementing Decision (EU) 2022/254 | Korea adequacy and GDPR Chapter V transfer limits |
| EDPB-BREACH | EDPB data breach notification examples | breach risk assessment and notification reasoning |
| DE-ZAG | Gesetze im Internet ZAG | German payment-service authorization and registration |
| BAFIN-ZAG | BaFin ZAG/payment services pages | German regulator response and authorization status |

Fast split:

- EU users or EU market: check GDPR and payment-service rules separately.
- Account lookup or payment initiation: test PSD2 categories before writing financial-law conclusions.
- German regulator letter: check German ZAG and BaFin sources, not only EU-level law.
- AI credit/financial decision: do not assume AI Act high-risk status without source and date check.

## United States

| ID | Official Source | Use When |
| --- | --- | --- |
| US-CFPB-1033 | CFPB personal financial data rights page/rule materials | consumer financial data access and authorized third parties |
| US-GLBA-FTC | FTC GLBA business guidance | financial privacy and safeguards issue spotting |
| US-SAFEGUARDS-ECFR | eCFR 16 CFR Part 314 | written information security program and safeguards |
| US-NIST-AI-RMF | NIST AI Risk Management Framework | AI governance as non-binding risk framework |
| US-NIST-CSF | NIST Cybersecurity Framework | security governance as non-binding framework |

Fast split:

- Do not describe the US as having one single general federal privacy code.
- For fintech facts, start with CFPB/GLBA/Safeguards before state-law expansion.
- NIST is usually a governance benchmark, not binding law.

## Japan

| ID | Official Source | Use When |
| --- | --- | --- |
| JP-APPI-PPC | Personal Information Protection Commission legal page | APPI, privacy governance, breach and transfer issues |
| JP-APPI-JLT | Japanese Law Translation APPI translation | English reference for APPI structure |
| JP-FSA-LEGISLATION | Japan FSA legislation page | payment, banking, finance legislation entry point |

Fast split:

- Treat English translations as reference unless the official status is clear.
- For payments/remittance, verify the precise Japanese statute and article before citing.
- For data transfers, separate APPI duties from EU/Japan adequacy or supplementary rules.

## China

| ID | Official Source | Use When |
| --- | --- | --- |
| CN-PIPL | NPC/CAC official PIPL sources | personal information, sensitive PI, extraterritoriality, automated decision-making |
| CN-CAC-CROSS-BORDER-2024 | CAC cross-border data transfer rules | security assessment, standard contract, certification, exemption route |
| CN-DSL-CSL | Data Security Law and Cybersecurity Law official sources | important data, critical information infrastructure, cybersecurity duties |

Fast split:

- Do not merge personal information, sensitive personal information, and important data.
- Verify cross-border transfer route and thresholds before writing a deadline or filing duty.
- If only a translation is available during the round, mark the point `HOLD` or `GENERAL`.

## International Standards

| ID | Source | Use When |
| --- | --- | --- |
| OECD-AI | OECD AI Principles | transparency, accountability, safety, human-centered AI |
| COE-AI-CONVENTION | Council of Europe AI Framework Convention | human rights, democracy, rule-of-law AI governance |
| FATF-RECOMMENDATIONS | FATF Recommendations | AML/CFT risk-based approach |
| FATF-DIGITAL-ID | FATF Digital ID Guidance | non-face-to-face onboarding and identity risk |
| BIS-CPMI-IOSCO-PFMI | CPSS-IOSCO PFMI | payment/settlement infrastructure risk |

Use international standards as practical governance or risk-management support unless the problem asks for binding status.

## One-Minute Foreign-Law Prompt

```text
For the issue below, identify only the official source candidates for EU, US, Japan, China, or international standards.
Do not state final law from memory.
For each candidate, give: source ID, proposition to verify, risk if unverified, and status CONFIRM/MODIFY/HOLD/DELETE/GENERAL.
Issue:
```

