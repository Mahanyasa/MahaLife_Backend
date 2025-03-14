from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import cast, Date
from datetime import date
from app.database import get_db
from app.models.timetable import TimeTable
from app.schemas.timetable import TimeTableCreate, TimeTableResponse

router = APIRouter()

@router.post("/", response_model=TimeTableResponse)
def add_timetable_entry(entry: TimeTableCreate, db: Session = Depends(get_db)):
    print(f"🔥 Received Request: {entry}")

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

        print(f"✅ Stored Timetable Entry: {new_entry}")
        return new_entry

    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/by-date/", response_model=list[TimeTableResponse])
def get_timetable_by_date(query_date: date, db: Session = Depends(get_db)):
    try:
        timetable_entries = db.query(TimeTable).filter(
            cast(TimeTable.start_datetime, Date) == query_date
        ).all()

        if not timetable_entries:
            raise HTTPException(status_code=404, detail="No entries found for this date")

        print(f"✅ Retrieved Entries for {query_date}: {timetable_entries}")
        return timetable_entries

    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
