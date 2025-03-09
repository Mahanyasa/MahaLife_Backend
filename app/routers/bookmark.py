from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.bookmark import Bookmark
from app.schemas.bookmark import BookmarkCreate, BookmarkResponse

router = APIRouter()

@router.post("/", response_model=BookmarkResponse)
def add_bookmark(bookmark: BookmarkCreate, db: Session = Depends(get_db)):
    new_bookmark = Bookmark(title=bookmark.title, link=str(bookmark.link))  # ✅ Convert to string
    db.add(new_bookmark)
    db.commit()
    db.refresh(new_bookmark)
    return new_bookmark

@router.get("/", response_model=list[BookmarkResponse])
def get_bookmarks(db: Session = Depends(get_db)):
    return db.query(Bookmark).all()
