import subprocess
from datetime import datetime
from pathlib import Path


def git_auto_push(repo_path: str):
    repo = Path(repo_path).resolve()

    if not (repo / ".git").exists():
        print(f"{repo} is not a git repository.")
        return

    try:
        status = subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=repo
        ).decode().strip()

        if not status:
            print("No changes to commit.")
            return

        subprocess.run(["git", "add", "."], cwd=repo, check=True)

        commit_message = f"Auto-sync LeetCode - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        subprocess.run(
            ["git", "commit", "-m", commit_message],
            cwd=repo,
            check=True
        )

        subprocess.run(["git", "push", "origin", "main"], cwd=repo, check=True)

        print("LeetCode solutions pushed successfully 🚀")

    except subprocess.CalledProcessError as e:
        print("Git operation failed:", e)