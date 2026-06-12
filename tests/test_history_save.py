from database.db_manager import DatabaseManager

db = DatabaseManager()

db.save_generation(
    subject="Computer Science",
    grade="8",
    topic="Cyber Security",
    content_type="Lesson Plan"
)

print(
    "History Saved Successfully"
)