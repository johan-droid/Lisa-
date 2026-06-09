from typing import List, Dict
from app.models.base import ToolCandidate

class ToolRegistry:
    def __init__(self):
        self._trusted_tools: Dict[str, ToolCandidate] = {}

    def add_trusted(self, candidate: ToolCandidate):
        candidate.status = "trusted"
        self._trusted_tools[candidate.candidate_id] = candidate

    def get(self, candidate_id: str) -> ToolCandidate:
        return self._trusted_tools.get(candidate_id)

    def list_all(self) -> List[ToolCandidate]:
        return list(self._trusted_tools.values())
