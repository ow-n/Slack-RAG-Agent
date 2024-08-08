import sqlite3

class DatabaseManager:
    def __init__(self, db_path='conversation_history.db'):
        self.db_path = db_path
        self._initialize_db()


    def _initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # New table for conversations
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            user_id TEXT PRIMARY KEY,
            chat_history TEXT
        )
        """)

        # New table for active_channel
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS active_channel (
            id INTEGER PRIMARY KEY,
            channel_id TEXT
        )
        """)
        conn.commit()
        conn.close()

    def get_conversation_history(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT chat_history FROM conversations WHERE user_id=?", (user_id,))
        history = cursor.fetchone()
        conn.close()
        return history[0] if history else None

    def update_conversation_history(self, user_id, chat_history, max_messages=5):
        # Split the chat history into individual messages
        messages = chat_history.split('\n')
        
        # Only keep the last `max_messages` messages
        if len(messages) > max_messages:
            messages = messages[-max_messages:]
        
        # Join the messages back together
        truncated_chat_history = '\n'.join(messages)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO conversations (user_id, chat_history) VALUES (?, ?)", (user_id, truncated_chat_history))
        conn.commit()
        conn.close()

    def get_last_active_channel(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT channel_id FROM active_channel WHERE id = 1")
        channel = cursor.fetchone()
        conn.close()
        return channel[0] if channel else None

    def update_last_active_channel(self, channel_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO active_channel (id, channel_id) VALUES (1, ?)", (channel_id,))
        conn.commit()
        conn.close()
