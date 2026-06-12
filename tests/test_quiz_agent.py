from agents.quiz_agent import QuizAgent

agent = QuizAgent()

result = agent.generate_quiz(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security"
)

print(result)