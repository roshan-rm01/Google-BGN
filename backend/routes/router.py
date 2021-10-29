from fastapi import FastAPI

router = FastAPI()


@router.get("/")
async def welcome_page():
    return {
        "message": "Welcome to the BGN task everyone."
    }
