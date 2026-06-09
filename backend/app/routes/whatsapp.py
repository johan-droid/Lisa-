from fastapi import APIRouter

router = APIRouter()

@router.get("/webhooks/whatsapp")
def whatsapp_verify():
    return {"status": "ok"}

@router.post("/webhooks/whatsapp")
def whatsapp_webhook():
    return {"status": "ok"}
