from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.tags import create_tag, get_tag, get_tags, update_tag, delete_tag
from app.database import get_session
from app.schemas.tags import TagCreate, TagUpdate, TagRead, TagsRead

router = APIRouter(
    prefix='/tags',
    tags=['tags'],
    responses={404: {'description': 'Not found'}},
)


@router.post('/', response_model=TagRead)
def create_tag_endpoint(tag: TagCreate, db: Session = Depends(get_session)):
    return create_tag(db, tag)


@router.get('/{tag_id}', response_model=TagRead)
def read_tag_endpoint(tag_id: int, db: Session = Depends(get_session)):
    db_tag = get_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail='Tag not found')
    return db_tag


@router.get('/', response_model=List[TagsRead])
def read_tags_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return get_tags(db, skip=skip, limit=limit)


@router.put('/{tag_id}', response_model=TagRead)
def update_tag_endpoint(tag_id: int, tag: TagUpdate, db: Session = Depends(get_session)):
    db_tag = update_tag(db, tag_id, tag)
    if db_tag is None:
        raise HTTPException(status_code=404, detail='Tag not found')
    return db_tag


@router.delete('/{tag_id}', response_model=TagRead)
def delete_tag_endpoint(tag_id: int, db: Session = Depends(get_session)):
    db_tag = delete_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail='Tag not found')
    return db_tag
