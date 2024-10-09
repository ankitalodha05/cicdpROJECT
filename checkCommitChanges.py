import requests
import os

# Constants
GITHUB_USER = 'SyamalaKadmi'  
REPO_NAME = 'CICDProjectPipeline'           
TOKEN = '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'   
STORAGE_FILE = 'last_commit.txt'

# Function to fetch latest commits from Github using Github API
def get_latest_commit():
    url = f'https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/commits'
    print(url)
    headers = {'Authorization': f'token {TOKEN}'} if TOKEN else {}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        commits = response.json()
        latest_commit = commits[0]['sha']
        return latest_commit
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        return None

# Function to validate fetched commit against the last commit commit stored in the storage file
def check_for_changes():
    latest_commit = get_latest_commit()

    if latest_commit is None:
        return False
    # Read the last commit from the storage file
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as f:
            last_commit = f.read().strip()
    else:
        last_commit = None

    if latest_commit != last_commit:
        # Update the storage file with the latest commit
        with open(STORAGE_FILE, 'w') as f:
            f.write(latest_commit)
        return True
    else:
        return False

if __name__ == "__main__":
    if check_for_changes():
        print("Changes detected.")
    else:
        print("No changes detected.")
