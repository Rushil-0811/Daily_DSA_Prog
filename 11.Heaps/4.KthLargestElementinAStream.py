# Implement a class named KthLargest for a growing stream of integers. The class must support two operations:

# - KthLargest(k, nums): Initialize rank k and the initial stream nums. - add(value): Append value and return the kth largest stream value after the insertion.

# The kth largest value follows sorted order, not distinct-value order. Duplicate values occupy separate positions. Every add call occurs after the stream contains at least k values.

# Example 1
# Input: [KthLargest(3, [4, 6, 8, 2]), add(5), add(10), add(3)]
# Output: [null, 5, 6, 6]
# Explanation: The initial stream has 8, 6, and 4 as the three largest values. Insertion of 5 changes the third largest value to 5. Insertion of 10 changes the third largest value to 6. Insertion of 3 leaves the answer at 6.

# Example 2
# Input: [KthLargest(1, []), add(-3), add(-1), add(-4)]
# Output: [null, -3, -1, -1]
# Explanation: Rank 1 asks for the largest value. The running answers become -3, -1, and -1, so negative values require no special handling.

# Brute Force Approach
# The simplest way to find the k-th largest value in a stream is to keep every value seen so far. After each new value arrives, sorting all stored values makes the required rank directly available.

# This approach is easy to understand and verify, but it repeatedly sorts the entire stream. As more values arrive, the same elements are sorted again even though only the k-th largest value is needed.

# Algorithm
# Store k and all initial stream values so every later add operation can use the complete stream.

# When a new value arrives, append it to the stored values because it becomes part of the stream.

# Copy the stored values before sorting so the original stream remains unchanged for future additions.

# Sort the copied array in descending order so the largest values appear first.

# Access index k - 1 because zero-based indexing places the k-th largest value at that position.

# Return the value at index k - 1 as the updated k-th largest element.

from typing import List


class Solution:
    # Initialize the rank and initial stream.
    def __init__(self, k: int, nums: List[int]) -> None:
        # Store the requested sorted position.
        self.rank = k
        # Preserve every initial stream value.
        self.numbers = nums.copy()

    # Add a value and return the current kth largest.
    def add(self, value: int) -> int:
        # Append the newest stream value.
        self.numbers.append(value)
        # Copy values so stream history stays unchanged.
        ordered = self.numbers.copy()
        # Sort the copy from largest to smallest.
        ordered.sort(reverse=True)
        # Rank k uses zero-based index k minus one.
        return ordered[self.rank - 1]


# Driver code
def main() -> None:
    nums = [4, 6, 8, 2]
    obj = Solution(3, nums)
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(3))


if __name__ == "__main__":
    main()

# Optimal Approach
# The brute force method rebuilds a complete order after every insertion. Only the largest k values can affect the answer. A min-heap of size k keeps exactly the useful group, and the heap root remains the smallest member of the group: the current kth largest value.

# Each new value enters the heap. A size above k removes the smallest value. Duplicate values remain separate heap entries, so the kth largest value follows sorted position rather than distinct rank.

# Algorithm
# Begin with rank k and an empty min-heap, so storage can stay limited to the largest k values.

# Feed every initial value into the heap, allowing each number to compete for a place in the top-k group.

# Remove the heap root after size exceeds k because the smallest candidate cannot remain among the largest k values.

# Reuse the same push-and-trim rule for every add call, preserving the top-k group after each insertion.

# Keep at most k values in the heap so stream growth never increases the maintained working set.

# Return the heap root because the smallest value among the largest k values has overall rank k.

import heapq
from typing import List


class Solution:
    # Initialize the tracker with the top k values.
    def __init__(self, k: int, nums: List[int]) -> None:
        # Store the requested sorted position.
        self.rank = k
        # Create an empty min-heap.
        self.min_heap: List[int] = []
        # Process every initial stream value.
        for value in nums:
            # Add a new candidate for the top k group.
            heapq.heappush(self.min_heap, value)
            # Extra size means the smallest value is unneeded.
            if len(self.min_heap) > self.rank:
                heapq.heappop(self.min_heap)

    # Add a value and return the current kth largest.
    def add(self, value: int) -> int:
        # Add a new candidate for the top k group.
        heapq.heappush(self.min_heap, value)
        # Extra size means the smallest value is unneeded.
        if len(self.min_heap) > self.rank:
            heapq.heappop(self.min_heap)
        # The smallest top-k value has overall rank k.
        return self.min_heap[0]


# Driver code
def main() -> None:
    nums = [4, 6, 8, 2]
    obj = Solution(3, nums)
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(3))


if __name__ == "__main__":
    main()