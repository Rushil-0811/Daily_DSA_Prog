# Problem Statement: Given two integers n and i, return true if the ith bit in the binary representation of n (counting from the least significant bit, 0-indexed) is set (i.e., equal to 1). Otherwise, return false.
# Example 1:
# Input: 
# n = 5, i = 0
# Output: 
# true
# Explanation: 
# Binary representation of 5 is 101. The 0-th bit from LSB is set (1).

# Think of the binary form of a number as a series of switches representing powers of 2.
# The i-th bit corresponds to whether the 2ⁱ switch is on or off in the number.
# To check this, examine the bit at the i-th position from the right (least significant side).
# If the number doesn't have enough bits to reach position i, then that bit doesn't exist, return false.
# If it does exist, the bit's value tells you whether that power of 2 contributes to the number.

class Solution:
    # Function to check if the i-th bit of number n is set (1)
    def checkIthBit(self, n, i):
        binary = bin(n)[2:]  # Convert the number into binary string representation (strip '0b' prefix)

        # If the bit index is greater than the length of the binary string, the bit is 0
        if i >= len(binary):
            return False

        # Return True if the i-th bit is 1, otherwise False
        return binary[-(i + 1)] == '1'

# Main function to test the solution
if __name__ == "__main__":
    sol = Solution()
    num = 5  # Binary: 101
    bitIndex = 2  # Check the 2nd bit (0-based index)

    if sol.checkIthBit(num, bitIndex):
        print(f"The {bitIndex}-th bit of {num} is set (1).")
    else:
        print(f"The {bitIndex}-th bit of {num} is not set (0).")

# optimal
# Use bit masking to isolate the i-th bit in the binary representation of the number.
# By shifting 1 to the left i times, you create a mask where only the i-th bit is set.
# Perform a bitwise AND between the number and the mask to check if that specific bit is active.
# If the result is non-zero, the i-th bit is set to 1; otherwise, it is 0.
class Solution:
    # Function to check if the i-th bit of number n is set (1)
    def checkIthBit(self, n, i):
        # Check if the i-th bit is set using bitwise AND operation
        return (n & (1 << i)) != 0  # If the i-th bit is 1, the result will be non-zero

if __name__ == "__main__":
    sol = Solution()
    num = 5  # Binary: 101
    bitIndex = 2  # Check the 2nd bit (0-based index)

    if sol.checkIthBit(num, bitIndex):
        print(f"The {bitIndex}-th bit of {num} is set (1).")
    else:
        print(f"The {bitIndex}-th bit of {num} is not set (0).")