from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from model import User
from sqlalchemy.future import select
from fastapi import HTTPException
import random

class UserService:
    @staticmethod
    def generate_default_vector():
        """
        Generate a default list of three random float numbers.
        """
        return [random.uniform(0.0, 1.0) for _ in range(3)]

    async def create_user(self, db: AsyncSession, name: str, height: float, vector: list[float] = None):
        """
        Creates a new user and adds it to the database.
        """
        if vector is None:
            vector = self.generate_default_vector()

        if not isinstance(vector, list) or len(vector) != 3 or not all(isinstance(v, float) for v in vector):
            raise HTTPException(status_code=400, detail="Invalid vector. Must be a list of three floats.")
        
        new_user = User(name=name, height=height, vector=vector)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    async def get_all_users(self, db: AsyncSession):
        """
        Retrieve all users from the database.
        """
        result = await db.execute(select(User))
        return result.scalars().all()

    async def get_user_by_id(self, db: AsyncSession, user_id: int):
        """
        Retrieves a user by ID.
        """
        result = await db.execute(text("SELECT * FROM users WHERE id = :id"), {"id": user_id})
        user = result.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "id": user.id,
            "name": user.name,
            "height": user.height,
            "date": user.date,
            "time": user.time,
            "vector": user.vector,
        }

    async def update_user(self, db: AsyncSession, user_id: int, name: str = None, height: float = None):
        """
        Update a user's details in the database.
        """
        user = await db.get(User, user_id)
        if not user:
            return {"error": f"User with id {user_id} not found"}
        
        if name is not None:
            user.name = name
        if height is not None:
            user.height = height
        
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def delete_user_by_id(self, db: AsyncSession, user_id: int):
        """
        Deletes a user by ID.
        """
        result = await db.execute(text("DELETE FROM users WHERE id = :id RETURNING id"), {"id": user_id})
        deleted_user = result.fetchone()
        
        if not deleted_user:
            raise HTTPException(status_code=404, detail="User not found")

        await db.commit()
        return {"message": f"User with ID {user_id} has been deleted."}
