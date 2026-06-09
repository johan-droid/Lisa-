from typing import Dict, Any, List
from app.models.base import PlanPacket, ConstitutionalVerdict
from app.judicial.judicial_brain import JudicialBrain
from app.autopilot.decision_engine import DecisionEngine
from app.autopilot.workspace_runtime import WorkspaceRuntime

class BrainSwarmOrchestrator:
    def __init__(self, judicial_brain: JudicialBrain, workspace: WorkspaceRuntime):
        self.judicial_brain = judicial_brain  # Fix: use the injected instance instead of instantiating a new one
        self.decision_engine = DecisionEngine()
        self.workspace = workspace

    def run_loop(self, task_id: str, plan: PlanPacket, mode: str) -> Dict[str, Any]:
        current_step = 0
        results = []
        status = "completed"

        while current_step < len(plan.ordered_steps):
            decision = self.decision_engine.evaluate_next_step(plan, current_step, results)

            if decision["action"] == "complete":
                break

            step = decision["step"]

            # Simulated: Generate a command for the step
            cmd = f"echo 'Executing step: {step.description}'"

            # Inspect command before running
            verdict = self.judicial_brain.inspect_sandbox_command(task_id, cmd)

            gov_decision = self.decision_engine.handle_judicial_verdict(verdict)
            if gov_decision["action"] == "stop":
                 status = "stopped_by_judicial_police"
                 results.append({"step": current_step, "status": "blocked", "reason": gov_decision["reason"]})
                 break
            if gov_decision["action"] == "pause_for_approval":
                 status = "paused_for_approval"
                 results.append({"step": current_step, "status": "paused", "reason": gov_decision["reason"]})
                 break

            # Execute safely
            exec_result = self.workspace.execute_task(task_id, cmd)
            results.append({"step": current_step, "status": "success", "result": exec_result})

            current_step += 1

        return {
             "task_id": task_id,
             "status": status,
             "completed_steps": current_step,
             "results": results
        }
