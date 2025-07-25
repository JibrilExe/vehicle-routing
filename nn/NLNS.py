from data_representation import read_dimacs
from destroy import destroy_random_point
from greedy import greedy_start

import matplotlib.pyplot as plt

def plot_routes(coords, routes):
    plt.figure(figsize=(10, 10))
    
    # Plot all nodes
    for idx, (x, y) in enumerate(coords):
        plt.scatter(x, y, c='blue')
        plt.text(x, y, str(idx), fontsize=9)

    # Plot routes
    for route in routes:
        route_coords = coords
        xs, ys = zip(*route_coords)
        plt.plot(xs, ys, marker='o')
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Vehicle Routes')
    plt.grid(True)
    plt.show()

def main():
    """
    Applies NLNS to find solution to CVRP
    """
    (smallest_x, biggest_x, smallest_y, biggest_y, coords, dist_matrix, caps, capacity, depot) = read_dimacs("/home/cedric/Desktop/vehicle-bvvt/nn/first.vrp.txt")

    routes = []
    routes, node_to_route = greedy_start(depot, dist_matrix, caps, capacity)

    destroy_random_point(smallest_x, biggest_x, smallest_y, biggest_y, node_to_route, routes, coords, 5)
    
    


if __name__ == "__main__":
    main()
