from pydantic import BaseModel , Field , EmailStr , AfterValidator
from typing import Annotated 
import re

def phone_number_validation(phone_number: str| None):
    if phone_number is not None and not re.fullmatch('^[6-9]\d{9}',phone_number):
        raise ValueError('Enter proper mobile number')
    else:
        return phone_number
    

# Base model
class _UserBaseModel(BaseModel):
    user_name: Annotated[str,Field(description="user name")]
    user_email: Annotated[EmailStr,Field(description="user email")]
    phone_number: Annotated[str|None,Field(default=None,description="user phone number",min_length=10,max_length=10),AfterValidator(phone_number_validation)]

# Create the user with google login
class GooglLogin(_UserBaseModel):
    googl_id: Annotated[str,Field(description="googl id")]
    googl_id_token: Annotated[str,Field(description="googl idToken")]

# Create the user with mail and password
class EmailAndPassword(_UserBaseModel):
    phone_number: Annotated[str,Field(description="user phone number",min_length=10,max_length=10),AfterValidator(phone_number_validation)]
    password: Annotated[str,Field(description="user password",min_length=4)]

# Response
class UserResponse(_UserBaseModel):
    bearer_token : str
    refresh_token : str