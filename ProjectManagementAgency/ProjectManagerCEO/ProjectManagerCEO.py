from agency_swarm import Agent

class ProjectManagerCEO(Agent):
    def __init__(self):
        super().__init__(
            name="Project Manager CEO",
            description="Manages high-level project strategies and communicates with stakeholders.",
            instructions="./instructions.md",
            tools=[]
        )
