from agents.notes_agent import NotesAgent

agent = NotesAgent()

result = agent.generate_notes(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security"
)

print(result)