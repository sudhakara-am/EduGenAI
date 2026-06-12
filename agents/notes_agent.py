from llm.gemini_service import GeminiService
from prompts.notes_prompt import get_notes_prompt


class NotesAgent:

    def __init__(self):
        self.gemini_service = GeminiService()

    def generate_notes(
        self,
        subject,
        grade,
        topic
    ):

        prompt = get_notes_prompt(
            subject,
            grade,
            topic
        )

        notes = self.gemini_service.generate_content(
            prompt
        )

        return notes