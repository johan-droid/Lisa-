import pytest
from app.teacher.tool_discovery_brain import ToolDiscoveryBrain
from app.cyber_immune.tool_risk_scanner import ToolRiskScanner
from app.tools.tool_quarantine import ToolQuarantine
from app.principal.principal_approval_engine import PrincipalApprovalEngine

def test_teacher_brain_creates_candidates(): # Test 5
    teacher = ToolDiscoveryBrain()
    candidates = teacher.research("pdf parsing")
    assert len(candidates) > 0
    assert candidates[0].name == "pdfminer.six"

def test_tool_enters_quarantine_by_default(): # Test 6
    quarantine = ToolQuarantine()
    teacher = ToolDiscoveryBrain()
    candidate = teacher.research("pdf parsing")[0]
    quarantine.add(candidate)
    assert quarantine.get(candidate.candidate_id).status == "quarantined"

def test_cyber_immune_flags_risky_install(): # Test 7
    scanner = ToolRiskScanner()
    teacher = ToolDiscoveryBrain()
    candidate = teacher.research("github")[0] # The mock returns "sudo apt install gh"
    scanned = scanner.scan(candidate)
    assert "sudo" in str(scanned.risk_flags)
    assert scanned.trust_score < 1.0

def test_principal_approval_engine_creates_request(): # Test 8
    engine = PrincipalApprovalEngine()
    req = engine.create_request("t1", "teacher", "tool_promotion", "testing", "medium")
    assert req.status == "pending"
    assert engine.get_decision(req.approval_id) is None

# Test 9 is already covered in test_judicial_brain.py
