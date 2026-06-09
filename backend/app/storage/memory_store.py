from typing import Dict, Any, List, Optional
from app.storage.repository import BaseRepository

class MemoryStore(BaseRepository):
    def __init__(self):
        self._db: Dict[str, Dict[str, Dict[str, Any]]] = {}

    def _ensure_collection(self, collection: str):
        if collection not in self._db:
            self._db[collection] = {}

    def save(self, collection: str, item_id: str, data: Dict[str, Any]):
        self._ensure_collection(collection)
        self._db[collection][item_id] = data

    def get(self, collection: str, item_id: str) -> Optional[Dict[str, Any]]:
        self._ensure_collection(collection)
        return self._db[collection].get(item_id)

    def list_all(self, collection: str) -> List[Dict[str, Any]]:
        self._ensure_collection(collection)
        return list(self._db[collection].values())

    def delete(self, collection: str, item_id: str):
        self._ensure_collection(collection)
        if item_id in self._db[collection]:
            del self._db[collection][item_id]
