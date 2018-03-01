from class import Vehicule, Rides,

step = 0

def create_grid(rows, cols):
    grid = []
    for i in range(0, cols):
        grid.append(list());
        for n in range(0, rows):
            grid[n].append(0);
    return (grid)
