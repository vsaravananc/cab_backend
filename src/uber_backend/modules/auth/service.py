from .models import GooglLogin, EmailAndPassword, UserResponse
from sqlmodel import select
from .schema import User
from uber_backend.database import Session_dp


class AuthService:
    def login_with_google(
        google: GooglLogin, session: Session_dp
    ) -> UserResponse:
        _user_: User = User(
            **google.model_dump(),
            bearer_token="bearer",
            refresh_token="refresh",
            is_login=True,
        )
        session.add(_user_)
        session.commit()
        session.refresh(_user_)
        return UserResponse(**_user_.model_dump())

    def login_with_email_and_password(
        emailandpassword: EmailAndPassword, session: Session_dp
    ) -> UserResponse:
        _user_: User = User(
            **emailandpassword.model_dump(),
            bearer_token="bearer",
            refresh_token="refresh",
            is_login=True,
        )
        session.add(_user_)
        session.commit()
        session.refresh(_user_)
        return UserResponse(**_user_.model_dump())

    def logout(bearer_token: str,session: Session_dp) -> dict:
        statement = select(User).where(User.bearer_token == bearer_token)
        result = session.exec(statement).one_or_none()
        if result is None:
            raise ValueError("Unknow user of this bearer token")
        result.is_login = False
        session.add(result)
        session.commit()
        session.refresh(result)
        return {"success": True, "msg": "Successfully logout"}
