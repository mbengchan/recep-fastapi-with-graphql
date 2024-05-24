import typing

import strawberry
from database.category import create_category, get_categories, get_category
from database.dbconfig import Base, SessionLocal, engine
from fastapi import FastAPI, HTTPException
# from models.category import Base
from routes.category import router as CategoryRouter
from routes.user import router as UserRouter
from schemas.category import CategoryInput, CategoryType
from strawberry.fastapi import GraphQLRouter


# Define a graphql class type
@strawberry.type
class Query:
    @strawberry.field
    def hello() -> str:
        return "Hello Wolrd"
    
    @strawberry.field
    async def category(id: int) -> CategoryType:
        db = SessionLocal()
        category = await get_category(db, id)
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")
        
        return category
    
    @strawberry.field
    async def categories() -> typing.List[CategoryType]:
        db = SessionLocal()
        categories = await get_categories(db)
        return categories
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_category(new_data: CategoryInput) -> CategoryType:
        db = SessionLocal()
        category = await create_category(db, new_data)
        return category
    
schema = strawberry.Schema(Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema=schema)

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(bind=engine)

# startup and shutdown events


def appStartup():
    print("App started")

def appShutdown():
    print("App stopped")

app = FastAPI(
    debug=True,
    on_startup=appStartup()
)

@app.get('/')
def read_root():
    return {"API Status": "Active"}

@app.get('/live')
def read_live():
    return {"API Status": "Active"}

@app.get('/ready')
def read_ready():
    return {"API Status": "Active"}


app.include_router(UserRouter, prefix='/users', tags=["Users"], dependencies=[])
app.include_router(CategoryRouter, tags=["Categories"], prefix='/categories', dependencies=[])
app.include_router(graphql_app, prefix="/graphql")