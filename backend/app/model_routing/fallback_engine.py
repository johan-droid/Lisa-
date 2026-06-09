from typing import Dict, Any, List, Optional
import time
import uuid
from app.config import settings
from app.judicial.judicial_brain import JudicialBrain
from app.models.base import JudicialInspectionRequest

class FallbackEngine:
    def __init__(self, judicial_brain: JudicialBrain):
        self.max_fallbacks = settings.FREELLMAPI_MAX_FALLBACKS_PER_REQUEST
        self.judicial_brain = judicial_brain

    def execute_with_fallback(self, task_id: str, models: List[str], call_func) -> Dict[str, Any]:
         attempts = 0
         for model in models:
             if attempts >= self.max_fallbacks:
                  return {"status": "error", "reason": "max_fallbacks_reached"}

             # Call judicial before switch if not first attempt
             if attempts > 0:
                 req = JudicialInspectionRequest(
                     request_id=str(uuid.uuid4()), task_id=task_id, mode="autopilot",
                     actor_brain="model_router", action_type="model_switch",
                     action_summary=f"Switching to {model}", payload={"model": model},
                     risk_level="low", created_at=time.time()
                 )
                 verdict = self.judicial_brain.inspect(req)

                 if verdict.should_stop_loop:
                      return {"status": "error", "reason": "judicial_block_on_switch"}

             result = call_func(model)
             if result.get("status") == "success":
                  return result

             attempts += 1

         return {"status": "error", "reason": "all_models_failed"}
