from fastapi import APIRouter
from .handlers import account
from .handlers import auth
from .handlers import post
from .handlers import comment

router = APIRouter()

router.include_router(account.account_router, prefix="/accounts", tags=["accounts"])
router.include_router(auth.auth_router, tags=["auth"])
router.include_router(post.posts_router, prefix="/posts", tags=["posts"])
router.include_router(comment.comments_router, prefix="/comments", tags=["comments"])
