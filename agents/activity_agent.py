from llm.gemini_service import GeminiService
from prompts.activity_prompt import get_activity_prompt


class ActivityAgent:

    def __init__(self):
        self.gemini_service = GeminiService()

    def generate_activities(
        self,
        subject,
        grade,
        topic
    ):

        prompt = get_activity_prompt(
            subject,
            grade,
            topic
        )

        activities = self.gemini_service.generate_content(
            prompt
        )

        return activities