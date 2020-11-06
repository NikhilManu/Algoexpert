"""
---------------------
Minimun Window Substring [ Name of this Qn in LeetCode]
--------------------
Since this Qn same as in Algoexpert, same solution is viable in leetcode also.
"""

"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t.
If there is no such window in s that covers all characters in t, return the empty string "".

Note: If there is multiple small Window, any of these small window will Satisfy the ouptut answer.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""

# Time - O()  | Space - O()
--------------------------
from collections import Counter

def SmallestSubstringContains(s,t):
    if not s or not t or len(s) < len(t):  # if s or t is empty or if length of s is less than that of t.
        return '' 
    
    if len(s) == len(t):
        if s == t:
            return s
        else:
            return ''
    
    bound = [0,float('inf')]
    target = Counter(t)     # Ask to interviewer if you can use dependencies, if he says no implement it yourself like in Algoexpert
    current = {}
    targetlen = len(target)
    currentlen = 0
    
    l,r = 0,0
    while r < len(s):
        if s[r] not in target: 
            r += 1
            continue
            
        increaseCount(s[r],current)
        if current[s[r]] == target[s[r]]:
            currentlen += 1
        
        while currentlen == targetlen and l <= r:
            bound = [l,r] if r - l < bound[1] - bound[0] else bound
            
            if s[l] not in target:
                l += 1
                continue
            
            if current[s[l]] == target[s[l]]:
                currentlen -= 1
            decreaseCount(s[l],current)
            l += 1
        
        r += 1
        
    return getStringfromBound(s,bound)


def getStringfromBound(s,bound):
    if bound[1] == float('inf'):
        return ""
    return s[bound[0]: bound[1] + 1]
                         

def decreaseCount(char, current):
    current[char] -= 1

def increaseCount(char, current):
    if char in current:
        current[char] += 1
    current[char] = 1
    
    
    
