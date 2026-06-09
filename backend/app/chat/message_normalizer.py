from typing import Dict, Any
from app.models.base import IncomingChannelMessage, NormalizedMessage

class MessageNormalizer:
    def normalize(self, incoming: IncomingChannelMessage) -> NormalizedMessage:
        return NormalizedMessage(
            message_id=incoming.message_id,
            channel=incoming.channel,
            external_user_id=incoming.external_user_id,
            external_chat_id=incoming.external_chat_id,
            workspace_id=None,
            text=incoming.text,
            attachments=[],
            timestamp=incoming.timestamp,
            raw_payload_ref=incoming.raw_payload_ref
        )
