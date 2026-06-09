from fastapi import APIRouter, Request
from app.models.base import NormalizedMessage
from app.core.lisa_core import LisaCore
import time

router = APIRouter(prefix="/whatsapp", tags=["whatsapp"])
lisa = LisaCore()

@router.post("")
@router.post("/")
@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    payload = await request.json()

    # Assuming standard WhatsApp Business API payload
    entry = payload.get("entry", [{}])[0]
    changes = entry.get("changes", [{}])[0]
    value = changes.get("value", {})
    messages = value.get("messages", [{}])

    if not messages:
         return {"status": "ok"}

    msg_data = messages[0]
    text = msg_data.get("text", {}).get("body", "")

    if not text:
         return {"status": "ok"}

    msg = NormalizedMessage(
         message_id=msg_data.get("id", ""),
         channel="whatsapp",
         external_user_id=msg_data.get("from", ""),
         external_chat_id=msg_data.get("from", ""),
         text=text,
         timestamp=time.time(),
         raw_payload_ref=payload
    )

    result = lisa.process(msg)
    return {"status": "ok", "reply": result.reply}
