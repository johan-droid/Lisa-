import uuid
from app.models.base import NormalizedMessage, IdentitySession
from app.chat.session_store import SessionStore

class IdentityMapper:
    def __init__(self, session_store: SessionStore = None):
        self.session_store = session_store or SessionStore()

    def get_or_create_session(self, message: NormalizedMessage) -> IdentitySession:
        key = f"{message.channel}_{message.external_user_id}"
        session = self.session_store.get(key)

        if not session:
            user_id = str(uuid.uuid4())
            session = IdentitySession(
                user_id=user_id,
                channel=message.channel,
                external_user_id=message.external_user_id
            )
            self.session_store.save(key, session)

        return session
