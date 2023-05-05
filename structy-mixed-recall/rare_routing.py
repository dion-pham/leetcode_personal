def rare_routing(n, roads):
    graph = build_graph(n, roads)
    visited = set()
    valid = validate(graph, 0, visited, None)
    return valid and len(visited) == n


# given edge list
# turn into undirected graph with nodes, represented by an adjacency list

# 0 --- 1
# | \
# |  \
# |   \
# 2 -- 3

# There are two routes that can be used to travel from city 1 to city 2:
# - first route:  1, 0, 2
# - second route: 1, 0, 3, 2
# The answer is False, because routes should be unique.

# can consider this the same problem as a coloring problem


def validate(graph, node, visited, last_node):
    if node in visited:
        return False

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor != last_node and validate(graph, neighbor, visited, node) == False:
            return False

    return True


def build_graph(n, roads):
    graph = {}

    for city in range(n):
        graph[city] = []

    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)
    return graph


print(rare_routing(4, [(0, 1), (0, 2), (0, 3)]))  # -> True
