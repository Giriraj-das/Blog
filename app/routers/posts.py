from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.posts import create_post, get_post, get_posts, update_post, delete_post
from app.database import get_session
from app.schemas.posts import PostCreate, PostUpdate, PostRead

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=PostRead)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_session)):
    return create_post(db, post)


@router.get("/{post_id}", response_model=PostRead)
def read_post_endpoint(post_id: int, db: Session = Depends(get_session)):
    db_post = get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.get("/", response_model=List[PostRead])
def read_posts_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return get_posts(db, skip=skip, limit=limit)


@router.put("/{post_id}", response_model=PostRead)
def update_post_endpoint(post_id: int, post: PostUpdate, db: Session = Depends(get_session)):
    db_post = update_post(db, post_id, post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.delete("/{post_id}", response_model=PostRead)
def delete_post_endpoint(post_id: int, db: Session = Depends(get_session)):
    db_post = delete_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
