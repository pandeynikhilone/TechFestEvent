#!/usr/bin/env python3
"""Scan tracked source text for common hard-coded credential patterns.

This checks the current checkout only. It does not inspect Git history and is
not a substitute for provider-side secret scanning or credential rotation.
Matched line contents are never printed.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", "staticfiles", "uploads"}
TEXT_SUFFIXES = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".html", ".json", ".yml", ".yaml",
    ".toml", ".ini", ".cfg", ".txt", ".md", ".env", ".sh",
}

PATTERNS = [
    ("Django development secret", re.compile(r"django-insecure-[A-Za-z0-9!#$%&()*+,./:;<=>?@\[\]^_{|}~-]{12,}")),
    ("hard-coded Django SECRET_KEY", re.compile(r"""(?m)^\s*SECRET_KEY\s*=\s*(['"])[^'"\n]{12,}\1""")),
    ("hard-coded Razorpay secret", re.compile(r"""(?mi)^\s*RAZORPAY_KEY_SECRET\s*=\s*(['"])[^'"\n]{8,}\1""")),
    ("Razorpay key literal", re.compile(r"\brzp_(?:test|live)_[A-Za-z0-9]{12,}\b")),
    ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b")),
    ("OpenAI-style API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("private-key header", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("credential-bearing MongoDB URI", re.compile(r"mongodb(?:\+srv)?://[^/\s:@]+:[^/@\s]+@")),
]


def main() -> int:
    scanned = 0
    findings = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        relative_parts = path.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in relative_parts):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        scanned += 1
        for label, pattern in PATTERNS:
            match = pattern.search(content)
            if match:
                line = content.count("\n", 0, match.start()) + 1
                findings.append((path.relative_to(ROOT).as_posix(), line, label))

    if findings:
        print("Potential hard-coded credential patterns detected; matched content is withheld:")
        for path, line, label in findings:
            print(f"- {path}:{line} — {label}")
        return 1

    print(f"Credential-pattern scan passed for {scanned} source-text files in the current checkout.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
