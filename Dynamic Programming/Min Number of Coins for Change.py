"""
Coin Change
"""

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

def minNumberOfCoinsForChange(n, denoms):
	coins = [float('inf')] * (n + 1)
	coins[0] = 0
	for coin in denoms:
		for amt in range(1, n + 1):
			if amt - coin >= 0:
				coins[amt] = min(coins[amt], coins[amt - coin] + 1)
			
	return coins[n] if coins[n] != float('inf') else -1
