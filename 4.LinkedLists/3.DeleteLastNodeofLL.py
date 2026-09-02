# Given a Linked List, delete the tail of the list and print the updated list.
# To delete the tail of a linked list, we update the linkage between its last node and its second last node. The main intuition is to point the second last node to null to get the updated linked list.

# Some edge cases to consider is when the list is empty or when there is only one node in the entire list.
# If the list is empty, return immediately as there is nothing to delete.
# If list has only one node, delete the node and return an empty list.
# Traverse the linked list to the second last node and keep track of it using the tail pointer.
# Set the next pointer of the second last node to null. This step effectively disconnects the initial tail node from the list, making second last node as the new tail node.
# Deallocate the memory occupied by the tail node by deleting it.
# Return the head of the doubly linked list as the result.

# Definition for singly linked list
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    # Function to delete tail node of linked list
    def deleteTail(self, head):
        # If list is empty or has one node
        if head is None or head.next is None:
            return None

        # Traverse to the second last node
        curr = head
        while curr.next.next is not None:
            curr = curr.next

        # Delete tail node
        curr.next = None

        # Return updated head
        return head

# Driver code
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

obj = Solution()
head = obj.deleteTail(head)

# Print list after deletion
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
