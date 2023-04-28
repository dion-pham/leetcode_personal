# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


def linked_list_cycle(head):
    pass  # todo

    #   current = head
    #   hash = {}

    #   while current:
    #     if current.val not in hash:
    #       hash[current.val] = 1
    #     else:
    #       return True
    #     current = current.next
    #   return False

    current = head
    set_check = set()

    while current:
        if current in set_check:
            return True
        set_check.add(current)
        current = current.next
    return False
