# Building effective agents

- id：`anthropic-building-effective-agents`
- 作者：Anthropic（頁尾署名 Erik S. 與 Barry Zhang；Erik 的全名頁面未寫出，待確認）
- 年份：2024
- 日期：2024-12-19（頁面 JSON-LD datePublished）
- 類型：部落格文章
- 正式網址：https://www.anthropic.com/research/building-effective-agents
- 抓取紀錄：HTTP 200，但被轉址：/engineering/ → /research/。wiki 一律記錄轉址後的正式網址。
- 擷取時間：2026-11-17 09:38 (UTC+8)

## 摘錄（wiki 引文在原文中的上下文，已轉小寫並壓縮空白）

**引文**：Workflows are systems where LLMs and tools are orchestrated through predefined code paths.

> …s. at anthropic, we categorize all these variations as agentic systems, but draw an important architectural distinction between workflows and agents: workflows are systems where llms and tools are orchestrated through predefined code paths. agents, on the other hand, are systems where llms dynamically direct their own processes and tool usage, maintaining control over how they accomplish…

**引文**：Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

> …nt architectural distinction between workflows and agents: workflows are systems where llms and tools are orchestrated through predefined code paths. agents, on the other hand, are systems where llms dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks. below, we will explore both types of agentic systems in detail. in appendix 1 ("agents in practice"), we describe two domains where customers have fo…

**引文**：They are typically just LLMs using tools based on environmental feedback in a loop.

> …uch as a maximum number of iterations) to maintain control. agents can handle sophisticated tasks, but their implementation is often straightforward. they are typically just llms using tools based on environmental feedback in a loop. it is therefore crucial to design toolsets and their documentation clearly and thoughtfully. we expand on best practices for tool development in appe…

**引文**：The autonomous nature of agents means higher costs, and the potential for compounding errors.

> …any turns, and you must have some level of trust in its decision-making. agents' autonomy makes them ideal for scaling tasks in trusted environments. the autonomous nature of agents means higher costs, and the potential for compounding errors. we recommend extensive testing in sandboxed environments, along with the appropriate guardrails. examples where agents are useful: the following exam…
