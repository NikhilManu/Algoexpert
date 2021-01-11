"""
Permutation --> Name in leetCode
"""
"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order. 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""

#Solution 1
# Time O(N^2 . N!) | Space O(N * N!)
----------------------------------
def getPermutations(array):
	res = []
	getPerm(array, [], res)
	return res

def getPerm(arr, curPerm, res):
	if not arr and curPerm:
		res.append(curPerm)
		return 
	for i in range(len(arr)):
		newArr = arr[:i] + arr[i+1:]
		newPerm = curPerm + [arr[i]]
		getPerm(newArr, newPerm, res)

# Solution 2
# O(N * N!) Time | O(N * N!) Space 
-------------------------------
def getPermutations(array):
    permutations = []
	getPermutation(0, array, permutations)
	return permutations

def getPermutation(i, arr, perm):
	if i == len(arr) - 1:
		perm.append(arr[:])
	else:
		for j in range(i, len(arr)):
			swap(arr, i, j)
			getPermutation(i + 1, arr, perm)
			swap(arr, i, j)

def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

