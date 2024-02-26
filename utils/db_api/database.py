from sqlite3 import connect


class DataBase:
    def __init__(self, db_name):
        self.conn = connect(database=db_name)
        self.cur = self.conn.cursor()

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                tg_id INTEGER PRIMARY KEY,
                username TEXT,
                fullname TEXT
            )
            """
        )

        self.conn.commit()

    def get_users(self):
        users_id = self.cur.execute(
            """
            SELECT tg_id FROM users
            """
        ).fetchall()

        return [elem[0] for elem in users_id] if users_id else []

    def add_user(self, tg_id: int, username: str, fullname: str):
        self.cur.execute(
            """
            INSERT OR REPLACE INTO users
            (tg_id, username, fullname)
            VALUES
            (?, ?, ?)
            """,
            (tg_id, username, fullname)
        )

        self.conn.commit()

    def get_user(self, tg_id: int):
        user_info = self.cur.execute(
            """
            SELECT username, fullname FROM users
            WHERE tg_id = ?
            """,
            (tg_id,)
        ).fetchone()

        return user_info if user_info else ()

