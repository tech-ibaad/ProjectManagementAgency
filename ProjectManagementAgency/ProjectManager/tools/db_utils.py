import sqlite3

DB_PATH = "database/project_management.db"

def execute_query(query, params=()):
    """Executes a query and commits changes."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    """Fetches data from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

# CRUD Operations
def add_project(name, deadline, priority):
    execute_query("INSERT INTO projects (name, deadline, priority) VALUES (?, ?, ?)", (name, deadline, priority))

def remove_project(project_id):
    execute_query("DELETE FROM projects WHERE id = ?", (project_id,))

def update_project(project_id, name, deadline, priority):
    execute_query("UPDATE projects SET name = ?, deadline = ?, priority = ? WHERE id = ?", (name, deadline, priority, project_id))

def add_task(project_id, name, deadline):
    execute_query("INSERT INTO tasks (project_id, name, deadline) VALUES (?, ?, ?)", (project_id, name, deadline))

def update_task_status(task_id, status):
    execute_query("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))

def remove_task(task_id):
    execute_query("DELETE FROM tasks WHERE id = ?", (task_id,))

def add_strategy(project_id, description):
    execute_query("INSERT INTO strategies (project_id, description) VALUES (?, ?)", (project_id, description))

def remove_strategy(strategy_id):
    execute_query("DELETE FROM strategies WHERE id = ?", (strategy_id,))
