from typing import Dict, Any, List
from app.model_routing.fallback_engine import FallbackEngine
from app.model_routing.local_free_llmapi_simulator import LocalFreeLLMAPISimulator
from app.judicial.judicial_brain import JudicialBrain

class ModelRouter:
    def __init__(self, judicial_brain: JudicialBrain):
        self.judicial_brain = judicial_brain
        self.fallback_engine = FallbackEngine(judicial_brain)
        self.simulator = LocalFreeLLMAPISimulator()
        self.health_status = {model: True for model in self.simulator.models}

    def get_healthy_models(self) -> List[str]:
         return [m for m, healthy in self.health_status.items() if healthy]

    def route_request(self, task_id: str, prompt: str) -> Dict[str, Any]:
         models = self.get_healthy_models()
         if not models:
              return {"status": "error", "reason": "no_healthy_models"}

         def call_func(model):
              res = self.simulator.simulate_call(model, prompt)
              if res.get("status") == "error":
                   self.health_status[model] = False # Mark unhealthy
              return res

         return self.fallback_engine.execute_with_fallback(task_id, models, call_func)
