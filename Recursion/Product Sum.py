"""
Not Found Currently
"""
"""
"""

# time O(N) | Space O(d)
-------------------------------
def productSum(arr,depth = 1):
	prod = 0
	for i in arr:
		if type(i) is list:
			prod += depth * productSum(i, depth + 1)
		else:
			prod += depth * i
	return prod
			
