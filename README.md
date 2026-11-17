# AI Agents LLM Wiki ＋ 教學 HTML 簡報

宜大 r1545005 AI碩一 潘聖融｜TAICA 生成式 AI 作業：用 LLM Wiki 做一份教學 HTML 簡報

- 網站首頁：https://leonidas222069-dev.github.io/llm-wiki-ai-agents/
- Wiki：https://leonidas222069-dev.github.io/llm-wiki-ai-agents/wiki/index.html
- 教學簡報：https://leonidas222069-dev.github.io/llm-wiki-ai-agents/slides/index.html
- 流程與檢查紀錄：https://leonidas222069-dev.github.io/llm-wiki-ai-agents/process.html

## 怎麼跑

```bash
python3 checks/check.py --stage all --log   # fetch / wiki / outline / slides / site 五道檢查
python3 build.py                            # Markdown → HTML（需要 pip install markdown）
```

`raw/_full/` 的全文沒有放進 repo（版權考量），所以在別台電腦跑 fetch 和 wiki 檢查時，引文比對會跳過，只檢查網址和格式。

寫作規則見 [AGENTS.md](AGENTS.md)。
