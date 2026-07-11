from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserRegister


def register_user_service(user: UserRegister, db: Session):

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully",
        "user_id": new_user.id
    }
def get_all_users_service(db: Session):

    users = db.query(User).all()

    return users
def get_user_by_id_service(user_id: int, db: Session):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {
            "message": "User not found"
        }

    return user
def update_user_service(user_id: int, user_data: UserRegister, db: Session):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {
            "message": "User not found"
        }

    user.name = user_data.name
    user.email = user_data.email
    user.password = user_data.password

    db.commit()
    db.refresh(user)

    return {
        "message": "User Updated Successfully",
        "user": user
    }
def delete_user_service(user_id: int, db: Session):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {
            "message": "User not found"
        }

    db.delete(user)
    db.commit()

    return {
        "message": "User Deleted Successfully"
    }