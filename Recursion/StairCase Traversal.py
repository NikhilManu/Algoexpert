"""
Climbing Stairs --- Not Entirely similar
"""

"""

"""

#Solution 1 
# Time O(n * k) and O(n) Space 
-----------------------------------

def staircaseTraversal(height, maxSteps):
	res = [0] * (height+1)
	res[0] = 1
	for i in range(1, height + 1):
		step = 1
		while step <= maxSteps and step <= i:
			res[i] += res[i-step]
			step += 1
			
	return res[-1]
  
  
# SOlution 2
# O(n) Space and Time
--------------------------

def staircaseTraversal(height, maxSteps):
	res = [0] * (height + 1)
	ways, res[0] = 0, 1
  
	for i in range(1, len(res)):
		strt = i - maxSteps - 1
		end = i - 1
		
		if strt >= 0:
			ways -= res[strt]
			
		ways += res[end]
		res[i] = ways
		
	return res[-1]
