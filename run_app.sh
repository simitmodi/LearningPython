#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"

echo "Project root: ${ROOT_DIR}"

if [[ ! -d "${VENV_DIR}" ]]; then
  echo "Creating virtual environment..."
  python3 -m venv "${VENV_DIR}"
fi

source "${VENV_DIR}/bin/activate"

echo "Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r "${ROOT_DIR}/requirements.txt"

echo "Running project setup scripts..."
python "${ROOT_DIR}/Student_data_generator.py"
python "${ROOT_DIR}/Employee_data_generator.py"
python "${ROOT_DIR}/xlsxTocsv.py"
python "${ROOT_DIR}/csvTojson.py"

echo "Starting terminal app..."
if [[ $# -gt 0 ]]; then
  python "${ROOT_DIR}/main.py" "$1"
else
  python "${ROOT_DIR}/main.py"
fi
