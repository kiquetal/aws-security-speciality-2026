#!/bin/bash
# Daily cheat sheet drill — shows a random section
# Usage: ./scripts/daily-drill.sh

CHEAT="/mydata/codes/2026/aws-security-speciality-2026/notes/cheat-sheet.md"

# Pick a random domain section
SECTIONS=("D4: Identity" "D5: Data Protection" "D3: Infrastructure" "D1: Detection" "D2: Incident" "D6: Governance")
RANDOM_SECTION="${SECTIONS[$RANDOM % ${#SECTIONS[@]}]}"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  📖 DAILY DRILL — $RANDOM_SECTION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Extract that section using sed
sed -n "/## $RANDOM_SECTION/,/^## D[0-9]/p" "$CHEAT" | head -n -1 | glow -

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✅ Read it. Close your eyes. Recall 3 rules."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
