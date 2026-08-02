#!/usr/bin/env bash
# Export a Markdown document to DOCX and PDF.
#
# Default behavior for this project: whenever a new version of the plan or the
# curriculum is finalized (e.g. *-V2.md), regenerate its .docx and .pdf with this
# script so the repo always ships matching Word and PDF artifacts.
#
# Usage:
#   scripts/export-docs.sh [markdown_file ...]
# With no arguments, it exports the current plan and curriculum.
#
# Requires: pandoc (md -> docx) and LibreOffice `soffice` (docx -> pdf).

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Isolated LibreOffice profile so headless runs don't clash with a GUI session.
LO_PROFILE="$(mktemp -d)/lo_profile"

command -v pandoc >/dev/null || { echo "ERROR: pandoc not found"; exit 1; }
SOFFICE="$(command -v soffice || command -v libreoffice || true)"
[ -n "$SOFFICE" ] || { echo "ERROR: LibreOffice (soffice/libreoffice) not found"; exit 1; }

# Default targets when none are passed.
if [ "$#" -eq 0 ]; then
  set -- docs/med-tech-plan-V1.md docs/med-tech-curriculum-V1.md
fi

for md in "$@"; do
  [ -f "$md" ] || { echo "SKIP (missing): $md"; continue; }
  dir="$(dirname "$md")"
  base="$(basename "${md%.md}")"
  title="$(printf '%s' "$base" | sed 's/-/ /g')"

  echo "==> $md"
  pandoc "$md" -f gfm -t docx \
    --reference-doc "$ROOT/scripts/reference.docx" \
    --toc --toc-depth=2 \
    --metadata title="$title" \
    -o "$dir/$base.docx"
  echo "    wrote $dir/$base.docx"

  "$SOFFICE" --headless --convert-to pdf --outdir "$dir" "$dir/$base.docx" \
    -env:UserInstallation="file://$LO_PROFILE" >/dev/null 2>&1
  echo "    wrote $dir/$base.pdf"
done

echo "Done."
