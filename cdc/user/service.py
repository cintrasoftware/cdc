from logging import getLogger

from cdc.user.model import User
from cdc.user.repository import UserRepository

log = getLogger(__name__)


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User.Create) -> User:
        new_user = self.user_repository.create(user)
        log.info(f"User created: {new_user}")
        return new_user

    def list_users(self) -> list[User]:
        return self.user_repository.list()

    @classmethod
    def create_service(cls) -> "UserService":
        return cls(UserRepository())
