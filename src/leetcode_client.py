import requests
from config import LEETCODE_GRAPHQL_URL, HEADERS


class LeetCodeClient:

    def get_recent_submissions(self, username):
        query = """
        query recentSubmissionList($username: String!) {
          recentSubmissionList(username: $username) {
            id
            titleSlug
            lang
          }
        }
        """

        response = requests.post(
            LEETCODE_GRAPHQL_URL,
            json={
                "query": query,
                "variables": {"username": username}
            },
            headers=HEADERS
        )

        response.raise_for_status()

        data = response.json()

        if "errors" in data:
            return []

        return data.get("data", {}).get("recentSubmissionList", [])

    def get_submission_detail(self, submission_id):
        query = """
        query submissionDetails($submissionId: Int!) {
          submissionDetails(submissionId: $submissionId) {
            code
            question {
              questionId
              titleSlug
              difficulty
            }
          }
        }
        """

        response = requests.post(
            LEETCODE_GRAPHQL_URL,
            json={
                "query": query,
                "variables": {"submissionId": int(submission_id)}
            },
            headers=HEADERS
        )

        response.raise_for_status()

        data = response.json()

        if "errors" in data:
            return None

        return data.get("data", {}).get("submissionDetails")