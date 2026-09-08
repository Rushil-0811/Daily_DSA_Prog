# Given the head of a singly linked list containing integers, shift the elements of the linked list to the right by k places and return the head of the modified list. Do not change the values of the nodes, only change the links between nodes.

# Input : head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output : head -> 4 -> 5 -> 1 -> 2 -> 3
# Explanation :List after 1 shift to right: head -> 5 -> 1 -> 2 -> 3 -> 4.
# List after 2 shift to right: head -> 4 -> 5 -> 1 -> 2 -> 3.

# When asked to rotate a linked list to the right k times, we are essentially moving the last node to the front of the list, k times. Each rotation means: take the last node, disconnect it from the list, insert it at the front (head) of the list. We repeat this process k times. This approach is straightforward but not efficient because each rotation requires a traversal to the second-last node, which takes linear time. So in total, if we rotate k times and for each rotation we traverse the list (of n nodes), hence this approach is inefficient for large inputs.
# If the linked list is empty or has only one node, or k is 0, return the head as-is.
# Repeat the following steps k times:
# Initialize a pointer to traverse the list from head.
# Traverse to the second-last node of the list.
# Store the last node separately.
# Make the second-last node point to null (removing the last node).
# Insert the stored last node at the beginning by:
# Pointing its next to the current head.
# Updating the head to this node.
# Return the new head of the list.

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to rotate the list to the right by k positions
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # If list is empty or has one node or no rotation needed
        if not head or not head.next or k == 0:
            return head

        # Repeat the rotation k times
        for _ in range(k):
            # Initialize two pointers
            curr = head
            prev = None

            # Traverse to the last node
            while curr.next:
                prev = curr
                curr = curr.next

            # Remove last node and move it to front
            prev.next = None
            curr.next = head
            head = curr

        # Return the rotated list
        return head

# Driver code
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next

# Create linked list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
k = 2
newHead = sol.rotateRight(head, k)
printList(newHead)

# optimal
# When we rotate a linked list to the right by k positions, each node is effectively shifted forward k steps. Instead of performing k individual rotations, we observe that rotating a list by its own length results in the same list. So, we only need to rotate by k % length. We first compute the length of the list and connect the last node to the head, forming a circular linked list. Then we locate the new tail, which is at length - (k % length) steps from the start. The node next to this becomes the new head, and we break the circular link there. This transforms the list in a single traversal, making the process efficient.
# Handle edge cases where the list is empty, has one node, or k is 0 — in these cases, return head as-is.
# Traverse the list to calculate its total length.
# Connect the last node to the first node, converting the list into a circular linked list.
# Calculate effective rotations as k % length to avoid unnecessary full rotations.
# Find the new tail node, which is located at the (length - k % length - 1)th position from the start.
# Set the new head to the node just after the new tail.
# Break the circular link by setting newTail.next = null.
# Return the new head of the rotated list.
# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to rotate the linked list to the right by k places
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # If list is empty or has only one node or no rotation
        if not head or not head.next or k == 0:
            return head

        # Calculate the length and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Make it a circular linked list
        tail.next = head

        # Calculate effective rotations
        k = k % length

        # Find the new tail (length - k steps)
        stepsToNewTail = length - k
        newTail = head
        for _ in range(stepsToNewTail - 1):
            newTail = newTail.next

        # Set new head
        newHead = newTail.next

        # Break the circle
        newTail.next = None

        return newHead

# Driver code
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Create linked list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
obj = Solution()
newHead = obj.rotateRight(head, k)
printList(newHead)
