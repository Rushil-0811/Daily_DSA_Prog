# Given the head of a linked list, print the length of the linked list.
# The simple idea to solve this problem is to traverse the linked list and count the number of nodes using a counter.
# Initialize a temporary pointer to the head of the list. The temporary pointer will be used to traverse the list.
# Traverse the linked list until the the current node is not null.
# At every node, increment the counter to count number of nodes.
# After reaching the end of the linked list, return the count. This will be your total number of nodes which is the length of the linked list.

# Node class to represent each element in the linked list
class Node:
    # Constructor to initialize data and next pointer
    def __init__(self, data1):
        self.data = data1
        self.next = None

# Solution class containing the method to find length
class Solution:
    # Function to find the length of the linked list
    def lengthOfLinkedList(self, head):
        # Initialize counter to 0
        count = 0

        # Initialize a temporary pointer to head
        temp = head

        # Traverse the linked list
        while temp is not None:
            # Increment count for each node
            count += 1

            # Move to the next node
            temp = temp.next

        # Return the total count
        return count

# Driver code
if __name__ == "__main__":
    # Creating a sample linked list
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    # Create Solution object
    obj = Solution()

    # Find and print the length of linked list
    print("Length of Linked List:",
          obj.lengthOfLinkedList(head))
