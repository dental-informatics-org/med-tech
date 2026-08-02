#!/usr/bin/env python3
"""Split docs/med-tech-curriculum-V1.md into per-chapter Theory / Labs / context files.

Creates the tree:
    docs/Volume <ROMAN>/Chapter <N>/
        Volume-<ROMAN>-Chapter-<N>-Theory.md
        Volume-<ROMAN>-Chapter-<N>-Labs.md
        Volume-<ROMAN>-Chapter-<N>-context.md   (AI interaction memory, append-only)

From this split onward each chapter is maintained independently; the Theory files
later feed PowerPoint/slide + video-explanation generation.

By default this does NOT overwrite existing Theory/Labs/context files, because from
the V1 split onward each chapter is edited independently and must not be clobbered by
re-running against the (frozen) master curriculum. Set FORCE=1 to regenerate Theory/Labs
from the curriculum anyway (context files are always preserved).
"""
import os
import re
import datetime
from pathlib import Path

FORCE = os.environ.get("FORCE") == "1"

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "med-tech-curriculum-V1.md"
DOCS = ROOT / "docs"
TODAY = datetime.date.today().isoformat()

CHAP_HDR = re.compile(r'^## Chapter (\d+) — (.*?) · \[Volume ([IVX]+)\]\s*$')
HEADING = re.compile(r'^#{1,6}\s')
THEORY = re.compile(r'^\*\*Topics \(theory\)')
LABS = re.compile(r'^\*\*(Labs|Project) \(hands-on\)')


def find_block(lines, label_re):
    """Return (start, end) covering: label line + following table + one trailing blank."""
    for k, l in enumerate(lines):
        if label_re.match(l):
            p = k + 1
            while p < len(lines) and lines[p].strip() == "":      # skip blanks before table
                p += 1
            while p < len(lines) and lines[p].lstrip().startswith("|"):  # consume table rows
                p += 1
            while p < len(lines) and lines[p].strip() == "":      # one/more trailing blanks
                p += 1
            return (k, p)
    return None


def main():
    lines = SRC.read_text(encoding="utf-8").splitlines()

    # locate chapter header lines
    starts = [(i, m) for i, l in enumerate(lines) for m in [CHAP_HDR.match(l)] if m]

    made = []
    for i, m in starts:
        n, title, roman = m.group(1), m.group(2), m.group(3)

        # chapter body = from header until next heading of any level
        j = i + 1
        while j < len(lines) and not HEADING.match(lines[j]):
            j += 1
        inner = lines[i + 1:j]
        while inner and inner[0].strip() == "":
            inner.pop(0)
        while inner and inner[-1].strip() in ("", "---"):
            inner.pop()

        tb = find_block(inner, THEORY)
        lb = find_block(inner, LABS)
        if not tb or not lb:
            raise SystemExit(f"Chapter {n}: could not locate theory/labs block")

        theory_body = "\n".join(inner[:lb[0]] + inner[lb[1]:]).rstrip()
        labs_body = "\n".join(inner[:tb[0]] + inner[tb[1]:]).rstrip()

        chap_dir = DOCS / f"Volume {roman}" / f"Chapter {n}"
        chap_dir.mkdir(parents=True, exist_ok=True)
        stem = f"Volume-{roman}-Chapter-{n}"

        note = (f"> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward "
                f"this chapter is maintained **independently** here. See "
                f"`{stem}-context.md` for the AI interaction log.\n")

        theory_path = chap_dir / f"{stem}-Theory.md"
        labs_path = chap_dir / f"{stem}-Labs.md"
        if FORCE or not theory_path.exists():
            theory_path.write_text(
                f"# Volume {roman} · Chapter {n} — {title} · Theory\n\n{note}\n{theory_body}\n",
                encoding="utf-8")
        if FORCE or not labs_path.exists():
            labs_path.write_text(
                f"# Volume {roman} · Chapter {n} — {title} · Labs\n\n{note}\n{labs_body}\n",
                encoding="utf-8")

        ctx = chap_dir / f"{stem}-context.md"
        if not ctx.exists():
            ctx.write_text(
                f"# Volume {roman} · Chapter {n} — {title} · AI Context Log\n\n"
                f"> Per-chapter memory for AI interactions on **this chapter only**. "
                f"Append-only, newest first. Read this before modifying the chapter, and add "
                f"an entry after each change.\n>\n"
                f"> Purpose: from this point each chapter progresses independently. The Theory/Labs "
                f"files + this context feed later AI runs that build **PowerPoint slides (theory)** "
                f"and **video explanations**.\n\n"
                f"| Field | Value |\n|---|---|\n"
                f"| Volume | {roman} |\n| Chapter | {n} |\n| Title | {title} |\n"
                f"| Source | `docs/med-tech-curriculum-V1.md` (V1 baseline) |\n\n"
                f"## Interactions (newest first)\n\n"
                f"### {TODAY} — Created from curriculum V1\n"
                f"- Split Chapter {n} out of the master curriculum into independent Theory and Labs files.\n"
                f"- V1 baseline; no content changes yet. Ready for independent iteration.\n",
                encoding="utf-8")

        made.append((roman, n, title))

    print(f"Wrote {len(made)} chapters:")
    for roman, n, title in made:
        print(f"  Volume {roman} / Chapter {n} — {title}")


if __name__ == "__main__":
    main()
