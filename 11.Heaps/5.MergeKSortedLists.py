# Given an array lists containing the heads of k singly linked lists, merge every node into one linked list sorted in non-decreasing order. Every input list is already sorted in non-decreasing order. Return the head of the merged list.

# Example 1
# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Explanation: The smallest available values appear in the order 1, 1, 2, 3, 4, 4, 5, 6, so the merged linked list follows the same order.

# Example 2
# Input: lists = []
# Output: []
# Explanation: An empty collection contains no nodes, so the merged head is empty.

# Brute Force Approach
# The simplest way is to collect all node values from the k sorted linked lists into one array. Once all values are available together, sorting the array directly gives the final merged order.

# After sorting, build a new linked list using these values. This approach is easy to understand, but it does not use the fact that the input lists are already sorted.

# Algorithm
# Create an empty array named values to store all node values.

# Traverse every linked list and add each node value to values, because every element must appear in the final merged list.

# Sort values in non-decreasing order so all elements are arranged correctly.

# Create a dummy node and keep a tail pointer, because this makes building the new list simpler.

# Traverse the sorted values array:

# Create a new node for each value.

# Attach it after tail.

# Move tail to the newly created node.

# Return dummy.next because it points to the first node of the merged sorted list.

from typing import List, Optional


class ListNode:
    # Creates one linked-list node.
    def __init__(self, value: int) -> None:
        self.val = value
        self.next: Optional[ListNode] = None


