import sqlite3
from agency_swarm.tools import BaseTool
from pydantic import Field

DB_PATH = "database/project_management.db"

# Helper functions for database operations
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

def view_projects():
    return fetch_query("SELECT * FROM projects")

def add_task(project_id, name, deadline):
    execute_query("INSERT INTO tasks (project_id, name, deadline) VALUES (?, ?, ?)", (project_id, name, deadline))

def update_task_status(task_id, status):
    execute_query("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))

def remove_task(task_id):
    execute_query("DELETE FROM tasks WHERE id = ?", (task_id,))

def view_tasks():
    return fetch_query("SELECT * FROM tasks")

def add_strategy(project_id, description):
    execute_query("INSERT INTO strategies (project_id, description) VALUES (?, ?)", (project_id, description))

def remove_strategy(strategy_id):
    execute_query("DELETE FROM strategies WHERE id = ?", (strategy_id,))

def view_strategies():
    return fetch_query("SELECT * FROM strategies")

# ProjectDatabaseTool for AI agent interaction
class ProjectDatabaseTool(BaseTool):
    """Tool for managing the project database (add, remove, update, and view projects, tasks, and strategies)."""

    action: str = Field(..., description="The action to perform: add, remove, update, view.")
    item_type: str = Field(..., description="Type of item: project, task, strategy.")
    item_data: dict = Field(None, description="The data for the item (only required for add, update, and remove).")

    def run(self):
        if self.item_type == "project":
            if self.action == "add":
                add_project(self.item_data["name"], self.item_data["deadline"], self.item_data["priority"])
                return f"✅ Project '{self.item_data['name']}' added successfully."
            elif self.action == "remove":
                remove_project(self.item_data["id"])
                return f"🗑️ Project ID {self.item_data['id']} removed."
            elif self.action == "update":
                update_project(self.item_data["id"], self.item_data["name"], self.item_data["deadline"], self.item_data["priority"])
                return f"🔄 Project ID {self.item_data['id']} updated."
            elif self.action == "view":
                projects = view_projects()
                return f"📋 Projects: {projects}" if projects else "⚠️ No projects found."

        elif self.item_type == "task":
            if self.action == "add":
                add_task(self.item_data["project_id"], self.item_data["name"], self.item_data["deadline"])
                return f"✅ Task '{self.item_data['name']}' added."
            elif self.action == "remove":
                remove_task(self.item_data["id"])
                return f"🗑️ Task ID {self.item_data['id']} removed."
            elif self.action == "update":
                update_task_status(self.item_data["id"], self.item_data["status"])
                return f"🔄 Task ID {self.item_data['id']} status updated to {self.item_data['status']}."
            elif self.action == "view":
                tasks = view_tasks()
                return f"📋 Tasks: {tasks}" if tasks else "⚠️ No tasks found."

        elif self.item_type == "strategy":
            if self.action == "add":
                add_strategy(self.item_data["project_id"], self.item_data["description"])
                return f"✅ Strategy added to Project ID {self.item_data['project_id']}."
            elif self.action == "remove":
                remove_strategy(self.item_data["id"])
                return f"🗑️ Strategy ID {self.item_data['id']} removed."
            elif self.action == "view":
                strategies = view_strategies()
                return f"📋 Strategies: {strategies}" if strategies else "⚠️ No strategies found."

        return "⚠️ Invalid action or item type."
