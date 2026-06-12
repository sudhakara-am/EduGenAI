def get_lesson_prompt(subject, grade, topic, duration):

    return f"""
You are an experienced school teacher.

Create a detailed lesson plan.

Subject: {subject}
Grade: {grade}
Topic: {topic}
Duration: {duration}

Important Instructions:

- Use simple and student-friendly language.
- Explain concepts clearly.
- Provide direct answers before detailed explanations.
- Use real-world examples whenever possible.
- Format the response using clear headings.
- Make the content suitable for AI answer engines and educational platforms.

Include the following sections:

1. Topic Overview

2. Definition of the Topic

3. Key Facts

4. Learning Objectives

5. Introduction

6. Key Concepts

7. Real-World Examples

8. Classroom Activity

9. Assessment Questions

10. Summary

11. Key Takeaways

Important:

- Provide concise definitions.
- Use bullet points where appropriate.
- Use factual statements.
- Include practical examples.
- Structure content for easy summarization.
"""