class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowest_common_ancestor(root, val1, val2):
    pass  # todo
    path1 = get_paths(root, val1)
    path2 = get_paths(root, val2)

    set2 = set(path2)
    print(path1)
    print(path2)
    print(set2)

    for node in path1:
        if node in set2:
            return node


#   path G: [G,E,B,A]
#   path D: [D,B,A]


# helper function to get the paths from root to val1 and val2
def get_paths(root, target_val):
    if root is None:
        return None

    if root.val == target_val:
        return [root.val]

    # final_list = []
    # these recursive calls should produce an array
    left_path = get_paths(root.left, target_val)
    if left_path is not None:
        left_path.append(root.val)
        return left_path
    # recursion would append node values from the bottom up

    right_path = get_paths(root.right, target_val)
    if right_path is not None:
        right_path.append(root.val)
        return right_path
    # recursion would append node values from the bottom up

    return None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

lowest_common_ancestor(a, "d", "h")  # b
