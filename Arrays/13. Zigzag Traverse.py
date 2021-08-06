"""
-------------------
Diagonal Traverse [Name of this Qn in LeetCode]
------------------
"""
"""
Type 1 of ZigZag.

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,4,2,3,5,7,8,6,9]

"""
# Time - O(n)  |  Space - O(1)
def ZigZag(arr):
    if not arr:
        return []
    res = []
    tr = len(m) - 1
    tc = len(m[0]) - 1
    r,c = 0,0
    down = True
    while r >= 0 and r <= tr and c >= 0 and c <= tc:
        res.append(arr[r][c])
        if down:
            if c == 0 or r == tr:
                down = False
                if r == tr:
                    c += 1
                else:
                    r += 1
            else:
                r += 1
                c -= 1
        else:
            if r == 0 or c == tc:
                down = True
                if c == tc:
                    r += 1
                else:
                    c += 1
            else:
                r -= 1
                c += 1


    return res



"""
Type 2 of ZigZag.

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

"""

"""
 Solution 1 ---> Same as the above Solution. 
 Only change is to make the variable 'down = False' initially.
"""

# Solution 2 -->
# This uses concept that sum of indexes of every diagonal is equal.
# Time - O(n)  |  Space - O(n)
def ZigZag(arr):
    if not m:
        return []
    r = len(m)
    c = len(m[0])
    dic = defaultdict(list)
    for i in range(r):
        for j in range(c):
            dic[i+j].append(m[i][j])  # Since this is defaultdict, we dont need to code for condition,  when i+j is not in dic

    res = []
    for i in range(r+c):
        if i % 2 == 0:
            res += dic[i][::-1]
        else:
            res += dic[i]

    return res



  

