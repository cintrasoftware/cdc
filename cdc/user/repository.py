from sqlalchemy import Column, Integer, String, create_engine
from cdc.user.model import User
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


engine = create_engine("sqlite://", echo=True)


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fistname: Mapped[str] = mapped_column(String)
    lastname: Mapped[str] = mapped_column(String)


class UserRepository:
    def create(self, user: User.Create) -> User:
        with Session(engine) as db:
            db_user = UserModel(fistname=user.fistname, lastname=user.lastname)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
        return User(id=db_user.id, fistname=db_user.fistname, lastname=db_user.lastname)
