"""
Given a string and a substring. Add underscore before and after each occurences of that substring in the given string.

Input: "testthis now of testtest and testestest"
Output: "_test_this now of _testtest_ and _testestest_"
"""

# Solution ---
# Time - O(n^2 + nm)  | Space - O(n)
------------------------
def UnderScorify(s,sub):
    location = collapse(getlocation(s,sub))
    return underscorify(s,location)

def getlocation(s,sub):
    location = []
    startidx = 0
    while startidx < len(s):
        nextidx = s.find(sub,startidx)
        if nextidx == -1:
            break
        loaction.append([nextidx,nextidx + len(sub)])
        startidx = nextidx + 1
        
    return location

def collapse(location):
    if not location or len(location) == 1:
        return location
    
    newLocations = [location[0]]
    prev = newlocations[0]
    for i in range(1,len(location)):
        cur = location[i]
        if cur[0] <= prev[1]:
            prev[1] = cur[1]
        else:
            newLocations.append(cur)
            prev = cur
    return newLocations

def Underscorify(s,location):
    res = []
    startidx = 0
    locidx = 0
    i = 0
    inbetween = False # Denotes if in between underscore or not
    while startidx < len(s) and locidx < len(location):
        if startidx == location[locidx][i]:
            res.append("_")
            inbetween = not inbetween
            if not inbetween:
                locidx += 1
            i = 0 if i == 1 else 1
        res.append(s[startidx])
        startidx += 1
        
    if locidx < len(location):
        res.append("_")
    
    if startidx < len(s):
        res.append(s[startidx:])
        
    return ''.join(res)
            
            
            
        
    
  
