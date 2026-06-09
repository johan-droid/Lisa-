from fastapi import APIRouter, Request
from app.models.base import NormalizedMessage
from app.core.lisa_core import LisaCore
import time

router = APIRouter(prefix="/slack", tags=["slack"])
lisa = LisaCore()

@router.post("")
@router.post("/")
@router.post("/events")
async def slack_events(request: Request):
    payload = await request.json()

    if payload.get("type") == "url_verification":
        return {"challenge": payload.get("challenge")}

    event = payload.get("event", {})
    text = event.get("text", "")

    if not text:
         return {"status": "ok"}

    msg = NormalizedMessage(
         message_id=event.get("client_msg_id", ""),
         channel="slack",
         external_user_id=event.get("user", ""),
         external_chat_id=event.get("channel", ""),
         text=text,
         timestamp=time.time(),
         raw_payload_ref=payload
    )

    result = lisa.process(msg)
    return {"status": "ok", "reply": result.reply}
