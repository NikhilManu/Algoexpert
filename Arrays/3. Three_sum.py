1.) # 3 Sum with distinct elements
    # resultant array cannot contain duplicate triplets

# Time - O(n^2)   Space - O(n)
def 3Sum(nums,target):
    nums.sort()
    for i in range(len(nums) - 2):
        l, r = i+1, len(nums) - 1
        while l < r:
            cur_sum = nums[i] + nums[r] + nums[l]
            if cur_sum == target:
                res.append([ nums[i], nums[l], nums[r] ])
                l += 1
                r -= 1
            elif cur_sum > target:
                r -= 1
            else:
                l += 1
                
    return res


2.) #3 sum with regular array which can contain duplicate elements
    #resultant array cannot contain duplicate triplets

# Time  - O(n^2)   Space - O(n)
def 3Sum(nums,target):
    nums.sort()
    for i in range(len(nums) - 2):
        
        if i > 0 and nums[i] == nums[i-1]:      #this case is important
            continue                            
            
        l, r = i+1, len(nums) - 1
        while l < r:
            cur_sum = nums[i] + nums[r] + nums[l]
            if cur_sum == target:
                res.append([ nums[i], nums[l], nums[r] ])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif cur_sum > target:
                r -= 1
            else:
                l += 1
    return res
                
