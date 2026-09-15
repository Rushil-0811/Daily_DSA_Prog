# Problem Statement: Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two if there exists an integer x such that n == 2ˣ.
# Example 1:
# Input: 
# n = 16
# Output: 
# true
# Explanation: 
# 2⁴ = 16, so 16 is a power of two.

# Power of two numbers have exactly one bit set in their binary form.
# Subtracting one flips all bits after the set bit, creating no overlap with the original number.
# A bitwise AND between the number and one less than itself will be zero only for powers of two.
# This property allows for a fast check without looping or dividing.

class Solution:
    # Function to check if a number is a power of two
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0  # Check if n is greater than 0 and has only one bit set

if __name__ == "__main__":
    sol = Solution()
    num = 8

    if sol.isPowerOfTwo(num):
        print(f"{num} is a power of two.")
    else:
        print(f"{num} is not a power of two.")