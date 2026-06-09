from app.models.base import ConstitutionalVerdict
from typing import List, Optional
import time
import uuid

def create_verdict(
    request_id: str,
    mode: str,
    verdict_type: str,
    allowed: bool,
    approval_required: bool,
    should_pause_loop: bool,
    should_stop_loop: bool,
    suspicion_score: float,
    risk_level: str,
    reason: str,
    violated_rules: Optional[List[str]] = None,
    warnings: Optional[List[str]] = None,
    required_action: Optional[str] = None
) -> ConstitutionalVerdict:
    return ConstitutionalVerdict(
        verdict_id=str(uuid.uuid4()),
        request_id=request_id,
        mode=mode,
        verdict_type=verdict_type,
        allowed=allowed,
        approval_required=approval_required,
        should_pause_loop=should_pause_loop,
        should_stop_loop=should_stop_loop,
        suspicion_score=suspicion_score,
        risk_level=risk_level,
        violated_rules=violated_rules or [],
        warnings=warnings or [],
        reason=reason,
        required_action=required_action,
        created_at=time.time()
    )
