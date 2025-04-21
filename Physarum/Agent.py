import random
from typing import List, Tuple
import numpy as np

class Agent:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.energy: int = 10  # Energie initiale

    def perceive(self, grid: np.ndarray) -> List[Tuple[Tuple[int, int], str]]:
        """
        Perçoit les 8 cellules voisines autour de l'agent.

        :param grid: Grille du monde (numpy array)
        :return: Liste de tuples ((x, y), contenu)
        """
        neighbors: List[Tuple[Tuple[int, int], str]] = []
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                neighbors.append(((nx, ny), grid[nx][ny]))
        return neighbors

    def choose_move(self, neighbors: List[Tuple[Tuple[int, int], str]]) -> Tuple[int, int]:

    # 5% de chance de mouvement aléatoire
        if random.random() < 0.05:
            random_neighbors = [pos for (pos, cell) in neighbors]
            if random_neighbors:
                return random.choice(random_neighbors)
            else:
                return (self.x, self.y)

    # Comportement normal
        food_cells: List[Tuple[int, int]] = []
        pheromone_cells: List[Tuple[int, int]] = []
        empty_cells: List[Tuple[int, int]] = []

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


    def move(self, new_position: Tuple[int, int]) -> None:
        """
        Déplace l'agent à une nouvelle position.

        :param new_position: Coordonnées (x, y)
        """
        self.x, self.y = new_position

    def deposit_pheromone(self, grid: np.ndarray) -> None:
        """
        Dépose une phéromone à la position actuelle si possible.

        :param grid: Grille du monde
        """
        if grid[self.x][self.y] == 'empty':
            grid[self.x][self.y] = 'pheromone'
