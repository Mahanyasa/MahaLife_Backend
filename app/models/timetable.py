from sqlalchemy import Column, Integer, String, Time
from app.database import Base

class TimeTable(Base):
    __tablename__ = "timetable"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(String, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    activity = Column(String, nullable=False)
