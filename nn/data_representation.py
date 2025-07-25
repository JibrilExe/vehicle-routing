import sys

def read_dimacs(file: str):
    """
    Helper to read DIMACS VRP file format
    """
    dist_matrix = []
    caps = []
    coords = []
    smallest_x = pow(2,16)
    smallest_y = pow(2,16)
    biggest_x = 0
    biggest_y = 0
    depot_id = 0
    capacity = 0
    with open(file, 'r') as f:
        lines = f.readlines()
        edge_weight_section = False
        edge_coords = False
        edge_cap = False
        depot = False
        for line in lines:
            if line.startswith("CAPACITY"):
                capacity = int(line.split()[2])
                continue
            if line.startswith("EDGE_WEIGHT_SECTION"):
                edge_weight_section = True
                continue
            if line.startswith("NODE_COORD_SECTION"):
                edge_coords = True
                edge_weight_section = False
                continue
            if line.startswith("DEMAND_SECTION"):
                edge_cap = True
                edge_coords = False
                continue
            if line.startswith("DEPOT_SECTION"):
                depot = True
                edge_cap = False
                continue
            if depot:
                depot_id = int(line) - 1
                depot = False
            if edge_cap:
                caps.append(int(line.split()[1]))
            if edge_weight_section:
                if line.strip() == "EOF":
                    break
                dist_matrix.append(list(map(int, line.split())))
            if edge_coords:
                coordx, coordy = map(int, line.split()[1:])
                if coordx < smallest_x:
                    smallest_x = coordx
                elif coordx > biggest_x:
                    biggest_x = coordx
                if coordy < smallest_y:
                    smallest_y = coordy
                elif coordy > biggest_y:
                    biggest_y = coordy
                coords.append((coordx, coordy))
                continue

    return (smallest_x, biggest_x, smallest_y, biggest_y, coords, dist_matrix, caps, capacity, depot_id)

if __name__ == "__main__":
    read_dimacs("/home/cedric/Desktop/vehicle-bvvt/nn/first.vrp.txt")