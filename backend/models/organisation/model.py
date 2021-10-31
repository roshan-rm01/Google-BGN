from typing import Optional, List

from odmantic import Model, EmbeddedModel
from pydantic import EmailStr, BaseModel


class OrganisationData(EmbeddedModel):
    name: Optional[str]
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
    companyName: str
    email: EmailStr
    password: str
    companyName: str
    data: Optional[OrganisationData]

    class Config:
        schema_extra = {
            "example": {
                "companyName": "Google",
                "email": "page@gmail.com",
                "password": "Strong+Password",
            }
        }
        
    
class Job(Model):
    title: str
    role: str
    description: str
    industry: str
    skillset: List[str]
    company: OrganisationData
    experience: str
    salary: float
    location: str
        
    class Config:
        schema_extra = {
            "example": {
                "title": "Software Engineer",
                "role": "Junior",
                "description": "Python developer needed to develop the Backend",
                "industry": "Internet and Technology",
                "skillset": ["Go", "Python"],
                "company": { 
                    "location": "USA",
                    "companyBio": "Google is the largest technology company",
                    "industry": "Technology",
                    "telephone": "+447398346125",
                    "companySize": "10,000+ Employees"
                },
                "experience": "0-2 years",
                "salary": 1500.00,
                "location": "Remote"
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
    skillset: List[str]
    company: OrganisationData
    experience: str
    salary: float


class JobFilters(BaseModel):
    location: Optional[str]
    industry: Optional[str]
    skillset: Optional[List[str]]
    role: Optional[str]
    title: Optional[str]
    company: Optional[str]
    salary: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "location": "EMEA",
                "industry": "IT",
                "skillset": ["Go", "Python", "Jira"],
                "role": "senior",
                "title": "DevOps",
                "company": "Google",
                "salary": "10000"
            }
        }