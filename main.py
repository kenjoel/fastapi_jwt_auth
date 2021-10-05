from bottle import Response
from fastapi import FastAPI, Depends
from fastapi_users import fastapi_users
from fastapi_users.authentication import JWTAuthentication

app = FastAPI()

SECRET = "468f94fa929018362423aebd2d1e0dbc122452f5c5a65a39def692a2d1f4bb49"

jwt = JWTAuthentication(SECRET, lifetime_seconds=3000, tokenUrl="/jwt_auth")


@app.post("/jwt_auth")
async def login(response: Response, user=Depends(fastapi_users.current_user(active=True))):
    return await jwt.get_login_response(user, response, None)
