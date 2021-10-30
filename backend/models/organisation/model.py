from typing import Optional

from odmantic import Model, EmbeddedModel
from pydantic import EmailStr, BaseModel


class OrganisationData(EmbeddedModel):
    location: str
    companyBio: str
    industry: str
    telephone: str
    companySize: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "location": "USA",
                "companyBio": "Google is the largest technology company",
                "industry": "Technology",
                "telephone": "+447398346125",
                "companySize": "10,000+ Employees"
            }
        }


class Organisation(Model):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    companyName: str
    data: Optional[OrganisationData]

    class Config:
        schema_extra = {
            "example": {
                "firstName": "Larry",
                "lastName": "Page",
                "email": "page@gmail.com",
                "password": "Strong+Password",
                "companyName": "Google"
            }
        }
        
    
class Job(Model):
    title: str
    role: str
    description: str
    industry: str
    company: OrganisationData
    experience: str
    salary: float
        
    class Config:
        schema_extra = {
            "example": {
                "title": "Software Engineer",
                "role": "Junior",
                "description": "Python developer needed to develop the Backend",
                "industry": "Internet and Technology",
                "company": { 
                    "location": "USA",
                    "companyBio": "Google is the largest technology company",
                    "industry": "Technology",
                    "telephone": "+447398346125",
                    "companySize": "10,000+ Employees"
                },
                "experience": "0-2 years",
                "salary": 1500.00
            }
        }


class JobResponse(BaseModel):
    action: str
    message: str


class JobDetails(BaseModel):
    title: str
    role: str
    description: str
    industry: str
    company: OrganisationData
    experience: str
    salary: float
