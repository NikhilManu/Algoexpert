"""
Write a function that takes in two non-empty arrays of integers.
The function should find the pair of numbers (one from the first array, one from the second array)
whose absolute difference is closest to zero.
The function should return an array containing these two numbers,
with the number from the first array in the first position.

Assume that there will only be one pair of numbers with the smallest difference.
Sample input: nums1 = [-1, 5, 10, 20, 28, 3], nums2 = [26, 134, 135, 15, 17]
Sample output: [28, 26]
"""

# Time - O(nlog(n) + mlog(m)) | Space - O(1)

def smallestdiff(nums1,nums2):
    nums1.sort()
    nums2.sort()
    p1, p2, smallest_diff = 0, 0, float('inf')
    result = []
    while p1 < len(nums1) and p2 < len(nums2):
        f = nums1[p1]
        s = nums2[p2]
        cur_diff = abs(f - s)
        if f < s:
            p1 += 1
        elif s < f:
            p2 += 1
        else:
            return [f, s]
        
        if smallest_diff > cur_diff:
            smallest_diff = cur_diff
            result = [f, s]
            
    return result
            
