"""
"""
# O(2 ^ N) Time and O(N) Space
------------------------
def getNthFib(num):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)
    
# O(N) Space and Time
--------------------
def getNthfib(num, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    
    memoize[n] = getNthfib(n-1, memoize) + getNthfib(n-2, memoize)
    return memoize[n]

# O(N) Time and O(1) Space
----------------------
def getNthfib(num):
    lastTwo = [0,1]
    counter = 3
    while counter <= n:
        next = sum(lastTwo)
        lastTwo[0], lastTwo[1] = lastTwo[1], next
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

    
