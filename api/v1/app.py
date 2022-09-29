from fastapi import APIRouter
from .routers import temp


router = APIRouter()

@router.get("/")
async def endpoint_index():
    return {"success": True}

router.include_router(temp.router)