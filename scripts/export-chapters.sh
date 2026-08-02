#!/usr/bin/env bash
# Export every per-chapter Theory/Labs Markdown file to DOCX and PDF, in place.
# Skips *-context.md (internal AI logs). Pipeline: pandoc (md->docx) + LibreOffice (docx->pdf).
#
# Usage: scripts/export-chapters.sh
# Run after scripts/split-chapters.py (which regenerates the Theory/Labs .md files).

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"

command -v pandoc >/dev/null || { echo "ERROR: pandoc not found"; exit 1; }
SOFFICE="$(command -v soffice || command -v libreoffice || true)"
[ -n "$SOFFICE" ] || { echo "ERROR: LibreOffice (soffice/libreoffice) not found"; exit 1; }
LO_PROFILE="$(mktemp -d)/lo"

count=0
find docs -type d -name "Chapter *" -print0 | sort -z | while IFS= read -r -d '' dir; do
  shopt -s nullglob
  mds=("$dir"/*-Theory.md "$dir"/*-Labs.md)
  [ ${#mds[@]} -gt 0 ] || continue
  for md in "${mds[@]}"; do
    base="$(basename "${md%.md}")"
    pandoc "$md" -f gfm -t docx -o "$dir/$base.docx"
  done
  # one soffice call per chapter dir converts both docx to pdf beside them
  "$SOFFICE" --headless --convert-to pdf --outdir "$dir" "$dir"/*-Theory.docx "$dir"/*-Labs.docx \
    -env:UserInstallation="file://$LO_PROFILE" >/dev/null 2>&1 || true
  echo "  exported: $dir"
done
echo "Done."
