from typing import Optional, Dict
from app.models.base import IdentitySession

class SessionStore:
    def __init__(self):
        self._store: Dict[str, IdentitySession] = {}

    def get(self, key: str) -> Optional[IdentitySession]:
        return self._store.get(key)

    def save(self, key: str, session: IdentitySession) -> None:
        self._store[key] = session
