from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import cast, Date
from datetime import date
from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter()

@router.post("/", response_model=TaskResponse)
def add_task(entry: TaskCreate, db: Session = Depends(get_db)):
    print(f"🔥 Received Request: {entry}")

    try:
        new_task = Task(
            title=entry.title,
            description=entry.description,
            start_datetime=entry.start_datetime,
            end_datetime=entry.end_datetime,
            status=entry.status
        )

        db.add(new_task)
        db.commit()
        db.refresh(new_task)

        print(f"✅ Stored Task Entry: {new_task}")
        return new_task

    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/by-date/", response_model=list[TaskResponse])
def get_tasks_by_date(query_date: date, db: Session = Depends(get_db)):
    try:
        tasks = db.query(Task).filter(
            cast(Task.start_datetime, Date) == query_date
        ).all()

        if not tasks:
            raise HTTPException(status_code=404, detail="No tasks found for this date")

        print(f"✅ Retrieved Tasks for {query_date}: {tasks}")
        return tasks

    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
