def paired_parentheses(string):
  pass # todo

# if string has (, do recursion/or add to call stack to find the missing half

  count = 0
  for char in string:
    if char == '(':
      count += 1
    elif char == ')':
      if count == 0:
        return False
      count -= 1

  return count == 0
