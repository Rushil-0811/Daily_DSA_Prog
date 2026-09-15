# Problem Statement: Given an integer n, return the number of set bits (1s) in its binary representation.
# Can you solve it in O(log n) time complexity?

# Example 1:
# Input: 
# n = 5
# Output:
#  2
# Explanation: 
# The binary representation of 5 is 101, which has 2 set bits.

# Initialize a counter to zero.
# While the number is greater than zero:
# Check if the least significant bit (LSB) is 1 by performing bitwise AND with 1.
# If LSB is 1, increment the counter.
# Right shift the number by one bit.
# Return the counter.

class Solution:
    # Function to count the number of set bits (1s) in the binary representation of n
    def countSetBits(self, n):
        count = 0  # Variable to store the count of set bits

        # Step 1: Count the number of set bits using bitwise operations
        while n > 0:
            count += (n & 1)  # Check if the least significant bit is set (1)
            n >>= 1  # Right shift n by 1 to process the next bit

        # Step 2: Return the count of set bits
        return count

# Main function to test the solution
if __name__ == "__main__":
    n = 29  # Example input for n (binary: 11101)

    sol = Solution()
    result = sol.countSetBits(n)

    print(f"The number of set bits is: {result}")


# optimal
# Initialize a counter to zero.
# While the number is greater than zero:
# Check if the least significant bit (LSB) is 1 by performing bitwise AND with 1.
# If LSB is 1, increment the counter.
# Right shift the number by one bit.
# Return the counter.

class Solution:
    # Function to count the number of set bits (1s) in the binary representation of n using Brian Kernighan's Algorithm
    def countSetBits(self, n):
        count = 0  # Variable to store the count of set bits

        # Step 1: While n is non-zero, turn off the rightmost set bit
        while n:
            n &= (n - 1)  # Turn off the rightmost set bit
            count += 1  # Increment the count

        # Step 2: Return the count of set bits
        return count

# Main function to test the solution
if __name__ == "__main__":
    n = 29  # Example input for n (binary: 11101)

    sol = Solution()
    result = sol.countSetBits(n)

    print(f"The number of set bits is: {result}")