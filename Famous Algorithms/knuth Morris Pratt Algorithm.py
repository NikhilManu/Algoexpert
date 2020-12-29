"""
Implement strStr() --> Name of this Qn in LeetCode

"""

"""
Implement strStr().

Return the index of the first occurrence of sub in string, or -1 if sub is not part of string.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview. Here we return 0

Example 1:
Input: string = "hello", sub = "ll"
Output: 2

Example 2:
Input: string = "aaaaa", sub = "bba"
Output: -1

Example 3:
Input: string = "", sub = ""
Output: 0

"""
# Solution - Knuth Morris Pratt Algo
# Time O(N + M) and O(M) Space
----------------------------
def strstr(string, sub):
    pattern = BuildPattern(sub)
    return indexofMatch(string, sub, pattern)

def BuildPattern(sub):
    pattern = [-1] * len(sub)
    j, i = 0, 1
    while i < len(sub):
        if sub[i] == sub[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j-1] + 1
        else:
            i += 1
            
    return pattern

def indexofMatch(string, sub, pattern):
    i, j = 0, 0
    while i + len(sub) - j <= len(string):
        if string[i] == sub[j]:
            if j == len(sub):
                return i - len(sub) + 1
            
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j-1] + 1
        else:
            i += 1
            
    return -1
            
    
    
    
  
