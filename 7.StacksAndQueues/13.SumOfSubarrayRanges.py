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

