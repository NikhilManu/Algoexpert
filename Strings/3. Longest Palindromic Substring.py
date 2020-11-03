"""
-----------------------------------
Longest Palindromic Substring [Name of this Qn in Leetcode]
-----------------------------------
"""

"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

# Solution -->
# Time - O(n^2)  |  Space - O(1)
--------------------------
def LongestPalindrome(s):
    long = [0,1]
    for i in range(1,len(s)):
        odd = expand(s,i-1,i+1)
        even = expand(s,i-1,i)
        cur_long = max(odd,even,key= lambda x: x[1] - x[0])
        long = max(cur_long,long,key= lambda x: x[1] - x[0])
        
    return s[long[0] : long[1]]

def expand(s,r,l):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
        
    return [l + 1,r]
  
