class CriticAgent:
    def review(self, plan):
        risk_level = plan["risk_level"]
        churn_probability = plan["churn_probability"]
        actions = plan["recommended_actions"]

        critique = {
            "approved": True,
            "concerns": [],
            "final_actions": actions
        }

        # Rule 1: Avoid aggressive action for borderline risk
        if risk_level == "High" and churn_probability < 0.55:
            critique["approved"] = False
            critique["concerns"].append(
                "Churn risk is only marginally high; aggressive incentives may reduce revenue."
            )
            critique["final_actions"] = [
                "Upgrade plan for 1 month",
                "Free access for 3 months"
            ]

        # Rule 2: No action should be taken for low risk
        if risk_level == "Low" and "No immediate action" not in actions:
            critique["approved"] = False
            critique["concerns"].append(
                "Customer is low risk; intervention is unnecessary."
            )
            critique["final_actions"] = ["No immediate action"]

        return critique
