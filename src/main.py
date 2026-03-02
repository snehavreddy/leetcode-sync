import time
from config import LEETCODE_USERNAME
from leetcode_client import LeetCodeClient
from file_manager import FileManager
from git_manager import git_auto_push
from file_manager import BASE_DIR


def main():
    client = LeetCodeClient()
    file_manager = FileManager()

    submissions = client.get_recent_submissions(LEETCODE_USERNAME)

    seen = set()

    for sub in submissions:
        submission_id = sub["id"]
        title_slug = sub["titleSlug"]
        lang = sub["lang"]

        if title_slug in seen:
            continue

        folder, extension = file_manager.get_language_info(lang)
        if folder is None:
            continue

        detail = client.get_submission_detail(submission_id)
        if not detail:
            continue

        question = detail["question"]
        question_id = question["questionId"]
        difficulty = question["difficulty"].lower()
        code = detail["code"]

        filename = f"{difficulty}_{question_id}-{title_slug}{extension}"
        file_manager.save_code(folder, filename, code)

        seen.add(title_slug)

        time.sleep(1)

    print("Sync complete.")


if __name__ == "__main__":
    main()
    git_auto_push(BASE_DIR)