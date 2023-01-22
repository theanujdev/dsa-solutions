# Group Anagrams (Medium)
# Link - https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for str in strs:
            hashmap[tuple(sorted(str))].append(str)
        return hashmap.values()

    # def groupAnagrams(self, strs):
    #         h = {}
    #         for word in strs:
    #             sortedWord = ''.join(sorted(word))
    #             if sortedWord not in h:
    #                 h[sortedWord] = [word]
    #             else:
    #                 h[sortedWord].append(word)
    #         return h.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
