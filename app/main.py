from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth

app = FastAPI(title="MahaLife API")

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def home():
    return {"message": "Welcome to MahaLife API"}
