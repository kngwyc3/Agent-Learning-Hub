"""Offline smoke test for Stage 4.

Run: python step99_smoke.py
"""

from __future__ import annotations

import os

os.environ.pop("OPENAI_API_KEY", None)

from coordinator import run_fixed_pipeline, run_supervised, state_to_dict


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    fixed = run_fixed_pipeline("写一段解释多 agent 协调的短文")
    expect(bool(fixed.final), "fixed pipeline should produce final output")
    expect(len(fixed.trace) == 4, "fixed pipeline should write four trace events")

    supervised = run_supervised("写一段解释 supervisor 模式的短文", max_steps=8)
    expect(bool(supervised.final), "supervisor flow should produce final output")
    data = state_to_dict(supervised)
    expect(isinstance(data["trace"], list) and data["trace"], "state_to_dict should serialize trace")

    print("stage-4 smoke ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
