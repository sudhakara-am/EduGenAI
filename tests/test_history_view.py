from database.db_manager import DatabaseManager

db = DatabaseManager()

history = db.get_history()

for row in history:

    print(row)