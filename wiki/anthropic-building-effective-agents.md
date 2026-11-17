---
id: anthropic-building-effective-agents
title: 來源｜Anthropic〈Building effective agents〉
type: source
sources:
  - anthropic-building-effective-agents
related:
  - workflow-patterns
  - agent-definition
  - risks
  - tool-use
updated: 2026-11-17
---

## 基本資料

- 標題：Building effective agents
- 作者：Anthropic（頁尾署名 Erik S. 與 Barry Zhang，Erik 的全名頁面沒寫，待確認）
- 年份：2024（頁面標示 2024-12-19）
- 類型：部落格文章
- 正式網址：https://www.anthropic.com/research/building-effective-agents
- 抓取備註：原本的 /engineering/ 網址會被轉到 /research/，這裡記轉址後的網址。

## 一句話摘要

Anthropic 根據跟客戶合作的經驗，把「agentic 系統」分成 **workflow（流程寫死）** 和 **agent（模型自己決定步驟）** 兩種，並整理出五種常見 workflow 模式，核心建議是：能簡單就簡單，真的需要才加複雜度。

## 重點整理

1. **Workflow vs Agent**：workflow 是用預先寫好的程式路徑串起 LLM 和工具；agent 則是 LLM 自己決定流程和要用哪些工具。
2. **基本積木是「增強型 LLM」（augmented LLM）**：LLM 加上檢索、工具、記憶。
3. **五種 workflow 模式**：Prompt chaining（串接）、Routing（分流）、Parallelization（平行，含 sectioning 和 voting）、Orchestrator-workers（指揮者與工人）、Evaluator-optimizer（評估者與優化者）。詳見 [工作流模式](workflow-patterns.md)。
4. **Agent 的本質很單純**：就是 LLM 在迴圈裡，根據環境回饋來用工具。每一步都要從環境拿到「ground truth」（例如工具結果、程式執行結果）來判斷進度。
5. **要設停止條件**：例如最多跑幾輪，避免失控。
6. **風險**：自主性帶來更高成本和錯誤累積（compounding errors），建議在沙盒裡大量測試並加上 guardrails。
7. **三個原則**：保持簡單、讓規劃步驟透明、好好設計 agent-computer interface（ACI，也就是工具的說明和測試）。

## 原文摘錄

> "Workflows are systems where LLMs and tools are orchestrated through predefined code paths."
> "Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."
> "They are typically just LLMs using tools based on environmental feedback in a loop."
> "The autonomous nature of agents means higher costs, and the potential for compounding errors."

## 跟其他頁的關係

- 「workflow vs agent」的分法是 [Agent 定義](agent-definition.md) 的主軸，[LangGraph 文件](langgraph-workflows-agents.md) 也沿用同一套分類。
- 五種模式整理在 [工作流模式](workflow-patterns.md)。
- 成本、錯誤累積、停止條件放在 [風險與陷阱](risks.md)。
- ACI 與工具設計放在 [工具使用](tool-use.md)。
