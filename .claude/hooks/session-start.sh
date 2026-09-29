#!/bin/bash
# Pin mermaid-cli at 11.17.0 in Claude Code on the web sessions.
#
# scripts/build_deck.py passes -w to mmdc, and mermaid-cli 12 removed that option, so under 12 every
# diagram in a deck silently falls back to its source text. This checks the installed version and
# reinstalls 11.17.0 only when it differs, so a session that already has it pays one `mmdc -V`.
# It never fails the session: a missed pin is reported and the session starts anyway.
set -uo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

WANT="11.17.0"
HAVE="$(mmdc -V 2>/dev/null | tail -1)"
if [ "$HAVE" = "$WANT" ]; then
  exit 0
fi
if ! command -v npm >/dev/null 2>&1; then
  echo "[session-start] npm not found; mermaid-cli stays at ${HAVE:-none}, and deck diagrams need $WANT"
  exit 0
fi
if PUPPETEER_SKIP_DOWNLOAD=1 PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1 \
     npm install -g --silent "@mermaid-js/mermaid-cli@$WANT" >/dev/null 2>&1; then
  echo "[session-start] mermaid-cli pinned: ${HAVE:-none} -> $(mmdc -V 2>/dev/null | tail -1)"
else
  echo "[session-start] mermaid-cli $WANT install failed; mmdc is ${HAVE:-missing}, so deck diagrams will fall back to text"
fi
exit 0
