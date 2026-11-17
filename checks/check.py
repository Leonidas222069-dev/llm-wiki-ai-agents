#!/usr/bin/env python3
"""AI Agents LLM Wiki 的自動檢查。

用法：python3 checks/check.py --stage fetch|wiki|slides|site|all [--log]
每個 stage 對應 loop/graph 裡的一個檢查節點（見 process.md）。
FAIL 會讓程式回傳非 0，代表要回到上一個節點重做。
"""
import argparse, datetime, html, json, os, re, sys, urllib.request, urllib.error
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
UA = "Mozilla/5.0 (X11; Linux x86_64) llm-wiki-checker"
OUT = []
FAILS = []
WARNS = []

def say(msg=""):
    OUT.append(msg); print(msg)

def fail(msg):
    FAILS.append(msg); say("  FAIL  " + msg)

def warn(msg):
    WARNS.append(msg); say("  WARN  " + msg)

def ok(msg):
    say("  ok    " + msg)

def load_sources():
    path = os.environ.get("SOURCES_JSON", os.path.join(ROOT, "raw", "sources.json"))
    with open(path, encoding="utf-8") as f:
        return {s["id"]: s for s in json.load(f)["sources"]}

def norm(text):
    """比對用：統一引號、去掉斷行連字號、壓縮空白、轉小寫。"""
    text = text.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u200b", "").replace("\u00a0", " ").replace("\\&", "&")
    text = re.sub(r"-\s*\n\s*", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r" ([,.;:!?)])", r"\1", text)   # 網頁轉文字時常在標點前多一個空白
    return text.lower().strip()

def full_text(src):
    p = os.path.join(ROOT, src["full_text"])
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read(400000)
            return r.status, r.geturl(), body
    except urllib.error.HTTPError as e:
        return e.code, url, b""
    except Exception as e:  # 網路錯誤
        return None, url, str(e).encode()

# ---------- stage: fetch ----------
def stage_fetch():
    say("== stage fetch：來源是否真的抓到正文 ==")
    for sid, s in load_sources().items():
        status, final, body = fetch(s["url"])
        if status != 200:
            fail(f"{sid}: 正式網址回應 {status}")
            continue
        if final.rstrip("/") != s["url"].rstrip("/"):
            warn(f"{sid}: 正式網址又被轉到 {final}，請更新 sources.json")
        head = body[:3000].decode("utf-8", "replace").lower()
        if 'http-equiv="refresh"' in head or "redirecting..." in head:
            fail(f"{sid}: HTTP 200 但內容是轉址殘頁（meta refresh）")
        if s["requested_url"] != s["url"]:
            st2, fin2, body2 = fetch(s["requested_url"])
            stub = b'http-equiv="refresh"' in body2[:3000].lower()
            say(f"  info  {sid}: 原本要求的網址 → {st2} {fin2}{'（轉址殘頁）' if stub else ''}")
        txt = full_text(s)
        if txt is None:
            warn(f"{sid}: 本機沒有全文 {s['full_text']}（在別台電腦跑時正常）")
        else:
            words = len(re.findall(r"[A-Za-z]+", txt))
            if words < 1500:
                fail(f"{sid}: 全文只有 {words} 個英文字，可能沒抓到正文")
            elif s.get("anchor") and norm(s["anchor"]) not in norm(txt):
                fail(f"{sid}: 全文找不到錨點句（可能是 PDF 欄位交錯或抓錯版本）：{s['anchor'][:50]}…")
            else:
                ok(f"{sid}: HTTP 200，全文 {words} 字，錨點句吻合")
        if not os.path.exists(os.path.join(ROOT, "raw", sid + ".md")):
            warn(f"{sid}: 還沒有 raw/{sid}.md 摘錄")

