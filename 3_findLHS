def findLHS(nums):
    num_counts = {}
    max_length = 0

    # Count the frequency of each number
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    # Check for pairs with a difference of 1 and update max_length
    for num in num_counts:
        if num + 1 in num_counts:
            length = num_counts[num] + num_counts[num + 1]
            max_length = max(max_length, length)

    return max_length


nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print(result)  
