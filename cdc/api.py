from cdc.user.model import User
from cdc.user.service import UserService
from fastapi import APIRouter, Depends


router = APIRouter()


@router.post("/users")
def create_user(
    user: User.Create, user_service: UserService = Depends(UserService.create_service)
) -> User:
    return user_service.create_user(user)
