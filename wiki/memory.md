---
id: memory
title: 記憶
type: concept
sources:
  - weng-llm-powered-agents
  - langgraph-workflows-agents
related:
  - planning
  - agent-definition
  - risks
updated: 2026-11-17
---

## 白話說

想像你在做期末報告：桌上攤開的幾張筆記是「短期記憶」，一次只放得下那麼多；書櫃裡整理好的資料夾是「長期記憶」，要用的時候再去翻。Agent 也一樣：**短期記憶是這次對話放得進 context window 的內容，長期記憶是存在外部資料庫、需要時再檢索回來的資料**。

## 重點

- **短期記憶 ≈ in-context learning**：就是放在 prompt／context 裡的內容，受 context window 長度限制。
- **長期記憶 ≈ 外部向量資料庫**：把資料轉成 embedding 存起來，查詢時用快速檢索取回最相關的幾筆。
- **快速檢索**：常用近似最近鄰（ANN）演算法，例如 HNSW、FAISS、ScaNN，犧牲一點準確度換取大幅加速。
- **框架裡的記憶**：LangGraph 把 short term memory 列為增強 LLM 的方式之一。
- **限制**：context 長度有限，向量檢索的表達能力也比不上完整的 attention。

## 各來源怎麼說

- Weng：用人腦的感官記憶、短期記憶、長期記憶來類比，並對應到 embedding、in-context learning、外部向量資料庫（[Weng](weng-llm-powered-agents.md)）。
- LangGraph：tool calling、structured output、short term memory 是常見的 LLM 增強方式（[LangGraph 文件](langgraph-workflows-agents.md)）。

## 常見誤會

- 「LLM 會記得上次聊過什麼」：不會自動記得，要靠系統把內容放回 context 或存進長期記憶再取回。
- 「context window 很長就不需要記憶設計」：長度再長還是有限，見 [風險與陷阱](risks.md)。

## 延伸閱讀

- [規劃](planning.md)：Reflexion 會把反思寫進工作記憶。
- [Agent 定義](agent-definition.md)
