from collections import deque

# deque allows for O(1) addition or removal from structure


def shortest_path(edges, node_A, node_B):
    pass  # todo
    # edges = number of nodes - 1
    graph = build_graph(edges)

    visited = set([node_A])

    queue = deque([(node_A, 0)])

    while queue:
        node, distance = queue.popleft()

        if node == node_B:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1


# convert edge list into adjacency list
def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]

# print(build_graph(edges))
# {'w': ['x', 'v'], 'x': ['w', 'y'], 'y': ['x', 'z'], 'z': ['y', 'v'], 'v': ['z', 'w']}

# shortest_path(edges, 'w', 'z') # -> 2
