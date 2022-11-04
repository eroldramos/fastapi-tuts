from pydoc import plain
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password:str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

    # {
    #     "Post": {
    #         "content": "content of post 1",
    #         "title": "updated title 2",
    #         "created_at": "2022-10-27T14:32:11.015714+08:00",
    #         "id": 10,
    #         "published": true,
    #         "user_id": 14
    #     },
    #     "votes": 1
    # },
