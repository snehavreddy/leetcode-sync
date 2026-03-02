# 📘 LeetCode Sync Automation

Automatically sync your accepted LeetCode submissions to a separate GitHub portfolio repository.

This project:

- Fetches recent accepted submissions using LeetCode GraphQL
- Extracts solution code
- Organizes files by language and difficulty
- Prevents duplicate overwrites
- Automatically commits & pushes to a separate solutions repository

Built with clean modular architecture and automation mindset.

---

# Architecture Overview

This setup uses **two repositories**:

### 1 leetcode-sync
Automation engine (this repository)

### 2 LeetCode-Practice-Solutions
Public portfolio repository containing only solutions

This separation keeps:

- Automation logic clean  
- Portfolio repository clean 

---

# Project Structure

```
leetcode-sync/
│
├── src/
│   ├── config.py
│   ├── leetcode_client.py
│   ├── file_manager.py
│   ├── git_manager.py
│   └── main.py
│
├── LeetCode-Practice-Solutions/   ← separate git repo
├── requirements.txt
├── .gitignore
└── README.md
```

---

#  Complete Setup Guide

Follow these steps carefully.

---

## 1 Clone Automation Repository

```
git clone https://github.com/YOUR_USERNAME/leetcode-sync.git
cd leetcode-sync
```

---

## 2 Clone Solutions Repository Inside It

```
git clone https://github.com/YOUR_USERNAME/LeetCode-Practice-Solutions.git
```

Your structure should now look like:

```
leetcode-sync/
└── leetcode-solutions/
```

> Important: `LeetCode-Practice-Solutions` must already exist on GitHub.

---

## 3 Create Virtual Environment

```
python -m venv venv
```

Activate:

### Windows
```
venv\Scripts\activate
```

### Mac / Linux
```
source venv/bin/activate
```

---

## 4 Install Dependencies

```
pip install -r requirements.txt
```

Dependencies:
- requests
- python-dotenv

---

## 5 Create `.env` File

Create a `.env` file in the project root:

```
LEETCODE_SESSION=your_session_cookie
LEETCODE_CSRFTOKEN=your_csrf_token
LEETCODE_USERNAME=your_leetcode_username
```

---

### How To Get Session & CSRF Token

1. Login to LeetCode
2. Open Developer Tools (F12)
3. Go to Application → Cookies
4. Copy:
   - LEETCODE_SESSION
   - csrftoken

⚠ Never commit this file.  
⚠ Tokens may expire and need regeneration.

---

# Run the Sync

```
python src/main.py
```

What happens automatically:

1. Fetches latest accepted submissions
2. Saves solutions into `LeetCode-Practice-Solutions`
3. Detects file changes
4. Runs `git add`
5. Runs `git commit`
6. Runs `git push`

No manual Git steps required.

---

# Output Format

Solutions are organized as:

```
leetcode-solutions/
├── python/
├── csharp/
└── sql/
```

File naming format:

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

# Features

✔ GraphQL submission fetch  
✔ Language-based organization  
✔ Difficulty tagging  
✔ Duplicate prevention  
✔ Separate portfolio repository  
✔ Automatic commit & push  
✔ Modular and clean architecture  

---

# Security Notes

- `.env` is ignored via `.gitignore`
- Never expose session tokens publicly
- Regenerate tokens if expired

---

# 🔮 Future Enhancements

- Smart commit messages with problem count
- README stats auto-generation (Easy/Medium/Hard counter)
- GitHub Actions scheduled automation
- Submission metadata logging (runtime, memory)
- Retry mechanism for network failures
- Branch auto-detection

---

# License

This project is for educational and personal automation purposes.