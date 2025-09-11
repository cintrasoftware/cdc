from cdc.user.model import User
from cdc.user.service import UserService
from cdc.user.repository import Base, engine
from fastapi import Depends
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine, checkfirst=True)
    print("Database initialized")


@app.post("/users")
def create_user(
    user: User.Create, user_service: UserService = Depends(UserService.create_service)
) -> User:
    return user_service.create_user(user)


@app.get("/users")
def list_users(
    user_service: UserService = Depends(UserService.create_service),
) -> list[User]:
    return user_service.list_users()
