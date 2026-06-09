from fastapi import APIRouter, Request, HTTPException, Query
from app.models.base import IncomingChannelMessage
from app.chat.gateway import UnifiedChatGateway
import time
import uuid

router = APIRouter()
gateway = UnifiedChatGateway()

@router.get("/webhooks/whatsapp")
def whatsapp_verify(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token")
):
    if hub_mode == "subscribe" and hub_verify_token == "lisa_whatsapp_token":
        return int(hub_challenge)
    raise HTTPException(status_code=403, detail="Invalid token")

@router.post("/webhooks/whatsapp")
async def whatsapp_webhook(request: Request):
    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    try:
        entry = payload.get("entry", [])[0]
        changes = entry.get("changes", [])[0]
        value = changes.get("value", {})
        messages = value.get("messages", [])

        if not messages:
            return {"status": "ok"}

        msg = messages[0]
        text = msg.get("text", {}).get("body", "")

        if not text:
            return {"status": "ok"}

        incoming = IncomingChannelMessage(
            message_id=msg.get("id", str(uuid.uuid4())),
            channel="whatsapp",
            external_user_id=msg.get("from", "unknown"),
            external_chat_id=msg.get("from", "unknown"), # WA chats are often 1:1
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
    except Exception:
        return {"status": "ok", "message": "Ignored invalid structure"}
