from fastapi import FastAPI
from service import router as user_router
from database import engine, Base

# Create FastAPI instance
app = FastAPI()

# Include user router
app.include_router(user_router, prefix="/users", tags=["Users"])

# Create tables on startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Hello, Async FastAPI!"}
