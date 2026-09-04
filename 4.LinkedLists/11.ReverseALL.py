# Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.

# The core idea is to change the next pointers of the nodes one by one so that they point backward instead of forward. By maintaining references to the current node, its previous node, and the next node, we can safely rewire the links without losing track of the list. Once all links are reversed, the last node of the original list becomes the new head.
# Initialize a traversal pointer at the head of the linked list.
# Also initialize a pointer for the previous node and set it to NULL.
# Repeat the following steps until the traversal pointer reaches the end:
# Save the next node in a temporary pointer.
# Reverse the `next` pointer of the current node to point to the previous node.
# Move the previous pointer to the current node.
# Advance the traversal pointer to the next node (saved earlier).
# Once the traversal is complete, return the previous node as the new head of the reversed list.

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    # Function to reverse a linked list iteratively
    def reverseList(self, head):
        # Initialize previous pointer to None
        prev = None

        # Start from the head of the list
        temp = head

        # Traverse the list
        while temp:
            # Save the next node
            front = temp.next

            # Reverse the current node's pointer
            temp.next = prev

            # Move prev to current node
            prev = temp

            # Move to the next node
            temp = front

        # Return new head (last node becomes first)
        return prev

# Driver code
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
# Reversing the list
newHead = sol.reverseList(head)

# Printing the reversed list
printList(newHead)
