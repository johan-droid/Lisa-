from fastapi import APIRouter

router = APIRouter()

@router.post("/webhooks/slack/events")
def slack_webhook():
    return {"status": "ok"}
