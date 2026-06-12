import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
import time

USE_MOCK = False

# Load environment variables
load_dotenv()

class GeminiService:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(
            api_key=api_key
        )

    def generate_content(self, prompt):
        
        if USE_MOCK:

            return f"""
    MOCK MODE ENABLED

    Prompt Received:

    {prompt}

    ===================================

    This is sample AI-generated content.

    Learning Objectives:
    - Understand the topic
    - Explain the topic
    - Apply the concepts

    Key Concepts:
    - Introduction
    - Core Ideas
    - Examples

    Activities:
    - Group Discussion
    - Quiz Activity

    Assessment:
    - MCQs
    - Short Answers

    Summary:
    This is a mock response generated without using Gemini API.
    """
        
        max_retries = 3
        for attempt in range(max_retries):

            try:

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=prompt
                )

                return response.text

            except Exception as e:

                print(
                    f"Attempt {attempt + 1} failed: {e}"
                )

                time.sleep(3)

        return "Unable to generate content at the moment. Please try again."