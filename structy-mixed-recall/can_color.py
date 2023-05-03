def can_color(graph):
    pass  # todo
    # every other node can be the same color
    # adjacent nodes CANNOT be the same color adjacent

    # iterate through the adjaceny list
    # use hash map??
    coloring = {}
    for node in graph:
        if node not in coloring and validate(graph, node, coloring, False) == False:
            return False

    return True


def validate(graph, node, coloring, current_color):
    if node in coloring:
        return current_color == coloring[node]

    coloring[node] = current_color

    for neighbor in graph[node]:
        if validate(graph, neighbor, coloring, not current_color) == False:
            return False

    return True
