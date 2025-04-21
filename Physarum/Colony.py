# /Physarum/Colony.py

import random
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
            x = random.randint(0, self.grid.width - 1)
            y = random.randint(0, self.grid.height - 1)
            agent = Agent(self.grid, x, y)
            self.agents.append(agent)

    def add_agent(self, position, mutation_rate=0.05):
        x, y = position
        # Créer un nouvel agent à une position donnée
        new_agent = Agent(self.grid, x, y)

        # Appliquer une mutation légère sur ses caractéristiques
        new_agent.mutation(mutation_rate)
        
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
                # Division imparfaite : trouver une cellule voisine disponible
                new_position = self.get_random_neighbor(agent.position)

                if new_position:
                    new_agents.append(new_position)

                    # Division asymétrique de l'énergie
                    child_energy = agent.energy * 0.4
                    agent.energy *= 0.6

        # Supprimer les agents morts
        for agent in agents_to_remove:
            self.remove_agent(agent)

        # Ajouter les nouveaux agents
        for position in new_agents:
            self.add_agent(position)

    def get_random_neighbor(self, position):
        """Retourne une position voisine aléatoire disponible autour de la position donnée"""
        x, y = position
        neighbors = [
            (x-1, y), (x+1, y),
            (x, y-1), (x, y+1),
            (x-1, y-1), (x+1, y+1),
            (x-1, y+1), (x+1, y-1)
        ]
        random.shuffle(neighbors)  # Choisir au hasard

        for nx, ny in neighbors:
            if self.grid.is_valid_position((nx, ny)) and self.grid.is_empty((nx, ny)):
                return (nx, ny)
        return None
