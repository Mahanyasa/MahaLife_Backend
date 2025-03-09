from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class TimeTable(Base):
    __tablename__ = "timetable"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(String, nullable=False)
    start_datetime = Column(DateTime, nullable=False)  # ✅ Using DateTime
    end_datetime = Column(DateTime, nullable=False)  # ✅ Using DateTime
    activity = Column(String, nullable=False)
