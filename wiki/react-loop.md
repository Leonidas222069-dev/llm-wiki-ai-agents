---
id: react-loop
title: ReAct 迴圈
type: concept
sources:
  - yao-react
  - weng-llm-powered-agents
  - openai-practical-guide
  - anthropic-building-effective-agents
related:
  - tool-use
  - planning
  - agent-definition
  - risks
updated: 2026-11-17
---

## 白話說

像偵探辦案：**先想**「兇手可能是誰？我該去查什麼？」→ **再做**「去調監視器」→ **看結果**「監視器拍到某人」→ 再想下一步……一直循環到破案。ReAct（Reasoning + Acting）就是讓 LLM 用這種「想 → 做 → 看」的節奏解題。

## 重點

- **三個步驟不斷重複**：
  - Thought（想）：用自然語言推理，決定下一步。
  - Action（做）：呼叫工具，例如 Wikipedia 搜尋。
  - Observation（看）：讀取工具回傳的結果。
- **為什麼有效**：推理幫助擬定和更新計畫；行動讓模型拿到外部的真實資訊，減少幻覺和錯誤傳遞。
- **實驗結果**：在 HotpotQA、Fever 上比純 chain-of-thought 更少幻覺；在 ALFWorld、WebShop 上，成功率比模仿學習和強化學習方法高出 34% 和 10%（絕對值）。
- **什麼時候停**：工程上的 agent「run」就是一個 while 迴圈，直到呼叫最終輸出工具、模型不再呼叫工具、發生錯誤，或達到最大輪數。

## 各來源怎麼說

- ReAct 論文：讓 LLM 交錯產生推理軌跡和任務行動（[ReAct 論文](yao-react.md)）。
- Weng：ReAct 的提示格式大致是 Thought / Action / Observation 重複多次；拿掉 Thought 的 Act-only 版本表現比較差（[Weng](weng-llm-powered-agents.md)）。
- OpenAI：每種編排方式都需要「run」的概念，通常是一個跑到結束條件為止的迴圈（[OpenAI 指南](openai-practical-guide.md)）。
- Anthropic：agent 每一步都要從環境拿到 ground truth，也常加上最大輪數這類停止條件（[Anthropic](anthropic-building-effective-agents.md)）。

## 常見誤會

- 「Thought 只是讓輸出比較好看」：拿掉 Thought 的版本表現比較差，推理是真的有用。
- 「迴圈會自己停」：一定要設停止條件，不然可能一直燒錢，見 [風險與陷阱](risks.md)。

## 延伸閱讀

- [工具使用](tool-use.md)：Action 背後的工具。
- [規劃](planning.md)：ReAct 在規劃裡屬於「自我反思」。
- [Agent 定義](agent-definition.md)
