from fastapi import APIRouter, Response, Depends, HTTPException, status, Body
from passlib.context import CryptContext

from database.database_methods import Database
from models.applicant.model import Applicant, ApplicantData
from models.authentication.models import AuthResponse, SignIn
from utilities.jwt_handler import sign_jwt
from utilities.validate_session import validate_applicant_session

applicant_router = APIRouter()
applicant_database = Database(Applicant)
hash_helper = CryptContext(schemes=["bcrypt"])


@applicant_router.post("/sign-in", response_model=AuthResponse)
async def sign_user_in(response: Response, form: SignIn = Body(...)):
    # TODO: Return a token that'll instruct the frontend to give user access.

    # check if such user exist

    applicant: Applicant = await applicant_database.find_one(Applicant.email == form.email)

    if not applicant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect Details"
        )

    if applicant:
        check_password = hash_helper.verify(
            form.password, applicant.password
        )

        if check_password:
            token = sign_jwt(applicant.email)
            response.set_cookie("session", token)

            return {
                "action": "Sign In",
                "message": "Sign In Successful",
                "token": token
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Invalid Operation"
    )


@applicant_router.post("/sign-up", response_model=AuthResponse)
async def sign_user_up(form: Applicant):
    # Check if such user already exist.

    applicant_exists = await applicant_database.find_one(Applicant.email == form.email)
    if applicant_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Applicant with email exist already!"
        )

    form.password = hash_helper.encrypt(form.password)
    _ = await applicant_database.save(form)

    return {
        "action": "Sign Up",
        "message": "New applicant registered with email {}".format(form.email)
    }


@applicant_router.post("/sign-out", response_model=AuthResponse)
async def sign_user_out(response: Response):
    response.delete_cookie("session")
    return {
        "action": "Sign Out",
        "message": "You have successfully signed out."
    }


@applicant_router.post("/personal-details", response_model=AuthResponse)
async def insert_personal_data(form: ApplicantData = Body(...), session: str = Depends(validate_applicant_session)):
    applicant: Applicant = await applicant_database.find_one(Applicant.email == session)

    if not applicant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Operation not found."
        )

    applicant.data = form
    await applicant_database.save(applicant)

    return {
        "action": "Personal Details Upload",
        "message": "Applicant's data saved successfully."
    }
