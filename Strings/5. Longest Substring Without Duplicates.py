"""
--------------
Longest Substring Without Repeating Characters [Name of this Qn in LeetCode]
--------------
"""

"""
Given a string s, find the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: "abc"
Explanation: The answer is "abc" or "bca" or "cab"
"""

# Solution 1 -->
# Time - O(N)  | Space - O(min(N,A)) 
--------------
def LongestSubstringWithoutDuplicates(s):
    used = {}
    long = [0,1]    #Since a single letter can be also the answer
    start = 0
    for i,ch in enumerate(s):
        if ch in used:
            start = max(start,used[ch] + 1)
        if long[1] - long[0] < start - i + 1:
            long = [start,i + 1]
        used[ch] = j
    return s[long[0] : long[1]]


"""
LeetCode Qn:
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

# Solution 1 --> Using Same logic of AlgoExpert
# Time - O(N)  | Space - O(min(N,A)) 
--------------------------
def LongestSubstringWithoutDuplicates(s):
    used = {}
    long = 0    # intialising to zero since there can be a empty string
    start = 0
    for i,ch in enumerate(s):
        if ch in used:
            start = max(start, used[ch] + 1)    # if max(start,....) is not used. Try Solving it for the case 'abba'. This will break
        long = max(long, i-start +1)   
        used[ch] = j
    return long

# Solution 2 --> slightly different Logic
# Time - O(N)  | Space - O(min(N,A)) 
--------------------------
def LongestSubstringWithoutDuplicates(s):
    used = set()    #using set instead of dictionary or hashmap
    long = 0 
    l,r = 0,0
    while r < len(s):   # We dont have to include l < len(s) since l will never be greater than r
        if s[r] not in used:
            used.add(s[r])
            long = max(long,r - l+1) 
            r += 1
        else:
            used.remove(s[l])
            l += 1
    return long
    


        
  
