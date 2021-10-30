from odmantic import Field, Model
from datetime import date
from typing import Optional, List, IO
from pydantic import EmailStr


class SignIn(Model):
    email: EmailStr
    password: str

# need more clarification for sign up model
# what fields do we add?
class SignUp(Model):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    