from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from utility import UserService
from database import get_db

# Create a router instance
router = APIRouter()

# Instantiate UserService
user_service = UserService()

@router.post("/")
async def api_create_user(
    name: str,
    height: float,
    db: AsyncSession = Depends(get_db)
):
    """
    Endpoint to create a new user.
    """
    return await user_service.create_user(db=db, name=name, height=height)

@router.get("/")
async def api_get_all_users(db: AsyncSession = Depends(get_db)):
    """
    Endpoint to retrieve all users.
    """
    return await user_service.get_all_users(db=db)

@router.get("/{user_id}")
async def api_get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Endpoint to retrieve a user by ID.
    """
    return await user_service.get_user_by_id(db=db, user_id=user_id)

@router.put("/{user_id}")
async def api_update_user(
    user_id: int,
    name: str = None,
    height: float = None,
    db: AsyncSession = Depends(get_db),
):
    """
    Endpoint to update a user's details.
    """
    return await user_service.update_user(db=db, user_id=user_id, name=name, height=height)

@router.delete("/{user_id}")
async def api_delete_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Endpoint to delete a user by ID.
    """
    return await user_service.delete_user_by_id(db=db, user_id=user_id)
