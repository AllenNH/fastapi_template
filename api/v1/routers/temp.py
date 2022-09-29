from fastapi import APIRouter

from .. import  schemas
from ..repository import temp

router = APIRouter(
    prefix = '/temp',
    tags = ['Temp'])


@router.get('/', status_code=200)
async def endpoint():    
    return await temp.endpoint()