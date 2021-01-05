"""
No LeetCode Found Currently
"""
"""
Given a 2D array which contains 0 and 1, 0 denotes Free Passages and 1 denotes Blocked Path.

Initially a starting source is given and water pours straight down

"""
#
-----------------
def waterfallStreams(arr, src):
	rowabove = arr[0][:]
	rowabove[src] = -1
	
	for row in range(1, len(arr)):
		curRow = arr[row][:]
		for ind in range(len(curRow)):
			above = rowabove[ind]
			
			waterAbove = above < 0
			presentBlock = curRow[ind] == 1
			
			if not waterAbove:
				continue
				
			if not presentBlock:
				curRow[ind] += above
			else:
				curRow = splitWaterandfill(curRow, rowabove, ind, above)
					
		rowabove = curRow
				
	return [i * -100 for i in rowabove]
				
	
def splitWaterandfill(curRow, rowabove, ind, above):
	split = above/2
	left = ind - 1
	while left >= 0 and rowabove[left] != 1:	
		if curRow[left] != 1:
			curRow[left] += split 
			break
		left -= 1


	right = ind + 1
	while right < len(curRow) and rowabove[right] != 1:
		if curRow[right] != 1:
			curRow[right] += split
			break
		right += 1
		
	return curRow
			
					
					
 					
			
			
			
			
			



