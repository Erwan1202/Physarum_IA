# /Physarum/Colony.py

from Physarum.Agent import Agent

class Colony:
    def __init__(self, grid, num_agents, energy_to_divide=10, energy_to_die=0):
        self.grid = grid
        self.agents = []
        self.energy_to_divide = energy_to_divide
        self.energy_to_die = energy_to_die
        self.initialize_agents(num_agents)

    def initialize_agents(self, num_agents):
        for _ in range(num_agents):
            agent = Agent(self.grid)
            self.agents.append(agent)

    def add_agent(self, position):
        new_agent = Agent(self.grid, position)
        self.agents.append(new_agent)

    def remove_agent(self, agent):
        if agent in self.agents:
            self.agents.remove(agent)

    def update(self):
        new_agents = []
        agents_to_remove = []

        for agent in self.agents:
            agent.update()

            # Vérifier si l'agent doit mourir
            if agent.energy <= self.energy_to_die:
                agents_to_remove.append(agent)

            # Vérifier si l'agent peut se diviser
            elif agent.energy >= self.energy_to_divide:
                position = agent.position  # Position actuelle
                new_agents.append(position)  # On crée un nouvel agent au même endroit (ou proche)

                # Facultatif : réduire l'énergie de l'agent qui se divise
                agent.energy /= 2  

        # Supprimer les agents morts
        for agent in agents_to_remove:
            self.remove_agent(agent)

        # Ajouter les nouveaux agents
        for position in new_agents:
            self.add_agent(position)
