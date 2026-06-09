from typing import Dict, Any, List, Optional
import uuid
import time
from app.models.base import PrincipalApprovalRequest, PrincipalDecision

class PrincipalApprovalEngine:
    def __init__(self):
        self._requests: Dict[str, PrincipalApprovalRequest] = {}
        self._decisions: Dict[str, PrincipalDecision] = {}

    def create_request(self, task_id: str, requested_by: str, action_type: str, reason: str, risk_level: str, evidence: Dict[str, Any] = None, user_id: str = None) -> PrincipalApprovalRequest:
        req = PrincipalApprovalRequest(
             approval_id=str(uuid.uuid4()),
             task_id=task_id,
             requested_by_brain=requested_by,
             action_type=action_type,
             reason=reason,
             risk_level=risk_level,
             evidence=evidence or {},
             status="pending",
             created_at=time.time()
        )
        # We temporarily stash owner_id on evidence for simple validation
        req.evidence["owner_id"] = user_id
        self._requests[req.approval_id] = req
        return req

    def get_request(self, approval_id: str) -> Optional[PrincipalApprovalRequest]:
        return self._requests.get(approval_id)

    def record_decision(self, approval_id: str, decision: str, reason: str, user_id: str = None, restrictions: List[str] = None) -> Optional[PrincipalDecision]:
        req = self._requests.get(approval_id)
        if not req:
             return None

        # Rule: approval must belong to same user/session
        if req.evidence.get("owner_id") and req.evidence.get("owner_id") != user_id:
             raise ValueError("Unauthorized to approve this request.")

        # Rule: pending check
        if req.status != "pending":
             raise ValueError("Approval is not pending (may be expired, replayed, or already decided).")

        req.status = decision
        req.decided_at = time.time()

        dec = PrincipalDecision(
             approval_id=approval_id,
             decision=decision,
             reason=reason,
             restrictions=restrictions or [],
             created_at=time.time()
        )
        self._decisions[approval_id] = dec
        return dec

    def get_decision(self, approval_id: str) -> Optional[PrincipalDecision]:
        return self._decisions.get(approval_id)
