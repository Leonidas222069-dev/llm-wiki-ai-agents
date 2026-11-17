#!/usr/bin/env python3
"""把 wiki/*.md 與 process.md 轉成靜態 HTML（GitHub Pages 直接讀，不需要 build step）。"""
import html, json, os, re, sys
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "checks"))
from check import parse_page, load_sources

REPO = "https://github.com/Leonidas222069-dev/llm-wiki-ai-agents"
TYPE_LABEL = {"source": "來源摘要頁", "concept": "概念頁", "index": "Wiki 首頁"}

def nav(prefix):
    return (f'<nav class="top"><a class="brand" href="{prefix}index.html">AI Agents LLM Wiki</a>'
            f'<a href="{prefix}wiki/index.html">Wiki</a><a href="{prefix}slides/index.html">教學簡報</a>'
            f'<a href="{prefix}process.html">流程與檢查紀錄</a><a href="{REPO}">GitHub</a></nav>')

def page(title, body, prefix, extra_head=""):
    return f"""<!doctype html>
<html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}｜AI Agents LLM Wiki</title><link rel="stylesheet" href="{prefix}assets/style.css">{extra_head}</head>
<body>{nav(prefix)}<main>
{body}
</main><footer class="site">潘聖融（宜大 AI碩一）．內容依 <a href="{REPO}/blob/main/AGENTS.md">AGENTS.md</a> 規則撰寫，由 build.py 從 Markdown 產生。</footer></body></html>
"""

def fix_links(md_text):
    md_text = re.sub(r"\]\((?:\.\./)?AGENTS\.md\)", f"]({REPO}/blob/main/AGENTS.md)", md_text)
    md_text = re.sub(r"\]\(([^)\s]+?)\.md(#[^)]*)?\)", lambda m: f"]({m.group(1)}.html{m.group(2) or ''})", md_text)
    return md_text

def render(md_text):
    md_text = re.sub(r"```mermaid\n(.*?)```", lambda m: '<pre class="mermaid">\n' + html.escape(m.group(1)) + "</pre>", md_text, flags=re.S)
    return markdown.markdown(fix_links(md_text), extensions=["tables", "fenced_code", "sane_lists"])

def build_wiki():
    sources = load_sources()
    titles = {}
    for fn in os.listdir(os.path.join(ROOT, "wiki")):
        if fn.endswith(".md"):
            meta, _ = parse_page(os.path.join(ROOT, "wiki", fn)); titles[fn[:-3]] = meta["title"]
    n = 0
    for pid in sorted(titles):
        meta, body = parse_page(os.path.join(ROOT, "wiki", pid + ".md"))
        parts = [f'<span class="tag">{TYPE_LABEL.get(meta["type"], meta["type"])}</span>更新：{meta["updated"]}']
        if meta.get("sources") and meta["type"] == "concept":
            parts.append("來源：" + "、".join(f'<a href="{s}.html">{html.escape(sources[s]["title"])}</a>' for s in meta["sources"]))
        if meta.get("related"):
            parts.append("相關頁：" + "、".join(f'<a href="{r}.html">{html.escape(titles[r])}</a>' for r in meta["related"]))
        parts.append(f'<a href="{REPO}/blob/main/wiki/{pid}.md">看 Markdown 原檔</a>')
        out = f'<h1>{html.escape(meta["title"])}</h1><div class="meta">' + "<br>".join(parts) + "</div>\n" + render(body)
        open(os.path.join(ROOT, "wiki", pid + ".html"), "w", encoding="utf-8").write(page(meta["title"], out, "../"))
        n += 1
    return n

def build_process():
    text = open(os.path.join(ROOT, "process.md"), encoding="utf-8").read()
    head = '<script type="module">import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";mermaid.initialize({startOnLoad:true,theme:"neutral"});</script>'
    title = re.search(r"^# (.+)$", text, re.M).group(1)
    open(os.path.join(ROOT, "process.html"), "w", encoding="utf-8").write(page(title, render(text), "", head))

def build_home():
    body = """<h1>AI Agents LLM Wiki ＋ 教學簡報</h1>
<p>這是 TAICA 生成式 AI 課程的作業：先用「先討論、後生成」建立一份 AI Agents 主題的 LLM Wiki（ingest 6 份資料），再讓 AI 只用這份 Wiki 當知識來源，產生一份給新手看的教學 HTML 簡報。整個過程有自動檢查和執行紀錄。</p>
<div class="cards">
<a class="card" href="slides/index.html"><b>🎞️ 教學簡報</b>「AI Agents 是什麼？」15 張，每張都標出處</a>
<a class="card" href="wiki/index.html"><b>📚 LLM Wiki</b>6 篇來源摘要＋8 個概念頁</a>
<a class="card" href="process.html"><b>🔁 流程與檢查紀錄</b>loop / graph 設計、實際執行結果、反思</a>
</div>
<h2>專案結構</h2>
<ul>
<li><code>raw/</code>：來源 metadata（sources.json）和摘錄</li>
<li><code>wiki/</code>：Wiki 頁（Markdown 為主，HTML 由 build.py 產生）</li>
<li><code>slides/</code>：簡報大綱 outline.md 與 index.html</li>
<li><code>checks/</code>：check.py 自動檢查與每次執行的 log</li>
<li><code>AGENTS.md</code>：給 AI 的寫作規則</li>
</ul>"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page("首頁", body, ""))

if __name__ == "__main__":
    n = build_wiki(); build_process(); build_home()
    print(f"built {n} wiki pages + process.html + index.html")
