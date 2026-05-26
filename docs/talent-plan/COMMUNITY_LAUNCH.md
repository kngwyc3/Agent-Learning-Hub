# 社区冷启动与传播 playbook

目标：2026-07-31 前 **≥60 Fork**，2026-09-05 前 **>200 Fork**。

## 为什么 Fork 本仓库（README 已同步）

1. **8 阶段可运行代码** — clone 后 `./scripts/bootstrap.sh` 即可 smoke test
2. **Cursor Skill 脚手架** — `python3 scripts/scaffold_skill.py` 生成可安装 skill
3. **Eval 基准包** — stage-7 输出 CSV + HTML 报告，可复用到自己的 agent

## Phase 1 — 冷启动（6 月底 ~ 7 月中，目标 30–50 Fork）

### 1. Awesome 列表 PR

准备 PR 文案（替换为实际 URL）：

**Target:** [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) 或同类列表

```markdown
| [Agent-Learning-Hub](https://github.com/kngwyc3/Agent-Learning-Hub) | Chinese Agent engineering roadmap with runnable stage-1–8 code, skill scaffolds, and eval suite. |
```

**Target:** Cursor rules / skills awesome lists（搜索 `awesome-cursor`）

```markdown
| [Agent-Learning-Hub](https://github.com/kngwyc3/Agent-Learning-Hub) | Skill templates + `scaffold_skill.py` for Cursor Agent Skills. |
```

### 2. 深度帖大纲（V2EX / 即刻 / Datawhale 群）

标题：**15 分钟跑通第一个 Agent Loop（含可运行仓库）**

结构：
1. 痛点：资料太散、缺可运行代码
2. Demo：`bootstrap.sh` + `hub_progress.py status` 截图
3. 路线图：stage-1 → stage-8 一张表
4. CTA：Fork + Star，欢迎 good first issue

### 3. 小红书系列（2–3 篇）

| 篇 | 标题 | 内容要点 |
|----|------|----------|
| 1 | 15 分钟跑通 Agent Loop | 录屏 stage-1 step05 |
| 2 | 给 Cursor 写第一个 Skill | scaffold_skill.py 演示 |
| 3 | Agent 怎么评测 | stage-7 report.html 截图 |

文末统一：GitHub 链接 +「Fork 跟着进度 CLI 打卡」。

## Phase 2 — 放大（7 月中 ~ 8 月底，目标 100–150 Fork）

- 发起 **30 天打卡**：用 Issue 模板 `30-day-checkin.yml`，每周置顶 Day 1 示例
- README **Contributors** 区展示合并 PR 名单（每周更新）
- B 站/录屏：**7 天 Agent 工程化入门**，简介放 GitHub
- 与 1–2 位 AI 博主互推（Datawhale / 小红书生态）

## Phase 3 — 冲刺（8 月底 ~ 9 月初，目标 200+ Fork）

- 发布 **v1.0.0** + Release notes（汇总 bootstrap、progress CLI、eval report、skill scaffold、Stage 8 CLI agent）
- 若 Fork <150：知乎/V2EX 长文 + 合规「Fork 打卡」活动（真实参与，不刷量）
- 每日 `./scripts/milestone_check.sh` 监控增速

### v1.0.0 Release checklist

- [ ] 确认 clone-ready PR 栈已合并到 `main`
- [ ] `./scripts/bootstrap.sh` 在 fresh clone 下通过
- [ ] README badge、Quick Start、30 天打卡、good first issues 链接可打开
- [ ] 更新 [CHANGELOG.md](../../CHANGELOG.md)
- [ ] 创建 Git tag：`v1.0.0`
- [ ] GitHub Release 标题：`v1.0.0: Runnable Agent Learning Path`
- [ ] Release body 复制 `CHANGELOG.md` 中的 v1.0.0 段落，并附 30 天打卡入口

## Gitee 备选（8 月初未达 80 Fork 时启动）

```bash
# 在 gitee.com 导入 GitHub 仓库，开启 Gitee Pages
# 在国内社区（CSDN、掘金）同步发布，链到 Gitee 主站
```

Gitee 路径需同样满足 Fork >200 + 贡献 >200（手机号唯一认定）。

## 传播素材清单

- [ ] 30s bootstrap 终端录屏 GIF
- [ ] index.html 交互页截图
- [ ] eval report.html 截图
- [ ] hub_progress.py status 截图
- [ ] 政策核实清单链接（docs/talent-plan/POLICY_VERIFICATION.md）
- [ ] v1.0.0 Release 链接

## 数据追踪

| 日期 | Stars | Forks | 本周新增 Fork | 渠道 |
|------|-------|-------|---------------|------|
| 2026-06-30 | | | | |
| 2026-07-31 | | | | |
| 2026-08-31 | | | | |
| 2026-09-05 | | | | |

使用 `./scripts/milestone_check.sh` 自动拉取 GitHub API 数据（需 gh CLI）。
