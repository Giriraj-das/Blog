from datetime import datetime, timezone
from typing import List

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped

Base = declarative_base()


class PostTag(Base):
    __tablename__ = 'posts_tags'

    post_id: Mapped[int] = Column(Integer, ForeignKey('post.id'), primary_key=True)
    tag_id: Mapped[int] = Column(Integer, ForeignKey('tag.id'), primary_key=True)


class Post(Base):
    __tablename__ = 'post'

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    title: Mapped[str] = Column(String, nullable=False)
    content: Mapped[str] = Column(Text, nullable=False)
    author_id: Mapped[int] = Column(Integer, ForeignKey('author.id'), nullable=False)
    category_id: Mapped[int] = Column(Integer, ForeignKey('category.id'), nullable=False)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    author: Mapped['Author'] = relationship('Author', back_populates='posts')
    category: Mapped['Category'] = relationship('Category', back_populates='posts')
    tags: Mapped[List['Tag']] = relationship('Tag', secondary='posts_tags', back_populates='posts')


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)

    posts: Mapped[List['Post']] = relationship('Post', back_populates='category')


class Tag(Base):
    __tablename__ = 'tag'

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)

    posts: Mapped[List['Post']] = relationship('Post', secondary='posts_tags', back_populates='tags')


class Author(Base):
    __tablename__ = 'author'

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    email: Mapped[str] = Column(String, unique=True, nullable=False)

    posts: Mapped[List['Post']] = relationship('Post', back_populates='author')
