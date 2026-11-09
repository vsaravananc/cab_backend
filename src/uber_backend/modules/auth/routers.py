from fastapi import APIRouter , Body ,Header , Depends
from typing import Annotated 
from .models import GooglLogin , EmailAndPassword , UserResponse
from .service import AuthService
from uber_backend.database import Session_dp

auth_router : APIRouter = APIRouter(prefix="/auth",tags=['Login'])

@auth_router.put('/login/google')
async def login_with_google(
    google : Annotated[GooglLogin , Body(description="Google sign in")],
    session:Session_dp) -> UserResponse:
    return AuthService.login_with_google(google,session=session)

@auth_router.put('/login/emailandpassword')
def login_with_email_and_password(emailandpassword: Annotated[EmailAndPassword,Body()]) -> UserResponse:
    return UserResponse(**emailandpassword.model_dump(),bearer_token="bearer",refresh_token="refresh")

@auth_router.get('/logout')
def logout(bearer_token : Annotated[str,Header()])-> dict:
    return {'success': True, 'msg':'Successfully logout'}