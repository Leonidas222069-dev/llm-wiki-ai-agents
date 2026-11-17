---
id: openai-practical-guide
title: 來源｜OpenAI〈A practical guide to building agents〉
type: source
sources:
  - openai-practical-guide
related:
  - agent-definition
  - multi-agent
  - risks
  - tool-use
updated: 2026-11-17
---

## 基本資料

- 標題：A practical guide to building agents
- 作者：OpenAI
- 年份：2025（PDF 內文沒寫日期，依 PDF metadata 建立日 2025-04-07；精確發布日待確認）
- 類型：PDF 指南（34 頁）
- 正式網址：https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf

## 一句話摘要

寫給產品和工程團隊的實務指南：什麼是 agent、什麼時候值得做、agent 的三個核心元件（模型、工具、指令）、單代理與多代理的編排方式，以及 guardrails 和人工介入。

## 重點整理

1. **定義**：agent 是能「代替你、獨立完成任務」的系統。單純的聊天機器人、單輪 LLM、情緒分類器**不算** agent，因為它們沒有用 LLM 來控制流程執行。
2. **什麼時候值得做**：複雜判斷（例如退款審核）、規則多到難以維護、需要大量處理非結構化資料的流程。
3. **三個核心元件**：Model（負責推理和決策的 LLM）、Tools（可以呼叫的外部函式或 API）、Instructions（明確的指示和 guardrails）。
4. **工具三類**：Data（取資料，例如查資料庫、讀 PDF、搜尋網頁）、Action（做事，例如寄信、更新紀錄）、Orchestration（agent 本身也能當別的 agent 的工具）。
5. **「run」就是一個迴圈**：一直跑直到遇到結束條件，例如呼叫了最終輸出工具、模型回覆時沒有呼叫工具、發生錯誤，或達到最大輪數。
6. **先把單一 agent 做到極致**，真的需要時才拆成多代理。拆分訊號：提示裡 if-else 太多、工具太多或彼此太像。文中提到有些系統能管好超過 15 個定義清楚的工具，有些則在不到 10 個重疊工具時就出錯。
7. **多代理兩種模式**：Manager（一個管理者 agent 把其他 agent 當工具呼叫）、Decentralized（agent 之間互相 handoff 交接）。
8. **Guardrails 要分層**：相關性分類、安全分類（擋 jailbreak、prompt injection）、PII 過濾、內容審核、工具風險分級、規則式防護（黑名單、正規表達式）等。
9. **人工介入**兩個時機：失敗次數超過門檻、要做高風險動作（例如取消訂單、大額退款、付款）。

## 原文摘錄

> "Agents are systems that independently accomplish tasks on your behalf."
> "Our general recommendation is to maximize a single agent's capabilities first."
> "Think of guardrails as a layered defense mechanism."

## 跟其他頁的關係

- 定義和「什麼不算 agent」放在 [Agent 定義](agent-definition.md)。
- Manager／Decentralized 放在 [多代理](multi-agent.md)。
- Guardrails 和人工介入放在 [風險與陷阱](risks.md)。
- 工具三類放在 [工具使用](tool-use.md)。
