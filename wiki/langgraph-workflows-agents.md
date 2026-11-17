---
id: langgraph-workflows-agents
title: 來源｜LangGraph 文件〈Workflows and agents〉
type: source
sources:
  - langgraph-workflows-agents
related:
  - workflow-patterns
  - agent-definition
  - react-loop
updated: 2026-11-17
---

## 基本資料

- 標題：Workflows and agents（LangGraph 官方文件）
- 作者：LangChain
- 年份：文件頁沒有日期，以擷取日 2026-11-17 為準（待確認）
- 類型：官方文件
- 正式網址：https://docs.langchain.com/oss/python/langgraph/workflows-agents
- 抓取備註：舊網址 langchain-ai.github.io/langgraph/tutorials/workflows/ 回 HTTP 200，但內容只是轉址殘頁，見 [流程說明](../process.md)。

## 一句話摘要

LangGraph 官方把常見的 workflow 和 agent 模式，各用一張「graph（節點＋邊）」實作出來：prompt chaining、parallelization、routing、orchestrator-worker、evaluator-optimizer，以及用工具的 agent 迴圈。

## 重點整理

1. **分類跟 Anthropic 一樣**：workflow 的程式路徑是事先決定好的；agent 會動態決定自己的流程和工具。
2. **增強型 LLM**：tool calling、structured output、short term memory 是常見的增強方式。
3. **每個模式都是一張圖**：用 StateGraph 定義 state、節點（node）、邊（edge），compile 後執行。
4. **Orchestrator-worker**：用 `Send` API 動態產生 worker 節點，每個 worker 有自己的 state，結果寫回共享的 state 讓 orchestrator 彙整。
5. **Evaluator-optimizer**：一個 LLM 產生、另一個評估；不合格就帶著回饋重做，直到可以接受為止，也可以由人（human-in-the-loop）來評估。
6. **Agent**：LLM 透過工具行動，在持續的回饋迴圈裡運作，適合問題和解法都難以預測的情境；開發者仍然可以限定可用工具和行為準則。

## 原文摘錄

> "Workflows have predetermined code paths and are designed to operate in a certain order."
> "Agents are dynamic and define their own processes and tool usage."
> "This loop continues until an acceptable response is generated."

## 跟其他頁的關係

- 五種模式的比較表在 [工作流模式](workflow-patterns.md)。
- workflow／agent 的分界在 [Agent 定義](agent-definition.md)。
- 工具迴圈跟 [ReAct 迴圈](react-loop.md) 是同一個想法。
