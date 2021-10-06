from typing import Optional

from fastapi import Depends
from fastapi_users import BaseUserManager
from requests import Request

from authentication.Models import UserDB, UserCreate
from db.db_sqlite import get_user_db
from main import SECRET


class UserManager(BaseUserManager[UserDB, UserCreate]):
    user_db_model = UserDB
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    @staticmethod
    def on_user_register(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has registered")

    @staticmethod
    def on_forgot_password(user: UserDB, token: str, request: Optional[Request] = None):
        print(f"{user.id} has forgotten its password {token}")

    @staticmethod
    def on_request_verify(user: UserDB, token: str, request: Optional[Request] = None):
        print(f"{user.first_name} has requested verification password reset request on token {token}")


def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
