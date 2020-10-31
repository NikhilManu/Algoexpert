"""
Q. Traverse the mxn Array in spiral order and return the resultant array.

Case 1:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Case 2:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Case 3:
[
  [7],
  [9],
  [6]
]
Output: [7,9,6]
"""

# ALgoExpert Solution
# Time  -  O(n)  |   Space  -  O(n)  

def Spiral(arr):
  res = []
  row_beg,row_end = 0,len(arr)-1
  col_beg,col_end = 0,len(arr[0])-1
  while row_beg <= row_end and col_beg <= col_end:
        
        for i in range(col_beg, col_end + 1):
            res.append(arr[row_beg][i])
            
        for i in range(row_beg + 1, col_end + 1):
            res.append(arr[i][col_end])
            
        for i in range(col_end - 1, col_beg - 1,-1):   # In AlgoExpert reversed(range()) is used. Both are same
            if row_beg == row_end:    # If this condition is not coded Case 2 will Fail.
                break
            res.append(arr[row_end][i])
            
            
        for i in range(row_end - 1, row_beg ,-1):      # In AlgoExpert reversed(range()) is used. Both are same
            if  col_beg == col_end:   # If this condition is not coded Case 3 will Fail.
                break
            res.append(arr[i][col_beg])
            
        col_beg += 1
        col_end -= 1
        row_beg += 1
        row_end -= 1
            
    return res



# My Similar Solution
# Time  -  O(n)  |   Space  -  O(n)  

def Spiral(arr):
    res = []
    rbeg ,rend, cbeg, cend = 0, len(arr)-1, 0, len(arr[0])-1

    while rbeg <= rend and cbeg <= cend:
        
        for i in range(cbeg,cend+1):
            res.append(arr[rbeg][i])
        rbeg += 1

        for i in range(rbeg,rend+1):
            res.append(arr[i][cend])
        cend -= 1

        if rbeg <= rend:    # This condition is important
            for i in range(cend,cbeg-1,-1):
                res.append(arr[rend][i])
            rend -= 1
            
        if cbeg <= cend:    # This condition is important
            for i in range(rend,rbeg-1,-1):
                res.append(arr[i][cbeg])
            cbeg += 1

    return res

   
   """ There exist a Recursive Solution which is almost similar to the above method """
