# Longest Substring Without Repeating Characters (Medium)
# Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, start = 0, 0
        used_char = {}
        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]]+1
            else:
                max_length = max(max_length, i-start+1)
            used_char[s[i]] = i
        return max_length

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     charSet = set()
    #     l = 0
    #     res = 0
    #     for r in range(len(s)):
    #         while s[r] in charSet:
    #             charSet.remove(s[l])
    #             l += 1
    #         charSet.add(s[r])
    #         res = max(res, r - l + 1)
    #     return res


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
