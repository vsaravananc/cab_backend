from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from typing import Annotated


class User(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Annotated[int, Field(primary_key=True)]
    user_name: Annotated[str, Field(description="User name")]
    user_email: Annotated[EmailStr, Field(description="user email")]
    phone_number: Annotated[
        str | None,
        Field(
            default=None,
            description="user phone number",
            min_length=10,
            max_length=10,
        ),
    ]
    googl_id: Annotated[str | None, Field(description="googl id")]
    googl_id_token: Annotated[str | None, Field(description="googl idToken")]
    password: Annotated[
        str | None, Field(description="user password", min_length=4)
    ]
    bearer_token: Annotated[str, Field(description="Bearer token")]
    refresh_token: Annotated[str, Field(description="refresh token")]
    is_login: Annotated[bool | None, Field(default=None)]
