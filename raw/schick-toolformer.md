# Toolformer: Language Models Can Teach Themselves to Use Tools

- id：`schick-toolformer`
- 作者：Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- 年份：2023
- 日期：arXiv v1 2023-02-09
- 類型：論文（arXiv 2302.04761）
- 正式網址：https://arxiv.org/abs/2302.04761
- 抓取紀錄：HTTP 200。作者與日期取自 arXiv citation_* meta；全文取自 PDF（pdftotext）。 第一次用 pdftotext -layout 轉檔，雙欄排版造成摘要和圖說交錯，引文比對失敗；改用預設模式（依閱讀順序）重新轉檔。 另外發現 arXiv 摘要頁寫 "two different search engines"，PDF（v1）摘要寫 "a search engine"，正文列出五種工具（含一個 Wikipedia 搜尋引擎）；wiki 以 PDF 為準。
- 擷取時間：2026-11-17 09:38 (UTC+8)

## 摘錄（wiki 引文在原文中的上下文，已轉小寫並壓縮空白）

**引文**：We introduce Toolformer, a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction.

> …smaller models excel. in this paper, we show that lms can teach themselves to use external tools via simple apis and achieve the best of both worlds. we introduce toolformer, a model trained to decide which apis to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. this is done in a self-supervised way, requiring nothing more than a handful of demonstrations for each api. we incorporate a range of tools, includi…

**引文**：Concretely, we explore the following five tools: a question answering system, a Wikipedia search engine, a calculator, a calendar, and a machine translation system.

> …ls is that (i) both their inputs and outputs can be represented as text sequences, and (ii) we can obtain a few demonstrations of their intended use. concretely, we explore the following five tools: a question answering system, a wikipedia search engine, a calculator, a calendar, and a machine translation system. some examples of potential calls and return strings for the apis associated with each of these tools are shown in table 1. we briefly discuss all too…
