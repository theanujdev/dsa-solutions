# Minimum Window Substring (Hard)
# Link - https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring
# of s such that every character in t(including duplicates) is included in the window. If there
# is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


class Solution:
    # Solution 1 (optimized)
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        res, res_len = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                # update our result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if res_len != float("infinity") else ""

    # Solution 2 (not optimized)
    # def minWindow(self, s: str, t: str) -> str:
    #     if not t:
    #         return ""
    #     s_count, t_count = Counter(), Counter(t)
    #     res, res_len = [-1, -1], float("inf")
    #     l = 0
    #     for r in range(len(s)):
    #         char = s[r]
    #         s_count[char] += 1
    #         while len(t_count - s_count)==0:
    #             if (r - l + 1) < res_len:
    #                 res = [l, r]
    #                 res_len = r - l + 1
    #             s_count[s[l]] -= 1
    #             l += 1
    #     l, r = res
    #     return s[l: r + 1] if res_len != float("inf") else ""
