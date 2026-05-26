"""Offline smoke test for Stage 2.

Run: python step99_smoke.py
"""

from __future__ import annotations

from ragflow_helper import format_chunks_for_prompt, retrieve
from step01_memory_layers import LONG_TERM_MEMORY, SESSION_STORE, SHORT_TERM_CONTEXT, build_prompt


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    prompt = build_prompt(SHORT_TERM_CONTEXT, SESSION_STORE, LONG_TERM_MEMORY)
    expect("长期记忆" in prompt and "当前窗口" in prompt, "memory prompt missing sections")

    chunks = retrieve("agent memory", top_k=2)
    expect(chunks, "local RAG fallback should return at least one chunk")
    formatted = format_chunks_for_prompt(chunks)
    expect("[1]" in formatted and "来源" in formatted, "formatted chunks should include citations")

    print("stage-2 smoke ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
