"""
House Robber 
"""

""" 
# Qn is the same in algo Expert

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

# O(n) Time and O(1) Space
-----------------------------
def maxSubsetSumNoAdjacent(array):
	if not array: return 0
	if len(array) == 1: return array[0]
	
	f, s = array[0], max(array[0], array[1])
	res = max(f, s)
	for i in range(2, len(array)):
		res = max(s, f + array[i])
		f = s
		s = res
		
	return res
