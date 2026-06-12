from agents.lesson_agent import LessonAgent
from utils.pdf_generator import PdfGenerator

agent = LessonAgent()

lesson = agent.generate_lesson_plan(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security",
    duration="1 Hour"
)

pdf_buffer = (
    PdfGenerator.create_pdf_buffer(
        "Cyber Security Lesson Plan",
        lesson
    )
)

with open(
    "cyber_security_lesson.pdf",
    "wb"
) as f:

    f.write(
        pdf_buffer.getvalue()
    )

print(
    "Lesson PDF Created"
)