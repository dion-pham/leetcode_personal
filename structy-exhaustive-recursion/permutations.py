def permutations(items):
    pass  # todo
    if len(items) == 0:
        return [[]]

    first = items[0]
    items_wo_first = permutations(items[1:])
    #   assume you get back correct data from your recursive call

    items_w_first = []

    for item in items_wo_first:
        for i in range(len(item) + 1):
            items_w_first.append(item[:i] + [first] + item[i:])
    #       item[:i] + [first] + item[i:] will insert the first element into
    #       index i of that element

    return items_w_first
