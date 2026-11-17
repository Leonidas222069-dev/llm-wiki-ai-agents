---
id: schick-toolformer
title: 來源｜Toolformer（Schick et al., 2023）
type: source
sources:
  - schick-toolformer
related:
  - tool-use
  - react-loop
updated: 2026-11-17
---

## 基本資料

- 標題：Toolformer: Language Models Can Teach Themselves to Use Tools
- 作者：Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- 年份：2023（arXiv 2302.04761 第一版 2023-02-09）
- 類型：論文（Meta AI Research）
- 正式網址：https://arxiv.org/abs/2302.04761

## 一句話摘要

語言模型很會寫文章，卻常算錯數學、記錯事實；Toolformer 讓模型**自己學會什麼時候該呼叫哪個 API**（問答、Wikipedia 搜尋、計算機、日曆、翻譯），而且只需要每個工具少量示範。

## 重點整理

1. **矛盾點**：大模型能做很多新任務，卻在算術、查事實這種基本功上輸給簡單的小工具。
2. **做法（自我監督，三步）**：
   - 先讓模型在一般文字裡「試著插入」大量可能的 API 呼叫（sample）；
   - 實際執行這些 API 呼叫（execute）；
   - 只保留「真的有幫助預測後面文字」的呼叫（filter），再拿這些資料微調模型。
3. **工具清單（依 PDF 正文）**：問答系統、Wikipedia 搜尋引擎、計算機、日曆、機器翻譯系統，共五種。注意：arXiv 摘要頁寫「two different search engines」，但 PDF（v1）摘要寫「a search engine」，兩邊不一致，本 wiki 以 PDF 為準。
4. **結果**：以 6.7B 參數的 GPT-J 為底，零樣本（zero-shot）表現大幅提升，常常能和大很多的模型競爭，又不犧牲原本的語言能力。
5. **跟 agent 的關係**：Toolformer 回答的是「模型怎麼學會用工具」，是 agent「工具使用」能力的早期研究之一。

## 原文摘錄

> "We introduce Toolformer, a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction."
> "Concretely, we explore the following five tools: a question answering system, a Wikipedia search engine, a calculator, a calendar, and a machine translation system."

## 跟其他頁的關係

- 工具使用的整體整理在 [工具使用](tool-use.md)。
- Toolformer 是「訓練模型學會用工具」，[ReAct](react-loop.md) 則是「用提示讓模型邊想邊用工具」，兩種路線可以對照。
