# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def flip_tree(root):
  pass # todo
# if node.left, make it equal node.right and vice-versa
# return root of the tree at the end

  if root is None:
    return None

  left = flip_tree(root.left)
  right = flip_tree(root.right)
  root.right = left
  root.left = right
  # this works because you are returning that individual root back up the call stack
  return root
