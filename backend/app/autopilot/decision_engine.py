from typing import Dict, Any, List
import uuid
import time
from app.models.base import PlanPacket, ConstitutionalVerdict

class DecisionEngine:
    def evaluate_next_step(self, plan: PlanPacket, current_step_index: int, previous_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        if current_step_index >= len(plan.ordered_steps):
            return {"action": "complete"}

        step = plan.ordered_steps[current_step_index]

        # Determine if we need to route to a specific brain or tool
        # For this skeleton, we assume all steps require sandbox execution
        return {
            "action": "execute_sandbox",
            "step": step,
            "index": current_step_index
        }

    def handle_judicial_verdict(self, verdict: ConstitutionalVerdict) -> Dict[str, Any]:
         if verdict.should_stop_loop:
             return {"action": "stop", "reason": verdict.reason}
         if verdict.should_pause_loop:
             if verdict.approval_required:
                 return {"action": "pause_for_approval", "reason": verdict.reason}
             return {"action": "pause", "reason": verdict.reason}
         return {"action": "continue"}
