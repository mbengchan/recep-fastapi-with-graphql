from database.dbconfig import Base, SessionLocal, engine
from fastapi import FastAPI, HTTPException
# from models.category import Base
from routes.category import router as CategoryRouter
from routes.user import router as UserRouter

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