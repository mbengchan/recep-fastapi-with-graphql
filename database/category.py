from models.category import Category
from sqlalchemy.orm import Session


async def get_category(db: Session, category_id: int) -> Category:
    category =  db.query(Category).filter(Category.id == category_id).first()
    return category

async def get_categories(db: Session) -> list[Category]:
    return db.query(Category).all()

async def create_category(db: Session, category: Category) -> Category:
    print(category)
    db_category = Category(
        name=category.name,
        slug=category.name.lower().replace(" ", "-"),
        description=category.description,
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
