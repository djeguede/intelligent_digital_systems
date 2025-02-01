from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.user import User

class Experience(Base):

    __tablename__ = "experiences"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    company: Mapped[str]
    position: Mapped[str]
    started_at: Mapped[datetime]
    ended_at: Mapped[datetime]
    user_id: Mapped[int] = mapped_column( ForeignKey("users.id", ondelete='cascade') )

    user:Mapped[User] = relationship("User", lazy="joined", cascade="all")