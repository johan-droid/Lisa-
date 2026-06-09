from app.models.base import PlanPacket, FeasibilityReport, RankerScore

class RankerBrain:
    def score(self, plan: PlanPacket, feasibility: FeasibilityReport) -> RankerScore:
        if not feasibility.feasible:
            return RankerScore(
                clarity_score=0.1,
                feasibility_score=0.1,
                safety_score=0.1,
                implementation_readiness_score=0.1,
                token_efficiency_score=0.1,
                overall_score=0.1,
                replan_required=True,
                reasons=["Plan is not feasible"]
            )

        return RankerScore(
            clarity_score=0.9,
            feasibility_score=0.9,
            safety_score=0.8,
            implementation_readiness_score=0.8,
            token_efficiency_score=0.7,
            overall_score=0.82,
            replan_required=False,
            reasons=["Plan is well-formed"]
        )
