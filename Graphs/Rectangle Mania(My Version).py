"""
"""
"""
This Solution is Similar to Solution 3, can be more understandable than solution 3 sometimes
"""

def rectangleMania(coords):
	coordSet = createCoordSet(coords)
	rect = 0
	for firstIdx in range(len(coords)):
		x1, y1 = coords[firstIdx]
		for secondIdx in range(firstIdx, len(coords)):
			x2, y2 = coords[secondIdx]
			hasSamePoint = x1 == x2 or y1 == y2

			if hasSamePoint:
				continue

			point3 = tuple((x1, y2)) in coordSet
			point4 = tuple((x2, y1)) in coordSet

			if point3 and point4:
				rect += 1

		coordSet.remove((x1,y1))
	return rect

def createCoordSet(coords):
	coordSet = set()
	for coord in coords:
		coordSet.add(tuple(coord))

	return coordSet 
