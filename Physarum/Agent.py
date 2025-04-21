import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 10  # Energie initiale

    def perceive(self, grid):
        # Retourne une liste des voisins [(position, contenu), ...]
        neighbors = []
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                neighbors.append(((nx, ny), grid[nx][ny]))
        return neighbors

    def choose_move(self, neighbors):
        food_cells = []
        pheromone_cells = []
        empty_cells = []

        for (pos, cell) in neighbors:
            if cell == 'food':
                food_cells.append(pos)
            elif cell == 'pheromone':
                pheromone_cells.append(pos)
            elif cell == 'empty':
                empty_cells.append(pos)

        if food_cells:
            return random.choice(food_cells)
        elif pheromone_cells:
            return random.choice(pheromone_cells)
        elif empty_cells:
            return random.choice(empty_cells)
        else:
            return (self.x, self.y)

    def move(self, new_position):
        self.x, self.y = new_position

    def deposit_pheromone(self, grid):
        if grid[self.x][self.y] == 'empty':
            grid[self.x][self.y] = 'pheromone'
