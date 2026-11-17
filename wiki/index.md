---
id: index
title: AI Agents LLM Wiki
type: index
sources:
related:
  - agent-definition
  - react-loop
  - workflow-patterns
updated: 2026-11-17
---

這是一份用「先討論、後生成」方式建立的 AI Agents 知識庫：先在對話裡決定主題、來源和頁面結構，再讓 AI 依照 [AGENTS.md 規則](../AGENTS.md) 寫成 wiki，最後拿這份 wiki 產生[教學簡報](../slides/index.html)。

## 建議閱讀順序

1. [Agent 定義](agent-definition.md)：聊天機器人和 agent 差在哪？
2. [工具使用](tool-use.md)：agent 怎麼「動手」。
3. [ReAct 迴圈](react-loop.md)：想 → 做 → 看。
4. [規劃](planning.md)：拆任務、自我反思。
5. [記憶](memory.md)：短期 vs 長期。
6. [工作流模式](workflow-patterns.md)：五種常見模式。
7. [多代理](multi-agent.md)：什麼時候該拆成很多個 agent。
8. [風險與陷阱](risks.md)：guardrails 與人工把關。

## 來源摘要頁（6 篇）

| 來源 | 年份 | 主要餵給哪些概念頁 |
|---|---|---|
| [Anthropic〈Building effective agents〉](anthropic-building-effective-agents.md) | 2024 | Agent 定義、工作流模式、風險 |
| [Lilian Weng〈LLM Powered Autonomous Agents〉](weng-llm-powered-agents.md) | 2023 | 規劃、記憶、工具、風險 |
| [ReAct（Yao et al.）](yao-react.md) | 2022 | ReAct 迴圈、規劃 |
| [Toolformer（Schick et al.）](schick-toolformer.md) | 2023 | 工具使用 |
| [OpenAI〈A practical guide to building agents〉](openai-practical-guide.md) | 2025 | Agent 定義、多代理、風險、工具 |
| [LangGraph〈Workflows and agents〉](langgraph-workflows-agents.md) | 待確認 | 工作流模式、Agent 定義 |

## 這份 wiki 怎麼做出來的

完整流程圖、檢查紀錄和反思在 [流程說明](../process.md)。
