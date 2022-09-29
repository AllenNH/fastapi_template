from fastapi import APIRouter
from ..mdb import db

from .. import  schemas
from ..repository import temp

router = APIRouter(
    prefix = '/temp',
    tags = ['Temp'])


@router.get('/', status_code=200)
async def endpoint():    
    return await ocr.get_data(db, id)