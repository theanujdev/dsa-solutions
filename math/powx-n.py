# Pow(x, n) (Medium)
# Link - https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n(i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000


class Solution:
    # recursive solution
    def myPow(self, x: float, n: int) -> float:
        # base condition
        if not n:
            return 1
        # negative power
        elif n < 0:
            return 1 / self.myPow(x, -n)
        # if n is odd
        elif n % 2 != 0:
            return x * self.myPow(x, n-1)
        # if n is even
        return self.myPow(x*x, n/2)
