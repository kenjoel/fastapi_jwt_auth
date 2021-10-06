import datetime
from typing import Optional

from fastapi_users import models


class User(models.BaseUser):
    first_name = str
    birthday = Optional[datetime.date]

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class UserCreate(models.BaseUserCreate):
    first_name = str
    birthday = Optional[datetime.date]


class UserUpdate(models.BaseUserUpdate):
    first_name = Optional[str]
    birthday = Optional[datetime.date]


class UserDB(User, models.BaseUserDB):
    pass


class SUser(models.BaseUser, models.BaseOAuthAccountMixin):
    pass
