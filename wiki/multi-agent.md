---
id: multi-agent
title: 多代理
type: concept
sources:
  - openai-practical-guide
  - anthropic-building-effective-agents
related:
  - workflow-patterns
  - tool-use
  - agent-definition
updated: 2026-11-17
---

## 白話說

一個人包辦所有事情會手忙腳亂，所以公司會分部門。多代理（multi-agent）就是**把工作分給好幾個各有專長的 agent**。但分部門也有成本：溝通變多、出錯更難追。所以建議**先把一個 agent 做到極致，真的撐不住再拆**。

## 重點

- **先單、後多**：單一 agent 靠逐步加工具就能處理很多任務，也比較好評估和維護。
- **什麼時候該拆**：
  - 提示裡的條件分支（if-else）多到難以維護；
  - 工具彼此太像、模型一直選錯（有些系統能管好超過 15 個清楚的工具，有些在不到 10 個重疊工具時就出問題）。
- **兩種常見模式**：
  - Manager（管理者）：一個中央 agent 把其他專門 agent 當成工具呼叫，由它統一跟使用者互動。例子：翻譯請求交給西班牙文、法文、義大利文 agent。
  - Decentralized（去中心化）：agent 之間平起平坐，用 handoff 把控制權交給另一個 agent。例子：分流 agent 把訂單問題交給訂單管理 agent。
- **用圖來想**：多代理系統可以看成一張圖，agent 是節點；manager 模式的邊是工具呼叫，decentralized 模式的邊是 handoff。

## 各來源怎麼說

- OpenAI：建議先最大化單一 agent 的能力；多代理分 manager 和 decentralized 兩類，並給出拆分的實務準則（[OpenAI 指南](openai-practical-guide.md)）。
- Anthropic：orchestrator-workers 是由中央 LLM 動態分派任務給 worker LLM，概念上很接近 manager 模式（[Anthropic](anthropic-building-effective-agents.md)）。

## 常見誤會

- 「agent 越多越聰明」：多代理會增加複雜度和額外負擔，常常一個 agent 加工具就夠了。
- 「多代理一定要畫完整的圖」：OpenAI 提到宣告式的圖在流程變複雜時會很笨重，它的 SDK 採 code-first 的方式。

## 延伸閱讀

- [工作流模式](workflow-patterns.md)：orchestrator-workers。
- [工具使用](tool-use.md)：agent 也能當工具。
- [Agent 定義](agent-definition.md)
