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
def SmallestSubstringContains(s,t):
    if not s or not t:  # if s or t is empty
        return '' 
