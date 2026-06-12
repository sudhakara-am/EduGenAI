from agents.activity_agent import ActivityAgent

agent = ActivityAgent()

result = agent.generate_activities(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security"
)

print(result)