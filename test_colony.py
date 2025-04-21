# test_colony.py

from Physarum.Colony import Colony
import Physarum.Agent
Physarum.Agent.Agent = FakeAgent

class FakeGrid:
    def __init__(self):
        self.width = 10
        self.height = 10

    def is_valid_position(self, pos):
        return True

    def is_empty(self, pos):
        return True


class FakeAgent:
    def __init__(self, grid, position=(0,0), energy=5):
        self.grid = grid
        self.position = position
        self.energy = energy

    def update(self):
        pass  # Ne fait rien pour ce test (pas de déplacement)

    def mutation(self, rate):
        pass  # Pas besoin pour ce test




def test_colony_behavior():
    grid = FakeGrid()
    colony = Colony(grid, num_agents=3, energy_to_divide=10, energy_to_die=1)

    # On donne des énergies différentes pour simuler des comportements
    colony.agents[0].energy = 12  # Doit se diviser
    colony.agents[1].energy = 0   # Doit mourir
    colony.agents[2].energy = 5   # Reste normal

    print(f"Avant update: {len(colony.agents)} agents")
    colony.update()
    print(f"Après update: {len(colony.agents)} agents")

if __name__ == "__main__":
    test_colony_behavior()
