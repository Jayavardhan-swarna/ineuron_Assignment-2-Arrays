def minimumScore(nums, k):
    minimum = min(nums)
    maximum = max(nums)
    score = maximum - minimum

    if 2 * k >= score:
        return 0

    min_score = min(maximum - k, minimum + k)
    return min_score


nums = [1]
k = 0
result = minimumScore(nums, k)
print(result) 
