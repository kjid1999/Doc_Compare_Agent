# Doc_Compare_Agent

這是一個pdf比較Agent。 Google Gemini 模型可以查閱`pdfs`資料夾下的 pdf 檔案來回答使用者的提問。

- 只能讀取文字，不支援圖片
- pdf 檔案中的數學公式不能很好的讀取，因此 Gemini 可能無法正確的回答相關的問題

---

## 檔案與目錄結構
```
.
│  .env
│  .gitignore
│  main.py
│  README.md
│  tools.py
│
└─pdfs
       ElementaryCalculus.pdf
       mitres_18_001_f17_full_book.pdf
```

- 在`.env`中以 `GEMINI_API_KEY=<api_key>`存放你的 Gemini API 金鑰  

> ⚠️ 這檔案不會包含在 GitHub 中，請自行建立並避免上傳。

可以在下面兩個網址下載測試用的 pdf:
1. https://www.mecmath.net/calculus/ElementaryCalculus.pdf
2. https://ocw.mit.edu/courses/res-18-001-calculus-fall-2023/mitres_18_001_f17_full_book.pdf

---

## 注意事項

- 請勿輸入任何敏感或個人隱私資訊。

---

## 安裝相依套件

```bash
pip install -r requirements.txt
```

## 執行
執行`main.py`
