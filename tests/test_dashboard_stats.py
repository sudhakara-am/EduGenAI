from database.db_manager import DatabaseManager

db = DatabaseManager()

lesson_count = db.get_content_count(
    "Lesson Plan"
)

print(
    "Lesson Plans:",
    lesson_count
)