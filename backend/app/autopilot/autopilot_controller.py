from typing import Dict, Any, Optional
import uuid
from app.models.base import PlanPacket
from app.judicial.judicial_brain import JudicialBrain
from app.autopilot.brain_swarm_orchestrator import BrainSwarmOrchestrator
from app.autopilot.workspace_runtime import WorkspaceRuntime
from app.sandbox.sandbox_runtime import SandboxRuntime

class AutopilotController:
    def __init__(self):
        self.judicial_brain = JudicialBrain()
        self.sandbox = SandboxRuntime()
        self.workspace = WorkspaceRuntime(self.sandbox)
        self.orchestrator = BrainSwarmOrchestrator(self.judicial_brain, self.workspace)

    def start_task(self, plan: PlanPacket, mode: str) -> Dict[str, Any]:
        # 1. Inspect Activation
        verdict = self.judicial_brain.inspect_autopilot_activation(plan.task_id)

        if verdict.should_stop_loop:
             return {
                 "status": "blocked",
                 "reason": verdict.reason,
                 "task_id": plan.task_id
             }

        if verdict.should_pause_loop and verdict.approval_required:
             return {
                 "status": "requires_approval",
                 "reason": verdict.reason,
                 "task_id": plan.task_id
             }

        # 2. Run Brain Swarm
        result = self.orchestrator.run_loop(plan.task_id, plan, mode)

        return result
