import jwt
from decouple import config
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyCookie
from database.database_methods import Database
from models.applicant.model import Applicant
from models.organisation.model import Organisation

applicant_database = Database(Applicant)
org_database = Database(Organisation)
cookie = APIKeyCookie(name="session")
org_cookie = APIKeyCookie(name="org_session")
secret_key = config("secret")


async def validate_applicant_session(session: str = Depends(cookie)) -> bool:
    try:
        payload = jwt.decode(session, secret_key, algorithms="HS256")
        ctx_id = await applicant_database.find_one(Applicant.email == payload["uid"])
        return payload["uid"]

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token passed"
        )


async def validate_org_session(session: str = Depends(org_cookie)) -> bool:
    try:
        payload = jwt.decode(session, secret_key, algorithms="HS256")
        ctx_id = await org_database.find_one(Organisation.email == payload["uid"])
        return payload["uid"]

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token passed"
        )