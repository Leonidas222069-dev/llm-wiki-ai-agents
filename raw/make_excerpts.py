#!/usr/bin/env python3
"""從 raw/_full/ 全文產生 raw/<id>.md：metadata＋wiki 引文在原文中的上下文（各約 300 字元）。"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "checks"))
from check import norm

data = json.load(open(os.path.join(ROOT, "raw", "sources.json"), encoding="utf-8"))
for s in data["sources"]:
    page = open(os.path.join(ROOT, "wiki", s["id"] + ".md"), encoding="utf-8").read()
    quotes = re.findall(r'^>\s*"(.+?)"\s*$', page, re.M)
    full = norm(open(os.path.join(ROOT, s["full_text"]), encoding="utf-8", errors="replace").read())
    lines = [f"# {s['title']}", "", f"- id：`{s['id']}`", f"- 作者：{s['author']}", f"- 年份：{s['year'] or '待確認'}",
             f"- 日期：{s['date']}", f"- 類型：{s['type']}", f"- 正式網址：{s['url']}", f"- 抓取紀錄：{s['fetch']}",
             f"- 擷取時間：{data['fetched_at']}", "", "## 摘錄（wiki 引文在原文中的上下文，已轉小寫並壓縮空白）", ""]
    for q in quotes:
        i = full.find(norm(q))
        ctx = full[max(0, i - 150): i + len(norm(q)) + 150] if i >= 0 else "（找不到）"
        lines += [f"**引文**：{q}", "", f"> …{ctx}…", ""]
    open(os.path.join(ROOT, "raw", s["id"] + ".md"), "w", encoding="utf-8").write("\n".join(lines))
    print("wrote raw/%s.md (%d excerpts)" % (s["id"], len(quotes)))
