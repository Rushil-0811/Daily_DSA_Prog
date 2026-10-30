# Design a class for a growing stream of integers. The class must support two operations:

# - addNum(value): Add value to the stream. - findMedian(): Return the median of all values added so far.

# An odd-sized ordered stream has one middle value. An even-sized ordered stream has a median equal to the average of the two middle values. Every findMedian call occurs after at least one insertion.

# Example 1
# Input: [Solution(), addNum(1), addNum(2), findMedian(), addNum(3), findMedian()]
# Output: [null, null, null, 1.5, null, 2.0]
# Explanation: Values [1, 2] have two middle positions, so the first median equals (1 + 2) / 2 = 1.5. Values [1, 2, 3] have middle value 2, so the second median equals 2.0.

# Example 2
# Input: [Solution(), addNum(-5), addNum(-5), findMedian(), addNum(10), findMedian()]
# Output: [null, null, null, -5.0, null, -5.0]
# Explanation: Duplicate values occupy separate positions. Ordered values [-5, -5] produce median -5.0, and ordered values [-5, -5, 10] also produce median -5.0.

# Brute Force Approach
# The easiest starting point saves every arriving value. No ordering work is needed during insertion, so each new number simply joins the stored stream.

# A median query creates a sorted copy. Sorting exposes the middle position directly, but repeated queries rebuild the same order again and again. Long streams therefore make the simple method expensive.

# Algorithm
# Begin with an empty list of stream values, allowing each insertion to preserve the complete history without extra ordering work.

# Append every new value to the list because a later median query depends on every occurrence, including duplicates.

# Copy the stored list during findMedian, preserving the insertion storage while a temporary ordered view is prepared.

# Sort the copied values in ascending order because direct middle indices define the median in an ordered collection.

# Return index n / 2 for an odd size because zero-based indexing places the single middle value at index n / 2.

# Average indices n / 2 - 1 and n / 2 for an even size, using two half-values to avoid integer overflow during addition.

from typing import List


class Solution:
    # Create empty stream storage.
    def __init__(self) -> None:
        self.numbers: List[int] = []

    # Add one value to the stored stream.
    def addNum(self, value: int) -> None:
        # Preserve the newest stream value.
        self.numbers.append(value)

    # Return the median after sorting a copied stream.
    def findMedian(self) -> float:
        # Sort a copy so insertion storage stays unchanged.
        ordered = sorted(self.numbers)
        size = len(ordered)
        middle = size // 2

        # Odd size has one value at the middle index.
        if size % 2 == 1:
            return float(ordered[middle])

        # Half-value addition avoids integer overflow.
        return ordered[middle - 1] / 2.0 + ordered[middle] / 2.0


# Driver code
def main() -> None:
    obj = Solution()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())


if __name__ == "__main__":
    main()

# Better Approach
# The brute force method repeats a full sort for every query. A sorted list keeps earlier ordering work and places each arriving value directly into the correct position.

# The middle value then stays available without another sort. Array insertion can shift many larger values, so updates remain linear even though median queries become constant time.

# Algorithm
# Begin with an empty sorted list, preserving ascending order from the first insertion onward.

# Locate the first position containing a value not smaller than the new value, keeping duplicate placement valid and predictable.

# Insert the new value at the located position because all earlier entries are smaller and all later entries are at least as large.

# Shift later array entries because array insertion must open one position while preserving the complete sorted order.

# Return index n / 2 for an odd size because the sorted list exposes the single middle value immediately.

# Average indices n / 2 - 1 and n / 2 for an even size, avoiding another traversal or sorting pass.

from bisect import insort_left
from typing import List


class Solution:
    # Create empty sorted stream storage.
    def __init__(self) -> None:
        self.ordered: List[int] = []

    # Add one value while preserving sorted order.
    def addNum(self, value: int) -> None:
        # Insert before the first value not smaller.
        insort_left(self.ordered, value)

    # Return the median from the sorted stream.
    def findMedian(self) -> float:
        size = len(self.ordered)
        middle = size // 2

        # Odd size has one value at the middle index.
        if size % 2 == 1:
            return float(self.ordered[middle])

        # Half-value addition avoids integer overflow.
        return (
            self.ordered[middle - 1] / 2.0
            + self.ordered[middle] / 2.0
        )


# Driver code
def main() -> None:
    obj = Solution()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())


if __name__ == "__main__":
    main()

# Optimal Approach
# The sorted-list method maintains more order than a median actually needs. We only need to separate the values into a smaller half and a larger half. A max-heap stores the smaller half, while a min-heap stores the larger half, so the two values closest to the median are always available at the heap roots.

# The approach maintains two important invariants after every insertion:

# Every value in the max-heap is less than or equal to every value in the min-heap.

# The max-heap has either the same number of values as the min-heap or exactly one extra value.

# These invariants keep the median at the boundary between the two heaps.

# Algorithm
# Create a max-heap for the smaller half and a min-heap for the larger half.

# For every new value:

# Insert it into the max-heap first.

# Move the max-heap root to the min-heap so that every value in the smaller half remains less than or equal to every value in the larger half.

# If the min-heap becomes larger, move its root back to the max-heap so the max-heap has either the same size or one extra value.

# After every insertion, maintain the invariant that:

# all max-heap values are <= all min-heap values, and

# maxHeap.size() is either equal to minHeap.size() or exactly one greater.

# For an odd number of values, return the max-heap root because it contains the single middle value.

# For an even number of values, return the average of both heap roots because they are the two middle values.

import heapq
from typing import List


class Solution:
    # Create two empty stream halves.
    def __init__(self) -> None:
        self.lower: List[int] = []
        self.upper: List[int] = []

    # Add one value and restore both heap rules.
    def addNum(self, value: int) -> None:
        # Negation turns the lower heap into a max-heap.
        heapq.heappush(self.lower, -value)
        # Move the largest lower value across the boundary.
        moved = -heapq.heappop(self.lower)
        heapq.heappush(self.upper, moved)

        # Extra upper size must return one middle value.
        if len(self.upper) > len(self.lower):
            moved_back = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -moved_back)

    # Return the median from the heap boundary.
    def findMedian(self) -> float:
        # Equal sizes place two values at the middle.
        if len(self.lower) == len(self.upper):
            # Half-value addition avoids integer overflow.
            return -self.lower[0] / 2.0 + self.upper[0] / 2.0

        # Extra lower value becomes the single middle.
        return float(-self.lower[0])


# Driver code
def main() -> None:
    obj = Solution()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())


if __name__ == "__main__":
    main()