#!/usr/bin/env bash
# Cloud environment setup script for c2-content-factory.
# Paste into Claude Code on the web: Environments -> your environment -> Setup script.
# Order: cheap and certain first, heavy downloads last. Every step tolerates failure,
# reports what it could not do, and the script always exits zero.
set +u
set +e
log() { echo "[setup] $*"; }
export PIP_ROOT_USER_ACTION=ignore
export PIP_BREAK_SYSTEM_PACKAGES=1
export DEBIAN_FRONTEND=noninteractive
export PLAYWRIGHT_BROWSERS_PATH="$HOME/.cache/ms-playwright"
export PUPPETEER_SKIP_DOWNLOAD=1
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
mkdir -p "$HOME/.local/bin"

# ---------------------------------------------------------------- privilege check
SUDO=""
if [ "$(id -u)" != "0" ] && command -v sudo >/dev/null 2>&1 && sudo -n true >/dev/null 2>&1; then
  SUDO="sudo"
fi
APT_OK=0
if command -v apt-get >/dev/null 2>&1; then
  if [ "$(id -u)" = "0" ] || [ -n "$SUDO" ]; then APT_OK=1; fi
fi
[ "$APT_OK" = "1" ] && log "system package installs available" || log "no root or sudo: system libraries cannot be installed, so weasyprint, playwright browsers and mermaid rendering will be unavailable"

# ---------------------------------------------------------------- python packages
log "Python packages"
pip install --quiet --upgrade pip >/dev/null 2>&1
pip install --quiet openpyxl pandas numpy matplotlib scikit-learn jupyter nbconvert nbformat ipykernel \
  "markitdown[pptx,docx,xlsx]" Pillow defusedxml lxml python-pptx python-docx pyyaml playwright weasyprint >/dev/null 2>&1 \
  && log "python packages ok" || log "some python packages failed; continuing"
python3 -m ipykernel install --user --name python3 >/dev/null 2>&1

# ---------------------------------------------------------------- node packages
log "Node packages"
if command -v npm >/dev/null 2>&1; then
  npm install -g --silent pptxgenjs docx react react-dom react-icons sharp >/dev/null 2>&1 \
    && log "document node packages ok" || log "document node packages failed; python fallbacks will be used"
  npm install -g --silent @mermaid-js/mermaid-cli >/dev/null 2>&1 \
    && log "mermaid-cli installed" || log "mermaid-cli install failed"
  NODE_GLOBAL="$(npm root -g 2>/dev/null)"
  if [ -n "$NODE_GLOBAL" ]; then
    export NODE_PATH="$NODE_GLOBAL"
    grep -q "NODE_PATH=" "$HOME/.bashrc" 2>/dev/null || echo "export NODE_PATH=$NODE_GLOBAL" >> "$HOME/.bashrc"
  fi
else
  log "npm not found; node packages skipped"
fi

# ---------------------------------------------------------------- system libraries
if [ "$APT_OK" = "1" ]; then
  log "System libraries"
  $SUDO apt-get update -qq >/dev/null 2>&1
  $SUDO apt-get install -y -qq --no-install-recommends \
    libreoffice-impress libreoffice-calc libreoffice-writer poppler-utils pandoc \
    fonts-dejavu fonts-liberation \
    libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b libcairo2 libgdk-pixbuf-2.0-0 shared-mime-info libffi8 \
    >/dev/null 2>&1 && log "libreoffice, poppler, pandoc, fonts and weasyprint libraries ok" \
    || log "one or more system libraries failed; see the report below for what works"
  # playwright's own dependency installer covers chromium's shared libraries
  if command -v playwright >/dev/null 2>&1 || python3 -c "import playwright" >/dev/null 2>&1; then
    $SUDO env PLAYWRIGHT_BROWSERS_PATH="$PLAYWRIGHT_BROWSERS_PATH" python3 -m playwright install-deps chromium >/dev/null 2>&1 \
      && log "chromium system dependencies ok" || log "chromium system dependencies failed"
  fi
fi

# ---------------------------------------------------------------- chromium, shared by playwright and mermaid
log "Chromium for playwright and mermaid"
if python3 -c "import playwright" >/dev/null 2>&1; then
  python3 -m playwright install chromium >/dev/null 2>&1 && log "playwright chromium downloaded" || log "playwright chromium download failed (check network access to the playwright download hosts)"
fi
CHROME_PATH="$(find "$PLAYWRIGHT_BROWSERS_PATH" -type f -name chrome -path '*chrome-linux*' 2>/dev/null | head -1)"
if [ -n "$CHROME_PATH" ]; then
  cat > "$HOME/.mmdc-puppeteer.json" << JSON
{ "executablePath": "$CHROME_PATH", "args": ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"] }
JSON
  # wrapper so plain "mmdc" works without downloading a second browser
  MMDC_REAL="$(command -v mmdc 2>/dev/null)"
  if [ -n "$MMDC_REAL" ]; then
    cat > "$HOME/.local/bin/mmdc" << WRAP
#!/usr/bin/env bash
exec "$MMDC_REAL" -p "$HOME/.mmdc-puppeteer.json" "\$@"
WRAP
    chmod +x "$HOME/.local/bin/mmdc"
  fi
  grep -q "PLAYWRIGHT_BROWSERS_PATH=" "$HOME/.bashrc" 2>/dev/null || echo "export PLAYWRIGHT_BROWSERS_PATH=$PLAYWRIGHT_BROWSERS_PATH" >> "$HOME/.bashrc"
  grep -q 'PATH="$HOME/.local/bin' "$HOME/.bashrc" 2>/dev/null || echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
  export PATH="$HOME/.local/bin:$PATH"
else
  log "no chromium binary found; mermaid-cli and playwright rendering are unavailable this session"
fi

# ---------------------------------------------------------------- report
log "Report"
python3 -c "import openpyxl, matplotlib, nbconvert" >/dev/null 2>&1 && log "python deps ok" || log "python deps incomplete"
node -e "require('pptxgenjs')" >/dev/null 2>&1 && log "pptxgenjs ok" || log "pptxgenjs unavailable"
command -v soffice >/dev/null 2>&1 && log "libreoffice ok" || log "libreoffice unavailable"
command -v pdftoppm >/dev/null 2>&1 && log "poppler ok" || log "poppler unavailable"
command -v pandoc >/dev/null 2>&1 && log "pandoc ok" || log "pandoc unavailable"
python3 -c "import weasyprint; print('[setup] weasyprint', weasyprint.__version__, 'ok')" 2>/dev/null || log "weasyprint unavailable (needs pango and cairo system libraries)"
python3 - << 'PY' 2>/dev/null || echo "[setup] playwright browser launch failed"
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(args=["--no-sandbox"]); v = b.version; b.close()
print("[setup] playwright chromium", v, "ok")
PY
if command -v mmdc >/dev/null 2>&1; then
  printf 'flowchart LR\n  A[setup] --> B[ok]\n' > /tmp/_mm.mmd
  mmdc -i /tmp/_mm.mmd -o /tmp/_mm.svg >/dev/null 2>&1 && log "mermaid-cli render ok" || log "mermaid-cli installed but render failed"
else
  log "mermaid-cli unavailable"
fi
log "done"
exit 0
