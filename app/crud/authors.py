from sqlalchemy.orm import Session
from models import Author
from schemas.authors import AuthorCreate, AuthorUpdate


def create_author(db: Session, author: AuthorCreate):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()


def update_author(db: Session, author_id: int, author: AuthorUpdate):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author is None:
        return None
    for key, value in author.dict(exclude_unset=True).items():
        setattr(db_author, key, value)
    db.commit()
    db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author is None:
        return None
    db.delete(db_author)
    db.commit()
    return db_author
