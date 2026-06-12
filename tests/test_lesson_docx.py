from agents.lesson_agent import LessonAgent
from utils.docx_generator import DocxGenerator

agent = LessonAgent()

lesson = agent.generate_lesson_plan(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security",
    duration="1 Hour"
)

DocxGenerator.create_docx(
    title="Cyber Security Lesson Plan",
    content=lesson,
    filename="cyber_security_lesson.docx"
)

print(
    "Lesson Plan DOCX Created"
)