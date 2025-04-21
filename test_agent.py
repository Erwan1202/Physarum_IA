import numpy as np
from Physarum.Agent import Agent  # à adapter selon ton projet

def create_test_grid():
    grid = np.full((5, 5), 'empty', dtype=object)
    grid[2][3] = 'food'  # placer de la nourriture pas loin
    return grid

def print_grid(grid, agent):
    display_grid = grid.copy()
    display_grid[agent.x][agent.y] = 'A'  # Marquer l'agent
    for row in display_grid:
        print(' '.join(row))
    print()

def run_test():
    grid = create_test_grid()
    agent = Agent(2, 2)  # Position initiale au centre
    
    print("Grille initiale :")
    print_grid(grid, agent)

    for step in range(5):
        neighbors = agent.perceive(grid)
        new_position = agent.choose_move(neighbors)
        agent.move(new_position)
        agent.deposit_pheromone(grid)
        
        print(f"Après étape {step+1}:")
        print_grid(grid, agent)

if __name__ == "__main__":
    run_test()
