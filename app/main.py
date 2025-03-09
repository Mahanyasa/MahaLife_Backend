from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth
from app.routers import timetable
from app.routers import bookmark
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MahaLife API")

# Create tables
Base.metadata.create_all(bind=engine)
origins = [
    "http://localhost:4200",  # Your frontend (Angular)
    "http://localhost:3000",  # If you plan to use React
    "https://your-frontend-domain.com",  # Your deployed frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(timetable.router, prefix="/timetable", tags=["Timetable"])
app.include_router(bookmark.router, prefix="/bookmark", tags=["Bookmark"])

@app.get("/")
def home():
    return {"message": "Welcome to MahaLife API"}
