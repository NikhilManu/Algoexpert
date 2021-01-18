"""
Lowest Common Ancestor
"""

"""
"""

# Solution
# Time O(N) | O(d) Space
--------------------------
def getLowestManager(topManager, reportOne, reportTwo):
    return dfs(topManager, reportOne, reportTwo).manager

def dfs(manager, one, two):
    reportingPerson = 0
    for directReport in manager.directReports:
        info = dfs(directReports, one, two)
        if info.manager:
            return info
        reportingPerson += info.reportingPerson
        
    if manager == one or manager == two:
        reportingPerson += 1
    lowestManager = manager if reportingPerson == 2 else None 
    return managerInfo(lowestManager, reportingPerson)

class managerInfo:
    def __init__(self, manager, reportingPerson):
        self.manager = manager
        self.reportingPerson = reportingPerson
        
# given node format

class Org:
    def __init__(self, manager):
        self.manager = manager 
        self.directReports = []
  
