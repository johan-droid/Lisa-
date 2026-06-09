from fastapi import APIRouter, Request
from app.models.base import IncomingChannelMessage, NormalizedMessage
from app.core.lisa_core import LisaCore
import time

router = APIRouter(prefix="/telegram", tags=["telegram"])
lisa = LisaCore()

@router.post("")
@router.post("/")
@router.post("/webhook")
async def telegram_webhook(request: Request):
    payload = await request.json()

    # Extract data from telegram payload
    message = payload.get("message", {})
    text = message.get("text", "")
    chat = message.get("chat", {})
    from_user = message.get("from", {})

    if not text:
         return {"status": "ok"}

    msg = NormalizedMessage(
         message_id=str(message.get("message_id", "")),
         channel="telegram",
         external_user_id=str(from_user.get("id", "")),
         external_chat_id=str(chat.get("id", "")),
         text=text,
         timestamp=time.time(),
         raw_payload_ref=payload
    )

    result = lisa.process(msg)

    # Send back required test fields
    return {
        "status": result.status,
        "reply": result.reply,
        "task_id": result.task_id,
        "approval_required": result.approval_required,
        "risk_level": result.risk_level
    }
