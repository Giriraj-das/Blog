from datetime import datetime, timezone
from typing import List

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped

Base = declarative_base()


class PostTag(Base):
    __tablename__ = 'posts_tags'

    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    author: Mapped['Author'] = relationship("Author", back_populates="posts")
    category: Mapped['Category'] = relationship("Category", back_populates="posts")
    tags: Mapped[List['Tag']] = relationship(secondary='posts_tags', back_populates="posts")


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    posts: Mapped[List['Post']] = relationship("Post", back_populates="category")


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    posts: Mapped[List['Post']] = relationship(secondary='posts_tags', back_populates="tags")


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    posts: Mapped[List['Post']] = relationship("Post", back_populates="author")

