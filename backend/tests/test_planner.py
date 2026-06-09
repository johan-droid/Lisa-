from app.brains.planner import PlannerBrain

def test_planner_creates_plan():
    planner = PlannerBrain()
    plan = planner.create_plan("build auth system")

    assert plan.goal == "build auth system"
    assert len(plan.ordered_steps) > 0
    assert plan.task_id is not None
