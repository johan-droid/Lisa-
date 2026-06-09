from app.chat.message_normalizer import MessageNormalizer
from app.models.base import IncomingChannelMessage

def test_normalizer():
    normalizer = MessageNormalizer()
    incoming = IncomingChannelMessage(
        message_id="msg123",
        channel="telegram",
        external_user_id="user1",
        external_chat_id="chat1",
        text="/lisa plan stuff",
        timestamp=123.45,
        raw_payload_ref={}
    )

    normalized = normalizer.normalize(incoming)
    assert normalized.message_id == "msg123"
    assert normalized.channel == "telegram"
    assert normalized.text == "/lisa plan stuff"
    assert normalized.workspace_id is None
