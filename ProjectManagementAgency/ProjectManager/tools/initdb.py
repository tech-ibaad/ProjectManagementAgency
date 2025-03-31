import sqlite3
import os

# Ensure the database directory exists
if not os.path.exists("database"):
    os.makedirs("database")

# Connect to SQLite database
conn = sqlite3.connect("database/project_management.db")
cursor = conn.cursor()

# Create Projects table
cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    deadline TEXT,
    priority TEXT
)
''')

# Create Tasks table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER,
    name TEXT NOT NULL,
    status TEXT DEFAULT 'Pending',
    deadline TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
)
''')

# Create Strategies table
cursor.execute('''
CREATE TABLE IF NOT EXISTS strategies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER,
    description TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
)
''')

# Commit and close connection
conn.commit()
conn.close()

print("✅ Database setup completed successfully!")
