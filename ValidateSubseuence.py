# Time - O(n)   Space - O(1)
def validate(nums,seq):
    if len(seq) > len(nums):
        return False
    
    if nums == seq:
        return True
    
    ind = 0
    for x in nums:
        if len(seq) == ind:
            return True
        if x == seq[ind]:
            ind += 1
    return False



# we dont need to continue if length of seq array is greater than the input array
# we can also check if input array and the sequence array are equal
