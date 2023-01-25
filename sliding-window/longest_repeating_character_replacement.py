# Longest Repeating Character Replacement (Medium)
# Link - https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

    #  def characterReplacement(self, s: str, k: int) -> int:
    #     l = 0
    #     c_frequency = {}
    #     longest_str_len = 0
    #     for r in range(len(s)):
    #         if not s[r] in c_frequency:
    #             c_frequency[s[r]] = 0
    #         c_frequency[s[r]] += 1
    #         cells_count = r - l + 1
    #         if cells_count - max(c_frequency.values()) <= k:
    #             longest_str_len = max(longest_str_len, cells_count)
    #         else:
    #             c_frequency[s[l]] -= 1
    #             l += 1
    #     return longest_str_len


s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))
