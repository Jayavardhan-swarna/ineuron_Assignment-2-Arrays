def array_pair_sum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0

    # Iterate through the array, incrementing by 2 to form pairs
    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum


nums = [1, 4, 3, 2]
result = array_pair_sum(nums)
print(result) 
