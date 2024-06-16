from fastapi import FastAPI, Depends
from . import schemas, crud, database
from sqlalchemy.orm import Session

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

@app.on_event("startup")
async def startup():
    await database.database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_user(user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(database.SessionLocal)):
    return crud.get_user(user_id=user_id)