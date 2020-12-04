""" 
Given list of coordinates, Find the number rectangles which can be formed by those given coordinates
"""

# Solution --
# O(N^2) Time | O(N) Space
------------------
def RectangleMania(coords):
    coordsTable = getcoordsTable(coords)
    return getRectangleCount(coords, coordsTable)

def getcoordsTable(coords):
    coordTable = { 'x' : {}, 'y' : {} }
    for coord in coords:
        x,y = coord
        if x not in coordTable['x']:
            coordTable['x'][x] = []
        coordTable['x'][x].append(coord)
        
        if y not in coordTable['y']:
            coordTable['y'][y] = []
        coordTable['y'][y].append(coord)
        
    return coordTable

def getRectangleCount(coords, coordTable):
    rectangleCount = 0 
    for coord in coords:
        lowerleftY = coord[1]
        rectangleCount += clockwiseRectangleCount(coord, coordTable, UP, lowerleftY)
        
    return rectangleCount

def clockwiseRectangleCount(coord, coordTable, direction, lowerleftY):
    x1, y1 = coord
    if diretion == DOWN:
        relevantCoords = coordTable['x'][x1]
        for coord2 in relevantCoords:
            lowerRightY = coord2[1]
            if lowerRightY == lowerleftY:
                return 1
        return 0
    else:
        rectangleCount = 0
        if direction == UP:
            relevantCoords = coordTable['x'][x1]
            for coord2 in relevantCoords:
                x2, y2 = coord2
                isAbove = y2 > y1
                if isAbove:
                    rectangleCount += clockwiseRectangleCount(coord2, coordTable, RIGHT, lowerleftY)
        elif direction == RIGHT:
            relevantCoords = coordTable['y'][y1]
            for coord2 in relevantCoords:
                x2, y2 = coord2
                isRight = x2 > x1
                if isRight:
                    rectangleCount += clockwiseRectangleCount(coord2, coordTable, DOWN, lowerleftY)
                    
    return rectangleCount


DOWN = 'down'
RIGHT = 'right'
UP = 'up'
                    
            
        
        
        
        
        
