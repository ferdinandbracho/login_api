
from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.db.db import not_real_db
from app.utils import UserInDB, decode_token, token_generator

# Init router
router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# 'Hello Palenca' Endpoint
@router.get('/', status_code=status.HTTP_200_OK)
def hello() -> str:
    """
    todo: Add docstring
    """

    return 'Hello Palenca'


# Login endpoint
@router.post('/uber/login', status_code=status.HTTP_200_OK)
async def login(email: str, password: str):
    """
    todo: Add docstring
    """

    user_dict = not_real_db.get(email)

    user = UserInDB(**user_dict)

    if not user_dict or not password == user.hashed_password:
        raise HTTPException(
            status_code=400,
            detail={
                'message': 'CREDENTIALS_INVALID',
                'details': 'Incorrect username or password'
            }
        )

    token = token_generator(email)

    res = {
            'message': 'SUCCESS',
            'access_token': token
        }

    return res


# Profile endporint
@router.get('/uber/profile', status_code=status.HTTP_200_OK)
async def get_profile(access_token: str):
    """
    todo: Add docstring
    """

    try:
        payload = decode_token(access_token)
        res = {
            'message': 'SUCCESS',
            'access_token': payload
        }

        return res
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail={
                'message': 'CREDENTIALS_INVALID',
                'details': 'Incorrect token’'
            }
        )
