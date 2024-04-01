from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database
categories = []

# Pydantic model for blog data
class Category(BaseModel):
    name: str
    slug: str
    description: str

@app.get('/')
def read_root():
    return "Hello World"

@app.get('/categories', response_model=list[Category])
async def getAllCategories():
    return categories

@app.post('/categories', response_model=Category)
async def createCategory(newCat: Category):
    categories.append(newCat)
    return newCat

@app.get('/categories/{id}', response_model=Category)
async def getCategoryById(id: int):
    # try:
        if id < 0 or id >= len(categories):
            raise HTTPException(status_code=404, detail="Resource not found")
        return categories[id]
    # except Exception as e:
    #     print(e)
    #     return "An internal error"

@app.put('/categories/{id}', response_model=Category)
def updateCategory(id: int, updatedCat: Category):
    if id < 0 or id >= len(categories):
        raise HTTPException(status_code=404, detail="Resource not found")
    
    # Update the old cat with updated cat
    categories[id] = updatedCat

    return updatedCat

# @app.patch('/categories/{id}', response_model=Category)
# def updateCategory(id: int, updatedCat: Category):
#     if id < 0 or id >= len(categories):
#         raise HTTPException(status_code=404, detail="Resource not found")
    
#     # category: Category = categories[id]

#     # for cat in updatedCat:
#     #     print(cat)

#     #     if name 

#     return updatedCat

@app.delete('/categories/{id}', response_model=Category)
def deletCategory(id: int):
    if id < 0 or id >= len(categories):
        raise HTTPException(status_code=404, detail="Resource not found")
    
    deleted_cat = categories.pop(id)
    return deleted_cat