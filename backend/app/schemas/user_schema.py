from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        description="User Name"
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=30,
        description="Password"
    )