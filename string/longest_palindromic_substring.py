# Longest Palindromic Substring (Medium)
# Link - https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l: r + 1]
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
