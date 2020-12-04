""" 
Given list of coordinates, Find the number rectangles which can be formed by those given coordinates
"""

# Solution --
# O(N^2) Time | O(N) Space
------------------
def RectangleMania(coords):
    coordsTable = getcoordsTable(coords)
    return getRectangleCount(coords, coordsTable)
