from pydantic import BaseModel
from datetime import datetime

class TimeTableCreate(BaseModel):
    day: str
    start_datetime: datetime  # ✅ Changed to datetime
    end_datetime: datetime  # ✅ Changed to datetime
    activity: str

class TimeTableResponse(TimeTableCreate):
    id: int

    class Config:
        orm_mode = True
