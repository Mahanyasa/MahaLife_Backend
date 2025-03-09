from pydantic import BaseModel, HttpUrl

class BookmarkCreate(BaseModel):
    title: str
    link: HttpUrl

class BookmarkResponse(BookmarkCreate):
    id: int

    class Config:
        orm_mode = True
