def get_activity_prompt(subject, grade, topic):

    return f"""
You are an experienced school teacher.

Create engaging classroom activities.

Subject: {subject}
Grade: {grade}
Topic: {topic}

Generate:

1. Individual Activity
2. Pair Activity
3. Group Activity
4. Hands-On Activity
5. Fun Classroom Challenge

Make activities age appropriate.

Use simple instructions.

Format clearly with headings.
"""