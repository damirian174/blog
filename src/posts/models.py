
from datetime import  datetime
from sqlalchemy import Integer, String, DateTime, MetaData, func
from sqlalchemy.orm import Mapped, mapped_column
from src.base import Base
metadata = MetaData()

from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

roles = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String, nullable=False),
    Column("content", String, nullable=False),
    Column("at_created", TIMESTAMP),
)


# class Post(Base):
#     __tablename__ = 'post'  # Убедитесь, что запятая убрана
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(String(50), nullable=False)
#     description: Mapped[str] = mapped_column(String(100), nullable=False)
#     content: Mapped[str] = mapped_column(String(600), nullable=False)
#     at_created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
