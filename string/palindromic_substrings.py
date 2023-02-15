# Palindromic Substrings (Medium)
# Link - https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def count_palindrome(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):
            res += count_palindrome(i, i)
            res += count_palindrome(i, i+1)

        return res
