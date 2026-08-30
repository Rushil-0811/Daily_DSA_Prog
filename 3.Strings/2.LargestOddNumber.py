# Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
# The number returned should not have leading zero's. But the given input string may have leading zero.

# Example 1
# Input:
#  s = "5347"
# Output:
#  "5347"
# Explanation:
#  The odd numbers formed by the given string are → 5, 3, 53, 347, 5347. The largest odd number without leading zeroes is 5347.

# Focus on finding the longest valid odd number starting from the original string.
# An odd number must end with an odd digit, so we look for the last odd digit when scanning from the end.
# Leading zeroes don’t add value to the number, so we aim to remove them for a cleaner representation.
# Once the endpoint (last odd digit) is determined, we identify the starting point by skipping any leading zeroes before it.
# Extract the portion between these two positions, this gives the largest possible odd integer from the string.

class Solution:
    # Function to find the largest odd number that is a substring of given string 
    def largeOddNum(self, s: str) -> str:
        ind = -1
        
        # Iterate through the string from the end to beginning
        i = 0
        for i in range(len(s) - 1, -1, -1):
            # Break if an odd digit is found
            if (int(s[i]) % 2) == 1:
                ind = i
                break
        
        # Skipping any leading zeroes
        i = 0
        while i <= ind and s[i] == '0':
            i += 1
        
        # Return the largest odd number substring
        return s[i:ind + 1]

# Driver code
solution = Solution()
num = "504"
result = solution.largeOddNum(num)
print("Largest odd number:", result)