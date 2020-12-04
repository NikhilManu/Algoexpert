"""

"""
"""
Given list of co ordinates, Find the number of rectangle which can be formed by the given list of coordinates

"""

# Solution
# Time O(N^2) | Space O(N^2)
-------------------------------
# Hard Code
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def RectangleMania(coords):
    coordTable = getcoordTable(coords)
    return getRectangleCount(coords, coordTable)

def getRectangleCount(coords, coordTable):
    rectangleCount = 0
    for coord in coords:
        rectangleCount += clockwiseCountRectangle(coord, coordTable, UP, coord)
    return rectangleCount

def clockwiseCountRectangle(coord, coordTable, direction, origin):
    coordString = coordtoString(coord)
    if direction == LEFT:
        rectangleFound = origin in coordTable[coordString][direction]
        return 1 if rectangleFound else 0
    else:
        rectangleCount = 0
        nextDirection = getnextDirection(direction)
        for nextcoord in coordTable[coordString][direction]:
            rectangleCount += clockwiseCountRectangle(nextcoord, coordTable, nextDirection, coord)
    return rectangleCount 

def getnextDirection(direction):
    if direction == UP:
        return RIGHT
    if direction == RIGHT:
        return DOWN
    if direction == DOWN:
        return LEFT
    return ""

def getcoordTable(coords):
    coordTable = {}
    for coord1 in coords:
        coord1Direction = { UP: [], LEFT: [], RIGHT: [], DOWN: [] }
        for coord2 in coords:
            direction = getDirection(coord1, coord2)
            if direction in coordDirection:
                coord1Direction[direction].append(coord2)
        coord1String = coordtoString(coord1)
        coordTable[coord1String] = coord1Direction
        
    return coordTable

def coordtoString(coord):
    x,y = coord
    return str(x) + '-' + str(y)

def getDirection(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    if y1 == y2:
        if x1 < x2:
            return RIGHT
        elif x1 > x2:
            return LEFT
     elif x1 == x2:
        if y1 < y2:
            return UP
        elif y1 > y2:
            return DOWN
        
    return ''
    
  
