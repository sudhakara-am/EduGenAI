from agents.lesson_agent import LessonAgent


agent = LessonAgent()

result = agent.generate_lesson_plan(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security",
    duration="1 Hour"
)

print(result)