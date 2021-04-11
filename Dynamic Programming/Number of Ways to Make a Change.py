"""
Coin Change 2
"""

"""
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

""""
def numberOfWaysToMakeChange(n, denoms):
	ways = [0] * (n + 1)
	ways[0] = 1 # There is Exactly one way to make 0 Rs 
	for coin in denoms:
		for i in range(1, n + 1):
			if i - coin >= 0:
				ways[i] += ways[i - coin]
	return ways[n]
