"""
provide a link to a github and a clean version of the issue history will be returned
"""

from urllib.parse import urlparse, parse_qs
import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('GITHUB_TOKEN')

def main():
    site = get_site('https://github.com/goemeritus/edsl/issues/56')
    issue = get_issue_history(site)
    issue_str = format_issue(issue)
    return issue_str

def get_site(url):
    # Parse the provided URL
    path = urlparse(url).path
    parts = path.split('/')
    
    # Extract the owner and repo from the URL
    owner = parts[1]
    repo = parts[2]
    issue_number = parts[4]

    # Construct the API URL
    return f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}'

def get_issue_history(site):
    # Send a GET request to the GitHub API for the issue
    response = requests.get(site, headers={'Authorization': f'token {token}'})
    issue = response.json()

    # Check the response status code
    if response.status_code != 200:
        # If the request was not successful, print an error message and return None
        print(f'Error: {response.status_code}')
        return None

    # Send a GET request to the GitHub API for the comments
    response = requests.get(issue['comments_url'], headers={'Authorization': f'token {token}'})
    comments = response.json()

    # Check the response status code
    if response.status_code != 200:
        # If the request was not successful, print an error message and return None
        print(f'Error: {response.status_code}')
        return None

    # Add the comments to the issue data
    issue['comments_data'] = comments

    return issue
    
def format_issue(issue):
    # Extract the relevant fields
    title = issue['title']
    user = issue['user']['login']
    state = issue['state']
    created_at = issue['created_at']
    updated_at = issue['updated_at']
    body = issue['body']

    # Format the comments
    comments = '\n'.join([f"{comment['user']['login']}: {comment['body']}" for comment in issue['comments_data']])

    # Format the fields into a string
    issue_str = f'Title: {title}\nUser: {user}\nState: {state}\nCreated at: {created_at}\nUpdated at: {updated_at}\nBody: {body}\nComments:\n{comments}'

    return issue_str

if __name__ == "__main__":
    print(main())