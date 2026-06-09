from app.loop.loop_governor import LoopGovernor
from app.brains.planner import PlannerBrain
from app.brains.feasibility import FeasibilityBrain
from app.brains.ranker import RankerBrain

def test_loop_governor_runs_once():
    governor = LoopGovernor()
    planner = PlannerBrain()
    feasibility = FeasibilityBrain()
    ranker = RankerBrain()

    # an empty goal leads to a bad score
    plan = planner.create_plan("")
    feas = feasibility.evaluate(plan)
    score = ranker.score(plan, feas)

    res = governor.run(plan, score)

    # Since we trigger a replan when score < min_score,
    # loop count should be exactly 1, no infinite loops
    assert res["loop_count"] == 1
    assert res["replan_performed"] is True
