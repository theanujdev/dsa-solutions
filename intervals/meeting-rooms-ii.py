# Meeting Rooms II (Medium)
# Link - https://www.lintcode.com/problem/919/

# Given an array of meeting time intervals consisting of start and end times[[s1, e1], [s2, e2], ...](si < ei), find the minimum number of conference rooms required.)

# (0,8),(8,10) is not conflict at 8

# Example 1:
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)


class Solution:
    def min_meeting_rooms(self, intervals):
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))
        time.sort(key=lambda x: x[0])
        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count

    # def min_meeting_rooms(self, intervals):
    #     start = sorted([i[0] for i in intervals])
    #     end = sorted([i[1] for i in intervals])
    #     res, count = 0, 0
    #     s, e = 0, 0
    #     while s < len(intervals):
    #         if start[s] < end[e]:
    #             s += 1
    #             count += 1
    #         else:
    #             e += 1
    #             count -= 1
    #         res = max(res, count)
    #     return res


intervals = [(0, 30), (5, 10), (15, 20)]
print(Solution().min_meeting_rooms(intervals))
