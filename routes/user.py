from typing import List

from database.dbconfig import SessionLocal, get_db
from database.user import create_user, get_user, get_user_by_email, get_users
from fastapi import APIRouter, Depends, HTTPException
from schemas.user import User, UserCreate
from sqlalchemy.orm import Session

# Create a router for the user endpoints

router = APIRouter()

@router.get('', summary="Get all users", description= "This endpoint returns all users", response_model=List[User])
async def getAllUsers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print("This is the function that will return all users from the database")
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post('', summary= "Create a new user", description= "This endpoint creates a new user")
async def createUser(user: UserCreate, db: Session = Depends(get_db)):
    print(f"User object received: {user.model_dump()}")
    db = SessionLocal()
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    return create_user(db=db, user=user)

@router.get('/{id}', summary= "Get a user by id", description= "This endpoint returns a user by id", response_model=User)
async def getUserById(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put('/{id}', summary= "Update a user by id", description= "This endpoint updates a user by id")
async def updateUserById(id: int):
    print("This is the function that will update a user by id in the database")
    return {}

@router.delete('/{id}', summary= "Delete a user by id", description= "This endpoint deletes a user by id")
async def deleteUserById(user_id: int, db: Session = Depends(get_db)):
    print("This is the function that will delete a user by id from the database")
    return {}