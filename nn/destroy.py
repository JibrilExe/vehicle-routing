import random
import math
import time

def eucl_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def destroy_random_point(smallest_x, biggest_x, smallest_y, biggest_y, node_to_route, routes, coords, to_delete):
    """
    Generates a random point and destroys 
    the to_delete nearest nodes their routes
    by splitting on the nodes.
    """
    x = random.randint(smallest_x, biggest_x)
    y = random.randint(smallest_y, biggest_y)
    start_time = time.time()

    distances = [(i, eucl_dist(x, y, coord[0], coord[1])) for i, coord in enumerate(coords)]
    distances.sort(key=lambda item: item[1])

    smallest = [distances[i][0] for i in range(to_delete)] # first we find the nearest nodes

    for s in smallest: # for each nearest node
        route_id = node_to_route[s]
        route = routes.pop(route_id) # remove the original route
        for i in range(route_id, len(routes)):
            for r in routes[i]:
                node_to_route[r] = i # update the mapping for all nodes that shifted
        index = route.index(s)
        before_s = route[:index]
        only_s = [route[index]]
        after_s = route[index + 1:] # split in 3 parts
        if len(before_s) > 1:
            routes.append(before_s) # only if it contains more than only the depot
            for r in before_s:
                node_to_route[r] = len(routes) - 1
        if len(after_s) > 1:
            routes.append(after_s)
            for r in after_s:
                node_to_route[r] = len(routes) - 1
        node_to_route[s] = len(routes)
        routes.append(only_s)

    print("Destroy time: ", time.time() - start_time)

    return routes
