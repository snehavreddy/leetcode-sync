# 📘 LeetCode Sync Automation

This project automatically fetches your recent LeetCode submissions and stores them locally, organized by language.

It uses your LeetCode session cookie to access submission details via GraphQL.

---

# Complete Setup Guide (From Scratch)

Follow these steps exactly.

---

## 1️. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/leetcode-sync.git
cd leetcode-sync
```

---

## 2️. Create a Virtual Environment

Create the virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows (PowerShell)

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

If successful, your terminal will show:

```
(venv)
```

---

## 3️. Install Required Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `requests`
- `python-dotenv`

---

## 4️. Create a `.env` File

In the project root, create a file named:

```
.env
```

Add the following content:

```
LEETCODE_SESSION=your_session_cookie_here
LEETCODE_CSRFTOKEN=your_csrf_token_here
LEETCODE_USERNAME=your_leetcode_username
```

---

### How to Get LeetCode Session & CSRF Token ??

1. Login to LeetCode in your browser
2. Open Developer Tools (Press F12)
3. Go to **Application → Cookies**
4. Copy:
   - `LEETCODE_SESSION`
   - `csrftoken`

Paste them into your `.env` file.

⚠️ Never commit this file.

---

## 5️⃣ Run the Script

```bash
python src/main.py
```

---

# 📂 Output

Solutions will be generated inside:

```
leetcode-solutions/
```

Organized like:

```
leetcode-solutions/
├── python/
├── csharp/
└── sql/
```

Each file is named:

```
<difficulty>_<questionId>-<titleSlug>.<extension>
```

Example:

```
easy_1-two-sum.py
medium_56-merge-intervals.py
hard_4-median-of-two-sorted-arrays.py
```

---

# Project Structure

```
leetcode-sync/
│
├── src/
│   ├── config.py
│   ├── leetcode_client.py
│   ├── file_manager.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Security Notes

- `.env` is ignored via `.gitignore`
- Do NOT share your session token
- Tokens may expire — regenerate if needed

---

# What This Tool Does ??

✔ Fetches recent submissions  
✔ Extracts solution code  
✔ Organizes by language  
✔ Prevents duplicates  
✔ Structured and modular architecture  

---

# Possible Improvements

- Auto Git commit & push to solutions repo
- GitHub Actions daily automation
- Submission metadata logging
- Stats generation (easy/medium/hard count)
- Overwrite detection for modified submissions

---

# 📜 License

This project is for educational and personal automation purposes.