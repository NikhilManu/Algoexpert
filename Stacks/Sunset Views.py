"""
"""

"""

"""

#Solution
# O(N) Time and space
-------------------------
def sunsetViews(buildings, direction):
	res = []
	strt = 0 if direction == "WEST" else len(buildings) - 1
	step = 1 if direction == "WEST" else -1
	idx = strt
	curMax = 0
	while idx >= 0 and idx < len(buildings):
		if buildings[idx] > curMax:
			res.append(idx)
		curMax = max(curMax, buildings[idx])
		
		idx += step
		
	return res if direction == "WEST" else res[::-1]
