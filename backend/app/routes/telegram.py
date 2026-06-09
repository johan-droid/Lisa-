from fastapi import APIRouter, Request, HTTPException
from app.models.base import IncomingChannelMessage
from app.chat.gateway import UnifiedChatGateway
import time
import uuid

router = APIRouter()
gateway = UnifiedChatGateway()

@router.post("/webhooks/telegram")
async def telegram_webhook(request: Request):
    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    message_data = payload.get("message")
    if not message_data:
        return {"status": "ok", "message": "Ignored non-message update"}

    text = message_data.get("text", "")
    if not text:
        return {"status": "ok", "message": "Ignored non-text message"}

    incoming = IncomingChannelMessage(
        message_id=str(message_data.get("message_id", uuid.uuid4())),
        channel="telegram",
        external_user_id=str(message_data.get("from", {}).get("id", "unknown")),
        external_chat_id=str(message_data.get("chat", {}).get("id", "unknown")),
        text=text,
        timestamp=time.time(),
        raw_payload_ref=payload
    )

    result = gateway.process_message(incoming)

    return {
        "status": result.status,
        "reply": result.reply,
        "task_id": result.task_id,
        "approval_required": result.approval_required,
        "risk_level": result.risk_level
    }
