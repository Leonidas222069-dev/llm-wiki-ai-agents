---
id: tool-use
title: 工具使用
type: concept
sources:
  - openai-practical-guide
  - schick-toolformer
  - weng-llm-powered-agents
  - anthropic-building-effective-agents
related:
  - agent-definition
  - react-loop
  - multi-agent
  - risks
updated: 2026-11-17
---

## 白話說

LLM 就像一個讀過很多書、但被關在房間裡的人：它知道很多，卻不知道今天的新聞，心算也可能出錯。**工具（tool）就是從房間伸出去的手**：查網路、算數學、讀資料庫、寄信。Agent 會判斷「現在需要哪隻手」，呼叫工具、拿回結果，再決定下一步。

## 重點

- **為什麼需要工具**：補上模型權重裡沒有的東西，例如最新資訊、程式執行、私有資料。
- **工具三類**：Data（取得資訊）、Action（採取行動）、Orchestration（把別的 agent 當工具）。
- **模型怎麼學會用工具**：Toolformer 用自我監督的方式，讓模型自己插入 API 呼叫、執行、只保留有幫助的，再微調；論文用了五種工具：問答系統、Wikipedia 搜尋、計算機、日曆、機器翻譯。
- **工具說明要寫清楚**：Anthropic 叫它 agent-computer interface（ACI），要像寫給新同事的說明文件一樣，附範例、邊界情況、輸入格式。
- **工具多了要注意**：問題不只是數量，而是工具彼此太像。分不清時考慮拆成 [多代理](multi-agent.md)。

## 各來源怎麼說

- OpenAI：工具分 Data、Action、Orchestration 三類；每個工具要有標準化定義、文件完整、測試過（[OpenAI 指南](openai-practical-guide.md)）。
- Toolformer：模型可以只靠每個工具少量示範，自己學會什麼時候呼叫哪個 API（[Toolformer](schick-toolformer.md)）。
- Weng：MRKL、TALM、Toolformer 都是讓 LLM 使用外部工具的方法（[Weng](weng-llm-powered-agents.md)）。
- Anthropic：建議花在工具設計上的心力要跟寫 prompt 一樣多（[Anthropic](anthropic-building-effective-agents.md)）。

## 常見誤會

- 「模型會自己知道工具怎麼用」：不一定，工具名稱、參數、說明寫不清楚，模型就容易用錯。
- 「工具越多越強」：工具重疊會讓模型選錯，見 [風險與陷阱](risks.md)。

## 延伸閱讀

- [ReAct 迴圈](react-loop.md)：工具呼叫怎麼嵌進「想→做→看」的循環。
- [Agent 定義](agent-definition.md)
