
import numpy as np
import matplotlib.pyplot as plt
from Environment.Diffusion import diffuse_pheromones
from Environment.Grid import Grid

# Paramètres du test
grid_size = 20
initial_pheromone_value = 100

# Initialisation de la grille
grid = Grid(grid_size, grid_size)
grid.cells = np.zeros((grid_size, grid_size))

# Concentration initiale au centre
grid.cells[grid_size // 2, grid_size // 2] = initial_pheromone_value

# Affichage initial
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Avant diffusion")
plt.imshow(grid.cells, cmap='hot', interpolation='nearest')

# Première diffusion
grid.cells = diffuse_pheromones(grid.cells)
plt.subplot(1, 3, 2)
plt.title("Après 1 diffusion")
plt.imshow(grid.cells, cmap='hot', interpolation='nearest')

# Deuxième diffusion
grid.cells = diffuse_pheromones(grid.cells)
plt.subplot(1, 3, 3)
plt.title("Après 2 diffusions")
plt.imshow(grid.cells, cmap='hot', interpolation='nearest')

plt.show()
