def max_chocolates(jars):
    n = len(jars)
    if n == 0:
        return 0
    if n == 1:
        return jars[0]

    # Initialize two variables to keep track of maximum chocolates picked
    # when the last jar is picked or not picked
    max_with_last = jars[0]
    max_without_last = 0

    for i in range(1, n):
        # If the current jar is picked, add its chocolates to the maximum picked
        # when the last jar was not picked, and update the variables accordingly
        new_max_with_last = max_without_last + jars[i]
        new_max_without_last = max(max_with_last, max_without_last)
        print(new_max_with_last,'new max with last')
        print(new_max_without_last,'new max without last')

        # Update the variables for the next iteration
        max_with_last = new_max_with_last
        max_without_last = new_max_without_last
        print(max_with_last,'max with last')
        print(max_without_last,'max without last')
        print(i, 'i')

    # Return the maximum of the two variables
    return max(max_with_last, max_without_last)

print(max_chocolates([5,30,99,60,5,10]))
