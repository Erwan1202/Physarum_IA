import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 10

    def perceive(self, grid):
        neighbors = []
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                neighbors.append(((nx, ny), grid[nx, ny]))
        return neighbors

    def choose_move(self, neighbors):
        food_cells = []
        pheromone_cells = []
        empty_cells = []

        for (pos, cell) in neighbors:
            if cell == 2:  # food
                food_cells.append(pos)
            elif cell > 0 and cell < 1:  # pheromone
                pheromone_cells.append(pos)
            elif cell == 0:  # empty
                empty_cells.append(pos)

        if food_cells:
            return random.choice(food_cells)
        elif pheromone_cells:
            return random.choice(pheromone_cells)
        elif empty_cells:
            return random.choice(empty_cells)
        else:
            return (self.x, self.y)

    def move(self, new_pos):
        self.x, self.y = new_pos

    def deposit_pheromone(self, grid):
        grid[self.x, self.y] = min(grid[self.x, self.y] + 0.1, 0.9)
