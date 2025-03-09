from pydantic import BaseModel
from datetime import time

class TimeTableCreate(BaseModel):
    day: str
    start_time: time
    end_time: time
    activity: str

class TimeTableResponse(TimeTableCreate):
    id: int

    class Config:
        orm_mode = True  # ✅ Works with Pydantic v1 & v2
