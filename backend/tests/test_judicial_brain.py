import pytest
from app.judicial.judicial_brain import JudicialBrain
from app.models.base import JudicialInspectionRequest

def test_judicial_blocks_bypassing_approval(): # Test 10, 14
    brain = JudicialBrain()
    req = JudicialInspectionRequest(
        request_id="1", task_id="t1", mode="autopilot", actor_brain="user",
        action_type="bypass_approval", action_summary="", risk_level="high", created_at=0.0
    )
    verdict = brain.inspect(req)
    assert verdict.should_stop_loop is True
    assert verdict.verdict_type == "block_action"

def test_judicial_blocks_disabling_itself(): # Test 11
    brain = JudicialBrain()
    req = JudicialInspectionRequest(
        request_id="1", task_id="t1", mode="autopilot", actor_brain="user",
        action_type="disable_judicial_police", action_summary="", risk_level="high", created_at=0.0
    )
    verdict = brain.inspect(req)
    assert verdict.should_stop_loop is True
    assert verdict.verdict_type == "block_action"

def test_judicial_blocks_disabling_audit_log(): # Test 12
    brain = JudicialBrain()
    req = JudicialInspectionRequest(
        request_id="1", task_id="t1", mode="autopilot", actor_brain="user",
        action_type="disable_audit_log", action_summary="", risk_level="high", created_at=0.0
    )
    verdict = brain.inspect(req)
    assert verdict.should_stop_loop is True
    assert verdict.verdict_type == "block_action"

def test_judicial_blocks_disabling_sandbox(): # Test 13
    brain = JudicialBrain()
    req = JudicialInspectionRequest(
        request_id="1", task_id="t1", mode="autopilot", actor_brain="user",
        action_type="disable_sandbox", action_summary="", risk_level="high", created_at=0.0
    )
    verdict = brain.inspect(req)
    assert verdict.should_stop_loop is True
    assert verdict.verdict_type == "block_action"

def test_suspicion_detector_flags_approval_bypass(): # Test 15 (added here because it fits)
    from app.judicial.suspicion_detector import SuspicionDetector
    detector = SuspicionDetector()
    req = JudicialInspectionRequest(
        request_id="1", task_id="t1", mode="autopilot", actor_brain="user",
        action_type="bypass_approval", action_summary="", risk_level="high", created_at=0.0
    )
    score = detector.detect(req)
    assert score >= 0.95

def test_judicial_requires_approval_for_tool_promotion(): # Test 9 (also fits here)
    brain = JudicialBrain()
    req = JudicialInspectionRequest(
        request_id="1", task_id="t1", mode="autopilot", actor_brain="teacher",
        action_type="trusted_tool_activation", action_summary="", risk_level="high", created_at=0.0,
        payload={"status": "pending"}
    )
    verdict = brain.inspect(req)
    assert verdict.approval_required is True
    assert verdict.verdict_type == "require_approval"

def test_security_expired_or_unowned_approval_rejected():
    from app.principal.principal_approval_engine import PrincipalApprovalEngine
    engine = PrincipalApprovalEngine()
    req = engine.create_request("t1", "user", "deploy", "reason", "high", user_id="user1")

    # Try approve with wrong user
    try:
        engine.record_decision(req.approval_id, "approved", "reason", user_id="user2")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Unauthorized" in str(e)

    # Valid approve
    engine.record_decision(req.approval_id, "approved", "reason", user_id="user1")

    # Try approve again (replay)
    try:
        engine.record_decision(req.approval_id, "approved", "reason", user_id="user1")
        assert False, "Should have raised ValueError for replay"
    except ValueError as e:
        assert "not pending" in str(e)
