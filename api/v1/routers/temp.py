from fastapi import APIRouter,  Depends

from .. import  schemas
from ..repository import temp
from .. import  schemas, oauth2

router = APIRouter(
    prefix = '/temp',
    tags = ['Temp'])


@router.get('/', status_code=200 )
async def endpoint(current_user: str = Depends(oauth2.get_current_user)):    
    return await temp.endpoint()