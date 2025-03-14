from sqlalchemy import Column, Integer, String, DateTime, Text
from app.database import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)  # e.g., "Pending", "In Progress", "Completed"
