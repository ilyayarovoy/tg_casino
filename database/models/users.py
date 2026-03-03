from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from database.base import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(30), nullable=False)
    lastname: Mapped[str] = mapped_column(String(30), nullable=True)
    balance: Mapped[float]