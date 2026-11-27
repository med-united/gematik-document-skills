#!/usr/bin/env bash
# Kopiert shared/gemeinsam.md und shared/steckbrief.py in jeden Skill, damit jeder Skill für sich installierbar ist.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
for skill in "$root"/skills/*/; do
  mkdir -p "$skill/references"
  cp "$root/shared/gemeinsam.md" "$skill/references/gemeinsam.md"
  mkdir -p "$skill/scripts"
  cp "$root/shared/steckbrief.py" "$skill/scripts/steckbrief.py"
done
echo "gemeinsame Dateien in $(ls -d "$root"/skills/*/ | wc -l) Skills aktualisiert"
