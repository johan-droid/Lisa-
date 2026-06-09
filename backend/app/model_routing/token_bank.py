from typing import Dict, Any
from app.judicial.judicial_brain import JudicialBrain
from app.model_routing.local_free_llmapi_simulator import LocalFreeLLMAPISimulator
from app.config import settings

class TokenBankBroker:
    def __init__(self, judicial_brain: JudicialBrain):
        self.judicial_brain = judicial_brain
        self.simulator = LocalFreeLLMAPISimulator()
        self.enabled = settings.FREELLMAPI_ENABLE_TOKEN_BANK

    def reserve(self, task_id: str, amount: int) -> bool:
        if not self.enabled:
             return True

        verdict = self.judicial_brain.inspect_token_reservation(task_id, amount)
        if verdict.should_stop_loop or verdict.approval_required:
             return False

        return self.simulator.reserve(task_id, amount)

    def release(self, task_id: str, amount: int):
         if not self.enabled:
              return
         self.simulator.release(task_id, amount)
