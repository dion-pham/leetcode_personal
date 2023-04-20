def subsets(elements):
    pass  # todo
    # include an index in the parameters
    # starting stack is [[]]
    if len(elements) == 0:
        return [[]]

    first = elements[0]
    subs_wo_first = subsets(elements[1:])

    subs_w_first = []
    for sub in subs_wo_first:
        subs_w_first.append([first, *sub])

    return subs_w_first + subs_wo_first
