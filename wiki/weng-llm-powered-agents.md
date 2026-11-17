---
id: weng-llm-powered-agents
title: 來源｜Lilian Weng〈LLM Powered Autonomous Agents〉
type: source
sources:
  - weng-llm-powered-agents
related:
  - planning
  - memory
  - tool-use
  - risks
updated: 2026-11-17
---

## 基本資料

- 標題：LLM Powered Autonomous Agents（文末引用格式寫成 LLM-powered Autonomous Agents，以頁面標題為準）
- 作者：Lilian Weng
- 年份：2023（2023 年 6 月）
- 類型：部落格文章（Lil'Log）
- 正式網址：https://lilianweng.github.io/posts/2023-06-23-agent/

## 一句話摘要

把 LLM 當成 agent 的「大腦」，再配上三個元件：**規劃（Planning）、記憶（Memory）、工具使用（Tool use）**，並整理各元件的代表方法和目前的限制。

## 重點整理

1. **系統總覽**：LLM 是大腦，旁邊配規劃、記憶、工具三大元件。
2. **規劃**：
   - 任務拆解：Chain of Thought（CoT，一步一步想）、Tree of Thoughts（每一步展開多種想法，像樹一樣搜尋）。
   - 自我反思：ReAct（把推理和行動交錯）、Reflexion（失敗後寫反思，放進工作記憶再試）。
3. **記憶**：用人腦記憶類比，短期記憶 ≈ in-context learning（受限於 context window），長期記憶 ≈ 外部向量資料庫，查詢時用快速檢索（MIPS／ANN）取回。
4. **工具使用**：MRKL、TALM、Toolformer 等方法讓 LLM 呼叫外部 API，補上模型權重裡沒有的資訊（例如最新資訊、執行程式碼）。
5. **三個挑戰**：context 長度有限、長期規劃與任務拆解困難、自然語言介面不可靠（模型可能格式錯誤或不照指示）。
6. 文中把 ReAct 標為「Yao et al. 2023」，但 arXiv 第一版是 2022 年（ICLR 2023 發表）。本 wiki 以 arXiv 年份 2022 為準，見 [ReAct 論文](yao-react.md)。

## 原文摘錄

> "In a LLM-powered autonomous agent system, LLM functions as the agent's brain, complemented by several key components:"
> "Short-term memory as in-context learning."
> "Long-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval."
> "LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error."

## 跟其他頁的關係

- 三大元件分別展開成 [規劃](planning.md)、[記憶](memory.md)、[工具使用](tool-use.md)。
- 三個挑戰整理進 [風險與陷阱](risks.md)。
- 文中的 ReAct 段落和 [ReAct 迴圈](react-loop.md) 互相對照。
