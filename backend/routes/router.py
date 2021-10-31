from fastapi import FastAPI, Depends
from routes.applicant.route import applicant_router
from routes.organisation.route import job_router
from routes.organisation.org_routes import org_router
from starlette.middleware.cors import CORSMiddleware

router = FastAPI()
router.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@router.get("/")
async def welcome_page():
    return {
        "message": "Welcome to the BGN task everyone."
    }


router.include_router(applicant_router, prefix="/applicant", tags=["Applicant"])
router.include_router(job_router, prefix="/job", tags=["Job"])
router.include_router(org_router, prefix="/org", tags=["Org"])
