"""
Given List of dict of blocks and requirement Array.
Choose the Best apartment from where the distance to each requirement is minimum.
Assume each index of Array block is an Apartment

Input: Block - [ {sc:True,g:False,st:False}, {sc:False,g:True,st:False}, {sc:True,g:True,st:False}, {sc:True,g:False,st:False}, {sc:True,g:False,st:True} ]     
       Req - [ g,sc,st] # Assume sc - school and g - gym and st - store 
Ouptut: 3
Explanation: since we have to travel maximum of 1 block for every requirement

"""

#Solution 1 ---> Not Optimal Solution
# Time - O(B^2 * R)  |  Space - O(B)
----------------------------------
def ApartmentHunting(blocks,reqs):
    maxdistfromblock = [float('-inf')] * len(blocks)
    for i in range(len(blocks)):
        for req in reqs:
            closest = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closest = min(closest,abs(i - j))
            maxdistfromblock[i] = max(maxdistfromblock[i],closest)
            
    return maxdistfromblock.index(min(maxdistfromblock))        #finds the index of the minimum Value


# Solution 2 ----> Optimal Solution
# Time - O(BR)  |  Space - O(BR)
------------------------------
def ApartmentHunting(blocks,req):
    minDistancesfromblock = list(map(lambda req: getminDistancefromblock(blocks,req), reqs)) # Minimum Distance for each block for each requirement
    maxDistancefromblock = getmaxDistancefromblock(blocks,minDistancesfromblock)
    return maxDistancefromblock.index(min(maxDistancefromblock))
    
def getminDistancefromblocks(blocks,req):
    minDistances = [0] * len(blocks)
    closestidx = -1
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestidx = i
        if closestidx != -1:
            minDistances[i] = abs(i - closestidx)
    
    closestidx = -1
    for i in reveresd(range(len(blocks))):
        if blocks[i][req]:
            closestidx = i
        if closestidx != -1:
            minDistances[i] = min(minDistances[i], abs(i - closestidx))
        
    return minDistances

def getmaxDistancefromBlock(blocks,minDistancesfromblock):
    maxDistance = [0] * len(blocks)
    for i in range(len(blocks)):
        maxdist = float('-inf')
        for j in range(len(minDistancesfromblock)):
            maxdist = max(maxdist, minDistancesfromblock[j][i])
        maxDistance[i] = maxdist
    return maxDistance
        
    
                
            
     
    
 
      
