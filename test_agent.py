import numpy as np
import matplotlib.pyplot as plt
from Physarum.Agent import Agent  # à adapter selon ton projet

def create_test_grid():
    grid = np.full((10, 10), 'empty', dtype=object)
    grid[5][6] = 'food'  # placer de la nourriture pas loin
    return grid

def grid_to_colors(grid, agent):
    color_grid = np.zeros((grid.shape[0], grid.shape[1], 3))  # RGB

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if (i, j) == (agent.x, agent.y):
                color_grid[i, j] = [0, 0, 1]  # bleu pour agent
            elif grid[i, j] == 'food':
                color_grid[i, j] = [0, 1, 0]  # vert pour nourriture
            elif grid[i, j] == 'pheromone':
                color_grid[i, j] = [1, 0, 1]  # rose pour phéromone
            else:
                color_grid[i, j] = [1, 1, 1]  # blanc pour vide

    return color_grid

def run_test():
    grid = create_test_grid()
    agent = Agent(5, 5)

    plt.ion()  # Mode interactif ON
    fig, ax = plt.subplots()

    for step in range(30):
        neighbors = agent.perceive(grid)
        new_position = agent.choose_move(neighbors)
        agent.move(new_position)
        agent.deposit_pheromone(grid)

        ax.clear()
        ax.imshow(grid_to_colors(grid, agent))
        ax.set_title(f"Étape {step+1}")
        ax.axis('off')
        plt.pause(0.3)

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    run_test()
