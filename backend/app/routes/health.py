from fastapi import APIRouter
from app.config import settings

router = APIRouter()

@router.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "mode": settings.mode,
        "chat_native": settings.chat_native,
        "dashboard_enabled": settings.dashboard_enabled
    }
