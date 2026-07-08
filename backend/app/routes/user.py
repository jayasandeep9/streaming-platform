from fastapi import APIRouter
from app.schemas.user_schema import UserRegister

router = APIRouter()

@router.get("/users")
def get_users():
    return {
        "message": "User API is working"
    }

@router.post("/register")
def register_user(user: UserRegister):
    return {
        "message": "User Registered Successfully",
        "user": user
    }