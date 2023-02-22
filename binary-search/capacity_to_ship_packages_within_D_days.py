# Capacity To Ship Packages Within D Days (Medium)
# Link - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Example 1:
# Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like(2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l+r)//2

            day_count = 1
            total_weight = 0

            for weight in weights:
                total_weight += weight
                if total_weight > mid:
                    day_count += 1
                    total_weight = weight

            # if takes more days than available, increase capacity to reduce days
            if day_count > days:
                l = mid + 1
            # if takes less days than available, reduce capacity
            else:
                r = mid

        return l
