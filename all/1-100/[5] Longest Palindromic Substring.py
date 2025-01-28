# Approach 1: Brute Force
# Idea: Check all possible substrings and find the longest one that is a palindrome.
# Time Complexity: O(n³) | Space Complexity: O(1)
def longestPalindrome(s: str) -> str:
    def is_palindrome(s):
        return s == s[::-1]

    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest

# Approach 2: Expand Around Center 
# Idea: Treat each character (and each pair of characters) as the center of a potential palindrome and expand outward to find the longest palindrome.
# Time Complexity: O(n²) | Space Complexity: O(1)
def longestPalindrome(s: str) -> str:
    def expand_around_center(left, right):
        # Expand as long as the characters are equal and within bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring
        return s[left + 1:right]

    n = len(s)
    longest = ""
    for i in range(n):
        # Odd-length palindromes (single center)
        palindrome1 = expand_around_center(i, i)
        # Even-length palindromes (double center)
        palindrome2 = expand_around_center(i, i + 1)
        # Update the longest palindrome
        longest = max(longest, palindrome1, palindrome2, key=len)
    return longest
