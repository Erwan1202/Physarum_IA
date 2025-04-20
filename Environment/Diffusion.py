import numpy as np
from config import PHEROMONE_DIFFUSION_RATE, PHEROMONE_EVAPORATION_RATE

def diffuse_pheromones(grid):
    # Copie temporaire de la grille pour éviter les influences simultanées
    temp_grid = np.copy(grid)

    rows, cols = grid.shape

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            # Moyenne des voisins immédiats (haut, bas, gauche, droite)
            neighbor_mean = (
                temp_grid[x-1, y] +
                temp_grid[x+1, y] +
                temp_grid[x, y-1] +
                temp_grid[x, y+1]
            ) / 4.0

            # Applique la diffusion selon le taux défini
            grid[x, y] += PHEROMONE_DIFFUSION_RATE * (neighbor_mean - grid[x, y])

    # Évaporation des phéromones
    grid *= PHEROMONE_EVAPORATION_RATE

    return grid
