"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""
# Easy Solution With division is not mentioned Here

# Solution 1 --- DP Solution
# Time O(N) | O(N) Space
--------------------------
def ProductExceptSelf(nums):
    left = [1] * len(nums)
    right = [1] * len(nums)
    
    for i in range(1, len(nums)):
        left[i] = left[i-1] * nums[i-1]
        
    for i in reversed(range(len(nums)-1)):
        right[i] = right[i+1] * nums[i+1]
        
    return [i*j for i,j in zip(left, right)]    # Same as multiplying left element and right element at same index


# Solution 2 --- Without left and right Array
# Time O(N) | O(1) space without including the output array
-------------------------------------
def ProductExceptself(nums):
    res = [1] * len(nums)
    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
    
    for i in reversed(range(len(nums)):
        res[i] *= R
        R *= nums[i]
  
    return res
             
                      
# Solution 3 ----- Errichto Solution ( Little Modified Solution )  ---> Errichto is Youtuber 
# O(N) Time | Space O(1) not including the output array
-----------------------------------
                      
def productExceptSelf(nums):
    product, zeros = 1, 0
    for x in nums:
        if x == 0:
            zeros += 1
        else:
            product *= x

    res = [0] * len(nums)

    if zeros:
        if zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = product
        else:
            pass

    else:
        for i in range(len(nums)):
            res[i] = product // nums[i]


    return res
