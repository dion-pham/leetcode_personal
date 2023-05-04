def tolerant_teams(rivalries):
    pass  # todo
    # given an edge list
    # turn into adjacency list

    graph = build_graph(rivalries)
    print(graph)
    coloring = {}
    for node in graph:
        if node not in coloring and is_bipartite(graph, node, coloring, False) == False:
            return False

    return True


def is_bipartite(graph, node, coloring, current_color):
    if node in coloring:
        return coloring[node] == current_color

    coloring[node] = current_color

    for neighbor in graph[node]:
        if is_bipartite(graph, neighbor, coloring, not current_color) == False:
            return False

    return True


def build_graph(edges):
    graph = {}
    #   basically building an adjacency list!!
    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


print(
    tolerant_teams(
        [("philip", "seb"), ("raj", "nader"), ("raj", "philip"), ("seb", "raj")]
    )
)  # -> False
