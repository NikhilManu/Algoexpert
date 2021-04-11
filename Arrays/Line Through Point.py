"""
Max Points on a Line
"""

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

"""

#Solution 
# Time - O(N ^ 2) | Space - O(N)
------------------------------
def lineThroughPoints(points):
	if len(points) <= 2:
		return len(points)
	maxCount = 2
	for i in range(len(points) - 1):
		x1, y1 = points[i]
		slopes = {}
		for j in range(i + 1, len(points)):
			x2, y2 = points[j]
			dx, dy = (x1 - x2), (y1 - y2)
			
			slope = findSlope(dx, dy)
				
			if slope not in slopes:
				slopes[slope] = 2
			else:
				slopes[slope] += 1
		maxCount = max(maxCount, max(slopes.values()))
		
	return maxCount
		
def findSlope(dx, dy):
	return 'vert' if dx == 0 else dy/dx
