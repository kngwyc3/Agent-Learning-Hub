"""Offline smoke test for Stage 1.

Run: python step99_smoke.py
"""

from __future__ import annotations

from tools import TOOL_SCHEMAS, calculator, read_file, run_tool


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    expect(any(item["function"]["name"] == "calculator" for item in TOOL_SCHEMAS), "calculator schema missing")
    expect(calculator("(2 + 3) * 4") == "20", "calculator failed")
    expect("非法字符" in calculator("__import__('os')"), "calculator should reject unsafe expression")
    expect("Agent" in read_file("notes.txt"), "read_file should read notes.txt")
    expect(run_tool("calculator", '{"expression":"1+2"}') == "3", "run_tool calculator failed")
    expect("合法 JSON" in run_tool("calculator", "{bad"), "run_tool should reject invalid JSON")
    print("stage-1 smoke ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
