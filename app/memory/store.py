import sqlite3

class MemoryStore:
    def __init__(self):
        self.conn = sqlite3.connect("memory.db")
        self.conn.execute("CREATE TABLE IF NOT EXISTS memory (user_id TEXT, message TEXT, response TEXT)")
        self.conn.commit()

    def save_fact(self, user_id, message, response):
        self.conn.execute("INSERT INTO memory VALUES (?, ?, ?)", (user_id, message, response))
        self.conn.commit()

    def get_history(self, user_id):
        cur = self.conn.execute("SELECT message, response FROM memory WHERE user_id=?", (user_id,))
        return cur.fetchall()

    def wipe(self, user_id):
        self.conn.execute("DELETE FROM memory WHERE user_id=?", (user_id,))
        self.conn.commit()
