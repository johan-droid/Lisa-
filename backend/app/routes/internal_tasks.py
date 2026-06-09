from fastapi import APIRouter

router = APIRouter()

@router.post("/internal/tasks")
def create_task():
    return {"status": "ok"}
