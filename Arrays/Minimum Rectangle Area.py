"""
Minimum Area Rectangle [ Name in LeetCode ]
"""

"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0. 

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

"""
def minimumAreaRectangle(points):
    minArea = float('inf')
    pointSet = createPointSet(points)

    for i in range(len(points)):
        x2,y2 = points[i]
        for prev in range(i):
            x1,y1 = points[prev]
            hasSamePoint = x1 == x2 or y1 == y2

            if hasSamePoint:
                continue

            point3 = tuple((x1, y2)) in pointSet
            point4 = tuple((x2, y1)) in pointSet

            if point3 and point4:
                curArea = abs(x1 - x2) * abs(y1 - y2)
                minArea = min(minArea, curArea)

    return 0 if minArea == float('inf') else minArea

def createPointSet(points):
    pointSet = set()
    for point in points:
        pointSet.add(tuple(point))

    return pointSet
