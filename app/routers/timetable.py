from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.timetable import TimeTable
from app.schemas.timetable import TimeTableCreate, TimeTableResponse
import os

router = APIRouter()

@router.post("/timetable", response_model=TimeTableResponse)
def add_timetable_entry(entry: TimeTableCreate, db: Session = Depends(get_db)):
    """
    Add a new entry to the timetable.
    """
    new_entry = TimeTable(
        day=entry.day,
        start_time=entry.start_time,
        end_time=entry.end_time,
        activity=entry.activity
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry

@router.get("/timetable", response_model=list[TimeTableResponse])
def get_timetable(db: Session = Depends(get_db)):
    """
    Retrieve the complete timetable.
    """
    timetable_entries = db.query(TimeTable).all()
    return timetable_entries

