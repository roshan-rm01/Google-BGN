from odmantic import Field, Model, EmbeddedModel
from datetime import date
from pydantic import EmailStr
from typing import Optional, List, IO


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
    

class Applicant(Model):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    location: str
    telephone: str
    education: Optional[List[Education]] = None 
    experience: Optional[List[WorkExperience]] = None
    skillset: List[str]
    certifications: Optional[List[str]] = None
    interests: List[str]
    cv_upload: Optional[IO]
    
    
    
    