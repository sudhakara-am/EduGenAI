from agents.main_agent import MainAgent

agent = MainAgent()

result = agent.generate_selected_content(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security",
    duration="1 Hour",
    selected_content=[
        "lesson_plan",
        "notes"
    ]
)

print(result.keys())