from tools.decision_rules import recommend_action


class PlannerAgent:
    def plan(self, analysis):
        risk_level = analysis["risk_level"]
        churn_probability = analysis["churn_probability"]

        possible_actions = recommend_action(risk_level)

        plan = {
            "risk_level": risk_level,
            "churn_probability": churn_probability,
            "recommended_actions": possible_actions,
            "decision_confidence": self._confidence_score(churn_probability)
        }

        return plan

    def _confidence_score(self, churn_probability):
        if churn_probability >= 0.7:
            return "Very High"
        elif churn_probability >= 0.5:
            return "High"
        elif churn_probability >= 0.3:
            return "Medium"
        else:
            return "Low"
