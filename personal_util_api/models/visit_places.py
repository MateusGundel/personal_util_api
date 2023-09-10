from sqlalchemy.orm import Mapped, mapped_column

from personal_util_api.models import Base


class VisitPlace(Base):
    __tablename__ = 'visit_place'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    visit_turn: Mapped[str]
    user_id: Mapped[int]
