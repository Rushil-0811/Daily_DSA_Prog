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

# Better Approach
# Sorting the whole array does more work than needed because only the k largest elements matter. A min-heap of size k keeps only these useful candidates, with the smallest among them always available at the root.

# Whenever the heap grows beyond k, remove its smallest value because it cannot remain among the current top k elements. After processing the complete array, the heap contains exactly the k largest occurrences, so its root is the k-th largest element.

# Algorithm
# Create an empty min-heap named minHeap so the smallest retained candidate always stays at the root.

# Traverse every value in nums so each occurrence gets a chance to enter the top k.

# Push the current value into minHeap because it may belong among the k largest elements.

# If the heap size becomes greater than k, remove the root because the smallest candidate is no longer needed.

# Keep duplicate values as separate heap entries because each occurrence has its own rank in sorted order.

# After processing all elements, return the heap root because it is the smallest value among the k largest elements, making it the k-th largest.

import heapq
from typing import List


class Solution:
    # Finds the kth largest value with a size-k heap.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap: List[int] = []

        # Process every value as a ranked candidate.
        for value in nums:
            # Add the current value to the candidate heap.
            heapq.heappush(min_heap, value)

            # An overflow contains one unnecessary value.
            if len(min_heap) > k:
                # Remove the smallest candidate after overflow.
                heapq.heappop(min_heap)

        # The root is smallest among the top k values.
        return min_heap[0]


# Driver code
def main() -> None:
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    obj = Solution()
    print(obj.findKthLargest(nums, k))


if __name__ == "__main__":
    main()