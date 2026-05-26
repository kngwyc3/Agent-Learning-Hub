#!/usr/bin/env bash
# One-shot bootstrap: deps + smoke tests for Agent Learning Hub stages.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
VENV="$ROOT/.venv"

echo "=== Agent Learning Hub Bootstrap ==="
echo "Root: $ROOT"
echo

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 not found"
  exit 1
fi

PY="${PYTHON:-python3}"
echo "Python: $($PY --version)"

if [[ ! -d "$VENV" ]]; then
  echo ">> Creating venv at .venv"
  "$PY" -m venv "$VENV"
fi
# shellcheck disable=SC1091
source "$VENV/bin/activate"
PY="$VENV/bin/python"
echo "Using venv: $PY"

install_req() {
  local dir="$1"
  if [[ -f "$dir/requirements.txt" ]]; then
    echo
    echo ">> Installing $dir/requirements.txt"
    "$PY" -m pip install -q -r "$dir/requirements.txt"
  fi
}

install_req stage-1
install_req stage-2
install_req stage-4
install_req stage-6
install_req stage-8

echo
echo ">> Stage 1 smoke"
(cd stage-1 && "$PY" step99_smoke.py)

echo
echo ">> Stage 2 smoke"
(cd stage-2 && "$PY" step99_smoke.py)

echo
echo ">> Stage 4 smoke"
(cd stage-4 && "$PY" step99_smoke.py)

echo
echo ">> Stage 5 smoke: skill validation"
(cd stage-5 && "$PY" step04_run_smoke_cases.py)

echo
echo ">> Stage 6 smoke"
(cd stage-6 && "$PY" step99_smoke.py)

echo
echo ">> Stage 7 smoke"
(cd stage-7 && "$PY" step01_smoke.py)

echo
echo ">> Stage 8 smoke"
(cd stage-8 && "$PY" step01_smoke.py)

echo
echo ">> Progress CLI"
"$PY" scripts/hub_progress.py status

echo
echo "=== Bootstrap complete ==="
echo "Next:"
echo "  ./scripts/check_github_setup.sh"
echo "  python3 scripts/hub_progress.py --help"
echo "  python3 scripts/scaffold_skill.py --help"
