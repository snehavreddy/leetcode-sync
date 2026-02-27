import os
from dotenv import load_dotenv

load_dotenv()

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
LEETCODE_CSRFTOKEN = os.getenv("LEETCODE_CSRFTOKEN")
LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com/",
    "Content-Type": "application/json",
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={LEETCODE_CSRFTOKEN}",
    "X-CSRFToken": LEETCODE_CSRFTOKEN
}