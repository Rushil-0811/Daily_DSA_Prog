# Problem Statement: Given the head of a linked list and an integer value, find out whether the integer is present in the linked list or not. Return true if it is present, or else return false.
# To check if an element is present in the linked list, traverse the entire list and at every node, check whether the data matches with the specified value. If a match is found, return true, otherwise, after traversing the entire list, return false.
# Initialise a temporary pointer to traverse the entire list.
# During the traversal, check if the data on the current node matches the specified value. If no match is found, move to the next node.
# Continue this traversal until either fast (or next node of fast) reaches null or both the pointers, slow and fast, meet.
# At any moment, if the data of the node matches with the val, stop and return true.
# If the temporary pointer reaches null without finding the required value, return false.

# Node class for Linked List
class Node:
    def __init__(self, val):
        # Store data
        self.data = val
        # Store next pointer
        self.next = None

# Solution class containing search function
class Solution:
    # Function to search for a value in LL
    def searchValue(self, head, key):
        # Pointer to traverse the list
        current = head

        # Traverse until end
        while current is not None:
            # Check if current node matches key
            if current.data == key:
                # Return True if found
                return True
            # Move to next node
            current = current.next

        # Return False if not found
        return False

# Driver code
if __name__ == "__main__":
    # Creating linked list: 10 -> 20 -> 30
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    obj = Solution()

    # Search for value
    if obj.searchValue(head, 20):
        print("Found")
    else:
        print("Not Found")
