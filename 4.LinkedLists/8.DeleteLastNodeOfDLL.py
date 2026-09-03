# To delete the tail of a doubly linked list, we update the linkage between its last node and its second last node. Since a doubly linked list is bidirectional, we set the second last node's next pointer and the last node's back pointer to null. Then, we can return the head of the doubly linked list as the result.

# Some edge cases to consider is when the list is empty or when there is only one node in the entire list.
# If the list is empty, return immediately as there is nothing to delete.
# If list has only one node, delete the node and return an empty list.
# Traverse the doubly linked list to the last node and keep track of it using the tail pointer.
# Access the second last node using the tail's back pointer
# Set the next pointer of the second last node to null. This step effectively disconnects the initial tail node from the list in the forward direction, making second last node as the new tail node.
# Set the back pointer of the tail node to null. This ensures that the tail node no longer points back to the second last node.
# Return the head of the doubly linked list as the result.

# Node structure for DLL
class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

class Solution:
    # Function to delete tail of DLL
    def deleteTail(self, head):
        # If list is empty
        if not head:
            return None

        # If only one node present
        if not head.next:
            return None

        # Traverse to the last node
        temp = head
        while temp.next:
            temp = temp.next

        # Update second last node's next to None
        temp.prev.next = None

        # Return head
        return head

# Driver code
if __name__ == "__main__":
    # Create a sample DLL: 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    obj = Solution()
    head = obj.deleteTail(head)

    # Print list after deletion
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
