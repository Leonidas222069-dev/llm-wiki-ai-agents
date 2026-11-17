---
id: risks
title: 風險與陷阱
type: concept
sources:
  - anthropic-building-effective-agents
  - openai-practical-guide
  - weng-llm-powered-agents
related:
  - agent-definition
  - react-loop
  - tool-use
  - multi-agent
updated: 2026-11-17
---

## 白話說

把車鑰匙交給新司機前，你會想裝行車紀錄器、限速、規定哪些路不能開。Agent 也一樣：它能自己做決定、自己動手，所以**錯誤會累積、成本會變高、還可能被騙去做壞事**。要靠 guardrails（護欄）、停止條件和人工把關來控制風險。

## 重點

- **成本與錯誤累積**：自主代表更高成本，一步錯可能步步錯（compounding errors）。對策：沙盒測試、guardrails。
- **停不下來**：要設停止條件，例如最大輪數、失敗次數上限。
- **模型本身的限制**：context 長度有限、長期規劃困難、自然語言介面不可靠（格式錯誤、不照指示）。
- **被攻擊**：jailbreak、prompt injection 可能讓 agent 洩漏系統提示或做出不該做的事。
- **分層 guardrails**：相關性分類、安全分類、PII 過濾、內容審核、工具風險分級（低／中／高，看是否唯讀、能否復原、權限、金錢影響）、規則式防護（黑名單、長度限制、正規表達式）。
- **人工介入**：失敗超過門檻，或要做高風險、不可逆的動作（取消訂單、大額退款、付款）時，交給人。
- **別過度設計**：只有在真的能改善結果時才增加複雜度。

## 各來源怎麼說

- Anthropic：自主帶來更高成本和錯誤累積，建議在沙盒中大量測試並加上 guardrails；也提醒先找最簡單的解法（[Anthropic](anthropic-building-effective-agents.md)）。
- OpenAI：guardrails 是分層防禦，單一層不夠；高風險動作要人工把關（[OpenAI 指南](openai-practical-guide.md)）。
- Weng：列出三個挑戰：context 長度有限、長期規劃困難、自然語言介面不可靠（[Weng](weng-llm-powered-agents.md)）。

## 常見誤會

- 「加一個安全過濾就夠了」：OpenAI 明講單一層防護不夠，要多層。
- 「agent 做錯會自己發現」：不一定，所以要從環境拿 ground truth、設停止條件，必要時交給人，見 [ReAct 迴圈](react-loop.md)。

## 延伸閱讀

- [Agent 定義](agent-definition.md)
- [工具使用](tool-use.md)：工具風險分級。
- [多代理](multi-agent.md)：多代理帶來的額外複雜度。
