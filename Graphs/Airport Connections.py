"""
Similar Qn - Cheapest Flights Within K Stops
"""

"""
Given a list of Aiports, a list of OneWay Route, and a starting Airport.
Write a Program to find minimum number of connection which make every aiport accesible from the starting Airport
"""

# Solution
# 
--------------
def AirportConnections(airports, routes, start):
    airportGraph = getAirportGraph(airports, routes)
    
def getAirportGraph(airports, routes):
    airportGraph = {}
    for aiport in airports:
        airportGraph[airport] = AirportNode(airport)
        
    for route in routes:
        airport, connection = route
        airportGraph[airport].connections.append(connection)
    
    return airportGraph

class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isReachable = True
        self.unReachableConnections = []
        
    
