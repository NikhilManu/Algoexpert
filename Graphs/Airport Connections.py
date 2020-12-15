"""
Similar Qn - Cheapest Flights Within K Stops
"""

"""
Given a list of Aiports, a list of OneWay Route, and a starting Airport.
Write a Program to find minimum number of connection which make every aiport accesible from the starting Airport
"""

# Solution
# O( a * (a + r) + aloga ) Time | O(a + r)
--------------
def AirportConnections(airports, routes, start):
    airportGraph = getAirportGraph(airports, routes)
    unreachableAirportNodes = getunreachableAirportNodes(airportGraph, airports, start)
    markUnreachableAirportNodes(airportGraph, unreachableAirportNodes)
    retur getMinConnections(airportGraph, unreachableAirportNodes)
    
# Time O(a + r) and O(a + r) Space   
def getAirportGraph(airports, routes):
    airportGraph = {}
    for aiport in airports:
        airportGraph[airport] = AirportNode(airport)
        
    for route in routes:
        airport, connection = route
        airportGraph[airport].connections.append(connection)
    
    return airportGraph

# Time O(a + r) | Space O(a)
def getunreachableAirportNodes(airportGraph, airports, start):
    visited = {}
    dfsAirport(airportGraph, start, visited)
    unreachableAirportNodes = []
    for airport in airports:
        if airport in visited:
            continue
        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableAirportNode.append(airportNode)
    return unreachableAirportNodes

def dfsAirport(airportGraph, airport, vis):
    if airport in vis:
        return 
    vis[airport] = True
    connections = airportGraph[airport].connections
    for connection in connections:
        dfsAirport(aiportGraph, connection, vis)

# O(a * (a + r)) Time | O(a) Space
def markUnreachableAirportNodes(airportGraph, unreachableAirportNodes):
    for airportNode in unreachableAiportNodes:
        airport = aiportNode.airport
        UnreachableConnections = []
        dfsAddUnreachableConnections(airportGraph, airport, UnreachableConnections, {})
        aiportNode.unReachableConnections = UnreachableConnections

def dfsAddUnreachableConnections(airportGraph, airport, UnreachableConnections, vis):
    if airportGraph[airport].isReachable:
        return 
    if airport in vis:
        return 
    vis[airport] = True
    UnreachableConnections.append(airport)
    connections = airportGraph[airport].connections
    for connection in connections:
        dfsAddUnreachableConnections(airportGraph, connection, UnreachableConnections, vis)

# O( a log(a) + a + r ) Time | O(1) Space
def getMinConnections(airportGraph, unreachableAirportNodes):
    unreachableAirportNodes.sort(key = lambda airport: len(airport.unReachableConnections), reverse = True)
    newConnections = 0
    for airportNode in unreachableAirportNodes:
        if airportNode.isReachable:
            continue
        newConnections += 1
        for connection in airportNode.unReachableConnections:
            airportGraph[connection].isReachable = True
    
    return newConnections
    
class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isReachable = True
        self.unReachableConnections = []
        
    
