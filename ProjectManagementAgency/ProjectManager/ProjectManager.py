from agency_swarm import Agent
from ProjectManager.tools.ProjectDatabaseTool import ProjectDatabaseTool

class ProjectManager(Agent):
    def __init__(self):
        super().__init__(
            name="Project Manager",
            description="Handles project execution and manages the project database.",
            instructions="./instructions.md",
            tools=[ProjectDatabaseTool]
        )
