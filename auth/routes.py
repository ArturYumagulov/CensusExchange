from fastapi import APIRouter, Depends

from .model import User
from .schema import User as Schema_user

from .service import create_access_token, get_user_from_token, get_user_from_db


router = APIRouter(prefix="/auth", tags=['auth'])


@router.get('/test')
async def index():
    return {"message": "Hello World"}

#
# @router.post("/login")
# async def login(user_in: Schema_user):
#     for user in User:
#         if user.username == user_in.username and user.password == user_in.password:
#             return {"access_token": create_access_token({"sub": user_in.username}), "token_type": "bearer"}
#
#     return {"error": "Invalid credentials"}


@router.get('/about_me')
async def about_me(current_user: str = Depends(get_user_from_token)):
    user = get_user_from_db(current_user)
    if user:
        return user
    return {"error": "User not found"}

