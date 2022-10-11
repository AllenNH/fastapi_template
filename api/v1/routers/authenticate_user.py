from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import oauth2
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)


@router.post('')
def login(request: OAuth2PasswordRequestForm = Depends()):
    '''if request.username != "nighthack":
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
                    detail = f"Invalid Credentials")    '''
    if request.password != "kcahthgin":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = oauth2.create_access_token(data={"sub": request.username})
    return {"access_token": access_token, "token_type": "bearer"}