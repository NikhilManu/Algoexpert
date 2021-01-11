"""
Not Found Currently
"""
"""
Write a function that take in a "special" array and returns its product sum.

A "special" array is a non-empty array that contains either  integers other special array. The product sum of "special" array
is the sum of its elements, where "special" array insider it are summed themselves and multiplied by their depth

--->  [x,y] --> x + y
--->  [x, [y,z]] ---> x + 2 * (y + z)
--->  [x, [y, [z]]] ----> x + 2 *(y + 3z)
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

