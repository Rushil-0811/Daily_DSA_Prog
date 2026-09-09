#  Given the head of a doubly linked list with its values sorted in non-decreasing order. Remove all duplicate occurrences of any value in the list so that only distinct values are present in the list.

# Return the head of the modified linked list.
# Input: head -> 1 <-> 1 <-> 3 <-> 3 <-> 4 <-> 5

# Output: head -> 1 <-> 3 <-> 4 <-> 5
# Explanation: Duplicate occurences of 1 and 3 are deleted
# Input: head -> 1 <-> 1 <-> 1 <-> 1 <-> 1 <-> 2

# Output: head -> 1 <-> 2
# Explanation: All duplicate occurences of 1 is deleted

# Since the list is sorted in non-decreasing order, any duplicates will always be adjacent.Compare each node with the next node. If they have the same value, skip the duplicate node (and delete it).
# Start at the head of the list and traverse until the current node and the next node are not null.
# If the next node has the same value as the current node:
# Move forward until you find a node with a different value.
# Delete all the duplicate nodes in between.
# Link the current node to the first different node found.
# If the next node has a different value, move to the next node.
# Continue this process until the end of the list and return the head of the modified list.

# Node class representing a node in a doubly linked list
class Node:
    def __init__(self, value):
        self.data = value      
        self.prev = None       
        self.next = None       

# Solution class containing methods to manipulate the doubly linked list
class Solution:
    def __init__(self):
        self.head = None

    # Function to insert a node at the end of the list
    def insertAtEnd(self, value):
        newNode = Node(value)

        # If list is empty, set new node as head
        if self.head is None:
            self.head = newNode
            return

        current = self.head
        while current.next:
            current = current.next

        # Link the new node at the end
        current.next = newNode
        newNode.prev = current

    # Function to remove duplicate values from a sorted doubly linked list
    def removeDuplicates(self):
        # If the list is empty, return None
        if not self.head:
            return None

        current = self.head

        # Traverse the list until the second last node
        while current and current.next:
            nextDistinct = current.next

            # Skip all nodes with the same value as current
            while nextDistinct and nextDistinct.data == current.data:
                nextDistinct = nextDistinct.next

            # Connect current node to the next distinct node
            current.next = nextDistinct
            if nextDistinct:
                nextDistinct.prev = current

            # Move to the next node
            current = current.next

        return self.head

    # Function to print the list
    def printList(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Driver code
if __name__ == "__main__":
    sol = Solution()

    # Initial list values (with duplicates)
    values = [1, 2, 2, 2, 3, 4, 4, 5, 5, 6]

    for value in values:
        sol.insertAtEnd(value)

    # Print the original list
    print("Original List: ", end="")
    sol.printList()

    # Remove duplicate nodes
    sol.removeDuplicates()

    # Print the updated list
    print("After Removing Duplicates (keeping 1 occurrence): ", end="")
    sol.printList()
