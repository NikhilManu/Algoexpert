"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.

Input: [1,2,2,3]
Output: true

Input: [1,3,2]
Output: false
"""

# Time - O(n) |  Space - O(1)
def isMonotonic(nums):
    if len(nums) <= 2:
        return True
    
    direction = nums[1] - nums[0]
    for i in range(2,len(nums)):
        if direction == 0:
            direction = nums[i] - nums[i-1]
        else:
            current_direction = nums[i] - nums[i-1]
            if (direction > 0 and current_direction < 0) or (direction < 0 and current_direction > 0):
                return False
    return True
   
    
# Time - O(n)  |  Space - O(1)
def isMonotonice(nums):
    increasing, Decreasing = True, True
    for i in range(1,len(nums)):
        if a[i] > a[i-1]:
            decreasing = False
        if a[i] < a[i-1]:
            increasing = False
            
    return increasing or decreasing 
