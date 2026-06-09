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
