import sqlite3

class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "edugen.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS history (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                subject TEXT,

                grade TEXT,

                topic TEXT,

                content_type TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        self.connection.commit()
    
    def save_generation(
        self,
        subject,
        grade,
        topic,
        content_type
    ):

        self.cursor.execute(
            """
            INSERT INTO history
            (
                subject,
                grade,
                topic,
                content_type
            )

            VALUES
            (
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                subject,
                grade,
                topic,
                content_type
            )
        )

        self.connection.commit()       

    def get_history(self):

        self.cursor.execute(
            """
            SELECT *
            FROM history
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()      
    
    def get_content_count(
        self,
        content_type
    ):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM history
            WHERE content_type = ?
            """,
            (
                content_type,
            )
        )

        return self.cursor.fetchone()[0]   
    
    def get_recent_history(
        self,
        limit=5
    ):

        self.cursor.execute(
            """
            SELECT topic,
                   content_type,
                   created_at
            FROM history
            ORDER BY id DESC
            LIMIT ?
            """,
            (
                limit,
            )
        )

        return self.cursor.fetchall()    
    
    def clear_history(self):

        self.cursor.execute(
            """
            DELETE FROM history
            """
        )

        self.connection.commit()    