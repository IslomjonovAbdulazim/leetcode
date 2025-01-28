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


