def parenthetical_possibilities(s):
    pass  # todo
    if len(s) == 0:
        return [""]

    all_poss = []
    choices, remainder = get_choices(s)
    for choice in choices:
        remainder_possibilities = parenthetical_possibilities(remainder)
        for possibility in remainder_possibilities:
            all_poss.append(choice + possibility)
    return all_poss


# helper function.
# important to separate parsing logic from the recursion. for clarity
def get_choices(s):
    if s[0] == "(":
        end = s.index(")")
        choices = s[1:end]
        remainder = s[end + 1 :]
        return (choices, remainder)
    else:
        return (s[0], s[1:])


# parenthetical_possibilities('x(mn)yz') # ->
# [ 'xmyz', 'xnyz' ]

#    x
#   /\
#  m  n
