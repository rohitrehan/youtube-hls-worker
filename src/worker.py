import time
from pathlib import Path
from live_video_ids import video_ids
from utils import get_hls_manifest_url
import os
import subprocess


ROOT_DIR = Path(__file__).absolute().parent.parent


def git_pull(repo_path: str):
    try:
        # Navigate to the repository path and run 'git pull'
        result = subprocess.run(
            ["git", "-C", repo_path, "pull", "--rebase"],
            text=True,  # Ensures result.stdout and result.stderr are strings
            capture_output=True,
            check=True,  # Raises a CalledProcessError for non-zero exit codes
        )
        print(f"Git Pull Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git pull:\n{e.stderr}")
    except FileNotFoundError:
        print("Git is not installed or not found in PATH.")


def git_commit_and_push(repo_path: str, commit_message: str):
    """Commit changes and push them to the remote repository"""
    try:
        # Stage all changes
        subprocess.run(
            ["git", "-C", repo_path, "add", "."],
            text=True,
            capture_output=True,
            check=True,
        )

        # Commit the changes
        subprocess.run(
            ["git", "-C", repo_path, "commit", "-m", commit_message],
            text=True,
            capture_output=True,
            check=True,
        )

        # Push the changes
        result = subprocess.run(
            ["git", "-C", repo_path, "push"],
            text=True,
            capture_output=True,
            check=True,
        )
        print(f"Git Push Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git commit or push:\n{e.stderr}")
    except FileNotFoundError:
        print("Git is not installed or not found in PATH.")


def get_video_ids():
    return os.listdir(ROOT_DIR / "v")


def main():
    while True:
        git_pull(ROOT_DIR)

        # Replace this with your task logic
        with open(ROOT_DIR / "logs" / "job_output.log", "a") as log_file:
            log_file.write(f"Task executed at {time.ctime()}\n")

        for video_id in get_video_ids():
            url = get_hls_manifest_url(video_id)
            if url is not None:
                with open(ROOT_DIR / "hls" / video_id, "w") as file:
                    file.write(url)
            os.remove(ROOT_DIR / "v" / video_id)

        git_commit_and_push(ROOT_DIR, "Updated HLS urls")

        time.sleep(10)


if __name__ == "__main__":
    main()
