from sqlalchemy.orm import Session
from app.models import Tag
from app.schemas.tags import TagCreate, TagUpdate


def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()


def get_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Tag).offset(skip).limit(limit).all()


def update_tag(db: Session, tag_id: int, tag: TagUpdate):
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if db_tag is None:
        return None
    for key, value in tag.dict(exclude_unset=True).items():
        setattr(db_tag, key, value)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def delete_tag(db: Session, tag_id: int):
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if db_tag is None:
        return None
    db.delete(db_tag)
    db.commit()
    return db_tag
