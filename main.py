from agency_swarm import Agency
from ProjectManagerCEO import ProjectManagerCEO
from ProjectManager import ProjectManager

# Instantiate Agents
ceo = ProjectManagerCEO()
manager = ProjectManager()

# Define Agency Communication Flow
agency = Agency([
 ceo,  # CEO communicates with the user2
 [ceo, manager],  # CEO delegates tasks to Project Manager
])

# Run the Agency
if __name__ == "__main__":
 agency.demo_gradio()
