# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def lowest_common_ancestor(root, val1, val2):
    pass  # todo
    # traverse down the tree, keeping a track of how many edges you went down?
    #
    #   if root == val1 or root == val2:
    #     return #something

    # # expect to get a value from these recursive calls
    #   lowest_common_ancestor(root.left,val1,val2)
    #   lowest_common_ancestor(root.right,val1,val2)
    path1 = get_path(root, val1)
    path2 = get_path(root, val2)

    set2 = set(path2)
    for val in path1:
        if val in set2:
            return val


def get_path(root, target_val):
    if root is None:
        return None

    if root.val == target_val:
        return [root.val]

    left_path = get_path(root.left, target_val)
    if left_path is not None:
        left_path.append(root.val)
        return left_path

    right_path = get_path(root.right, target_val)
    if right_path is not None:
        right_path.append(root.val)
        return right_path

    return None
