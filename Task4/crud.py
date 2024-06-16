from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal

def create_user(user: schemas.UserCreate):
    db = SessionLocal()
    db_user = models.User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.close()
    return user