from fastapi import APIRouter
from app.config import settings

router = APIRouter()

@router.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "mode": getattr(settings, "mode", "unknown"),
        "chat_native": getattr(settings, "chat_native", True),
        "dashboard_enabled": getattr(settings, "dashboard_enabled", False)
    }
