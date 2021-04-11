"""
Smallest Non - Constructible Value
"""

"""
Given an array of positive integers (representing coins), find the smallest value that cannot be constructed from those integers.

coins = [5, 7, 1, 1, 2, 3, 22]
Ans : 20
"""

# O(n log(n)) Time | O(1) Space
-----------------------------
def nonConstructibleChange(coins):
	coins.sort()
	
	minChange = 0
	for coin in coins:
		if coin > minChange + 1:
			break
		
		minChange += coin
		
		
	return minChange + 1
