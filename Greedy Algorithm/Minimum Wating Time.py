"""
"""

"""
Given list of which contains the duration of each Queries. Minimize the total waiting time and return the waiting time.
Waiting Time is time process is waiting before its execution..ie.. 

eg: [1, 8, 5]
waiting time of 5 is 1 + 8 = 9

"""
# Solution - Algoexpert
# O(n logn) Time | O(1) Space
----------------------------
def minimumWaitingTime(queries):
	queries.sort()
	wt = 0
	for i in range(len(queries)):
		todo = len(queries) - (i + 1)
		wt += queries[i] * todo
		
	return wt
  
  
# Solution - For better understanding
# O(n logn) Time | O(n) SPace
-----------------------------------
def minimumWaitingTime(queries):
	queries.sort()
	wt = [0] * len(queries)
	wt[0] = queries[0]
	for i in range(1, len(queries)):
		wt[i] = wt[i-1] + queries[i]
		
	return sum(wt[:-1])   # Sum of the array wt excluding the last element
