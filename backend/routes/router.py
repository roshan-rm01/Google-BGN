from fastapi import FastAPI
from routes.applicant.route import applicant_router

router = FastAPI()


@router.get("/")
async def welcome_page():
    return {
        "message": "Welcome to the BGN task everyone."
    }


router.include_router(applicant_router, prefix="/applicant", tags=["Applicant"])