# Valid Anagram (Easy)
# Link - https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
