from sqlalchemy.orm import Session, joinedload
from app.models import Post, Tag
from app.schemas.posts import PostCreate, PostUpdate


def create_post(db: Session, post: PostCreate):
    # Создаем объект Post без списка тегов
    db_post = Post(
        title=post.title,
        content=post.content,
        author_id=post.author_id,
        category_id=post.category_id,
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    # Если есть теги, обрабатываем их
    if post.tags:
        for tag_data in post.tags:
            # Проверяем, существует ли тэг БД
            db_tag = db.query(Tag).filter(Tag.name == tag_data.name).first()
            if not db_tag:
                # Если тега нет, создаем его
                db_tag = Tag(name=tag_data.name)
                db.add(db_tag)
                db.commit()
                db.refresh(db_tag)

            db_post.tags.append(db_tag)

    # Сохраняем все изменения
    db.commit()
    db.refresh(db_post)

    return db_post


def get_post(db: Session, post_id: int):
    return db.query(Post).options(
        joinedload(Post.author),
        joinedload(Post.category),
        joinedload(Post.tags)).filter(Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()


def update_post(db: Session, post_id: int, post: PostUpdate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        return None
    for key, value in post.dict(exclude_unset=True).items():
        if key != 'tags':  # обновляем поля без тегов
            setattr(db_post, key, value)
        else:
            db_post.tags.clear()  # удаляем старые теги

            for tag_data in post.tags:
                db_tag = db.query(Tag).filter(Tag.name == tag_data.name).first()
                if not db_tag:
                    # Если тега нет, создаем его
                    db_tag = Tag(name=tag_data.name)
                    db.add(db_tag)
                    db.commit()
                    db.refresh(db_tag)

                db_post.tags.append(db_tag)

    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).options(
        joinedload(Post.author),
        joinedload(Post.category),
        joinedload(Post.tags)).filter(Post.id == post_id).first()
    if not db_post:
        return None

    db.delete(db_post)
    db.commit()
    return db_post
