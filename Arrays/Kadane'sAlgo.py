#  Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
# brute
# two loops to get all possible subarrays, a max value that keeps updating as we loop thru
from typing import List

class Solution:
    # Function to find maximum sum of subarrays
    def maxSubArray(self, nums: list[int]) -> int:
        
        """ Initialize maximum sum with
        the smallest possible integer"""
        maxi = float('-inf')

        # Iterate over each starting index of subarrays
        for i in range(len(nums)):
            
            """ Iterate over each ending index
            of subarrays starting from i"""
            for j in range(i, len(nums)):
                
                """ Variable to store the sum
                of the current subarray"""
                sum = 0

                # Calculate the sum of subarray nums[i...j]
                for k in range(i, j + 1):
                    sum += nums[k]

                """ Update maxi with the maximum of itscurrent
                value and the sum of the current subarray"""
                maxi = max(maxi, sum)

        # Return the maximum subarray sum found
        return maxi

# Test
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

#create an isinstance of Solution class
sol = Solution()

maxSum = sol.maxSubArray(arr)

#Print the max sum of subarrays
print("The maximum subarray sum is:", maxSum)

# better
# 2 loops, For each subarray defined by i and j, add the current element at arr[j] to the sum of the previous subarray.
# Keep track of the maximum sum encountered during the iteration using a variable, say maxSum, and update it whenever a greater sum is found.
# Once all iterations are complete, return maxSum as the maximum sum of all subarrays.
from typing import List

class Solution:
    # Function to find maximum sum of subarrays
    def maxSubArray(self, nums: List[int]) -> int:
        
        """ Initialize maximum sum with
         the smallest possible integer"""
        maxi = float('-inf')

        # Iterate over each starting index of subarrays
        for i in range(len(nums)):
            
            """ Variable to store the sum
             of the current subarray"""
            sum = 0
            
            """ Iterate over each ending index
             of subarrays starting from i"""
            for j in range(i, len(nums)):
                
                """ Add the current element nums[j] to
                 the sum i.e. sum of nums[i...j-1]"""
                sum += nums[j]

                """ Update maxi with the maximum of its current
                 value and the sum of the current subarray"""
                maxi = max(maxi, sum)

        # Return the maximum subarray sum found
        return maxi

# Main function to test the Solution class
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # Create an instance of Solution class
    sol = Solution()

    maxSum = sol.maxSubArray(arr)

    # Print the max subarray sum
    print(f"The maximum subarray sum is: {maxSum}")

# optimal
# kadane's algorithm
# terate through the array using a variable i. During each iteration, add the current element arr[i] to a running sum variable.
# Keep track of the maximum sum encountered during the iteration by comparing the current sum with the previous maximum sum, and update it if the current sum is greater.
# If at any point the sum becomes negative, reset it to 0, as a negative sum won't contribute positively to the overall maximum sum.
# Continue the iteration until all elements in the array are processed.
# Finally, return the maximum sum encountered during the iteration.

from typing import List

class Solution:
    # Function to find maximum sum of subarrays
    def maxSubArray(self, nums: List[int]) -> int:
        
        # maximum sum
        maxi = float('-inf') 
        
        # current sum of subarray
        sum = 0 
        
        # Iterate through the array
        for i in range(len(nums)):
            
            # Add current element to the sum
            sum += nums[i] 
            
            # Update maxi if current sum is greater
            if sum > maxi:
                maxi = sum 
            
            # Reset sum to 0 if it becomes negative
            if sum < 0:
                sum = 0 
        
        # Return the maximum subarray sum found
        return maxi

if __name__ == "__main__":
    arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]

    # Create an instance of Solution class
    sol = Solution()

    maxSum = sol.maxSubArray(arr)

    # Print the max subarray sum
    print(f"The maximum subarray sum is: {maxSum}")
