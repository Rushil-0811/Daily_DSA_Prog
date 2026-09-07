# Problem Statement: Given a linked list, sort its nodes based on the data value in them. Return the head of the sorted linked list.
# To sort a given linked list, we can simply create an array of all the elements of the linked list. Now, we can sort this array using any sorting technique and reassign the values of the sorted array to our linked list. This modified linked list will have all the elements in sorted order.
# Create an empty array to store the node values. Iterate the linked list using a temporary pointer to the head and push the value of temporary node into the array.
# Sort the array containing node values in ascending order.
# Convert the sorted array back to a linked list reassigning the values from the sorted array and overwriting them sequentially according to their order in the array.

# Node class represents a linked list node
class Node:
    # Constructor with data and next pointer
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node
        self.next = next1

# Solution class to hold sorting function
class Solution:
    # Function to sort the linked list
    def sortLL(self, head):
        # List to store node values
        arr = []

        # Pointer to traverse the list
        temp = head

        # Traverse and push values into list
        while temp is not None:
            arr.append(temp.data)
            temp = temp.next

        # Sort the list
        arr.sort()

        # Reassign sorted values to list nodes
        temp = head
        for val in arr:
            temp.data = val
            temp = temp.next

        # Return head of sorted list
        return head

# Function to print linked list
def printLinkedList(head):
    # Pointer to traverse list
    temp = head

    # Traverse and print values
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Driver code
if __name__ == "__main__":
    # Create linked list: 3 -> 2 -> 5 -> 4 -> 1
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(5)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(1)

    # Print original list
    print("Original Linked List:", end=" ")
    printLinkedList(head)

    # Create Solution object
    obj = Solution()

    # Sort the linked list
    head = obj.sortLL(head)

    # Print sorted list
    print("Sorted Linked List:", end=" ")
    printLinkedList(head)

# optimal
# Instead of using an external array to store node values, we can try to implement similar sorting techniques for linked lists as well. In order to sort the linked list, we can try to implement a modified version of Merge Sort Algorithm. This algorithm would divide the linked list into halves recursively until single nodes remain. These sorted halves of the linked list are merged back together in a sorted order.
# If the linked list is empty or has only one node, it is already sorted, thus we can return the head directly.
# Use the slow and fast pointer technique to find the middle of the linked list, where slow moves one step and fast moves two steps at a time.
# Split the linked list into two halves at the midpoint by pointing middle to null, where the left half starts from the head and the right half starts from the node after the middle.
# Recursively apply merge sort on both halves of the linked list until each part is broken down into single nodes or empty lists.
# Merge the two sorted halves using a helper function that compares node values from both halves, attaches the smaller one to the result list, and continues until all nodes from both halves are merged.
# Return the head of the merged and fully sorted linked list, which will represent the final sorted list.
# Node class represents a linked list node
class Node:
    # Constructor with data and next pointer
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node
        self.next = next1

# Solution class contains merge sort logic
class Solution:
    # Function to merge two sorted linked lists
    def mergeTwoSortedLinkedLists(self, list1, list2):
        # Create a dummy node
        dummyNode = Node(-1)
        
        # Temp pointer to build merged list
        temp = dummyNode

        # Traverse both lists
        while list1 and list2:
            # Choose smaller node
            if list1.data <= list2.data:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            # Move temp pointer
            temp = temp.next

        # Attach remaining nodes
        if list1:
            temp.next = list1
        else:
            temp.next = list2

        # Return head of merged list
        return dummyNode.next

    # Function to find middle of linked list
    def findMiddle(self, head):
        # If list empty or single node
        if not head or not head.next:
            return head

        # Slow and fast pointers
        slow = head
        fast = head.next

        # Move fast twice as fast as slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Return middle node
        return slow

    # Function to perform merge sort
    def sortLL(self, head):
        # Base case: empty or single node
        if not head or not head.next:
            return head

        # Find middle node
        middle = self.findMiddle(head)

        # Split into two halves
        right = middle.next
        middle.next = None
        left = head

        # Recursively sort both halves
        left = self.sortLL(left)
        right = self.sortLL(right)

        # Merge sorted halves
        return self.mergeTwoSortedLinkedLists(left, right)

# Function to print linked list
def printLinkedList(head):
    # Temp pointer to traverse
    temp = head

    # Traverse and print nodes
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Driver code
if __name__ == "__main__":
    # Create linked list: 3 -> 2 -> 5 -> 4 -> 1
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(5)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(1)

    # Print original list
    print("Original Linked List:", end=" ")
    printLinkedList(head)

    # Create Solution object
    obj = Solution()

    # Sort the linked list
    head = obj.sortLL(head)

    # Print sorted list
    print("Sorted Linked List:", end=" ")
    printLinkedList(head)

