from .models import GooglLogin , EmailAndPassword , UserResponse
from sqlmodel import Session
from .schema import User
from uber_backend.database import Session_dp

class AuthService():
    def login_with_google(google : GooglLogin ,session:Session_dp)-> UserResponse:
        print(google.model_dump())
        _user_ : User = User(**google.model_dump())
        session.add(_user_)
        session.commit()
        session.refresh(_user_)
        return UserResponse(**_user_.model_dump(),bearer_token="bearer",refresh_token="refresh")
