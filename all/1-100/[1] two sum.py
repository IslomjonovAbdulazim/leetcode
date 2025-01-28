# 1. Brute Force Approach
# Idea: Check all possible pairs using nested loops.
# Time Complexity: O(n²) | Space Complexity: O(1)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
# 2. Two-Pass Hash Map
# Idea: Store each number and its index in a hash map first, then check for complements.
# Time Complexity: O(n) | Space Complexity: O(n)
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        num_map[num] = i
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]

# 3. One-Pass Hash Map (Optimal)
# Idea: Check for complements and build the hash map in a single pass.
# Time Complexity: O(n) | Space Complexity: O(n)
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
        
# 4. Two-Pointer with Sorting
# Idea: Sort the array and use two pointers to find the pair.
# Caveat: Requires tracking original indices (modifies input).
# Time Complexity: O(n log n) | Space Complexity: O(n) 
def twoSum(nums, target):
    sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = sorted_nums[left][1] + sorted_nums[right][1]
        if current_sum == target:
            return [sorted_nums[left][0], sorted_nums[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

# 5. Binary Search Approach
# Idea: Sort the array and use binary search for each element's complement.
# Time Complexity: O(n log n) | Space Complexity: O(n)
def twoSum(nums, target):
    sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    for i in range(len(sorted_nums)):
        num, idx = sorted_nums[i][1], sorted_nums[i][0]
        complement = target - num
        left, right = i + 1, len(sorted_nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_nums[mid][1] == complement:
                return [idx, sorted_nums[mid][0]]
            elif sorted_nums[mid][1] < complement:
                left = mid + 1
            else:
                right = mid - 1

# 6. Recursive Approach (For Curiosity)
# Idea: Recursively check pairs (not efficient but demonstrates recursion).
# Time Complexity: O(n²) | Space Complexity: O(n) (call stack)
def twoSum(nums, target, start=0):
    if start >= len(nums):
        return []
    for i in range(start + 1, len(nums)):
        if nums[start] + nums[i] == target:
            return [start, i]
    return twoSum(nums, target, start + 1)