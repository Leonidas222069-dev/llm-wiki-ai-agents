---
id: planning
title: 規劃
type: concept
sources:
  - weng-llm-powered-agents
  - yao-react
related:
  - react-loop
  - memory
  - risks
updated: 2026-11-17
---

## 白話說

煮一頓晚餐不會一次想完所有動作，而是先拆成「買菜、洗菜、切菜、下鍋」，煮壞了還會想想哪裡出錯、下次改進。Agent 的規劃也是兩件事：**把大任務拆成小步驟（任務拆解）**，以及**回頭檢討、修正做法（自我反思）**。

## 重點

- **任務拆解**：
  - Chain of Thought（CoT）：要模型「一步一步想」，把難題拆成簡單步驟。
  - Tree of Thoughts：每一步展開多種可能，像樹一樣用 BFS 或 DFS 搜尋。
  - 拆解可以靠提示（例如「達成 XYZ 的子目標有哪些？」）、任務專用指令，或由人提供。
- **自我反思**：
  - ReAct：把推理和行動交錯，見 [ReAct 迴圈](react-loop.md)。
  - Reflexion：失敗後產生反思文字，存進工作記憶，下次嘗試時參考。
- **難處**：長期規劃和探索解法很難，遇到意外錯誤時 LLM 不太會調整計畫。

## 各來源怎麼說

- Weng：規劃包含「子目標與拆解」和「反思與修正」兩部分，並整理 CoT、Tree of Thoughts、ReAct、Reflexion 等方法（[Weng](weng-llm-powered-agents.md)）。
- ReAct：推理軌跡能幫模型擬定、追蹤、更新行動計畫，也能處理例外狀況（[ReAct 論文](yao-react.md)）。

## 常見誤會

- 「規劃就是一開始寫好完整計畫」：好的 agent 會邊做邊根據觀察結果修正計畫。
- 「會反思就不會犯錯」：反思能改善，但長期規劃仍然是公認的難題，見 [風險與陷阱](risks.md)。

## 延伸閱讀

- [記憶](memory.md)：反思要存在哪裡。
- [ReAct 迴圈](react-loop.md)
