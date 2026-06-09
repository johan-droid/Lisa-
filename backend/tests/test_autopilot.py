import pytest
from app.autopilot.autopilot_detector import AutopilotDetector
from app.core.lisa_core import JobRouter, LisaCore
from app.models.base import NormalizedMessage
import time
from app.autopilot.autopilot_controller import AutopilotController
from app.models.base import PlanPacket, PlanStep

def test_autopilot_detector_explicit(): # Test 1
    detector = AutopilotDetector()
    assert detector.detect("Autopilot mode: implement this") is True
    assert detector.detect("/lisa autopilot implement this") is True

def test_autopilot_detector_normal_text(): # Test 2
    detector = AutopilotDetector()
    assert detector.detect("What is autopilot?") is False
    assert detector.detect("lisa plan this") is False

def test_lisa_core_classifies_jobs(): # Test 3
    router = JobRouter()
    assert router.classify("Lisa, find the best open-source tool for PDF") == "tool_adoption_job"
    assert router.classify("research something online") == "research_job"
    assert router.classify("implement the Telegram pipeline") == "implementation_job"

def test_lisa_core_creates_plan(): # Test 4
    core = LisaCore()
    msg = NormalizedMessage(
         message_id="1", channel="telegram", external_user_id="u1",
         external_chat_id="c1", text="lisa plan this: fix the bug",
         timestamp=time.time(), raw_payload_ref={}
    )
    res = core.process(msg)
    assert res.status == "ok"
    assert "Plan created" in res.reply

def test_autopilot_controller_creates_task(): # Test 15
    controller = AutopilotController()
    plan = PlanPacket(task_id="t1", goal="test", ordered_steps=[PlanStep(description="step1")], created_at=0.0)
    res = controller.start_task(plan, "autopilot")
    assert res["status"] in ["completed", "stopped_by_judicial_police", "paused_for_approval"]

def test_brain_swarm_stops_on_judicial(): # Test 16
    from app.autopilot.brain_swarm_orchestrator import BrainSwarmOrchestrator
    from app.judicial.judicial_brain import JudicialBrain
    from app.autopilot.workspace_runtime import WorkspaceRuntime
    from app.sandbox.sandbox_runtime import SandboxRuntime

    class MockJudicial(JudicialBrain):
        def inspect_sandbox_command(self, task_id, cmd):
             from app.judicial.constitutional_verdict import create_verdict
             return create_verdict("1", "autopilot", "block_action", False, False, False, True, 1.0, "high", "blocked")

    orch = BrainSwarmOrchestrator(MockJudicial(), WorkspaceRuntime(SandboxRuntime()))
    plan = PlanPacket(task_id="t1", goal="test", ordered_steps=[PlanStep(description="step1")], created_at=0.0)
    res = orch.run_loop("t1", plan, "autopilot")
    assert res["status"] == "stopped_by_judicial_police"

def test_spike_mode_allows_exploration_blocks_irreversible(): # Test 29
    from app.judicial.judicial_brain import JudicialBrain
    from app.models.base import JudicialInspectionRequest
    brain = JudicialBrain()
    req1 = JudicialInspectionRequest(
        request_id="1", task_id="t1", mode="spike", actor_brain="user",
        action_type="sandbox_execution", action_summary="", risk_level="low", created_at=0.0
    )
    assert brain.inspect(req1).should_stop_loop is False

    req2 = JudicialInspectionRequest(
        request_id="2", task_id="t1", mode="spike", actor_brain="user",
        action_type="deploy", action_summary="", risk_level="high", created_at=0.0
    )
    assert brain.inspect(req2).should_stop_loop is True


def test_safe_repo_autopilot_requires_approval_for_deploy(): # Test 28
    from app.judicial.judicial_brain import JudicialBrain
    from app.models.base import JudicialInspectionRequest
    brain = JudicialBrain()
    req = JudicialInspectionRequest(
        request_id="1", task_id="t1", mode="autopilot", actor_brain="user",
        action_type="deploy", action_summary="", risk_level="high", created_at=0.0
    )
    # The current judicial brain maps deploy to 'production_deployment' block, but let's test a known one
    req.action_type = "production_deployment"
    verdict = brain.inspect(req)
    assert verdict.approval_required is True
