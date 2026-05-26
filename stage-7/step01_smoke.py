"""Offline smoke test for Stage 7 eval runner.

Run: python step01_smoke.py
"""

from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
from pathlib import Path


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        out = tmp_dir / "results.csv"
        traces = tmp_dir / "traces"
        proc = subprocess.run(
            [
                sys.executable,
                "scripts/eval_runner.py",
                "--tasks",
                "evals/tasks.csv",
                "--out",
                str(out),
                "--trace-dir",
                str(traces),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        expect(proc.returncode == 0, proc.stderr or proc.stdout)
        expect(out.exists(), "eval runner should write results.csv")
        with out.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        expect(len(rows) >= 20, "expected at least 20 eval rows")
        expect(any(traces.glob("*.jsonl")), "eval runner should write trace logs")

    print("stage-7 smoke ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
