from typing import List, Union

from database.category import create_category, get_categories
from database.dbconfig import get_db
from fastapi import APIRouter, Depends
from schemas.category import Category, CategoryCreate
from sqlalchemy.orm import Session

# Define the FastAPI router for the category resource

# Create a FastAPI router for the category resource

router = APIRouter()

@router.get('')
async def getAllCategories(db: Session = Depends(get_db)) -> List[Category]:
    return await get_categories(db)

@router.get('/{category_id}')
async def get_category(category_id: int):
    return {'category_id': category_id}

@router.post('')
async def createCategory(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        new_category =  await create_category(db, category)
        print("Here")
        if not new_category:
            return {'error': 'Category not created'}
        return {'message': "Category created successfully", 'category': new_category}
    
    except Exception as e:
        return {'error': str(e)}
