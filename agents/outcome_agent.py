from llm.gemini_service import GeminiService
from prompts.outcome_prompt import get_outcome_prompt


class OutcomeAgent:

    def __init__(self):
        self.gemini_service = GeminiService()

    def generate_outcomes(
        self,
        subject,
        grade,
        topic
    ):

        prompt = get_outcome_prompt(
            subject,
            grade,
            topic
        )

        outcomes = self.gemini_service.generate_content(
            prompt
        )

        return outcomes