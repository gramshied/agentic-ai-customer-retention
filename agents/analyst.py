from tools.decision_rules import classify_risk


class AnalystAgent:
    def analyze(self, customer_profile, churn_probability):
        risk_level = classify_risk(churn_probability)

        analysis = {
            "risk_level": risk_level,
            "churn_probability": churn_probability,
            "customer_summary": customer_profile
        }

        return analysis
