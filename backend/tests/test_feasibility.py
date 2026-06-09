from app.brains.feasibility import FeasibilityBrain
from app.models.base import PlanPacket
import time

def test_feasibility_catches_bad_plans():
    feasibility = FeasibilityBrain()
    bad_plan = PlanPacket(
        task_id="123",
        goal="",
        ordered_steps=[],
        created_at=time.time()
    )

    report = feasibility.evaluate(bad_plan)
    assert not report.feasible
    assert "Goal is empty" in report.blockers
    assert "Plan has no steps" in report.blockers

def test_feasibility_passes_good_plans():
    feasibility = FeasibilityBrain()
    from app.brains.planner import PlannerBrain
    planner = PlannerBrain()

    good_plan = planner.create_plan("build auth")
    report = feasibility.evaluate(good_plan)
    assert report.feasible
    assert len(report.blockers) == 0
