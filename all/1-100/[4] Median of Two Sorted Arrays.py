# Approach 1: Brute Force (Merge and Find Median)
# Idea: Merge the two sorted arrays into one sorted array, then compute the median.
# Time Complexity: O(n + m) | Space Complexity: O(n + m) 
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the two sorted arrays
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        # Compute median
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
    
# Approach 2: Binary Search (Optimal)
# Idea: Use binary search to partition the arrays such that the left half of the combined array contains elements ≤ the right half.
# Time Complexity: O(log(min(n, m))) | Space Complexity: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x  # Binary search on the shorter array
        
        while low <= high:
            partitionX = (low + high) // 2  # Midpoint of nums1
            partitionY = (x + y + 1) // 2 - partitionX  # Corresponding partition in nums2
            
            # Handle edge cases (empty partitions)
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if the partition is valid
            if maxX <= minY and maxY <= minX:
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1  # Move left in nums1
            else:
                low = partitionX + 1   # Move right in nums1
        
        # If the input arrays are invalid (shouldn't reach here in a valid scenario)
        raise ValueError("Input arrays are not sorted or valid.")