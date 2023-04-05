def prereqs_possible(num_courses, prereqs):
    pass  # todo
    # same as the last prereq problem...
    # directed path
    # use cycle detection -> if a cycle is present, then there is no way that you can take all of the courses
    graph = build_graph(num_courses, prereqs)

    #   2) start cycle detection
    visiting = set()
    visited = set()

    for node in graph:
        if has_cycle(graph, node, visiting, visited) == True:
            return False

    return True


# 3) cycle detection helper function
def has_cycle(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)
    for neighbor in graph[node]:
        if has_cycle(graph, neighbor, visiting, visited) == True:
            return True

    visiting.remove(node)
    visited.add(node)  # adding to visited set in order to avoid any extra traversals

    return False


#   1) convert edgelist into adjacency list
def build_graph(num_courses, prereqs):
    graph = {}

    for i in range(num_courses):
        graph[i] = []

    for prereq in prereqs:
        course_a, course_b = prereq
        graph[course_a].append(course_b)

    return graph


numCourses = 6
prereqs = [
    (0, 1),
    (2, 3),
    (0, 2),
    (1, 3),
    (4, 5),
]
prereqs_possible(numCourses, prereqs)  # -> True
