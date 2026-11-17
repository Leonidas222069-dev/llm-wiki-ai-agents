---
id: agent-definition
title: Agent 定義
type: concept
sources:
  - anthropic-building-effective-agents
  - openai-practical-guide
  - langgraph-workflows-agents
  - weng-llm-powered-agents
related:
  - workflow-patterns
  - tool-use
  - react-loop
  - risks
updated: 2026-11-17
---

## 白話說

聊天機器人像「很會回答問題的客服」：你問一句、它答一句，事情還是你自己去做。Agent 比較像「幫你跑腿的助理」：你交代目標，它自己決定要查什麼、用什麼工具、做幾步，做完（或卡住）再回來跟你報告。簡單講，**agent 就是讓 LLM 自己掌控流程、會用工具、在迴圈裡一步步把任務做完的系統**。

## 重點

- **關鍵差別在「誰決定下一步」**：流程寫死在程式裡的是 workflow；由 LLM 動態決定步驟和工具的才是 agent。兩者合稱 agentic 系統。
- **不算 agent 的例子**：單純的聊天機器人、單輪 LLM 呼叫、情緒分類器，因為它們沒有用 LLM 控制流程執行。
- **agent 的組成**：模型（大腦）＋工具＋指令／guardrails；Weng 的說法則是 LLM 大腦＋規劃＋記憶＋工具。
- **運作方式**：在迴圈中行動，每一步從環境拿回真實結果（工具輸出、程式執行結果）來判斷進度，直到完成或觸發停止條件。
- **各自適合什麼**：workflow 對定義清楚的任務提供可預測性和一致性；agent 適合步驟數量難以預測、沒辦法把路徑寫死的開放式問題，代價是成本較高、錯誤可能累積。
- **不是越自主越好**：先找最簡單的解法，很多應用只要把單次 LLM 呼叫做好就夠了。

## 各來源怎麼說

- Anthropic：把 workflow（預先寫好的程式路徑）和 agent（LLM 自己主導流程與工具）分開，並說 agent 本質上就是「LLM 根據環境回饋在迴圈中使用工具」（[Anthropic](anthropic-building-effective-agents.md)）。
- OpenAI：agent 是「代替你獨立完成任務」的系統；聊天機器人、單輪 LLM、情緒分類器不算（[OpenAI 指南](openai-practical-guide.md)）。
- LangGraph：workflow 有事先決定的程式路徑；agent 是動態的，自己決定流程和工具（[LangGraph 文件](langgraph-workflows-agents.md)）。
- Weng：LLM 是 agent 的大腦，再配上規劃、記憶、工具三個元件（[Weng](weng-llm-powered-agents.md)）。

## 常見誤會

- 「會聊天就是 agent」：不對，沒有自己控制流程、沒有用工具採取行動的，只是聊天機器人。
- 「agent 一定要很多個」：不用，單一 agent 加上適合的工具就能處理很多事，見 [多代理](multi-agent.md)。
- 「agent 一定比 workflow 好」：不一定，流程固定的任務用 workflow 更穩定、更好預測，見 [工作流模式](workflow-patterns.md)。

## 延伸閱讀

- [工具使用](tool-use.md)：agent 怎麼「動手」。
- [ReAct 迴圈](react-loop.md)：agent 一步一步做事的經典寫法。
- [風險與陷阱](risks.md)：自主帶來的代價。
