// Sum of Two Integers (Medium)
// Link - https://leetcode.com/problems/sum-of-two-integers/

// Given two integers a and b, return the sum of the two integers without using the operators + and -.

// Example 1:
// Input: a = 1, b = 2
// Output: 3

// NOTE: Same can be solved in python but it will give TLE as in Python unlike other languages
// the range of bits for representing a value is not 32, its much much larger than that. This
// is great when dealing with non negative integers, however this becomes a big issue when
// dealing with negative numbers (two's compliment)


class Solution {
    public int getSum(int a, int b) {
        while (b!=0){
            int temp = (a & b) << 1;  // carry digit
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}