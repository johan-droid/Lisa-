from app.tokenizer.universal_plan_tokenizer import UniversalPlanTokenizer
from app.brains.planner import PlannerBrain

def test_tokenizer_creates_summary():
    planner = PlannerBrain()
    tokenizer = UniversalPlanTokenizer()

    plan = planner.create_plan("build auth")
    tokenized = tokenizer.tokenize(plan)

    assert "compact_summary" in tokenized
    assert "step_count" in tokenized
    assert tokenized["step_count"] > 0
    assert "token_estimate" in tokenized
