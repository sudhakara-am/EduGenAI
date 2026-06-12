def get_quiz_prompt(subject, grade, topic):

    return f"""
You are an experienced school teacher.

Create a complete assessment.

Subject: {subject}
Grade: {grade}
Topic: {topic}

Generate:

SECTION A:
10 Multiple Choice Questions
Each question should have 4 options.

SECTION B:
5 True or False Questions

SECTION C:
5 Short Answer Questions

SECTION D:
Answer Key

Use simple language suitable for the given grade.

Format clearly using headings.
"""