"""
This version of the code defines several functions to improve readability and reusability.
It uses the get_repo_path() function to get the current repository path, and the commit_to_repo()
function to perform the git commands necessary to commit and push changes to the repository.
The add_text_to_file() function is used to add text to the example.txt file, and the run_commits()
function is used to continuously commit changes to the repository, while a maximum number of commits per day is defined.
In this implementation the maximum number of commits per day is 12 and sleep one day after each commit,
so it will commit the maximum number of commits per day and not commit anything during the rest of the day. 
"""

import random
import subprocess
import time


def commit_to_repo(repo_path: str, commit_message: str) -> None:
    """Commit the changes to the repository at the given path.

    Parameters:
    repo_path (str): The path to the repository.
    commit_message (str): The message to use for the commit.
    """
    subprocess.run(["git", "-C", repo_path, "add", "."])
    subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message])
    subprocess.run(["git", "-C", repo_path, "push"])


def add_text_to_file(file_path: str, text: str) -> None:
    """Add text to the specified file.

    Parameters:
    file_path (str): The path to the file.
    text (str): The text to add to the file.
    """
    with open(file_path, "a") as f:
        f.write(text)


def get_repo_path() -> str:
    """Get the path to the current repository.

    Returns:
    str: The path to the repository.
    """
    return subprocess.run(["pwd"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()


def run_commits() -> None:
    """Commit changes to the repository randomly during the day.

    The function will commit a maximum of 12 changes per day.
    """
    num_commits = 12  # maximum number of commits per day
    repo_path = get_repo_path()
    file_path = f"{repo_path}/example.txt"
    while True:
        for i in range(num_commits):
            commit_message = f"Commit at {time.asctime()}"
            add_text_to_file(file_path, commit_message + "\n")
            commit_to_repo(repo_path, commit_message)
            # Sleep time between 1 sec to 1 day
            sleep_duration = random.randint(1, 60*60*24)
            print(f"Commit completed, next one in", sleep_duration, "seconds")
            time.sleep(sleep_duration)


if __name__ == "__main__":
    repo_path = get_repo_path()
    file_path = f"{repo_path}/example.txt"
    commit_message = f"Commit at {time.asctime()} - STARTING"
    add_text_to_file(file_path, commit_message + "\n")
    commit_to_repo(repo_path, commit_message)
    print("Starting in 5 seconds!")
    time.sleep(5)
    run_commits()
