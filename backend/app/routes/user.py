from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user_schema import UserRegister
from app.services.user_service import (
    register_user_service,
    get_all_users_service,
    get_user_by_id_service,
    update_user_service,
    delete_user_service
)

router = APIRouter()


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return get_all_users_service(db)


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id_service(user_id, db)


@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return update_user_service(user_id, user, db)


# ================= DELETE USER =================
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_user_service(user_id, db)


@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user_service(user, db)