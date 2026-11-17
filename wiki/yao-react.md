---
id: yao-react
title: 來源｜ReAct（Yao et al., 2022）
type: source
sources:
  - yao-react
related:
  - react-loop
  - planning
  - tool-use
updated: 2026-11-17
---

## 基本資料

- 標題：ReAct: Synergizing Reasoning and Acting in Language Models
- 作者：Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- 年份：2022（arXiv 2210.03629 第一版 2022-10-06；ICLR 2023 發表）
- 類型：論文
- 正式網址：https://arxiv.org/abs/2210.03629

## 一句話摘要

讓 LLM **交錯產生「推理」（Thought）和「行動」（Action）**：想一下 → 做一個動作（例如查 Wikipedia）→ 看結果 → 再想，比只推理或只行動都好。

## 重點整理

1. **問題**：以前「推理」（例如 chain-of-thought）和「行動」（例如產生行動計畫）是分開研究的。
2. **做法**：讓模型交錯輸出推理軌跡和具體行動。推理幫助模型擬定、追蹤、更新計畫；行動讓模型能和外部（知識庫、環境）互動、拿到新資訊。
3. **好處一：比較不會亂編**。在 HotpotQA（問答）和 Fever（事實查核）上，透過一個簡單的 Wikipedia API 查資料，減少 chain-of-thought 常見的幻覺（hallucination）和錯誤傳遞。
4. **好處二：比較好懂**。產生的解題軌跡像人類一樣，比較容易解讀、也比較值得信任。
5. **決策任務**：在 ALFWorld 和 WebShop 兩個互動式任務上，只用一兩個範例提示，成功率分別比模仿學習和強化學習方法高出 34% 和 10%（絕對值）。

## 原文摘錄

> "In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two"
> "an absolute success rate of 34% and 10% respectively"

## 跟其他頁的關係

- 迴圈怎麼運作，用白話整理在 [ReAct 迴圈](react-loop.md)。
- Weng 在 [她的文章](weng-llm-powered-agents.md) 裡把 ReAct 歸在「自我反思」，放進 [規劃](planning.md)。
- ReAct 的 Action 就是一種 [工具使用](tool-use.md)。
