def largest_component(graph):
    pass  # todo
    #   iterate through the adjacency list
    # add your visited to a visited set
    # keep a track of how many visited with a count
    # will need a temp count variable that will be compared to the global max count variable
    visited = set()
    max_count = 0

    for node in graph:
        size = counter(graph, node, visited)
        if size > max_count:
            max_count = size

    return max_count


def counter(graph, current, visited):
    # component_count = 0
    if current in visited:
        return 0

    visited.add(current)

    component_count = 1

    for neighbor in graph[current]:
        component_count += counter(graph, neighbor, visited)

    return component_count


print(
    largest_component(
        {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}
    )
)  # -> 4)
