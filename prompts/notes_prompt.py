def get_notes_prompt(subject, grade, topic):

    return f"""
You are an expert school teacher.

Create detailed teacher notes.

Subject: {subject}
Grade: {grade}
Topic: {topic}

Requirements:

1. Explain concepts clearly.
2. Use simple language.
3. Include examples.
4. Include teaching tips.
5. Include important points to emphasize.

Format using headings and bullet points.
"""