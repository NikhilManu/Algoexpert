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
def apartmentHunting(blocks, reqs):
	minReqDist = []
	for req in reqs:
		minReqDist.append(getMinDist(blocks, req))
	
	maxDist = getMaxDist(blocks, minReqDist)
	return maxDist.index(min(maxDist))

def getMaxDist(blocks, minDist):
	maxDist = [0] * len(blocks)
	for i in range(len(blocks)):
		maxdist = float('-inf')
		for j in range(len(minDist)):
			maxdist = max(maxdist, minDist[j][i])
			
		maxDist[i] = maxdist
		
	return maxDist
	
def getMinDist(blocks, req):
	minDist = [float('inf')] * len(blocks)
	closest = float('inf')
	for i in range(len(blocks)):
		if blocks[i][req]:
			closest = i
			
		minDist[i] = abs(closest - i)
	closest = float('inf')
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closest = i
			
		minDist[i] = min(minDist[i], abs(closest - i))
		
	return minDist
				
        
    
                
            
     
    
 
      
