"""
Interleaving Strings [ Name of this Qn in LeetCode]
"""
"""
Given strings s1, s2, and s3, find whether s3 is formed by an interweaving of s1 and s2.

An interweaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1

The interweaving  is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

"""

# Solution --> Optimal Solution in AlgoExpert, but doest pass on LeetCode
# O(m*n) Time And space
-------------------------------
def interweavingStrings(one, two, three):
	if len(one) + len(two) != len(three):
		return False
	dp = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]
	return isInterweaving(one, two, three, 0, 0, dp)
	
def isInterweaving(one, two, three, i, j, dp):
	if dp[i][j]:
		return dp[i][j]
	
	k = i + j
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		dp[i][j] =  isInterweaving(one, two, three, i+1, j, dp)
		if dp[i][j]:
			return True
		
	if j < len(two) and two[j] == three[k]:
		dp[i][j] = isInterweaving(one, two, three, i, j+1, dp)
		return dp[i][j]
	
	dp[i][j] = False
	return False


# Solution 2 ---> modification of Optimal Solution in AlgoExpert which passes in LeetCode
# O(m*n) Time and Space
-------------------------------------
def interweavingStrings(one, two, three):
	if len(one) + len(two) != len(three):
		return False
	dp = set()
	return isInterweaving(one, two, three, 0, 0, dp)
	
def isInterweaving(one, two, three, i, j, dp):
	k = i + j
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k] and (i+1, j) not in dp:
		dp.add((i+1, j))
		if isInterweaving(one, two, three, i+1, j, dp):
			return True
		
	if j < len(two) and two[j] == three[k] and (i, j+1) not in dp:
		dp.add((i, j+1))
		return isInterweaving(one, two, three, i, j+1, dp)
		
	return False
