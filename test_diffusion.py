
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Environment.Diffusion import diffuse_pheromones
from Environment.Grid import Grid

# Paramètres du test
grid_size = 20
initial_pheromone_value = 100
num_iterations = 50  # nombre total d'itérations à visualiser

# Initialisation de la grille
grid = Grid(grid_size, grid_size)
grid.cells = np.zeros((grid_size, grid_size))
grid.cells[grid_size // 2, grid_size // 2] = initial_pheromone_value

# Création de la figure
fig, ax = plt.subplots()
cax = ax.matshow(grid.cells, cmap='hot', interpolation='nearest')
fig.colorbar(cax)

# Fonction d'animation
def update(frame):
    global grid
    grid.cells = diffuse_pheromones(grid.cells)
    cax.set_data(grid.cells)
    ax.set_title(f'Diffusion - Étape {frame + 1}')
    return [cax]

ani = animation.FuncAnimation(fig, update, frames=num_iterations, interval=200, repeat=False)
plt.show()

