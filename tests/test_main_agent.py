from agents.main_agent import MainAgent

agent = MainAgent()

result = agent.generate_complete_package(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security",
    duration="1 Hour"
)

print(result.keys())