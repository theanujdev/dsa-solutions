# Word Break (Medium)
# Link - https://leetcode.com/problems/word-break/

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".


class Solution:
    # dp bottom-up 1 (tabular)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

    # dp bottom-up 2 (tabular)
    # def wordBreak(self, s, wordDict):
    #     dp = [False]*(len(s)+1)
    #     dp[0] = True
    #     for i in range(1, len(s)+1):
    #         for j in range(i):
    #             if dp[j] and s[j:i] in wordDict:
    #                 dp[i] = True
    #                 break
    #     return dp[-1]

    # dp top-down (memoization)
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     wordDict = set(wordDict)
    #     dp = {}

    #     def getResult(s,index):
    #         if not s:
    #             return True
    #         if index in dp:
    #             return dp[index]
    #         for i in range(len(s)+1):
    #             k = s[:i]
    #             if k in wordDict:
    #                 if getResult(s[i:],index+i):
    #                     dp[index] = True
    #                     return dp[index]
    #         dp[index] = False
    #         return dp[index]

    #     return getResult(s,0)
