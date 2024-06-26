from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.authors import create_author, get_author, get_authors, update_author, delete_author
from app.database import get_session
from app.schemas.authors import AuthorCreate, AuthorUpdate, AuthorRead

router = APIRouter(
    prefix="/authors",
    tags=["authors"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=AuthorRead)
def create_author_endpoint(author: AuthorCreate, db: Session = Depends(get_session)):
    return create_author(db, author)


@router.get("/{author_id}", response_model=AuthorRead)
def read_author_endpoint(author_id: int, db: Session = Depends(get_session)):
    db_author = get_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.get("/", response_model=List[AuthorRead])
def read_authors_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return get_authors(db, skip=skip, limit=limit)


@router.put("/{author_id}", response_model=AuthorRead)
def update_author_endpoint(author_id: int, author: AuthorUpdate, db: Session = Depends(get_session)):
    db_author = update_author(db, author_id, author)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.delete("/{author_id}", response_model=AuthorRead)
def delete_author_endpoint(author_id: int, db: Session = Depends(get_session)):
    db_author = delete_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author
