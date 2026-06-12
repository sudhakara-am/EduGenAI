from agents.lesson_agent import LessonAgent
from agents.notes_agent import NotesAgent
from agents.quiz_agent import QuizAgent
from agents.activity_agent import ActivityAgent
from agents.outcome_agent import OutcomeAgent


class MainAgent:

    def __init__(self):

        self.lesson_agent = LessonAgent()

        self.notes_agent = NotesAgent()

        self.quiz_agent = QuizAgent()

        self.activity_agent = ActivityAgent()

        self.outcome_agent = OutcomeAgent()

    def generate_selected_content(
        self,
        subject,
        grade,
        topic,
        duration,
        selected_content
    ):

        results = {}

        if "lesson_plan" in selected_content:

            results["lesson_plan"] = (
                self.lesson_agent.generate_lesson_plan(
                    subject,
                    grade,
                    topic,
                    duration
                )
            )

        if "notes" in selected_content:

            results["notes"] = (
                self.notes_agent.generate_notes(
                    subject,
                    grade,
                    topic
                )
            )

        if "quiz" in selected_content:

            results["quiz"] = (
                self.quiz_agent.generate_quiz(
                    subject,
                    grade,
                    topic
                )
            )

        if "activities" in selected_content:

            results["activities"] = (
                self.activity_agent.generate_activities(
                    subject,
                    grade,
                    topic
                )
            )

        if "outcomes" in selected_content:

            results["outcomes"] = (
                self.outcome_agent.generate_outcomes(
                    subject,
                    grade,
                    topic
                )
            )

        return results