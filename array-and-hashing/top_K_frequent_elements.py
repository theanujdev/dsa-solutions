# Valid Anagram (Medium)
# Link - https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]


from collections import Counter
# import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        nums_counter = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for value, frequency in nums_counter.items():
            freq[frequency].append(value)
        top_k_result = []
        for i in range(len(nums), 0, -1):
            for ans in freq[i]:
                top_k_result.append(ans)
                if len(top_k_result) == k:
                    return top_k_result

    # def topKFrequent(self, nums, k: int):
    #     # O(1) time
    #     if k == len(nums):
    #         return nums

    #     # build hash map : character and how often it appears
    #     # O(N) time
    #     count = Counter(nums)
    #     # build heap of top k frequent elements and
    #     # convert it into an output array
    #     # O(N log k) time
    #     return heapq.nlargest(k, count.keys(), key=count.get)


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
