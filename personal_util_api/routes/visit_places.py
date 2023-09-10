from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from personal_util_api.database import get_session
from personal_util_api.models.visit_places import VisitPlace
from personal_util_api.schemas.user import Message
from personal_util_api.schemas.visit_place import (
    VisitPlaceList,
    VisitPlacePublic,
    VisitPlaceSchema,
)
from personal_util_api.security import get_current_user

router = APIRouter(prefix='/visit_places', tags=['visit_places'])


Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[VisitPlace, Depends(get_current_user)]


@router.get('/', response_model=VisitPlaceList)
def read_visit_place(
    session: Session,
    current_user: CurrentUser,
    offset: int = 0,
    limit: int = 100,
):
    places = session.scalars(
        select(VisitPlace).offset(offset).limit(limit)
    ).all()
    return {'visit_places': places}


@router.post('/', response_model=VisitPlacePublic, status_code=201)
def create_visit_place(
    visit_place: VisitPlaceSchema, current_user: CurrentUser, session: Session
):
    db_visit_place = VisitPlace(
        name=visit_place.name,
        description=visit_place.description,
        visit_turn=visit_place.visit_turn,
        user_id=current_user.id,
    )
    session.add(db_visit_place)
    session.commit()
    session.refresh(db_visit_place)
    return db_visit_place


@router.delete('/{visit_place_id}', response_model=Message)
def delete_user(
    session: Session,
    current_user: CurrentUser,
    visit_place_id: int,
):
    db_visit_place = session.scalar(
        select(VisitPlace).where(visit_place_id == VisitPlace.id)
    )
    if db_visit_place.user_id != current_user.id:
        raise HTTPException(status_code=400, detail='Not enough permissions')

    session.delete(db_visit_place)
    session.commit()

    return {'detail': 'Visit Place deleted'}
