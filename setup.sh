#!/usr/bin/env bash
# Cloud environment setup script for c2-content-factory.
# Paste into Claude Code on the web: Environments -> your environment -> Setup script.
# Every step tolerates failure and prints what it could not install.
set +u
log() { echo "[setup] $*"; }
export PIP_ROOT_USER_ACTION=ignore

log "Python packages"
pip install --quiet --upgrade pip >/dev/null 2>&1 || true
pip install --quiet openpyxl pandas numpy matplotlib scikit-learn jupyter nbconvert nbformat ipykernel \
  "markitdown[pptx,docx,xlsx]" Pillow defusedxml lxml python-pptx python-docx pyyaml >/dev/null 2>&1 \
  && log "python packages ok" || log "some python packages failed; continuing"

log "Node packages"
if command -v npm >/dev/null 2>&1; then
  npm install -g --silent pptxgenjs docx react react-dom react-icons sharp >/dev/null 2>&1 \
    && log "node packages ok" || log "npm global install failed; python-pptx and python-docx will be used"
  NODE_GLOBAL="$(npm root -g 2>/dev/null)"
  if [ -n "$NODE_GLOBAL" ]; then
    export NODE_PATH="$NODE_GLOBAL"
    echo "export NODE_PATH=$NODE_GLOBAL" >> "$HOME/.bashrc"
  fi
else
  log "npm not found"
fi

log "System tools for rendering and recalculation"
SUDO=""
if [ "$(id -u)" != "0" ] && command -v sudo >/dev/null 2>&1 && sudo -n true >/dev/null 2>&1; then
  SUDO="sudo"
fi
if command -v apt-get >/dev/null 2>&1; then
  if $SUDO apt-get update -qq >/dev/null 2>&1 && $SUDO apt-get install -y -qq libreoffice-impress libreoffice-calc libreoffice-writer poppler-utils pandoc >/dev/null 2>&1; then
    log "libreoffice, poppler and pandoc ok"
  else
    log "libreoffice, poppler or pandoc did not install; slide rendering and formula recalculation are unavailable in this session"
  fi
else
  log "apt-get not available; slide rendering and formula recalculation are unavailable in this session"
fi

python3 -m ipykernel install --user --name python3 >/dev/null 2>&1 || true

log "Report"
python3 -c "import openpyxl, matplotlib, nbconvert" >/dev/null 2>&1 && log "python deps ok" || log "python deps incomplete"
node -e "require('pptxgenjs')" >/dev/null 2>&1 && log "pptxgenjs ok" || log "pptxgenjs unavailable"
command -v soffice >/dev/null 2>&1 && log "libreoffice ok" || log "libreoffice unavailable"
command -v pdftoppm >/dev/null 2>&1 && log "poppler ok" || log "poppler unavailable"
log "done"
exit 0
