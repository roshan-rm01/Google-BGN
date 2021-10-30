from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from decouple import config
import time
from typing import Dict
import jwt

JWT_SECRET = config("secret")


def verify_jwt(jwtoken: str) -> bool:
    is_token_valid: bool = False

    try:
        payload = decode_jwt(jwtoken)
    except BaseException:
        payload = None
    if payload:
        is_token_valid = True
    return is_token_valid


class JWTBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403,
                    detail="Invalid authentication token")

            if not verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403,
                    detail="Invalid token or expired token")

            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403,
                detail="Invalid authorization token")


def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(ctx_id: str) -> str:
    # Set the expiry time.
    # ctx_id since it can be an employer or org depending on the use case.
    payload = {
        "uid": ctx_id,
        "expires": time.time() + (60 * 10)
    }

    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return decoded_token if decoded_token["expires"] >= time.time(
        ) else None
    except Exception as err:
        return {
            "error": err
        }
