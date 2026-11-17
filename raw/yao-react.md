# ReAct: Synergizing Reasoning and Acting in Language Models

- id：`yao-react`
- 作者：Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- 年份：2022
- 日期：arXiv v1 2022-10-06；v3 2023-03-10；發表於 ICLR 2023（PDF 首頁）
- 類型：論文（arXiv 2210.03629）
- 正式網址：https://arxiv.org/abs/2210.03629
- 抓取紀錄：HTTP 200。作者與日期取自 arXiv 頁面 citation_* meta；全文取自 PDF（pdftotext）。 第一次用 pdftotext -layout 轉檔；Toolformer 因雙欄交錯出錯後，這篇也一併改用預設模式重新轉檔（這篇的引文兩種模式都比對得到）。
- 擷取時間：2026-11-17 09:38 (UTC+8)

## 摘錄（wiki 引文在原文中的上下文，已轉小寫並壓縮空白）

**引文**：In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two

> …ir abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. in this paper, we explore the use of llms to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and ga…

**引文**：an absolute success rate of 34% and 10% respectively

> … furthermore, on two interactive decision making benchmarks (alfworld and webshop), react outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. 1 i ntroduction a unique feature of human intelligence is the ability to seamlessly c…
