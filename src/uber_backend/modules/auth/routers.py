from fastapi import APIRouter , Body ,Header
from typing import Annotated 
from .models import GooglLogin , EmailAndPassword , UserResponse

auth_router : APIRouter = APIRouter(prefix="/auth",tags=['Login'])

@auth_router.put('/login/google')
def login_with_google(google : Annotated[GooglLogin , Body(description="Google sign in")]) -> UserResponse:
    return UserResponse(**google.model_dump(),bearer_token="bearer",refresh_token="refresh")

@auth_router.put('/login/emailandpassword')
def login_with_email_and_password(emailandpassword: Annotated[EmailAndPassword,Body()]) -> UserResponse:
    return UserResponse(**emailandpassword.model_dump(),bearer_token="bearer",refresh_token="refresh")

@auth_router.get('/logout')
def logout(bearer_token : Annotated[str,Header()])-> dict:
    return {'success': True, 'msg':'Successfully logout'}