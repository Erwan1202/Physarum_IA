import numpy as np

# Constants for cell types
EMPTY = 0
FOOD = 1
OBSTACLE = 2


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Grille pour les types de cellules
        self.cells = np.full((height, width), EMPTY)
        # Grille pour les niveaux de phéromones
        self.pheromones = np.zeros((height, width))

    def set_food(self, x, y):
        if self.is_valid_position(x, y):
            self.cells[y, x] = FOOD

    def set_obstacle(self, x, y):
        if self.is_valid_position(x, y):
            self.cells[y, x] = OBSTACLE

    def add_pheromone(self, x, y, amount):
        if self.is_valid_position(x, y):
            self.pheromones[y, x] += amount

    def get_cell_type(self, x, y):
        if self.is_valid_position(x, y):
            return self.cells[y, x]
        return None

    def get_pheromone_level(self, x, y):
        if self.is_valid_position(x, y):
            return self.pheromones[y, x]
        return None

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def reset_pheromones(self):
        self.pheromones.fill(0)
