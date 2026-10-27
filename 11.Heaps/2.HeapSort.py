# An integer array arr is given. Rearrange every value in non-decreasing order with the Heap Sort algorithm.

# Use a max heap inside the array, move one greatest active value into a final position during every extraction, and return the sorted array.

# Example 1
# Input: arr = [4, 10, 3, 5, 1]
# Output: [1, 3, 4, 5, 10]
# Explanation: Max-heap construction produces [10, 5, 3, 4, 1]. Repeated root swaps place 10, 5, 4, and 3 into final positions from right to left.

# Example 2
# Input: arr = [7]
# Output: [7]
# Explanation: A single value already occupies the correct position, so heap construction and extraction require no swap.

# Approach
# Heap Sort avoids repeatedly scanning the unsorted part to find the largest value. A max heap keeps the largest value at the root, so the next maximum is always available at index 0. Since leaf nodes already satisfy the heap property, heap construction starts from the last parent at index (n / 2) - 1.

# After building the max heap, swap the root with the last position of the active heap. This places the current maximum in its final sorted position. Then reduce the heap size and apply sift-down from the root to restore the max-heap property. Repeating this process gradually builds the sorted array from right to left.

# Algorithm
# Treat the array as a complete binary tree, where the children of index i are at 2 * i + 1 and 2 * i + 2.

# Start heap construction from (n / 2) - 1 and move toward index 0, because all later positions are leaf nodes and already satisfy the heap property.

# For each parent, compare it with its valid children to find the largest value.

# If a child is larger than the parent:

# Swap the parent with the larger child because the greater value must move upward in a max heap.

# Continue sift-down from the swapped position until the heap property is restored.

# After building the heap, the maximum value stays at index 0.

# Swap the root with arr[end], because the maximum value can now be placed at the end of the unsorted region.

# Reduce the active heap size and sift down from the root, because the root swap may break the max-heap property.

# Repeat extraction until only one active element remains, then return the sorted array.

from typing import List


class Solution:
    # Restores max-heap order from a root index.
    def _heapify(
        self, arr: List[int], heap_size: int, root: int
    ) -> None:
        # Continue until the displaced value reaches a valid spot.
        while True:
            # Start with the current root as the largest value.
            largest = root

            # Locate both children in the array-based tree.
            left = 2 * root + 1
            right = 2 * root + 2

            # A larger left child becomes the swap target.
            if left < heap_size and arr[left] > arr[largest]:
                largest = left

            # A larger right child becomes the swap target.
            if right < heap_size and arr[right] > arr[largest]:
                largest = right

            # Heap order needs no change at the current root.
            if largest == root:
                break

            # Move the largest child into the parent position.
            arr[root], arr[largest] = arr[largest], arr[root]

            # Continue from the displaced value position.
            root = largest

    # Sorts an array in ascending order with a max heap.
    def heapSort(self, arr: List[int]) -> List[int]:
        n = len(arr)

        # Build the max heap from the lowest parent upward.
        for root in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, root)

        # Move every current maximum into the sorted suffix.
        for end in range(n - 1, 0, -1):
            # Place the maximum at the next final position.
            arr[0], arr[end] = arr[end], arr[0]

            # Restore heap order inside the reduced prefix.
            self._heapify(arr, end, 0)

        # Return the completed ascending order.
        return arr


# Driver code
def main() -> None:
    arr = [4, 10, 3, 5, 1]
    obj = Solution()
    answer = obj.heapSort(arr)
    print(answer)


if __name__ == "__main__":
    main()