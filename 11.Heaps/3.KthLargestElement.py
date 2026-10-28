# An integer array nums and a positive integer k are given. Arrange every array occurrence by value from largest to smallest and consider every duplicate occurrence as a separate position.

# Return the value occupying position k in the descending order.

# Example 1
# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
# Output: 4
# Explanation: Descending order becomes [6, 5, 5, 4, 3, 3, 2, 2, 1]. Position 4 contains 4, and both occurrences of 5 occupy separate positions.

# Example 2
# Input: nums = [7], k = 1
# Output: 7
# Explanation: A single-element array has the same value as the largest and smallest ranked element.

# Brute Force Approach
# Sorting the complete array makes the k-th largest element easy to locate. After sorting in ascending order, the k-th largest value appears at index n - k.

# This approach is simple and provides a clear baseline, but it sorts all elements even though only one value is required.

# Algorithm
# Copy nums into sortedNums so the original array remains unchanged.

# Sort sortedNums in ascending order so every element gets its correct sorted position.

# Store the array size in n because the k-th largest position depends on the total number of elements.

# Calculate the required index as n - k, because the k-th largest element appears at that position in ascending order.

# Return sortedNums[n - k] as the k-th largest element.

from typing import List


class Solution:
    # Finds the kth largest value by sorting a copy.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sort a copied list in ascending order.
        sorted_nums = sorted(nums)

        n = len(sorted_nums)

        # Convert the descending rank to an ascending index.
        target_index = n - k

        # Read the value stored at the required rank.
        return sorted_nums[target_index]


# Driver code
def main() -> None:
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    obj = Solution()
    print(obj.findKthLargest(nums, k))


if __name__ == "__main__":
    main()