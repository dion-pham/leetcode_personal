def decompress_braces(string):
    pass  # todo
    stack = []
    numbers = "123456789"
    for char in string:
        if char in numbers:
            stack.append(int(char))
        else:
            if char == "}":
                #       do something by popping and multiplying by that number
                string_formed = ""
                while not isinstance(stack[-1], int):

                    popped = stack.pop()
                    string_formed = popped + string_formed
                number = stack.pop()
                stack.append(string_formed * number)
            elif char != "{":
                stack.append(char)

    return "".join(stack)
