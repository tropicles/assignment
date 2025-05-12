import sqlite3


conn = sqlite3.connect("logs.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    time TEXT,
    message TEXT
)
""")

conn.commit()
print("Database and table created successfully.")


