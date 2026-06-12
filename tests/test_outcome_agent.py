from agents.outcome_agent import OutcomeAgent

agent = OutcomeAgent()

result = agent.generate_outcomes(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security"
)

print(result)