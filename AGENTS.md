# AGENTS.md：AI Agents LLM Wiki 的寫作規則

這份檔案是給 AI（和我自己）看的規則。照它做，新增資料、寫 wiki、產生簡報都會保持同一套格式，也比較不會亂編內容。

## 0. 專案結構

```
raw/sources.json      每份來源的 metadata（標題、作者、年份、正式網址、抓取紀錄）
raw/<id>.md           該來源的短摘錄（英文原文，供查證）
raw/_full/            全文（只在本機，不進 repo）
wiki/<id>.md          Wiki 頁（Markdown，唯一的內容來源）
wiki/<id>.html        由 build.py 產生，不要手改
slides/index.html     教學簡報，內容只能來自 wiki/
process.md            loop / graph 設計與執行紀錄（build 成 process.html）
checks/check.py       自動檢查；checks/logs/ 放每次執行的輸出
build.py              把 Markdown 轉成靜態 HTML
```

## 1. 先討論、後生成

1. 新增來源或新概念前，先在對話裡列出：要加哪份資料、為什麼、會影響哪些頁。
2. 使用者同意後才寫檔。
3. 寫完先跑 `python3 checks/check.py --stage fetch`／`--stage wiki`，通過才進下一步。

## 2. 頁面種類與 front matter

每個 wiki 頁開頭都要有 front matter，欄位不可省略：

```yaml
---
id: react-loop            # 跟檔名一樣，小寫英文加連字號
title: ReAct 迴圈          # 繁體中文標題
type: concept             # source（來源摘要頁）或 concept（概念頁）或 index
sources:                  # 這頁用到的來源 id（必須存在於 raw/sources.json）
  - yao-react
related:                  # 相關 wiki 頁 id，2～5 個
  - tool-use
  - planning
updated: 2026-11-17
---
```

### 來源摘要頁（type: source）固定段落

`## 基本資料` → `## 一句話摘要` → `## 重點整理` → `## 原文摘錄` → `## 跟其他頁的關係`

- 基本資料必須有：標題、作者、年份、類型、正式網址（轉址後的網址）。
- 原文摘錄用 `> "英文原文"` 一行一句，必須能在全文中逐字找到。

### 概念頁（type: concept）固定段落

`## 白話說` → `## 重點` → `## 各來源怎麼說` → `## 常見誤會` → `## 延伸閱讀`

- 「白話說」寫給完全沒碰過的人，3～5 句，先用生活比喻再講定義。
- 「各來源怎麼說」每一點都要連到來源摘要頁，例如 `（[Anthropic](anthropic-building-effective-agents.md)）`。

## 3. 不准編造

- 數字（百分比、模型大小、頁數）只能抄來源裡真的有的，`check.py` 會到全文裡比對。
- 來源沒寫清楚的作者、日期，寫「待確認」，不要猜。
- 兩份來源說法不同時（例如年份），兩種都寫出來並註明以哪個為準。

## 4. 連結規則

- wiki 內部連結一律用相對路徑 `xxx.md`，build 時會轉成 `.html`。
- 每個概念頁至少連到 1 個來源頁、2 個其他概念頁。
- 外部網址只放在來源頁的「基本資料」和 raw/sources.json。

## 5. 簡報規則（slides/index.html）

- 每張投影片是一個 `<section class="slide">`，內容只能來自 wiki。
- 每張投影片底部要有 `<footer class="cite">`，連到用到的 wiki 頁（`../wiki/xxx.html`）。
- 每張投影片要寫 `data-terms="詞1|詞2"`：列出這張的關鍵詞，check.py 會確認這些詞真的出現在引用的 wiki 頁。
- 一張只講一個重點；術語第一次出現要附中文解釋。
- 結構固定：開場 → 聊天機器人 vs Agent → 核心元件 → ReAct → 工作流模式 → 多代理 → 風險 → 總結 → 小測驗。

## 6. 新增一份來源的流程

1. 抓網頁或 PDF，存進 `raw/_full/`，在 `raw/sources.json` 補 metadata。
2. 跑 `python3 checks/check.py --stage fetch`：確認 HTTP 200、沒有轉址殘頁、全文字數夠多。
3. 寫 `raw/<id>.md` 摘錄、`wiki/<id>.md` 來源頁，再更新相關概念頁和 `wiki/index.md`。
4. 跑 `--stage wiki`：front matter、內部連結、引文逐字比對、數字比對。
5. 改簡報的話再跑 `--stage slides`，最後 `python3 build.py`。
6. 把檢查輸出存到 `checks/logs/`，有修正就寫進 process.md 的執行紀錄。
