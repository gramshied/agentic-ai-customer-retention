# Agentic AI Customer Retention Decision System

## Overview
Predictive churn models identify customers at risk of leaving but do not answer the critical business question: **what action should be taken, and why**.

This project implements an **Agentic AI decision system** that converts churn risk estimates into **auditable, manager-ready retention strategies**.  
The system uses a deterministic multi-agent architecture with explicit roles, internal critique, and explainable outputs—designed for real-world decision support rather than opaque automation.

---

## Problem Statement
Customer churn directly impacts revenue, yet retention actions are often applied uniformly or without clear justification.  
This project bridges the gap between **prediction** and **decision intelligence** by designing an AI system that:

- Interprets churn risk
- Proposes targeted retention strategies
- Reviews decisions for business risk
- Explains recommendations in clear managerial language

---

## System Architecture

The system is composed of four specialized agents operating in a fixed, auditable pipeline:

### Agent Roles
- **Analyst Agent**  
  Assesses churn risk using customer attributes and predicted churn probability.

- **Planner Agent**  
  Proposes retention actions based on explicit business rules and policy thresholds.

- **Critic Agent**  
  Validates and moderates decisions to prevent over-intervention and revenue loss.

- **Explainer Agent**  
  Produces concise, manager-friendly summaries including rationale and confidence.

### Execution Flow


Agents operate in a **deterministic and explainable sequence**, avoiding opaque prompt-based reasoning.

---

## Decision Logic
- Churn probability ≥ **0.5** triggers proactive retention actions  
- Business rules ensure revenue-sensitive decision-making  
- Internal critique prevents unnecessary incentives in borderline cases  
- All decisions are transparent and reproducible  

---

## Key Features
- Explicit multi-agent architecture
- Rule-based decision governance
- Internal self-critique for risk control
- Manager-oriented explanations
- Modular, extensible system design

---

## User Interface
A minimal **Streamlit UI** demonstrates the complete agentic workflow:
- Input churn probability and customer attributes
- Generate a full retention decision
- View risk assessment, recommended actions, rationale, and confidence

The interface is designed for **decision demonstration**, not model experimentation.

---

## Why Agentic AI?
Unlike single-model or prompt-driven systems, this project demonstrates:
- Agent orchestration instead of monolithic reasoning
- Built-in self-review and governance logic
- Decision intelligence rather than raw prediction
- Explainability by design

This mirrors how AI systems are expected to operate in production environments.

---

## Tech Stack
- Python  
- Streamlit  
- Modular multi-agent architecture  
- Rule-based decision logic  

---

## Intended Audience
- Business and product managers  
- Customer retention teams  
- AI/ML engineers evaluating agentic system design  

---

## Project Positioning
This project is a **portfolio-grade demonstration** of Agentic AI applied to real business decision-making, emphasizing transparency, accountability, and system design over model novelty.
