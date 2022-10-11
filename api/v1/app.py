from fastapi import APIRouter
from .routers import temp, authenticate_user


router = APIRouter()

@router.get("/")
async def endpoint_index():
    return {"success": True}

router.include_router(authenticate_user.router)
router.include_router(temp.router)
