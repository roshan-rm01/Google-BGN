from odmantic import Field, Model
from datetime import date
from typing import Optional, List, IO


class SignIn(Model):
    email: str
    password: str

# need more clarification for sign up model
# what fields do we add?
class SignUp(Model):
    firstName: str
    lastName: str
    email: str
    password: str
    