from typing import Dict, Any, List, Optional
from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def save(self, collection: str, item_id: str, data: Dict[str, Any]):
        pass

    @abstractmethod
    def get(self, collection: str, item_id: str) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def list_all(self, collection: str) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def delete(self, collection: str, item_id: str):
        pass
