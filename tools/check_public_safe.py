#!/usr/bin/env python3
"""Lightweight public-safe scanner for this repository.

The scanner is intentionally conservative. It flags common markers of real
competition work product, credentials, local-only folders, and submission data.
It does not prove a repository is safe; it helps reviewers find risky files.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


BLOCKED_PATH_PARTS = {
    "local-only",
    "scratch",
    "work",
    "tmp",
    "output",
    "submit",
    "submission",
    ".DS_Store",
    "__pycache__",
}

ALLOWLIST_FILES = {
    Path("README.md"),
    Path("docs/public-safe-policy.md"),
    Path("checklists/public-safe-release-checklist.md"),
    Path("tools/check_public_safe.py"),
}

RISK_PATTERNS = {
    "credential": re.compile(r"(password|passwd|비밀번호|api[_-]?key|secret|token)", re.I),
    "submission": re.compile(r"(제출\s*링크|submission\s*link|접수\s*확인|메일\s*제목)", re.I),
    "identity": re.compile(r"(학번|소속\s*로스쿨|팀원\s*성명|참가번호\s*[:=]\s*\d{1,4})", re.I),
    "real_problem": re.compile(r"(본선\s*문제\s*원문|결선\s*문제\s*원문|예선\s*문제\s*원문|최종\s*답안)", re.I),
    "transcript": re.compile(r"(AI\s*출력\s*전문|프롬프트\s*전문|대화기록)", re.I),
}


def should_scan(path: Path) -> bool:
    if any(part in BLOCKED_PATH_PARTS for part in path.parts):
        return False
    return path.suffix.lower() in {".md", ".txt", ".py", ".json", ".yml", ".yaml", ".csv"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    findings: list[str] = []

    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if path.is_dir():
            continue
        if rel in ALLOWLIST_FILES:
            continue
        if any(part in BLOCKED_PATH_PARTS for part in rel.parts):
            findings.append(f"blocked path marker: {rel}")
            continue
        if not should_scan(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"non-utf8 text candidate: {rel}")
            continue
        for label, pattern in RISK_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{label}: {rel}")

    if findings:
        print("PUBLIC-SAFE SCAN: REVIEW REQUIRED")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("PUBLIC-SAFE SCAN: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
