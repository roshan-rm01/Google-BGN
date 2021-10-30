from datetime import date
from typing import Optional, List

from odmantic import Model, EmbeddedModel
from pydantic import EmailStr


class WorkExperience(EmbeddedModel):
    companyName: str
    dateFrom: date
    dateTo: date
    description: str


class Education(EmbeddedModel):
    school: str
    educationType: str
    fieldOfStudy: Optional[str] = None
    modules: Optional[List[str]] = None
    grades: Optional[List[str]] = None



class ApplicantData(EmbeddedModel):
    location: str
    telephone: str
    education: Optional[List[Education]] = None
    experience: Optional[List[WorkExperience]] = None
    skillset: List[str]
    certifications: Optional[List[str]] = None
    interests: List[str]
    # cv_upload: Optional[]

    class Config:
        schema_extra = {
            "example": {
                "location": "Nigeria",
                "telephone": "+2341234t509",
                "education": [],
                "experience": [],
                "skillset": ["Python, Go"],
                "certifications": [],
                "interests": []
            }
        }


class Applicant(Model):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    data: Optional[ApplicantData]

    class Config:
        schema_extra = {
            "example": {
                "firstName": "Abdulazeez",
                "lastName": "Abdulazeez",
                "email": "youngestdev@gmail.com",
                "password": "Ston!gPasxword!"
            }
        }
