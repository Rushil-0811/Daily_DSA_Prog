# # You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'. Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, the sum of the division's result is less than or equal to the given threshold value.
# # Example 1:
# Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
# Result: 3
# Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
# The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

# brute 
# We will run a loop from 1 to max element of the array to check all possible divisors.
# To calculate the result, we will iterate over the given array using a loop. Within this loop, we will divide each element in the array by the current divisor, and sum up the obtained ceiling values.
# Inside the outer loop, If result <= threshold: We will return d as our answer.
# Finally, if we are outside the nested loops, we will return -1.
import math

class Solution:
    def smallestDivisor(self, arr, limit):
        n = len(arr)

        # Find the maximum element in the array
        max_val = max(arr)

        # Try all possible divisors from 1 to max_val
        for d in range(1, max_val + 1):
            total = 0
            for num in arr:
                # Divide each number by d and round up
                total += math.ceil(num / d)
            
            # If the total sum is within the limit, return this divisor
            if total <= limit:
                return d

        return -1  # If no such divisor found

# Driver code
arr = [1, 2, 3, 4, 5]
limit = 8
obj = Solution()
ans = obj.smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)

# optimal
# First, check if the number of elements is already greater than the allowed limit. If so, no answer is possible, so return -1.
# Then, identify the largest number in the list.
# Start with two markers , one at the smallest possible number (1), and another at the largest number in the list.
# Use a loop to narrow down the range. In each step, find the number that is in the middle of the current range.
# Check if using this middle number as a divisor results in a total that is within the allowed limit. This is done using a helper that adds up the rounded-up results of each division.
# If the result is within the allowed limit, it means this number might work, but a smaller one could be better. So, look in the lower half of the current range.
# If the result is too large, it means this number is too small. So, look in the upper half of the range instead.
# Repeat this process until the range closes. The smallest number that works will be pointed to by the left marker, and that's the answer.
import math

class SmallestDivisorFinder:
    # Helper method to calculate sum by divisor
    def sumByD(self, arr, div):
        return sum(math.ceil(x / div) for x in arr)

    # Method to find the smallest divisor using binary search
    def smallestDivisor(self, arr, limit):
        if len(arr) > limit:
            return -1

        low = 1
        high = max(arr)

        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(arr, mid) <= limit:
                high = mid - 1  # Try smaller divisor
            else:
                low = mid + 1   # Try larger divisor

        return low

# Driver code
solver = SmallestDivisorFinder()
arr = [1, 2, 3, 4, 5]
limit = 8
print("The minimum divisor is:", solver.smallestDivisor(arr, limit))
