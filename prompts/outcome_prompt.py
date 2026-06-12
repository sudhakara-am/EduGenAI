def get_outcome_prompt(subject, grade, topic):

    return f"""
You are an experienced educator.

Create learning outcomes.

Subject: {subject}
Grade: {grade}
Topic: {topic}

Generate:

1. Knowledge Outcomes
2. Skill Outcomes
3. Attitude Outcomes
4. Real World Applications

Use clear measurable statements.

Begin each outcome with:

Students will be able to...
"""