from odmantic import Field, Model
from datetime import date
from typing import Optional, List, IO


class WorkExperience(Model):
    companyName: str
    dateFrom: date
    dateTo: date
    description: str

class Education(Model):
    school: str
    educationType: str
    fieldOfStudy: Optional[str] = None
    modules: Optional[List[str]] = None
    grades: Optional[List[str]] = None
    

class Applicant(Model):
    firstName: str
    lastName: str
    email: str
    password: str
    location: str
    telephone: str
    education: Optional[List[Education]] = None 
    experience: Optional[List[WorkExperience]] = None
    skillset: List[str]
    certifications: Optional[List[str]] = None
    interests: List[str]
    cv_upload: Optional[IO]
    
    
    
    