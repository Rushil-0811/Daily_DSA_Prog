# Given an integer array nums, define the range of a non-empty contiguous subarray as the maximum element minus the minimum element. Return the sum of the ranges of all non-empty contiguous subarrays.

# Example 1
# Input: nums = [1, 2, 3]
# Output: 4
# Explanation: The subarrays are [1], [2], [3], [1, 2], [2, 3], and [1, 2, 3].

# Their corresponding ranges are 0, 0, 0, 1, 1, and 2.

# The sum of all subarray ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

# rute Force Approach
# Every subarray range is the difference between its largest and smallest values. Instead of checking each subarray again from the beginning, choose one starting index and keep extending the ending index toward the right.

# While extending, maintain the smallest and largest values found so far. Each new ending index creates one new subarray, so its range can be calculated immediately. This avoids an extra scan, although two nested loops are still needed to visit every subarray.

# Algorithm
# Initialize answer = 0 to store the sum of the ranges of all subarrays.

# Select every array index as the starting position of a subarray.

# Set currentMinimum and currentMaximum to the starting value, because the first subarray contains only that element.

# Extend the ending index from the starting position to the end of the array, so every subarray with the selected start is generated.

# Update currentMinimum with the smaller value and currentMaximum with the larger value after including each new element.

# Add currentMaximum - currentMinimum to answer, because this difference is the range of the current subarray.

# Return answer after processing every possible starting and ending index pair.

from typing import List


class Solution:
    # Return the sum of every subarray range.
    def subArrayRanges(self, nums: List[int]) -> int:
        # Store the accumulated range sum.
        answer = 0

        # Choose every possible starting index.
        for start in range(len(nums)):
            # Track extrema for the growing subarray.
            minimum = nums[start]
            maximum = nums[start]

            # Extend the current subarray to the right.
            for end in range(start, len(nums)):
                # Include the new value in both extrema.
                minimum = min(minimum, nums[end])
                maximum = max(maximum, nums[end])

                # Add the range of the current subarray.
                answer += maximum - minimum

        # Return the sum after every pair is visited.
        return answer


# Driver code
def main() -> None:
    nums = [1, 2, 3]
    obj = Solution()
    print(obj.subArrayRanges(nums))


if __name__ == "__main__":
    main()

# Complexity Analysis
# Time Complexity: O(N2), where N is the number of elements, because every possible start and end index pair is visited once.

# Space Complexity: O(1), because only the answer and the running minimum and maximum values are stored.

# Optimal Approach
# The key idea is to break the range of every subarray into two separate contributions: maximum − minimum. This means we can first calculate the sum of all subarray maximums and the sum of all subarray minimums, then subtract the latter from the former. This is similar to the contribution-based technique used in Sum of Subarray Minimums.

# Instead of generating every subarray, consider each element and count how many subarrays use it as the maximum or minimum. Monotonic stacks help find the nearest elements that can stop its contribution on the left and right. We use strict comparison on one side and non-strict comparison on the other so that duplicate values are assigned consistently and no subarray is counted more than once.

# Algorithm
# Create four boundary arrays to store the previous and next smaller and greater indices for every element.

# Traverse from left to right using monotonic stacks to find the previous smaller-or-equal and previous greater-or-equal boundaries.

# Remove equal values from the stacks while finding previous boundaries, so duplicate elements are handled consistently.

# Clear both stacks and traverse from right to left to find the next smaller and next greater boundaries.

# Keep equal values while finding next boundaries, completing the strict/non-strict comparison pattern needed to avoid duplicate counting.

# For each index, calculate the number of possible left and right boundaries using its distances from the corresponding smaller and greater elements.

# Calculate the element's contribution as a maximum using its greater boundaries and add it to the answer.

# Calculate the element's contribution as a minimum using its smaller boundaries and subtract it from the answer.

# Return answer, which now contains the sum of all subarray maximums minus the sum of all subarray minimums.

