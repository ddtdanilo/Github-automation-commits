# Automation Script

This script defines several functions to improve readability and reusability. It uses the `get_repo_path()` function to get the current repository path, and the `commit_to_repo()` function to perform the git commands necessary to commit and push changes to the repository. The `add_text_to_file()` function is used to add text to the `example.txt` file, and the `run_commits()` function is used to continuously commit changes to the repository, while a maximum number of commits per day is defined. In this implementation the maximum number of commits per day is 12, and it sleeps for one day after each commit, so it will commit the maximum number of commits per day and not commit anything during the rest of the day.

## How to run

Make sure you have python and git installed in your system and use python version 3.x.
Run the script using the following commands:

```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python automation.py
```

This will start the script, and it will begin committing changes to the repository. The script uses the current working directory as the repository path. Make sure the directory is a git repository and you have the permission to push the commits.
## Note
It will add a text to a file name example.txt and commit it with the commit message "Commit at current_time" and it will sleep random duration between 1 sec to 1 day before making another commit.
