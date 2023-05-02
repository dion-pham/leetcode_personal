# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def lefty_nodes(root):
    pass  # todo
    # requires a depth first traversal of some kind
    # as you traverse down, keep track of the level you are at
    # if you are at a new level, append the first node you see to list
    # return that list

    values = []
    traverse(root, 0, values)
    return values


def traverse(root, level, values):
    if root is None:
        return None

    if len(values) == level:
        values.append(root.val)

    traverse(root.left, level + 1, values)
    traverse(root.right, level + 1, values)
