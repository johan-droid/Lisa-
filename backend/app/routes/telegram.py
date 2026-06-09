from fastapi import APIRouter

router = APIRouter()

@router.post("/webhooks/telegram")
def telegram_webhook():
    return {"status": "ok"}
