from app.models.base import IncomingChannelMessage, LisaPipelineResult
from app.chat.message_normalizer import MessageNormalizer
from app.chat.identity_mapper import IdentityMapper
from app.core.lisa_core import LisaCore

class UnifiedChatGateway:
    def __init__(self):
        self.normalizer = MessageNormalizer()
        self.mapper = IdentityMapper()
        self.core = LisaCore()

    def process_message(self, message: IncomingChannelMessage) -> LisaPipelineResult:
        normalized = self.normalizer.normalize(message)
        session = self.mapper.get_or_create_session(normalized)
        return self.core.process(normalized, session)
