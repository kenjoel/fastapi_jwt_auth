import datetime
from typing import Optional

from fastapi_users import models


class User(models.BaseUser):
    first_name = str
    birthday = Optional[datetime.date]


class UserCreate(models.BaseUserCreate):
    first_name = str
    birthday = Optional[datetime.date]


class UserUpdate(models.BaseUserUpdate):
    first_name = Optional[str]
    birthday = Optional[datetime.date]


class UserDB(User, models.BaseUserDB):
    pass
