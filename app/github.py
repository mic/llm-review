from fastapi import HTTPException
import requests
from .config import GITHUB_TOKEN

BASE_URL = 'https://api.github.com'

def get_open_pull_requests(owner: str, repo: str):
    url = f'{BASE_URL}/repos/{owner}/{repo}/pulls'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        prs = response.json()
        return [{"title": pr['title'], "url": pr['html_url']} for pr in prs]
    else:
        raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch PRs: {response.text}")
