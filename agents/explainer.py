class ExplainerAgent:
    def explain(self, analysis, plan, critique):
        risk_level = analysis["risk_level"]
        churn_probability = analysis["churn_probability"]

        explanation = {
            "summary": "",
            "risk_assessment": "",
            "recommended_actions": critique["final_actions"],
            "rationale": [],
            "confidence": plan["decision_confidence"]
        }

        # High-level summary
        explanation["summary"] = (
            f"Customer is assessed as {risk_level} churn risk "
            f"with an estimated probability of {churn_probability:.0%}."
        )

        # Risk interpretation
        if risk_level == "High":
            explanation["risk_assessment"] = (
                "The customer shows a significant likelihood of churn "
                "and requires proactive retention measures."
            )
        elif risk_level == "Medium":
            explanation["risk_assessment"] = (
                "The customer has moderate churn risk; targeted engagement "
                "can help improve retention."
            )
        else:
            explanation["risk_assessment"] = (
                "The customer has low churn risk; no immediate intervention "
                "is required."
            )

        # Rationale
        explanation["rationale"].append(
            "Retention strategy was selected based on churn risk level "
            "and validated through internal review logic."
        )

        if not critique["approved"]:
            explanation["rationale"].extend(critique["concerns"])

        return explanation