# ---------- wiki 解析 ----------
def parse_page(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, text
    meta, key = {}, None
    for line in m.group(1).splitlines():
        li = re.match(r"^\s+-\s+(.*)$", line)
        if li and key:
            meta[key].append(li.group(1).split("#")[0].strip()); continue
        kv = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if kv:
            key = kv.group(1); val = kv.group(2).split("  #")[0].strip()
            meta[key] = [] if val == "" else val
    return meta, m.group(2)

def all_pages():
    pages = {}
    for fn in sorted(os.listdir(WIKI)):
        if fn.endswith(".md"):
            meta, body = parse_page(os.path.join(WIKI, fn))
            pages[fn[:-3]] = (meta, body)
    return pages

NUM_RE = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s*(%|B\b|億|萬)?")

def numbers_in(body):
    body = re.sub(r"\]\([^)]*\)", "]", body)          # 去掉連結網址
    body = re.sub(r"https?://\S+", "", body)
    body = re.sub(r"`[^`]*`", "", body)
    body = re.sub(r"\d{4}-\d{2}-\d{2}", "", body)      # 日期不算數據
    body = re.sub(r"HTTP \d{3}", "", body)               # HTTP 狀態碼不算數據
    found = set()
    for n, unit in NUM_RE.findall(body):
        v = float(n)
        if unit or "." in n or (v >= 10 and not (1990 <= v <= 2030)):
            found.add(n)
    return found

SECTIONS = {
    "source": ["## 基本資料", "## 一句話摘要", "## 重點整理", "## 原文摘錄", "## 跟其他頁的關係"],
    "concept": ["## 白話說", "## 重點", "## 各來源怎麼說", "## 常見誤會", "## 延伸閱讀"],
}

def stage_wiki():
    say("== stage wiki：格式、連結、引文、數字 ==")
    sources = load_sources()
    pages = all_pages()
    for pid, (meta, body) in pages.items():
        if meta is None:
            fail(f"{pid}: 沒有 front matter"); continue
        problems = []
        for k in ["id", "title", "type", "sources", "related", "updated"]:
            if k not in meta:
                problems.append(f"缺 {k}")
        if meta.get("id") != pid:
            problems.append(f"id={meta.get('id')} 跟檔名不同")
        ptype = meta.get("type")
        for s in meta.get("sources", []):
            if s not in sources:
                problems.append(f"sources 裡的 {s} 不存在")
        for r in meta.get("related", []):
            if r not in pages:
                problems.append(f"related 裡的 {r} 不存在")
        for sec in SECTIONS.get(ptype, []):
            if sec not in body:
                problems.append(f"缺段落 {sec}")
        links = re.findall(r"\]\(([^)#]+?\.md)(?:#[^)]*)?\)", body)
        for l in links:
            if not os.path.exists(os.path.join(WIKI, l)):
                problems.append(f"壞掉的內部連結 {l}")
        linked = {l[:-3] for l in links}
        if ptype == "concept":
            src_links = [l for l in linked if pages.get(l, ({},))[0] and pages[l][0].get("type") == "source"]
            con_links = [l for l in linked if pages.get(l, ({},))[0] and pages[l][0].get("type") == "concept" and l != pid]
            if len(src_links) < 1: problems.append("沒有連到任何來源頁")
            if len(con_links) < 2: problems.append(f"只連到 {len(con_links)} 個概念頁（至少 2）")
            for s in meta.get("sources", []):
                if s not in linked:
                    problems.append(f"front matter 寫了 {s} 但內文沒有連過去")
        if ptype == "source":
            sid = meta["sources"][0] if meta.get("sources") else None
            if sid in sources and sources[sid]["url"] not in body:
                problems.append("基本資料裡的網址跟 sources.json 的正式網址不一致")
        # 引文逐字比對
        corpus = "".join(norm(full_text(sources[s]) or "") for s in meta.get("sources", []) if s in sources)
        quotes = re.findall(r'^>\s*"(.+?)"\s*$', body, re.M)
        for q in quotes:
            if corpus and norm(q) not in corpus:
                problems.append(f'引文在全文找不到：「{q[:60]}…」')
        # 數字比對
        if corpus:
            for n in sorted(numbers_in(body)):
                if n.lower() not in corpus:
                    problems.append(f"數字 {n} 在引用來源的全文裡找不到")
        if problems:
            for p in problems: fail(f"{pid}: {p}")
        else:
            ok(f"{pid}: {ptype}，{len(quotes)} 句引文、{len(links)} 個內部連結全部通過")

# ---------- stage: outline ----------
def plain(md):
    md = re.sub(r"\*\*|`", "", md)
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
    return md

def load_outline():
    slides, cur = [], None
    for line in open(os.path.join(ROOT, "slides", "outline.md"), encoding="utf-8"):
        m = re.match(r"^## (\d+) (.*)$", line)
        if m:
            cur = {"no": int(m.group(1)), "title": m.group(2).strip(), "claims": []}; slides.append(cur); continue
        c = re.match(r"^- \[([a-z0-9-]+)\] (.+)$", line.strip())
        if c and cur: cur["claims"].append((c.group(1), c.group(2).strip()))
    return slides

def stage_outline():
    say("== stage outline：簡報大綱的每一句都逐字出自 wiki ==")
    pages = all_pages()
    for s in load_outline():
        problems = []
        for pid, snip in s["claims"]:
            if pid not in pages:
                problems.append(f"wiki 頁 {pid} 不存在"); continue
            if plain(snip) not in plain(pages[pid][1]):
                problems.append(f"「{snip[:40]}」不在 {pid}")
        if not s["claims"]: problems.append("沒有任何出處")
        if problems:
            for p in problems: fail(f"大綱第 {s['no']} 張: {p}")
        else:
            ok(f"大綱第 {s['no']} 張「{s['title']}」: {len(s['claims'])} 句都找得到")

# ---------- stage: slides ----------
class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.slides = []; self.cur = None; self.in_cite = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and "slide" in a.get("class", ""):
            self.cur = {"terms": [t for t in a.get("data-terms", "").split("|") if t], "text": "", "cites": [], "title": ""}
            self.slides.append(self.cur)
        elif self.cur is not None and tag == "footer" and "cite" in a.get("class", ""):
            self.in_cite = True
        elif self.cur is not None and self.in_cite and tag == "a":
            self.cur["cites"].append(a.get("href", ""))
    def handle_endtag(self, tag):
        if tag == "footer": self.in_cite = False
        if tag == "section": self.cur = None   # 不然最後一張會把 <script> 也算進去
    def handle_data(self, data):
        if self.cur is not None and not self.in_cite:
            self.cur["text"] += data

def stage_slides():
    say("== stage slides：每張投影片都對得回 wiki ==")
    with open(os.path.join(ROOT, "slides", "index.html"), encoding="utf-8") as f:
        p = SlideParser(); p.feed(f.read())
    pages = all_pages()
    n = len(p.slides)
    (ok if 12 <= n <= 15 else fail)(f"共 {n} 張投影片（規定 12～15）")
    outline = {o["no"]: o for o in load_outline()}
    if len(outline) != n:
        fail(f"大綱有 {len(outline)} 張，HTML 有 {n} 張，數量不一致")
    for i, s in enumerate(p.slides, 1):
        problems = []
        need = {pid for pid, _ in outline.get(i, {"claims": []})["claims"]}
        cited = []
        for href in s["cites"]:
            m = re.match(r"^\.\./wiki/([a-z0-9-]+)\.html$", href)
            if not m or m.group(1) not in pages:
                problems.append(f"出處連結無效 {href}")
            else:
                cited.append(m.group(1))
        if not cited:
            problems.append("沒有標出處")
        for pid in sorted(need - set(cited)):
            problems.append(f"大綱用了 {pid}，但投影片 footer 沒標")
        corpus = "\n".join(pages[c][1] + " " + pages[c][0].get("title", "") for c in cited)
        if not s["terms"]:
            problems.append("沒有 data-terms")
        for t in s["terms"]:
            if t.lower() not in corpus.lower():
                problems.append(f"關鍵詞「{t}」不在引用的 wiki 頁裡")
        for num in sorted(numbers_in(s["text"])):
            if num not in corpus:
                problems.append(f"數字 {num} 不在引用的 wiki 頁裡")
        if problems:
            for pr in problems: fail(f"第 {i} 張: {pr}")
        else:
            ok(f"第 {i} 張: {len(s['terms'])} 個關鍵詞 → {', '.join(cited)}")

# ---------- stage: site ----------
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ("href", "src"):
            if k in a: self.links.append(a[k])

def stage_site():
    say("== stage site：所有 HTML 的內部連結 ==")
    count = bad = 0
    for dp, dn, fns in os.walk(ROOT):
        if "/.git" in dp or "/raw/_" in dp: continue
        for fn in fns:
            if not fn.endswith(".html"): continue
            path = os.path.join(dp, fn)
            lp = LinkParser(); lp.feed(open(path, encoding="utf-8").read())
            for l in lp.links:
                if re.match(r"^(https?:|mailto:|#|data:|javascript:)", l): continue
                count += 1
                target = os.path.normpath(os.path.join(dp, l.split("#")[0].split("?")[0]))
                if os.path.isdir(target): target = os.path.join(target, "index.html")
                if not os.path.exists(target):
                    bad += 1; fail(f"{os.path.relpath(path, ROOT)} → {l} 不存在")
    if not bad: ok(f"檢查 {count} 個內部連結，全部存在")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all", choices=["fetch", "wiki", "outline", "slides", "site", "all"])
    ap.add_argument("--log", action="store_true")
    a = ap.parse_args()
    now = datetime.datetime.now()
    say(f"# check.py --stage {a.stage}  @ {now:%Y-%m-%d %H:%M:%S} (UTC+8)")
    stages = ["fetch", "wiki", "outline", "slides", "site"] if a.stage == "all" else [a.stage]
    for st in stages:
        globals()["stage_" + st](); say()
    say(f"結果：{len(FAILS)} FAIL、{len(WARNS)} WARN")
    if a.log:
        os.makedirs(os.path.join(ROOT, "checks", "logs"), exist_ok=True)
        fn = os.path.join(ROOT, "checks", "logs", f"{now:%Y%m%d-%H%M%S}-{a.stage}.txt")
        with open(fn, "w", encoding="utf-8") as f: f.write("\n".join(OUT) + "\n")
        print("log →", os.path.relpath(fn, ROOT))
    sys.exit(1 if FAILS else 0)

if __name__ == "__main__":
    main()
