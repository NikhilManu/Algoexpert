"""
You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment
that you could move into. In order to pick your apartment, you want to optimize its location.
You also have a list of requirements:a list of buildings that are important to you.
For instance, you might value having a school and a gym near your apartment.
The list of blocks that you have contains information at every block about all of the buildings that are present and
absent at the block in question.
For instance, for every block, you might know whether a school, a pool, an office, and a gym are present or not.
In order to optimize your life, you want to minimize the farthest distance you'd have to walk from your apartment to
reach all of your required buildings.
Write a function that takes in a list of blocks and a list of your required buildings and that returns the location
(the index) of the block that is most optimal for you.

Input: Block - [ {sc:True,g:False,st:False}, 
                     {sc:False,g:True,st:False}, 
                     {sc:True,g:True,st:False}, 
                     {sc:True,g:False,st:False}, 
                     {sc:True,g:False,st:True} ]     
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
            maxdist = max(maxdist, minDistancesfromblock[j][i])  # This is [j][i] not [i][j].
        maxDistance[i] = maxdist
    return maxDistance
        
    
                
            
     
    
 
      
