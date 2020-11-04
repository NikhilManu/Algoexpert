"""
-----------------------------
Group Anagrams [Name of this Qn in LeetCode
----------------------------
"""
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# Solution 1 in AlgoExpert ---> It is not a very good solution.

# Solution 2 ----> Solution Given in Algoexpert
# Time - O(wNlog(N))  | Space - O(wN)
--------------------------
def GroupAnagrams(words):
    groups = {}
    for word in words:
        sortedword = "".join(sorted(word))
        if sortedword in groups:
            groups[sortedword].apppend(word)
        else:
            group[sortedword] = [word]
            
    return group.values()   # list(group.values()) is not needed, but both are correct

#Solution 3 ---> My Solution
# Time - O(wNlog(N))  | Space - O(wN)
-------------------------------
import collections
def GroupAnagrams(words):
    groups = collections.defaultdict(list)
    for word in words:
        group[tuple(sorted(word))].append(word)
    return group.values()
