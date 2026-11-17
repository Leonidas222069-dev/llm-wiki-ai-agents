---
id: workflow-patterns
title: 工作流模式
type: concept
sources:
  - anthropic-building-effective-agents
  - langgraph-workflows-agents
related:
  - agent-definition
  - multi-agent
  - react-loop
updated: 2026-11-17
---

## 白話說

不是每件事都要請一個「自己做決定」的 agent。很多時候，把流程先畫好，讓 LLM 在固定的位置做事就夠了，就像工廠的生產線。Anthropic 和 LangGraph 都整理出**五種常見的 workflow 模式**，可以像積木一樣組合。

## 重點

| 模式 | 一句話 | 什麼時候用 | 例子 |
|---|---|---|---|
| Prompt chaining（串接） | 上一步的輸出是下一步的輸入，中間可以加檢查關卡（gate） | 任務能拆成固定步驟 | 先寫大綱、檢查大綱、再寫全文 |
| Routing（分流） | 先分類，再送到專門的處理流程 | 輸入有明顯不同的類別 | 客服問題分成一般、退款、技術支援 |
| Parallelization（平行） | 同時跑多個 LLM 再彙整；分成 sectioning（切塊）和 voting（投票） | 想加速，或想要多個角度提高信心 | 一個回答、另一個做內容把關 |
| Orchestrator-workers（指揮者與工人） | 中央 LLM 動態拆任務、分給 worker、再整合 | 事先不知道要拆成哪些子任務 | 要改的檔案數量不固定的程式任務 |
| Evaluator-optimizer（評估與優化） | 一個產生、一個評估，不合格就帶回饋重做 | 有明確評分標準、反覆修改有價值 | 文學翻譯 |

- **Workflow 和 agent 的分界**：上面五種的路徑大致由開發者決定；agent 則由 LLM 自己決定路徑。
- **Orchestrator-workers vs Parallelization**：圖長得很像，差別在子任務是不是事先定義好的。

## 各來源怎麼說

- Anthropic：從「增強型 LLM」出發，依序介紹五種 workflow，再到自主 agent，並強調這些是可以自由組合的積木（[Anthropic](anthropic-building-effective-agents.md)）。
- LangGraph：每種模式都用 StateGraph 實作一次；orchestrator-worker 用 `Send` API 動態產生 worker，evaluator-optimizer 一直循環到產生可以接受的回答為止（[LangGraph 文件](langgraph-workflows-agents.md)）。

## 常見誤會

- 「用框架就一定比較好」：Anthropic 提醒框架可能讓底層 prompt 不透明、難除錯，建議先直接用 LLM API。
- 「Evaluator-optimizer 一定會越改越好」：前提是評分標準要明確，見 [風險與陷阱](risks.md)。

## 延伸閱讀

- [多代理](multi-agent.md)：orchestrator-workers 再往前一步。
- [Agent 定義](agent-definition.md)
- [ReAct 迴圈](react-loop.md)
