from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.timetable import TimeTable
from app.schemas.timetable import TimeTableCreate, TimeTableResponse

router = APIRouter()

@router.post("/", response_model=TimeTableResponse)
def add_timetable_entry(entry: TimeTableCreate, db: Session = Depends(get_db)):
    print(f"🔥 Received Request: {entry}")  # Debugging log

    try:
        new_entry = TimeTable(
            day=entry.day,
            start_datetime=entry.start_datetime,
            end_datetime=entry.end_datetime,
            activity=entry.activity
        )

        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)

        print(f"✅ Stored Timetable Entry: {new_entry}")  # Debugging log
        return new_entry

    except Exception as e:
        print(f"❌ Error: {e}")  # Debugging log
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=list[TimeTableResponse])
def get_timetable(db: Session = Depends(get_db)):
    try:
        timetable_entries = db.query(TimeTable).all()
        print(f"✅ Retrieved Entries: {timetable_entries}")  # Debugging log
        return timetable_entries
    except Exception as e:
        print(f"❌ Error: {e}")  # Debugging log
        raise HTTPException(status_code=500, detail=str(e))
