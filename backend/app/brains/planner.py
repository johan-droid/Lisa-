import uuid
import time
from app.models.base import PlanPacket, PlanStep

class PlannerBrain:
    def create_plan(self, goal: str) -> PlanPacket:
        if not goal.strip():
            return PlanPacket(
                task_id=str(uuid.uuid4()),
                goal="",
                created_at=time.time()
            )

        steps = [
            PlanStep(description="Inspect current files"),
            PlanStep(description="Identify DB models"),
            PlanStep(description="Implement routes"),
            PlanStep(description="Implement tests"),
            PlanStep(description="Run validation")
        ]

        return PlanPacket(
            task_id=str(uuid.uuid4()),
            goal=goal,
            ordered_steps=steps,
            required_modules=["auth", "db"],
            created_at=time.time()
        )
