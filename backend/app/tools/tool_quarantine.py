from typing import List, Dict
from app.models.base import ToolCandidate

class ToolQuarantine:
    def __init__(self):
        self._quarantine: Dict[str, ToolCandidate] = {}

    def add(self, candidate: ToolCandidate):
        candidate.status = "quarantined"
        self._quarantine[candidate.candidate_id] = candidate

    def get(self, candidate_id: str) -> ToolCandidate:
        return self._quarantine.get(candidate_id)

    def list_all(self) -> List[ToolCandidate]:
        return list(self._quarantine.values())

    def remove(self, candidate_id: str):
        if candidate_id in self._quarantine:
             del self._quarantine[candidate_id]
