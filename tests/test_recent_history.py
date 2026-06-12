from database.db_manager import DatabaseManager

db = DatabaseManager()

recent = db.get_recent_history()

for row in recent:

    print(row)