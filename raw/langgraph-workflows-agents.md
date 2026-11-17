# Workflows and agents（LangGraph 官方文件）

- id：`langgraph-workflows-agents`
- 作者：LangChain
- 年份：待確認
- 日期：文件頁沒有日期，以擷取日 2026-11-17 為準
- 類型：官方文件
- 正式網址：https://docs.langchain.com/oss/python/langgraph/workflows-agents
- 抓取紀錄：第一次抓舊網址：HTTP 200 但內容只有 570 bytes 的 meta-refresh 轉址頁（證據：raw/evidence/langgraph-old-url-stub.html）。改抓新網址的 .md 版本才拿到正文。這是本次第一個被抓到的錯誤，促成「取得資料」節點加上內容檢查。
- 擷取時間：2026-11-17 09:38 (UTC+8)

## 摘錄（wiki 引文在原文中的上下文，已轉小寫並壓縮空白）

**引文**：Workflows have predetermined code paths and are designed to operate in a certain order.

> …e this file to discover all available pages before exploring further. # workflows and agents this guide reviews common workflow and agent patterns. * workflows have predetermined code paths and are designed to operate in a certain order. * agents are dynamic and define their own processes and tool usage.![agent workflow](https://mintcdn.com/langchain-5e9cc07a/-_xgpoyjhyidwtpj/oss/imag…

**引文**：Agents are dynamic and define their own processes and tool usage.

> …ts this guide reviews common workflow and agent patterns. * workflows have predetermined code paths and are designed to operate in a certain order. * agents are dynamic and define their own processes and tool usage.![agent workflow](https://mintcdn.com/langchain-5e9cc07a/-_xgpoyjhyidwtpj/oss/images/agent_workflow.png?fit=max&auto=format&n=-_xgpoyjhyidwtpj&q=85&s=…

**引文**：This loop continues until an acceptable response is generated.

> …/docs.langchain.com/oss/python/langgraph/interrupts.md) determines the response needs refinement, feedback is provided and the response is recreated. this loop continues until an acceptable response is generated. evaluator-optimizer workflows are commonly used when there's particular success criteria for a task, but iteration is required to meet that criteria.…
