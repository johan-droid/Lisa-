from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class IncomingChannelMessage(BaseModel):
    message_id: str
    channel: str # telegram, slack, whatsapp
    external_user_id: str
    external_chat_id: str
    text: str
    timestamp: float
    raw_payload_ref: Dict[str, Any]

class NormalizedMessage(BaseModel):
    message_id: str
    channel: str
    external_user_id: str
    external_chat_id: str
    workspace_id: Optional[str] = None
    text: str
    attachments: List[Any] = Field(default_factory=list)
    timestamp: float
    raw_payload_ref: Dict[str, Any]

class IdentitySession(BaseModel):
    user_id: str
    channel: str
    external_user_id: str

class ParsedCommand(BaseModel):
    command: str
    args: str
    is_valid: bool = True
    error_reason: Optional[str] = None

class PlanStep(BaseModel):
    description: str

class PlanPacket(BaseModel):
    task_id: str
    goal: str
    assumptions: List[str] = Field(default_factory=list)
    constraints: List[str] = Field(default_factory=list)
    required_modules: List[str] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list)
    ordered_steps: List[PlanStep] = Field(default_factory=list)
    approval_checkpoints: List[str] = Field(default_factory=list)
    expected_outputs: List[str] = Field(default_factory=list)
    created_at: float

class FeasibilityReport(BaseModel):
    feasible: bool
    blockers: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    missing_modules: List[str] = Field(default_factory=list)
    required_approvals: List[str] = Field(default_factory=list)
    deployment_notes: List[str] = Field(default_factory=list)
    safety_notes: List[str] = Field(default_factory=list)

class RankerScore(BaseModel):
    clarity_score: float
    feasibility_score: float
    safety_score: float
    implementation_readiness_score: float
    token_efficiency_score: float
    overall_score: float
    replan_required: bool
    reasons: List[str] = Field(default_factory=list)

class LisaPipelineResult(BaseModel):
    status: str
    reply: str
    task_id: Optional[str] = None
    approval_required: bool = False
    risk_level: Optional[str] = None

class AuditEvent(BaseModel):
    event_id: str
    task_id: Optional[str] = None
    channel: str
    stage: str
    summary: str
    timestamp: float
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ApprovalRequest(BaseModel):
    approval_id: str
    task_id: str
    reason: str

class ConstitutionalVerdict(BaseModel):
    verdict_id: str
    request_id: str
    mode: str
    verdict_type: str
    allowed: bool
    approval_required: bool
    should_pause_loop: bool
    should_stop_loop: bool
    suspicion_score: float
    risk_level: str
    violated_rules: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    reason: str
    required_action: Optional[str] = None
    created_at: float

class ConstitutionViolation(BaseModel):
    violation_id: str
    task_id: str
    mode: str
    actor_brain: str
    action_type: str
    violated_rule: str
    severity: str
    evidence: str
    judicial_verdict_id: str
    created_at: float

class Constitution(BaseModel):
    constitution_id: str
    mode: str
    version: str
    allowed_actions: List[str] = Field(default_factory=list)
    approval_required_actions: List[str] = Field(default_factory=list)
    always_blocked_actions: List[str] = Field(default_factory=list)
    suspicion_triggers: List[str] = Field(default_factory=list)
    loop_limits: Dict[str, Any] = Field(default_factory=dict)
    token_budget_limits: Dict[str, Any] = Field(default_factory=dict)
    sandbox_rules: Dict[str, Any] = Field(default_factory=dict)
    tool_adoption_rules: Dict[str, Any] = Field(default_factory=dict)
    principal_escalation_rules: Dict[str, Any] = Field(default_factory=dict)
    audit_requirements: List[str] = Field(default_factory=list)

class JudicialInspectionRequest(BaseModel):
    request_id: str
    task_id: str
    mode: str
    actor_brain: str
    action_type: str
    action_summary: str
    payload: Dict[str, Any] = Field(default_factory=dict)
    requested_capability: Optional[str] = None
    risk_level: str
    context: Dict[str, Any] = Field(default_factory=dict)
    created_at: float

class PrincipalApprovalRequest(BaseModel):
    approval_id: str
    task_id: str
    requested_by_brain: str
    action_type: str
    reason: str
    risk_level: str
    evidence: Dict[str, Any] = Field(default_factory=dict)
    cyber_immune_report: Optional[Dict[str, Any]] = None
    red_team_report: Optional[Dict[str, Any]] = None
    judicial_verdict: Optional[Dict[str, Any]] = None
    status: str
    created_at: float
    decided_at: Optional[float] = None

class PrincipalDecision(BaseModel):
    approval_id: str
    decision: str
    reason: str
    restrictions: List[str] = Field(default_factory=list)
    expires_at: Optional[float] = None
    created_at: float

class ToolCandidate(BaseModel):
    candidate_id: str
    name: str
    source_type: str
    source_url: str
    repository: Optional[str] = None
    package_name: Optional[str] = None
    license: Optional[str] = None
    stars: Optional[int] = None
    last_updated: Optional[str] = None
    maintainer_signal: Optional[str] = None
    install_commands: List[str] = Field(default_factory=list)
    required_permissions: List[str] = Field(default_factory=list)
    network_behavior: Optional[str] = None
    filesystem_behavior: Optional[str] = None
    risk_flags: List[str] = Field(default_factory=list)
    trust_score: Optional[float] = None
    teacher_summary: Optional[str] = None
    cyber_immune_report: Optional[Dict[str, Any]] = None
    red_team_report: Optional[Dict[str, Any]] = None
    principal_decision: Optional[Dict[str, Any]] = None
    judicial_verdict: Optional[Dict[str, Any]] = None
    status: str
