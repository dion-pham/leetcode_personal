def has_cycle(graph):
    pass  # todo
    # we are given the adjacency list
    # goal is to determine if the graph contains a cycle.
    #   how to do this??

    # white-grey-black algorithm: deals with cycle detection
    # using 3 colors (sets)
    # white: unexplored
    # grey: visiting
    # black: visited
    # DFS?: think possible recursion
    # in this algo, the only way to traverse back to an in progress(grey) node is if that part of the graph is cyclic
    visiting = set()
    visited = set()

    for node in graph:
        if cycle_detect(graph, node, visiting, visited) == True:
            return True

    return False


def cycle_detect(graph, node, visiting, visited):
    if node in visited:
        #     black
        return False
    if node in visiting:
        #     grey
        return True

    visiting.add(node)
    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited) == True:
            return True

    visiting.remove(node)
    visited.add(node)

    return False
