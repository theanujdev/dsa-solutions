# Valid Palindrome (Easy)
# Link - https://leetcode.com/problems/valid-palindrome/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while (not s[l].isalnum()) and l < r:
                l += 1
            while (not s[r].isalnum()) and r > l:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))


# Could write own alpha-numeric function
# def alphanum(c):
#     return (
#         ord("A") <= ord(c) <= ord("Z")
#         or ord("a") <= ord(c) <= ord("z")
#         or ord("0") <= ord(c) <= ord("9")
#     )
