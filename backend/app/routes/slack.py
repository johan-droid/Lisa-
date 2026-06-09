from fastapi import APIRouter, Request, HTTPException
from app.models.base import IncomingChannelMessage
from app.chat.gateway import UnifiedChatGateway
import time
import uuid

router = APIRouter()
gateway = UnifiedChatGateway()

@router.post("/webhooks/slack/events")
async def slack_webhook(request: Request):
    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    if "challenge" in payload:
        return {"challenge": payload["challenge"]}

    event = payload.get("event", {})
    if event.get("type") != "message" or "bot_id" in event:
        return {"status": "ok"}

    incoming = IncomingChannelMessage(
        message_id=event.get("client_msg_id", str(uuid.uuid4())),
        channel="slack",
        external_user_id=event.get("user", "unknown"),
        external_chat_id=event.get("channel", "unknown"),
        text=event.get("text", ""),
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
