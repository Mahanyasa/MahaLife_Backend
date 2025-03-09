from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth
from app.routers import timetable
from app.routers import bookmark

app = FastAPI(title="MahaLife API")

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(timetable.router, prefix="/timetable", tags=["Timetable"])
app.include_router(bookmark.router, prefix="/bookmark", tags=["Bookmark"])

@app.get("/")
def home():
    return {"message": "Welcome to MahaLife API"}
