#!/usr/bin/env python3
"""Track Agent Learning Hub stage progress locally."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE = ROOT / ".hub-progress.json"

STAGES: dict[str, list[str]] = {
    "stage-1": [
        "step01_chat.py — 最小对话",
        "step02_json.py — 结构化输出",
        "step03_tools_def.py — 工具定义",
        "step04_one_round_tool.py — 单轮工具调用",
        "step05_agent_loop.py — Agent loop",
    ],
    "stage-2": [
        "step01_memory_layers.py — 记忆分层",
        "step02_ragflow_ingest.py — 文档入库",
        "step03_ragflow_retrieve.py — RAG 检索",
        "step04_ragflow_answer.py — 带引用回答",
        "step05_mem0_memory.py — mem0 长期记忆",
        "step06_letta_compaction.py — Letta 上下文压缩",
        "step07_rag_as_tool.py — RAG 作为工具",
    ],
    "stage-3": [
        "阅读 claude-code-docs/00-概览与项目结构.md",
        "阅读 03-Agent系统.md 与 06-权限系统.md",
        "完成 claude-code-学习指南.html 至少 3 章",
    ],
    "stage-4": [
        "step01_roles_contracts.py — 角色契约",
        "step03_supervisor_router.py — Supervisor 路由",
        "step05_single_vs_multi.py — 单/多 Agent 对比",
    ],
    "stage-5": [
        "step01_boundaries.py — Skill 边界",
        "step03_validate_report.py — 报告校验",
        "step04_run_smoke_cases.py — Smoke test",
    ],
    "stage-6": [
        "step01_validate_url.py — URL 校验",
        "step02_observe_page.py — 页面观察",
        "step03_run_agent.py — Browser agent",
    ],
    "stage-7": [
        "step01_load_tasks.py — 加载 eval 任务",
        "step02_run_eval.py — 运行 eval",
        "step03_safety_gate.py — 安全门禁",
    ],
    "stage-8": [
        "common.py / tools.py — 配置、trace、成本与工具",
        "agent.py / cli.py — 可运行 CLI agent",
        "step01_smoke.py — 离线 smoke test",
    ],
}


def load_state(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"completed": {}, "updated_at": None}


def save_state(path: Path, state: dict) -> None:
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def item_key(stage: str, item: str) -> str:
    return f"{stage}::{item}"


def cmd_status(state_path: Path) -> int:
    state = load_state(state_path)
    done = state.get("completed", {})
    total = sum(len(items) for items in STAGES.values())
    finished = sum(1 for k, v in done.items() if v)

    print(f"Progress: {finished}/{total} ({round(finished / total * 100, 1) if total else 0}%)")
    if state.get("updated_at"):
        print(f"Updated:  {state['updated_at']}")
    print()

    for stage, items in STAGES.items():
        stage_done = sum(1 for item in items if done.get(item_key(stage, item)))
        mark = "✓" if stage_done == len(items) else " "
        print(f"[{mark}] {stage} ({stage_done}/{len(items)})")
        for item in items:
            checked = done.get(item_key(stage, item), False)
            box = "x" if checked else " "
            print(f"    [{box}] {item}")
    return 0


def cmd_check(state_path: Path, stage: str, index: int) -> int:
    if stage not in STAGES:
        print(f"Unknown stage: {stage}")
        print(f"Available: {', '.join(STAGES)}")
        return 1
    items = STAGES[stage]
    if index < 1 or index > len(items):
        print(f"Index must be 1..{len(items)} for {stage}")
        return 1

    state = load_state(state_path)
    key = item_key(stage, items[index - 1])
    state.setdefault("completed", {})[key] = True
    save_state(state_path, state)
    print(f"Marked done: {key}")
    return cmd_status(state_path)


def cmd_uncheck(state_path: Path, stage: str, index: int) -> int:
    if stage not in STAGES:
        return 1
    items = STAGES[stage]
    key = item_key(stage, items[index - 1])
    state = load_state(state_path)
    state.setdefault("completed", {})[key] = False
    save_state(state_path, state)
    print(f"Marked undone: {key}")
    return 0


def cmd_reset(state_path: Path) -> int:
    if state_path.exists():
        state_path.unlink()
    print(f"Reset {state_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE, help="Progress file path")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="Show progress")

    p_check = sub.add_parser("check", help="Mark one item done (1-based index)")
    p_check.add_argument("stage")
    p_check.add_argument("index", type=int)

    p_uncheck = sub.add_parser("uncheck", help="Mark one item undone")
    p_uncheck.add_argument("stage")
    p_uncheck.add_argument("index", type=int)

    sub.add_parser("reset", help="Clear all progress")

    args = parser.parse_args()
    if args.command == "status":
        return cmd_status(args.state)
    if args.command == "check":
        return cmd_check(args.state, args.stage, args.index)
    if args.command == "uncheck":
        return cmd_uncheck(args.state, args.stage, args.index)
    if args.command == "reset":
        return cmd_reset(args.state)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
