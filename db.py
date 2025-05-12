import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("logs.db")
cursor = conn.cursor()

# Create table
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


