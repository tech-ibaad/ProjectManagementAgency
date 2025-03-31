🏗️ Project Management Agency - Agency Swarm
🚀 Automate project management with AI-powered agents! This project creates a virtual agency consisting of:
✅ A CEO Agent who oversees project execution.
✅ A Project Manager Agent who manages tasks, projects, and strategies.
✅ A Database to store all project-related data.

With Gradio UI, you can easily interact with your agents in a web interface!

📌 Features
✔ Project & Task Management – Add, update, and remove tasks dynamically.
✔ Automated Decision-Making – AI agents coordinate projects intelligently.
✔ Database Integration – Ensures all project data is stored & managed efficiently.
✔ Gradio UI – A web-based interface for seamless interaction.

🚀 Installation
1️⃣ Install Dependencies
Make sure you have Python 3.8+ installed. Then run:

bash
Copy
Edit
pip install -r requirements.txt
2️⃣ Set Up Database
Run the following command to create the database:

bash
Copy
Edit
python setup_db.py
This will initialize a SQLite database to store projects, tasks, and strategies.

3️⃣ Start the Agency
To run the AI-powered Project Management Agency, use:

bash
Copy
Edit
python main.py
This will launch the Gradio UI, and you’ll see a link like:

nginx
Copy
Edit
Running on local URL:  http://127.0.0.1:7860
Click on it to interact with the CEO & Project Manager AI in a real-time chat interface.

🖥️ Usage
📌 Example Commands
Try these in the Gradio UI:

scss
Copy
Edit
What tasks are currently in progress?
sql
Copy
Edit
Add a new project called "Website Redesign" due "2024-06-15".
pgsql
Copy
Edit
Update task ID 3 to "Completed".
pgsql
Copy
Edit
View all strategies in the database.
🎯 How It Works
The CEO Agent manages high-level project oversight.

The Project Manager Agent updates the database and tracks tasks.

The Database stores all project data.

The Gradio UI lets users interact with the agents in real time.

🛠️ File Structure
graphql
Copy
Edit
📂 project-management-agency/
│── 📂 database/                # Contains SQLite database & utilities
│   ├── db_utils.py             # Helper functions for database management
│   ├── db_tool.py              # ProjectDatabaseTool for interacting with the database
│── 📂 agents/                  # AI-powered agency members
│   ├── CEO.py                  # CEO Agent logic
│   ├── ProjectManager.py        # Project Manager Agent logic
│── main.py                      # Entry point for the agency
│── setup_db.py                   # Initializes the database
│── requirements.txt              # Dependencies
│── README.md                     # Documentation (this file)
🛠 Development & Customization
🔹 Add More Agent Roles
Want to add a Software Developer Agent or a Marketing Agent?
Simply create a new agent file and add it to main.py.

🔹 Change Task Management Rules
Modify ProjectManager.py to change how the agent assigns, tracks, and prioritizes tasks.

🔹 Use a Different Database
By default, the system uses SQLite. To use PostgreSQL or MySQL, update db_utils.py.