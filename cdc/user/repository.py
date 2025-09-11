from typing import List
from sqlalchemy import Column, Integer, String, create_engine
from cdc.user.model import User
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/postgres", echo=True
)


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String)
    lastname: Mapped[str] = mapped_column(String)


class UserRepository:
    def create(self, user: User.Create) -> User:
        with Session(engine) as db:
            db_user = UserModel(firstname=user.firstname, lastname=user.lastname)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
        return User(
            id=db_user.id, firstname=db_user.firstname, lastname=db_user.lastname
        )

    def list(self) -> List[User]:
        with Session(engine) as db:
            db_users = db.query(UserModel).all()
        return [
            User(id=db_user.id, firstname=db_user.firstname, lastname=db_user.lastname)
            for db_user in db_users
        ]
