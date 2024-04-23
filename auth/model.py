from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, validates
from sqlalchemy import String, JSON, TIMESTAMP, ForeignKey, Boolean


class Base(DeclarativeBase):
    pass


class Roles(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    permissions: Mapped[JSON] = mapped_column(JSON, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    date_joined: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    last_created: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    roles_id: Mapped[int] = mapped_column(ForeignKey("role.id"))

    @validates("email")
    def validate_email(self, key, address):
        if "@" not in address:
            raise ValueError("failed simple email validation")
        return address


user_metadata = Base.metadata
