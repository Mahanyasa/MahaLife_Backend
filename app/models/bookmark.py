from sqlalchemy import Column, Integer, String
from app.database import Base

class Bookmark(Base):
    __tablename__ = "bookmark"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
