import numpy as np
import matplotlib.pyplot as plt
from Physarum.Agent import Agent  # adapte le chemin selon ton projet !

def create_test_grid() -> np.ndarray:
    grid = np.full((20, 20), 'empty', dtype=object)
    grid[5][5] = 'food'
    grid[15][15] = 'food'
    grid[10][10] = 'food'
    return grid

def grid_to_colors(grid: np.ndarray, agents: list[Agent]) -> np.ndarray:
    color_grid = np.ones((grid.shape[0], grid.shape[1], 3))  # tout blanc au départ

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 'food':
                color_grid[i, j] = [0, 1, 0]  # vert pour nourriture
            elif grid[i, j] == 'pheromone':
                color_grid[i, j] = [1, 0, 1]  # rose pour phéromones

    for agent in agents:
        color_grid[agent.x, agent.y] = [0, 0, 1]  # bleu pour agents

    return color_grid

def run_simulation():
    grid = create_test_grid()

    # ➔ Créer plusieurs agents
    agents = [
        Agent(0, 0),
        Agent(0, 19),
        Agent(19, 0),
        Agent(19, 19)
    ]

    plt.ion()
    fig, ax = plt.subplots()

    for step in range(100):
        agents_to_remove = []

        for agent in agents:
            neighbors = agent.perceive(grid)
            new_position = agent.choose_move(neighbors)
            agent.move(new_position, grid)
            agent.deposit_pheromone(grid)

            agent.energy -= 1  # Perte d'énergie à chaque déplacement

            if agent.energy <= 0:
                agents_to_remove.append(agent)

    # Retirer les agents morts
        for dead_agent in agents_to_remove:
            agents.remove(dead_agent)

        ax.clear()
        ax.imshow(grid_to_colors(grid, agents))
        ax.set_title(f"Étape {step+1} - Agents vivants : {len(agents)}")
        ax.axis('off')
        plt.pause(0.2)

        if not agents:
            print("Tous les agents sont morts.")
            break

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    run_simulation()
