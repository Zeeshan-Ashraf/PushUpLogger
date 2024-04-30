from dataclasses import dataclass

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from database import mysqlEngine


class Base(DeclarativeBase):
    pass


@dataclass
class UserRepository(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)


Base.metadata.create_all(mysqlEngine)
