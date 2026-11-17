# LLM Powered Autonomous Agents

- id：`weng-llm-powered-agents`
- 作者：Lilian Weng
- 年份：2023
- 日期：2023-06（文末 Cited as: Jun 2023）
- 類型：部落格文章（Lil'Log）
- 正式網址：https://lilianweng.github.io/posts/2023-06-23-agent/
- 抓取紀錄：HTTP 200，內容完整。注意：頁面標題是 "LLM Powered Autonomous Agents"，文末建議引用格式寫成 "LLM-powered Autonomous Agents"，以頁面標題為準。
- 擷取時間：2026-11-17 09:38 (UTC+8)

## 摘錄（wiki 引文在原文中的上下文，已轉小寫並壓縮空白）

**引文**：In a LLM-powered autonomous agent system, LLM functions as the agent's brain, complemented by several key components:

> …s beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver. agent system overview # in a llm-powered autonomous agent system, llm functions as the agent's brain, complemented by several key components: planning subgoal and decomposition: the agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks…

**引文**：Short-term memory as in-context learning.

> …ghly consider the following mappings: sensory memory as learning embedding representations for raw inputs, including text, image or other modalities; short-term memory as in-context learning. it is short and finite, as it is restricted by the finite context window length of transformer. long-term memory as the external vector store that th…

**引文**：Long-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval.

> …modalities; short-term memory as in-context learning. it is short and finite, as it is restricted by the finite context window length of transformer. long-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval. maximum inner product search (mips) # the external memory can alleviate the restriction of finite attention span. a standard practice is to save the …

**引文**：LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.

> …lenges in long-term planning and task decomposition: planning over a lengthy history and effectively exploring the solution space remain challenging. llms struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error. reliability of natural language interface: current agent system relies on natural language as an interface between llms and external components such …
