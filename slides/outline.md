# 簡報大綱（整理重點節點的產出）

規則：每一行 `- [wiki頁id] 片段` 的片段必須逐字出現在該 wiki 頁（忽略粗體符號）。
check.py --stage outline 會檢查；投影片的出處 footer 也必須包含這裡列的每個 wiki 頁。

## 1 AI Agents 是什麼？
- [index] 這是一份用「先討論、後生成」方式建立的 AI Agents 知識庫

## 2 今天的路線
- [index] 聊天機器人和 agent 差在哪？
- [index] 五種常見模式

## 3 客服 vs 跑腿的助理
- [agent-definition] 你問一句、它答一句，事情還是你自己去做
- [agent-definition] 單純的聊天機器人、單輪 LLM 呼叫、情緒分類器，因為它們沒有用 LLM 控制流程執行
- [agent-definition] agent 就是讓 LLM 自己掌控流程、會用工具、在迴圈裡一步步把任務做完的系統

## 4 誰決定下一步？
- [agent-definition] 流程寫死在程式裡的是 workflow；由 LLM 動態決定步驟和工具的才是 agent。兩者合稱 agentic 系統
- [agent-definition] workflow 對定義清楚的任務提供可預測性和一致性；agent 適合步驟數量難以預測
- [agent-definition] 代價是成本較高、錯誤可能累積
- [anthropic-building-effective-agents] 能簡單就簡單，真的需要才加複雜度

## 5 一個 agent 由什麼組成？
- [openai-practical-guide] Model（負責推理和決策的 LLM）、Tools（可以呼叫的外部函式或 API）、Instructions（明確的指示和 guardrails）
- [weng-llm-powered-agents] 規劃（Planning）、記憶（Memory）、工具使用（Tool use）

## 6 工具：從房間伸出去的手
- [tool-use] 它知道很多，卻不知道今天的新聞，心算也可能出錯
- [tool-use] Data（取得資訊）、Action（採取行動）、Orchestration（把別的 agent 當工具）
- [openai-practical-guide] Data（取資料，例如查資料庫、讀 PDF、搜尋網頁）、Action（做事，例如寄信、更新紀錄）
- [schick-toolformer] 自己學會什麼時候該呼叫哪個 API
- [tool-use] 要像寫給新同事的說明文件一樣

## 7 記憶與規劃
- [memory] 短期記憶是這次對話放得進 context window 的內容，長期記憶是存在外部資料庫、需要時再檢索回來的資料
- [planning] 把大任務拆成小步驟（任務拆解）
- [planning] 回頭檢討、修正做法（自我反思）
- [memory] 不會自動記得，要靠系統把內容放回 context 或存進長期記憶再取回

## 8 ReAct：想 → 做 → 看
- [react-loop] Thought（想）：用自然語言推理，決定下一步
- [react-loop] Action（做）：呼叫工具
- [react-loop] Observation（看）：讀取工具回傳的結果
- [react-loop] 像偵探辦案

## 9 為什麼有效？什麼時候停？
- [react-loop] 在 HotpotQA、Fever 上比純 chain-of-thought 更少幻覺；在 ALFWorld、WebShop 上，成功率比模仿學習和強化學習方法高出 34% 和 10%（絕對值）
- [react-loop] 直到呼叫最終輸出工具、模型不再呼叫工具、發生錯誤，或達到最大輪數
- [react-loop] 一定要設停止條件，不然可能一直燒錢

## 10 五種常見的工作流模式
- [workflow-patterns] 上一步的輸出是下一步的輸入，中間可以加檢查關卡（gate）
- [workflow-patterns] 先分類，再送到專門的處理流程
- [workflow-patterns] 同時跑多個 LLM 再彙整
- [workflow-patterns] 中央 LLM 動態拆任務、分給 worker、再整合
- [workflow-patterns] 一個產生、一個評估，不合格就帶回饋重做

## 11 多代理：先單、後多
- [multi-agent] 一個中央 agent 把其他專門 agent 當成工具呼叫，由它統一跟使用者互動
- [multi-agent] agent 之間平起平坐，用 handoff 把控制權交給另一個 agent
- [multi-agent] 有些系統能管好超過 15 個清楚的工具，有些在不到 10 個重疊工具時就出問題

## 12 把鑰匙交給新司機之前
- [risks] 一步錯可能步步錯（compounding errors）
- [risks] jailbreak、prompt injection 可能讓 agent 洩漏系統提示或做出不該做的事
- [risks] 相關性分類、安全分類、PII 過濾、內容審核、工具風險分級
- [risks] 失敗超過門檻，或要做高風險、不可逆的動作（取消訂單、大額退款、付款）時，交給人

## 13 五句話帶走今天的內容
- [agent-definition] 讓 LLM 自己掌控流程、會用工具
- [react-loop] 一定要設停止條件
- [multi-agent] 先把一個 agent 做到極致，真的撐不住再拆
- [risks] 要靠 guardrails（護欄）、停止條件和人工把關來控制風險

## 14 小測驗
- [agent-definition] 情緒分類器
- [react-loop] Observation（看）
- [workflow-patterns] 客服問題分成一般、退款、技術支援
- [multi-agent] Manager（管理者）
- [risks] 要做高風險、不可逆的動作

## 15 參考資料
- [index] 來源摘要頁（6 篇）
