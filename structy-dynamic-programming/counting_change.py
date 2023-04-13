def counting_change(amount, coins):
  return _counting_change(amount,coins,0, {})

def _counting_change(amount, coins, i,memo):
  pass # todo

# recursion taking an amount subtracting a coin
#  4 -1 = 3
# base case: when amount = 0: return 1 . then sum up all the return values to see how many times you reached amount == 0

  memo_things = (amount,i)
  if memo_things in memo:
    return memo[memo_things]

  if amount == 0:
    return 1

  if i == len(coins):
    return 0

  coin = coins[i]

  total_ways = 0
#   for this problem, drawing out the recursion tree (this one special because levels of tree are denoted by individual coin at i) really helps
#   with the iteration
  for qty in range(0, (amount // coin) + 1 ):
#     (0-5)
#   remainders = (4,3,2,1,0)
    remainder = amount - (qty * coin)
    total_ways += _counting_change(remainder, coins, i + 1,memo)

  memo[memo_things] = total_ways
  return memo[memo_things]



# we are iterating and branching for each individual coin
