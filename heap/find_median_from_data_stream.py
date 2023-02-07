# Find Median from Data Stream (Hard)
# Link - https://leetcode.com/problems/find-median-from-data-stream/

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# - For example, for arr = [2, 3, 4], the median is 3.
# - For example, for arr = [2, 3], the median is (2 + 3) / 2 = 2.5.

# Implement the MedianFinder class:
# - MedianFinder() initializes the MedianFinder object.
# - void addNum(int num) adds the integer num from the data stream to the data structure.
# - double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0


from heapq import *


class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # first offer to max heap
        heappush(self.maxHeap, -num)
        # bring highest of maxheap to min heap
        heappush(self.minHeap, -heappop(self.maxHeap))

        # if heaps become unbalanced
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        # if stream is odd
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        # else mean of mids
        return (-self.maxHeap[0] + self.minHeap[0])/2


# class MedianFinder:
#     def __init__(self):
#         self.small = []
#         self.large = []

#     def addNum(self, num: int) -> None:
#         if self.large and (num > self.large[0]):
#             heapq.heappush(self.large, num)
#         else:
#             heapq.heappush(self.small, -num)

#         # if heaps become unbalanced
#         if len(self.small) > len(self.large) + 1:
#             val = -heapq.heappop(self.small)
#             heapq.heappush(self.large, val)

#         if len(self.large) > len(self.small) + 1:
#             val = heapq.heappop(self.large)
#             heapq.heappush(self.small, -val)

#     def findMedian(self) -> float:
#         if len(self.small) > len(self.large):
#             return -self.small[0]
#         elif len(self.large) > len(self.small):
#             return self.large[0]
#         return (-self.small[0]+self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
