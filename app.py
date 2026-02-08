import streamlit as st

from agents.analyst import AnalystAgent
from agents.planner import PlannerAgent
from agents.critic import CriticAgent
from agents.explainer import ExplainerAgent


def run_agentic_decision(customer_profile, churn_probability):
    analyst = AnalystAgent()
    planner = PlannerAgent()
    critic = CriticAgent()
    explainer = ExplainerAgent()

    analysis = analyst.analyze(customer_profile, churn_probability)
    plan = planner.plan(analysis)
    critique = critic.review(plan)
    explanation = explainer.explain(analysis, plan, critique)

    return explanation


# ---------------- UI ---------------- #

st.set_page_config(page_title="Agentic AI Retention Decision System")

st.title("🤖 Agentic AI Customer Retention Decision System")
st.write(
    "This system transforms churn risk predictions into "
    "reasoned, manager-ready retention strategies using a multi-agent AI architecture."
)

st.divider()

# Input
st.subheader("Input Parameters")

churn_probability = st.slider(
    "Estimated Churn Probability",
    min_value=0.0,
    max_value=1.0,
    value=0.55,
    step=0.01
)

customer_profile = {
    "tenure": st.slider("Tenure (months)", 0, 72, 6),
    "contract": st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    ),
    "monthly_charges": st.slider("Monthly Charges", 0, 150, 70),
    "internet_service": st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )
}

st.divider()

if st.button("Generate Retention Decision"):
    decision = run_agentic_decision(customer_profile, churn_probability)

    st.subheader("📌 Decision Summary")
    st.write(decision["summary"])

    st.subheader("⚠️ Risk Assessment")
    st.write(decision["risk_assessment"])

    st.subheader("✅ Recommended Actions")
    for action in decision["recommended_actions"]:
        st.write(f"- {action}")

    st.subheader("🧠 Rationale")
    for reason in decision["rationale"]:
        st.write(f"- {reason}")

    st.subheader("📊 Decision Confidence")
    st.write(decision["confidence"])
