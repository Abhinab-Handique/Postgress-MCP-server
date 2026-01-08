from fastapi import FastAPI
from app.controller import user_controller
from app.core.database import engine, Base

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management CRUD")

app.include_router(user_controller.router)

@app.get("/")
def home():
    return {"message": "User API is up and running"}