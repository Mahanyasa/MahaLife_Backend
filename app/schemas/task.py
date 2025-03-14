from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    start_datetime: datetime
    end_datetime: datetime
    status: str  # e.g., "Pending", "In Progress", "Completed"

class TaskResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
