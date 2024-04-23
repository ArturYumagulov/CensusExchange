import jwt

from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from .model import User
from database import get_async_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_from_db(user_name: str):
    for user in USER_DATA:
        if user.username == user_name:
            return user
    return None


def authenticate_user(user_name: str, password: str):
    user = get_user_from_db(user_name)
    if not user or not verify_password(password, user.password):
        return False
    return True


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user_from_token(token: str):
    """Функция получения User'а по токену"""

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload.get('sub')
    except jwt.ExpiredSignatureError:
        pass  # тут какая-то логика ошибки истечения срока действия токена
    except jwt.InvalidTokenError:
        pass  # тут какая-то логика обработки ошибки декодирования токена


if __name__ == '__main__':
    token = create_access_token({"sub": "user1"})
    print(token)
    username = get_user_from_token(token)
    print(username)
    current_user = get_user_from_db(username)
    print(current_user)




