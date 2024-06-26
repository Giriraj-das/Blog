from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.categories import create_category, get_category, get_categories, update_category, delete_category
from database import get_session
from schemas.categories import CategoryCreate, CategoryUpdate, CategoryRead, CategoriesRead

router = APIRouter(
    prefix='/categories',
    tags=['categories'],
    responses={404: {'description': 'Not found'}},
)


@router.post('/', response_model=CategoryRead)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_session)):
    return create_category(db, category)


@router.get('/{category_id}', response_model=CategoryRead)
def read_category_endpoint(category_id: int, db: Session = Depends(get_session)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail='Category not found')
    return db_category


@router.get('/', response_model=List[CategoriesRead])
def read_categories_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return get_categories(db, skip=skip, limit=limit)


@router.put('/{category_id}', response_model=CategoryRead)
def update_category_endpoint(category_id: int, category: CategoryUpdate, db: Session = Depends(get_session)):
    db_category = update_category(db, category_id, category)
    if db_category is None:
        raise HTTPException(status_code=404, detail='Category not found')
    return db_category


@router.delete('/{category_id}', response_model=CategoryRead)
def delete_category_endpoint(category_id: int, db: Session = Depends(get_session)):
    db_category = delete_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail='Category not found')
    return db_category
