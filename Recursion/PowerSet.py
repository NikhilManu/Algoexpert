"""
Subsets --> Name of this Qn in LeetCode
"""
"""
"""
# 
----------------
def powerset(array):
	subsets = [[]]
	for num in array:
		for i in range(len(subsets)):
			curSub = subsets[i]
			subsets.append(curSub + [num])
	return subsets
