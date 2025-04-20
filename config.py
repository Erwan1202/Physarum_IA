# config.py

# Taille de la grille
GRID_WIDTH = 100
GRID_HEIGHT = 100

# Nutriments
INITIAL_NUTRIENT_AMOUNT = 500

# Agents (Physarum)
INITIAL_AGENT_COUNT = 50

# Phéromones
PHEROMONE_DIFFUSION_RATE = 0.2
PHEROMONE_EVAPORATION_RATE = 0.01

# Autres paramètres possibles (en cas de besoin)
AGENT_ENERGY_GAIN_FROM_NUTRIENT = 10
AGENT_INITIAL_ENERGY = 20
AGENT_ENERGY_LOSS_PER_STEP = 1

# Exploration
EXPLORATION_RATE = 0.05  # 5% du temps, l'agent explore aléatoirement

# Visualisation
CELL_SIZE = 5  # en pixels pour pygame/matplotlib
FPS = 30  # images par seconde pour l'animation
