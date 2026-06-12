from database.db_manager import DatabaseManager

db = DatabaseManager()

db.clear_history()

print(
    "History Cleared Successfully"
)