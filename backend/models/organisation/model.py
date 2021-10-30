from odmantic import Field, Model
from typing import Optional


class Organisation(Model):
    firstName: str
    lastName: str
    email: str
    password: str
    companyName: str
    location: str
    companyBio: str
    industry: str
    telephone: str
    companySize: Optional[str] = None
    
    
    