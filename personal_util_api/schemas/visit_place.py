from pydantic import BaseModel, ConfigDict


class VisitPlaceSchema(BaseModel):
    name: str
    description: str
    visit_turn: str


class VisitPlacePublic(BaseModel):
    id: int
    name: str
    description: str
    visit_turn: str
    user_id: int
    model_config = ConfigDict(from_attributes=True)


class UserDB(VisitPlaceSchema):
    id: int
    user_id: int


class VisitPlaceList(BaseModel):
    visit_places: list[VisitPlacePublic]
