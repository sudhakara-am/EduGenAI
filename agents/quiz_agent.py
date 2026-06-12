from llm.gemini_service import GeminiService
from prompts.quiz_prompt import get_quiz_prompt


class QuizAgent:

    def __init__(self):
        self.gemini_service = GeminiService()

    def generate_quiz(
        self,
        subject,
        grade,
        topic
    ):

        prompt = get_quiz_prompt(
            subject,
            grade,
            topic
        )

        quiz = self.gemini_service.generate_content(
            prompt
        )

        return quiz