class Solution:

    # Function to find the indices of next smaller elements.
    def findNSE(self, arr):
        
        # Size of array.
        n = len(arr)
        
        # To store the answer.
        ans = [0] * n
        
        # Stack.
        st = []
        
        # Start traversing from the back.
        for i in range(n - 1, -1, -1):
            
            # Get the current element.
            currEle = arr[i]
            
            # Remove elements that are not smaller.
            while st and arr[st[-1]] >= currEle:
                st.pop()
            
            # Store the next smaller element index.
            ans[i] = st[-1] if st else n
            
            # Push the current index into the stack.
            st.append(i)
        
        # Return the answer.
        return ans

    # Function to find the indices of next greater elements.
    def findNGE(self, arr):
        
        # Size of array.
        n = len(arr)
        
        # To store the answer.
        ans = [0] * n
        
        # Stack.
        st = []
        
        # Start traversing from the back.
        for i in range(n - 1, -1, -1):
            
            # Get the current element.
            currEle = arr[i]
            
            # Remove elements that are not greater.
            while st and arr[st[-1]] <= currEle:
                st.pop()
            
            # Store the next greater element index.
            ans[i] = st[-1] if st else n
            
            # Push the current index into the stack.
            st.append(i)
        
        # Return the answer.
        return ans

    # Function to find the indices of previous smaller or equal elements.
    def findPSEE(self, arr):
        
        # Size of array.
        n = len(arr)
        
        # To store the answer.
        ans = [0] * n
        
        # Stack.
        st = []
        
        # Traverse on the array.
        for i in range(n):
            
            # Get the current element.
            currEle = arr[i]
            
            # Remove elements that are greater.
            while st and arr[st[-1]] > currEle:
                st.pop()
            
            # Store the previous smaller or equal index.
            ans[i] = st[-1] if st else -1
            
            # Push the current index into the stack.
            st.append(i)
        
        # Return the answer.
        return ans

    # Function to find the indices of previous greater or equal elements.
    def findPGEE(self, arr):
        
        # Size of array.
        n = len(arr)
        
        # To store the answer.
        ans = [0] * n
        
        # Stack.
        st = []
        
        # Traverse on the array.
        for i in range(n):
            
            # Get the current element.
            currEle = arr[i]
            
            # Remove elements that are smaller.
            while st and arr[st[-1]] < currEle:
                st.pop()
            
            # Store the previous greater or equal index.
            ans[i] = st[-1] if st else -1
            
            # Push the current index into the stack.
            st.append(i)
        
        # Return the answer.
        return ans

    # Function to find the sum of minimum values in all subarrays.
    def sumSubarrayMins(self, arr):
        
        # Find the next smaller and previous smaller or equal indices.
        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)
        
        # Size of array.
        n = len(arr)
        
        # To store the sum.
        total = 0
        
        # Traverse on the array.
        for i in range(n):
            
            # Count of possible left boundaries.
            left = i - psee[i]
            
            # Count of possible right boundaries.
            right = nse[i] - i
            
            # Count of subarrays where current element is minimum.
            freq = left * right
            
            # Contribution of the current element.
            val = freq * arr[i]
            
            # Update the sum.
            total += val
        
        # Return the computed sum.
        return total

    # Function to find the sum of maximum values in all subarrays.
    def sumSubarrayMaxs(self, arr):
        
        # Find the next greater and previous greater or equal indices.
        nge = self.findNGE(arr)
        pgee = self.findPGEE(arr)
        
        # Size of array.
        n = len(arr)
        
        # To store the sum.
        total = 0
        
        # Traverse on the array.
        for i in range(n):
            
            # Count of possible left boundaries.
            left = i - pgee[i]
            
            # Count of possible right boundaries.
            right = nge[i] - i
            
            # Count of subarrays where current element is maximum.
            freq = left * right
            
            # Contribution of the current element.
            val = freq * arr[i]
            
            # Update the sum.
            total += val
        
        # Return the computed sum.
        return total

    # Function to find the sum of all subarray ranges.
    def subArrayRanges(self, arr):
        
        # Return maximum contribution minus minimum contribution.
        return self.sumSubarrayMaxs(arr) - self.sumSubarrayMins(arr)


# Driver code
arr = [1, 2, 3]

# Creating an instance of Solution class.
sol = Solution()

# Function call to find the sum of subarray ranges.
ans = sol.subArrayRanges(arr)

print("The sum of subarray ranges is:", ans)