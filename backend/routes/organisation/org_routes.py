from fastapi import APIRouter, Response, Depends, HTTPException, status, Body
from passlib.context import CryptContext

from database.database_methods import Database
from models.organisation.model import Organisation, OrganisationData
from models.authentication.models import AuthResponse, SignIn
from utilities.jwt_handler import sign_jwt
from utilities.validate_session import validate_org_session

org_router = APIRouter()
org_database = Database(Organisation)
hash_helper = CryptContext(schemes=["bcrypt"])


@org_router.post("/sign-in", response_model=AuthResponse)
async def sign_org_in(response: Response, form: SignIn = Body(...)):
    # TODO: Return a token that'll instruct the frontend to give org access.

    # check if such org exist

    org: Organisation = await org_database.find_one(Organisation.email == form.email)

    if not org:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect Details"
        )

    if org:
        check_password = hash_helper.verify(
            form.password, org.password
        )

        if check_password:
            token = sign_jwt(org.email)
            response.set_cookie("org_session", token)

            return {
                "action": "Sign In",
                "message": "Sign In Successful",
                "token": token
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Invalid Operation"
    )


@org_router.post("/sign-up", response_model=AuthResponse)
async def sign_org_up(response: Response, form: Organisation):
    # Check if such org already exist.

    org_exists = await org_database.find_one(Organisation.email == form.email)
    if org_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Organisation with email exist already!"
        )

    form.password = hash_helper.encrypt(form.password)
    _ = await org_database.save(form)
    token = sign_jwt(form.email)
    response.set_cookie("org_session", token)

    return {
        "action": "Sign Up",
        "message": "New org registered with email {}".format(form.email),
        "token": token
    }


@org_router.post("/sign-out", response_model=AuthResponse)
async def sign_org_out(response: Response):
    response.delete_cookie("org_session")
    return {
        "action": "Sign Out",
        "message": "You have successfully signed out."
    }


@org_router.post("/org-details", response_model=AuthResponse)
async def insert_org_data(form: OrganisationData = Body(...), session: str = Depends(validate_org_session)):
    org: Organisation = await org_database.find_one(Organisation.email == session)

    if not org:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Operation not found."
        )

    org.data = form
    await org_database.save(org)

    return {
        "action": "Organisation Details Upload",
        "message": "Organisation's data saved successfully."
    }


@org_router.get("/profile", response_model=OrganisationData)
async def get_org_data(session: str = Depends(validate_org_session)):
    org: Organisation = await org_database.find_one(Organisation.email == session)

    if not org:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Operation not found."
        )

    return org.data
