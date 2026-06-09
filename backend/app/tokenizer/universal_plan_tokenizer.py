from app.models.base import PlanPacket
from typing import Dict, Any

class UniversalPlanTokenizer:
    def tokenize(self, plan: PlanPacket) -> Dict[str, Any]:
        compressed_text = f"Goal:{plan.goal}|Steps:{len(plan.ordered_steps)}"
        token_estimate = len(compressed_text) // 4  # simple approximation

        return {
            "compact_summary": f"Plan for '{plan.goal}' with {len(plan.ordered_steps)} steps.",
            "step_count": len(plan.ordered_steps),
            "risk_count": len(plan.risks),
            "approval_count": len(plan.approval_checkpoints),
            "compressed_plan_text": compressed_text,
            "token_estimate": token_estimate
        }
