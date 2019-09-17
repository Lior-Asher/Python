# Given a list of numbers, 
# where every number shows up twice except for one number, 
# find that one number.
# Example:
#   Input: [4, 3, 2, 4, 1, 3, 2]
#   Output: 1

def singleNumber(nums):

    # Iterate the array
    for i in nums:
        if nums.count(i) == 1: # Return the value that appears only once.
            return i

    return -1 # Return (-1) if no such value was found

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1