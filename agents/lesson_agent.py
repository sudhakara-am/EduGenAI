from llm.gemini_service import GeminiService
from prompts.lesson_prompt import get_lesson_prompt


class LessonAgent:

    def __init__(self):
        self.gemini_service = GeminiService()

    def generate_lesson_plan(
        self,
        subject,
        grade,
        topic,
        duration
    ):
        print("SUBJECT:", subject)
        print("GRADE:", grade)
        print("TOPIC:", topic)
        print("DURATION:", duration)

        prompt = get_lesson_prompt(
            subject,
            grade,
            topic,
            duration
        )

        lesson_plan = self.gemini_service.generate_content(
            prompt
        )

        return lesson_plan