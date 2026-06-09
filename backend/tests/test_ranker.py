from app.brains.ranker import RankerBrain
from app.brains.planner import PlannerBrain
from app.brains.feasibility import FeasibilityBrain

def test_ranker_scores_valid_plans():
    planner = PlannerBrain()
    feasibility = FeasibilityBrain()
    ranker = RankerBrain()

    plan = planner.create_plan("build auth")
    feas = feasibility.evaluate(plan)
    score = ranker.score(plan, feas)

    assert score.overall_score > 0.7
    assert not score.replan_required

def test_ranker_scores_invalid_plans():
    planner = PlannerBrain()
    feasibility = FeasibilityBrain()
    ranker = RankerBrain()

    plan = planner.create_plan("")
    feas = feasibility.evaluate(plan)
    score = ranker.score(plan, feas)

    assert score.overall_score < 0.5
    assert score.replan_required
