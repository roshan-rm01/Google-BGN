from odmantic import Field, Model
from pydantic import EmailStr
from typing import Optional


class Organisation(Model):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    companyName: str
    location: str
    companyBio: str
    industry: str
    telephone: str
    companySize: Optional[str] = None
    
class Job(Model):
    title: str
    role: str
    description: str
    industry: str
    company: Organisation
    experience: str
    salary: float
    