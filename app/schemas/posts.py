from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from app.schemas.authors import AuthorRead
from app.schemas.categories import CategoryRead
from app.schemas.tags import TagBase, TagCreate


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    author_id: int
    category_id: int
    tags: Optional[List[TagCreate]] = None


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author_id: Optional[int] = None
    category_id: Optional[int] = None
    tags: Optional[List[TagCreate]] = None


class PostRead(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime
    author: AuthorRead
    category: CategoryRead
    tags: List[TagBase]

    class Config:
        orm_mode: True


class PostsRead(PostBase):
    id: int

    class Config:
        orm_mode: True
