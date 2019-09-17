# Given a list of numbers with only 3 unique numbers (1, 2, 3), 
# sort the list in O(n) time.
# Example 1:
#   Input: [3, 3, 2, 1, 3, 2, 1]
#   Output: [1, 1, 2, 2, 3, 3, 3]

def sortNums(nums):
    sz = len(nums);
    tmp = [0 for i in range(sz)] # Reset tmp to 0s
    sortedArray = []

    # Count the number of time each number appears in 'nums',
    # and add the count to tmp at the corelating index
    # Example: [0, 2, 2, 3, 0, 0, 0] -> 
    # the number '2' at index '1',
    # means that the number '1' appears twice in 'nums'. 
    for i in nums:
        tmp[i] += 1
    
    it = 0 
    for i in tmp:
        count = i 
        while count > 0:
            sortedArray.append(it)
            count -= 1
        it += 1

    return sortedArray

print (sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]