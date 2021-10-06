from datetime import datetime
from typing import Optional

from fastapi import Request, Depends, FastAPI
from fastapi_users import models, fastapi_users, FastAPIUsers
from fastapi_users.authentication import CookieAuthentication, JWTAuthentication

from auth_.Models import UserCreate, UserUpdate, UserDB
from auth_.package import get_user_manager

app = FastAPI()

SECRET = "SECRET"
jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)
cookie_authentication = CookieAuthentication(secret=SECRET, lifetime_seconds=3600)


class User(models.BaseUser):
    first_name = str
    birthday = Optional[datetime.date]

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


someother_router = FastAPIUsers(
    get_user_manager,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB
)


async def get_enabled_backends(request: Request):
    """Return the enabled dependencies following custom logic."""
    if request.url.path == "/protected-route-only-jwt":
        return [jwt_authentication]
    else:
        return [cookie_authentication, jwt_authentication]


current_active_user = fastapi_users.current_user(active=True, get_enabled_backends=get_enabled_backends)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}. You are authenticated with a cookie or a JWT."


@app.get("/protected-route-only-jwt")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}. You are authenticated with a JWT."
