def greedy_start(depot, dists, caps, capacity):
    """
    Simple initial greedy start
    """
    num_customers = len(dists)
    visited = [False] * num_customers
    visited[depot] = True
    node_to_route = {}
    routes = []
    current_route = [depot]
    current_capacity = 0
    route_index = 0

    while not all(visited): # as long as not all visited
        last_node = current_route[-1]
        nearest_node = None
        nearest_dist = float('inf')

        for i in range(num_customers): # find the closest non visited node
            if not visited[i]:
                if last_node < i:
                    if dists[i][last_node] < nearest_dist:
                        nearest_node = i
                        nearest_dist = dists[i][last_node]
                elif dists[last_node][i] < nearest_dist:
                    nearest_node = i
                    nearest_dist = dists[last_node][i]

        if nearest_node is not None and current_capacity + caps[nearest_node] <= capacity:
            #print("found nearest next")
            current_route.append(nearest_node) # add to the current route
            current_capacity += caps[nearest_node]
            visited[nearest_node] = True
            node_to_route[nearest_node] = route_index
        else:
            #print("new route started")
            current_route.append(depot) # we exceed capacity, make a new route
            routes.append(current_route)
            current_route = [depot]
            current_capacity = 0
            route_index += 1

    if current_route != [depot]:
        current_route.append(depot) # close off last route with depot
        routes.append(current_route)

    return routes, node_to_route
