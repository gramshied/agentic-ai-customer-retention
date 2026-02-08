🤖 Agentic AI Customer Retention Decision System
Overview

Traditional churn prediction models identify who is likely to leave but do not answer the more important business question:
what should be done next.

This project implements an Agentic AI decision system that transforms churn risk predictions into reasoned, auditable, and manager-ready retention actions.
Instead of relying on opaque prompt-based reasoning, the system uses a deterministic multi-agent architecture with explicit responsibilities and internal critique.

Problem Statement

Customer churn has a direct impact on revenue, yet retention strategies are often applied uniformly or reactively.
This project addresses the gap between predictive analytics and decision intelligence by designing an AI system that:

Interprets churn risk

Proposes retention actions

Reviews decisions for business risk

Explains recommendations in clear managerial language

System Architecture

The system follows a multi-agent pipeline, where each agent has a clearly defined role:

Agent Roles

Analyst Agent
Interprets customer profile and churn probability to assess risk level.

Planner Agent
Proposes retention strategies based on explicit business rules and policy thresholds.

Critic Agent
Reviews and moderates proposed actions to prevent over-intervention and protect revenue.

Explainer Agent
Generates clear, manager-friendly summaries explaining the final decision, rationale, and confidence.

Agents operate in a fixed, auditable sequence, ensuring transparency and reproducibility.

Customer Data + Churn Risk
        ↓
Analyst Agent
        ↓
Planner Agent
        ↓
Critic Agent
        ↓
Explainer Agent
        ↓
Manager-Ready Decision Output

Decision Logic

High churn risk (≥ 0.5) triggers proactive retention strategies

Business rules ensure revenue-sensitive interventions

Internal critique prevents unnecessary incentives for borderline cases

Decisions are deterministic and explainable

This design mirrors real-world decision committees rather than black-box automation.

Key Features

Multi-agent AI architecture with explicit responsibilities

Rule-based decision safety layer

Internal critique for self-validation

Explainable, manager-oriented outputs

Clean modular design suitable for extension with LLMs

User Interface

A minimal Streamlit interface demonstrates the agentic decision flow:

Input churn probability and customer attributes

Generate a full retention decision

View risk assessment, recommended actions, rationale, and confidence

This UI is designed for demonstration and managerial understanding, not model experimentation.

Why Agentic AI?

Unlike single-model or prompt-based systems, this project demonstrates:

Agent orchestration instead of monolithic reasoning

Self-critique and governance logic

Decision intelligence, not just prediction

Explainability by design, not as an afterthought

This aligns with how AI systems are expected to operate in production environments.

Tech Stack

Python

Streamlit

Modular agent architecture

Rule-based decision logic

(Designed to be LLM-agnostic and easily extensible)

Intended Audience

Product Managers

Customer Retention Teams

Business Decision-Makers

AI/ML Engineers evaluating agentic system design

Project Positioning

This project is intended as a portfolio-grade demonstration of Agentic AI applied to real business decision-making, emphasizing clarity, accountability, and system design over model novelty.
