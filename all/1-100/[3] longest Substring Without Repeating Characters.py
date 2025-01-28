# 1. Brute Force (Check All Substrings)
# Idea: Check every possible substring to see if it has repeating characters.
# Time Complexity: O(n³) | Space Complexity: O(1)
def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            # Check if substring s[i..j] has duplicates
            chars = set()
            duplicate = False
            for k in range(i, j+1):
                if s[k] in chars:
                    duplicate = True
                    break
                chars.add(s[k])
            if not duplicate:
                max_len = max(max_len, j - i + 1)
    return max_len

# 2. Sliding Window with Hash Set 
# Idea: Use two pointers (left and right) to define a window. Expand the window to the right, and if a duplicate is found, shrink the window from the left until duplicates are removed.
# Time: O(2n) | Space: O(min(n, 26)) 
def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    left = 0
    seen = set()  # Tracks characters in the current window
    
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])  # Shrink the window from the left
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

# 3. Optimized Sliding Window with Hash Map (Most Optimal)
# Idea: Track the last seen index of each character. When a duplicate is found, jump the left pointer to the right of the last occurrence, skipping unnecessary checks.
# Time: O(n) | Space: O(min(n, 128))
def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    left = 0
    char_map = {}  # {char: last_index}
    
    for right in range(len(s)):
        if s[right] in char_map:
            # Jump left to the right of the last duplicate
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right  # Update last seen index
        max_len = max(max_len, right - left + 1)
    
    return max_len
