# 1. Brute Force Approach
# Idea: Check all possible pairs using nested loops.
# Time Complexity: O(n²) | Space Complexity: O(1)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
# 2. One-Pass Hash Map (Optimal)
# Idea: Check for complements and build the hash map in a single pass.
# Time Complexity: O(n) | Space Complexity: O(n)
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
        