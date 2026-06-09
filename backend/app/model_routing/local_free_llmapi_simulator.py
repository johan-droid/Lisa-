from typing import Dict, Any, List
import uuid

class LocalFreeLLMAPISimulator:
    def __init__(self):
        self.available_tokens = 1000000
        self.models = ["gpt-3.5-turbo", "gpt-4o-mini", "claude-3-haiku"]
        self.usage_ledger = []

    def reserve(self, task_id: str, amount: int) -> bool:
        if self.available_tokens >= amount:
            self.available_tokens -= amount
            self.usage_ledger.append({"task_id": task_id, "amount": amount, "action": "reserve"})
            return True
        return False

    def release(self, task_id: str, amount: int):
         self.available_tokens += amount
         self.usage_ledger.append({"task_id": task_id, "amount": amount, "action": "release"})

    def simulate_call(self, model: str, prompt: str) -> Dict[str, Any]:
        if "rate_limit" in prompt:
             return {"status": "error", "reason": "rate_limit_exceeded"}
        return {"status": "success", "response": f"Simulated response from {model}"}
