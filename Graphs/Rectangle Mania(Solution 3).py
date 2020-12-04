""" 
Given list of coordinates, Find the number rectangles which can be formed by those given coordinates
"""

# Solution --
# O(N^2) Time | O(N) Space
------------------
def RectangleMania(coords):
    coordsTable = getCoordsTable(coords)
    return getRectangleCount(coords, coordsTable)

def getCoordsTable(coords):
    coordTable = {}
    for coord in coords:
        coord = tuple(coord)
        coordTable[coord] = True
    return coordTable

def getRectangleCount(coords, coordTable):
    rectangleCount = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if not isUpperRight([x1, y1], [x2, y2]):
                continue
            
            upperLeft = tuple([x1, y2])
            bottomRight = tuple([x2, y1])
            
            if upperLeft in coordTable and bottomRight in coordTable:
                rectangleCount += 1
                
    return rectangleCount

def isUpperRight(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    
    return x2 > x1 and y2 > y1
    
    
    
