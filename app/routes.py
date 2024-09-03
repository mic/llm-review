from fastapi import APIRouter
from .config import REPO_OWNER, REPO_NAME
from .github import get_open_pull_requests

router = APIRouter()

@router.get("/api/prs")
def get_prs():
    pr_list = get_open_pull_requests(REPO_OWNER, REPO_NAME)
    return pr_list