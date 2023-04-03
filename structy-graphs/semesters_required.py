# def semesters_required(num_courses, prereqs):
#   pass # todo
# # graph problem: need to traverse in order from 0 to n-1
# # convert the "edge list" into adjacency list?
# # iterate through the edge list
# # think about it as a length of the longest path problem

#   graph = build_graph(num_courses,prereqs)

#   distance = {}
#   for course in graph:
#     if graph[course] == 0:
# #       equal to 1 because we are counting the number of "nodes" as opposed to "edges"
#       distance[course] = 1

#   for course in graph:
#     traverse_distance(graph,course,distance)

#   return max(distance.values())


# def traverse_distance(graph,node,distance):
#   if node in distance:
# #     returning distance value because we want this function to return the maximum distance
#     return distance[node]

#   max_distance = 0
#   for neighbor in graph[node]:
# #     recursive leap of faith: assume that you will get back a number that rep the longest path beginning at said neighbor
#     neighbor_distance = traverse_distance(graph,neighbor,distance)
#     if neighbor_distance > max_distance:
#       max_distance = neighbor_distance
# #   including the 1 because we are considering our node's distance from its NEIGHBOR
#   distance[node] = 1 + max_distance
#   return distance[node]


# def build_graph(num_courses,prereqs):
#   graph = {}

# #   try using len(range(num_courses))
#   for course in (range(0,num_courses)):
#   # for course in range(0, num_courses):
#     #     initialize graph with keys having empty list values
#     graph[course] = []

#   for prereq in prereqs:
#     a,b = prereq
#     graph[a].append(b)
# #     we're only appending one way because it a directed graph. no symmetric appending


#   return graph

# num_courses = 6
# prereqs = [
#   (1, 2),
#   (2, 4),
#   (3, 5),
#   (0, 5),
# ]
# semesters_required(num_courses, prereqs) # -> 3


def semesters_required(num_courses, prereqs):
    pass  # todo
    #   directed graph, also acyclic. cant be cyclic because there would be no way you can take all the courses
    # convert the edge list into an adjacency list
    # iterate through adjacency list, keeping track of neighbors through a distance hashmap (k=prereq #, v=distance from terminal node)
    # recursive call a helper function in order to determine the max length as you go from neighbor to neighbor, adding to the distance hashmap as you go
    graph = build_graph(num_courses, prereqs)
    #  {0: [5], 1: [2], 2: [4], 3: [5], 4: [], 5: []}

    distance = {}
    for course in graph:
        if len(graph[course]) == 0:
            #       if length is zero, that means we have a terminal course
            distance[course] = 1

    for course in graph:
        count_distance(graph, course, distance)
    #     this should return a numbered value, possibly from a value from the distance map

    return max(distance.values())


def count_distance(graph, node, distance):
    if node in distance:
        return distance[node]

    max_distance = 0
    for neighbor in graph[node]:
        neighbor_distance = count_distance(graph, neighbor, distance)
        if max_distance < neighbor_distance:
            max_distance = neighbor_distance

    distance[node] = 1 + max_distance
    return distance[node]


def build_graph(num_courses, prereqs):
    map = {}
    for course in range(num_courses):
        #     each course key will have an empty list to begin with
        map[course] = []

    for prereq in prereqs:
        a, b = prereq
        #     only appending one direction because it is directed
        map[a].append(b)

    return map