class Solution:
    # Builds a linked list from fixed values.
    def _build_list(
        self, values: List[int]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        # Append every value in the supplied order.
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next

        return dummy.next

    # Prints all values in one linked list.
    def _print_list(
        self, head: Optional[ListNode]
    ) -> None:
        values: List[str] = []
        current = head

        # Collect display values from head to tail.
        while current is not None:
            values.append(str(current.val))
            current = current.next

        print(" ".join(values))

    # Merges all lists by sorting every value.
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # Store every node value for global sorting.
        values: List[int] = []

        # Visit every list because every node is required.
        for head in lists:
            current = head

            # Collect values until the current list ends.
            while current is not None:
                values.append(current.val)
                current = current.next

        # Arrange all collected values in final order.
        values.sort()

        # Use a dummy node to simplify first insertion.
        dummy = ListNode(0)
        tail = dummy

        # Build a fresh list from the sorted values.
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next

        # Skip the temporary dummy node in the result.
        return dummy.next

    # Runs the given example.
    def run(self) -> None:
        lists = [
            self._build_list([1, 4, 5]),
            self._build_list([1, 3, 4]),
            self._build_list([2, 6]),
        ]

        self._print_list(self.mergeKLists(lists))


# Driver code
def main() -> None:
    obj = Solution()
    obj.run()


if __name__ == "__main__":
    main()

# Better Approach
# The input lists are already sorted, so sorting all values again wastes useful information. Instead, merge two sorted lists at a time and keep the merged result sorted after every step.

# Each merge reuses the existing nodes and needs no extra values array. However, the growing merged list may be traversed again for every new list, so the total work can become large when many lists are present.

# Algorithm
# Initialize merged = null so the first list can become the starting result.

# Process each linked list one by one and merge it with merged, because both lists are already sorted.

# For each two-list merge, create a dummy node and a tail pointer to simplify attaching nodes.

# Compare the current nodes of both lists:

# Attach the node with the smaller value because it must come next in sorted order.

# Move only the pointer of the chosen node.

# Move tail forward after attaching the node.

# When one list becomes empty, attach the remaining part of the other list because it is already sorted.

# Update merged with the newly merged list after each step.

# Return merged after all input lists have been processed.

from typing import List, Optional


class ListNode:
    # Creates one linked-list node.
    def __init__(self, value: int) -> None:
        self.val = value
        self.next: Optional[ListNode] = None


class Solution:
    # Merges two sorted linked lists in place.
    def _merge_two(
        self,
        first: Optional[ListNode],
        second: Optional[ListNode],
    ) -> Optional[ListNode]:
        # Use a dummy node to simplify first attachment.
        dummy = ListNode(0)
        tail = dummy

        # Compare heads while both lists contain nodes.
        while first is not None and second is not None:
            # Choose first when the first value is smaller.
            if first.val <= second.val:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next

            tail = tail.next

        # Append the sorted suffix still containing nodes.
        if first is not None:
            tail.next = first
        else:
            tail.next = second

        return dummy.next

    # Builds a linked list from fixed values.
    def _build_list(
        self, values: List[int]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        # Append every value in the supplied order.
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next

        return dummy.next

    # Prints all values in one linked list.
    def _print_list(
        self, head: Optional[ListNode]
    ) -> None:
        values: List[str] = []
        current = head

        # Collect display values from head to tail.
        while current is not None:
            values.append(str(current.val))
            current = current.next

        print(" ".join(values))

    # Merges lists from left to right.
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        merged: Optional[ListNode] = None

        # Grow one sorted result with each input list.
        for head in lists:
            merged = self._merge_two(merged, head)

        return merged

    # Runs the given example.
    def run(self) -> None:
        lists = [
            self._build_list([1, 4, 5]),
            self._build_list([1, 3, 4]),
            self._build_list([2, 6]),
        ]

        self._print_list(self.mergeKLists(lists))


# Driver code
def main() -> None:
    obj = Solution()
    obj.run()


if __name__ == "__main__":
    main()

# Optimal Approach
# Since every linked list is already sorted, the next node in the merged list must be the smallest among the current list heads. A min-heap helps find this node quickly without checking all k lists every time.

# Keep only one active node from each list in the heap. After removing the smallest node, add its next node from the same list. This keeps the heap size at most k and builds the merged list in sorted order.

# Algorithm
# Create a min-heap ordered by node value so the smallest current node is always available at the top.

# Insert the head of every non-empty linked list because each head is the smallest remaining node from that list.

# Create a dummy node and keep a tail pointer to simplify building the merged list.

# While the heap is not empty:

# Remove the smallest node from the heap because it must be the next node in sorted order.

# Attach this node after tail.

# Move tail to the attached node.

# If the removed node has a next node, insert that next node into the heap because it becomes the new candidate from the same list.

# Return dummy.next because it points to the first node of the completely merged sorted list.

import heapq
from typing import List, Optional, Tuple


class ListNode:
    # Creates one linked-list node.
    def __init__(self, value: int) -> None:
        self.val = value
        self.next: Optional[ListNode] = None


class Solution:
    # Builds a linked list from fixed values.
    def _build_list(
        self, values: List[int]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        # Append every value in the supplied order.
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next

        return dummy.next

    # Prints all values in one linked list.
    def _print_list(
        self, head: Optional[ListNode]
    ) -> None:
        values: List[str] = []
        current = head

        # Collect display values from head to tail.
        while current is not None:
            values.append(str(current.val))
            current = current.next

        print(" ".join(values))

    # Merges all lists with a min-heap.
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # Store value, unique order, and node together.
        min_heap: List[Tuple[int, int, ListNode]] = []
        order = 0

        # Insert every available list head as a candidate.
        for head in lists:
            # Empty lists provide no heap candidate.
            if head is not None:
                heapq.heappush(
                    min_heap, (head.val, order, head)
                )
                order += 1

        # Use a dummy node to simplify first attachment.
        dummy = ListNode(0)
        tail = dummy

        # Extract the smallest remaining candidate.
        while min_heap:
            _, _, smallest = heapq.heappop(min_heap)

            tail.next = smallest
            tail = tail.next

            # Add the next candidate from the same list.
            if smallest.next is not None:
                next_node = smallest.next
                heapq.heappush(
                    min_heap,
                    (next_node.val, order, next_node)
                )
                order += 1

        # End the result after the final selected node.
        tail.next = None

        return dummy.next

    # Runs the given example.
    def run(self) -> None:
        lists = [
            self._build_list([1, 4, 5]),
            self._build_list([1, 3, 4]),
            self._build_list([2, 6]),
        ]

        self._print_list(self.mergeKLists(lists))


# Driver code
def main() -> None:
    obj = Solution()
    obj.run()


if __name__ == "__main__":
    main()