from typing import Optional

from pydantic import BaseModel, EmailStr


class SignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "youngestdev@gmail.com",
                "password": "Ston!gPasxword!"
            }
        }


class AuthResponse(BaseModel):
    action: str
    message: str
    token: Optional[str]
