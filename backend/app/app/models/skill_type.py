from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Skill_Type(Base):

    __tablename__ = "skill_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    type: Mapped[str]
