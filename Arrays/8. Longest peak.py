"""
---------------------------------
Q.Longest Mountain in Array    [Available in Leetcode]
---------------------------------
Let's call any (contiguous) subarray B (of the input array A) a mountain if the following properties hold:

1. B.length >= 3
2. There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

Note: B could be any subarray of A, including the entire array A

Given an array A of integers, Return the length of the longest mountain.
Return 0 if there is no mountain.

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

"""

# Time - O(n)  |  Space - O(1)   ----> This is a Single Pass Solution.
def LongestPeak(A):
    longest_peak_len = 0
    i = 1
    while i < len(A) - 1:
        if A[i-1] < A[i] > A[i+1]:
            
            left_ind = i - 2
            while left_ind >= 0 and A[left_ind] < A[left_ind + 1]:
                left_ind += 1
                
            right_ind = i + 2
            while right_ind < len(A) and A[right_ind] < A[right_ind - 1]:
                right_ind -= 1
                
            longest_peak_len = max(longest_peak_len, right_ind - left_ind - 1)
            i = right_ind   # This can be done because values before right_index cannot become a peak value itself. It only can become part of a mountain 
        else:
            i += 1
            
    return longest_peak_len
            
  
