def classify_risk(churn_probability, threshold=0.5):
    if churn_probability >= threshold:
        return "High"
    elif churn_probability >= 0.3:
        return "Medium"
    else:
        return "Low"


def recommend_action(risk_level):
    if risk_level == "High":
        return [
            "Offer discount",
            "Upgrade plan for 1 month",
            "Free access for 3 months"
        ]
    elif risk_level == "Medium":
        return [
            "Upgrade plan for 1 month",
            "Free access for 3 months"
        ]
    else:
        return [
            "No immediate action"
        ]
