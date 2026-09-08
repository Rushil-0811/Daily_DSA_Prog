# Problem Statement: Given a linked list containing ‘N’ head nodes where every node in the linked list contains two pointers:

# ‘Next’ points to the next node in the list
# ‘Child’ pointer to a linked list where the current node is the head

# Each of these child linked lists is in sorted order and connected by a 'child' pointer. Your task is to flatten this linked list such that all nodes appear in a single layer or level in a 'sorted order'.

# Initialize an array to store node values and traverse the list, collecting values from both top-level and child nodes.
# Sort the array to arrange the values in ascending order.
# Create and return a new linked list from the sorted array.

class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    # Function to convert a vector to a linked list
    def convertArrToLinkedList(self, arr):
        ''' Create a dummy node to serve as
         the head of the linked list '''
        dummyNode = ListNode(-1)
        temp = dummyNode

        ''' Iterate through the vector and
         create nodes with vector elements '''
        for i in range(len(arr)):
            # Create a new node with the vector element
            temp.child = ListNode(arr[i])
            
            # Update the temporary pointer
            temp = temp.child
        
        ''' Return the linked list starting
         from the next of the dummy node '''
        return dummyNode.child

    # Function to flatten a linked list with child pointers 
    def flattenLinkedList(self, head):
        arr = []

        # Traverse through the linked list
        while head is not None:
            ''' Traverse through the child
             nodes of each head node '''
            t2 = head
            
            while t2 is not None:
                # Store each node's data in the array
                arr.append(t2.val)
                
                # Move to the next child node
                t2 = t2.child

            # Move to the next head node
            head = head.next

        # Sort the array containing node values
        arr.sort()

        # Convert the sorted array back to a linked list
        return self.convertArrToLinkedList(arr)

# Function to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.child
    print()

# Function to print the linked list in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head is not None:
        print(head.val, end="")

        ''' If child exists, recursively
         print it with indentation '''
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars for each level in the grid
        if head.next:
            print()
            for i in range(depth):
                print("| ", end="")
        
        head = head.next

if __name__ == "__main__":
    # Create a linked list with child pointers
    head = ListNode(5)
    head.child = ListNode(14)

    head.next = ListNode(10)
    head.next.child = ListNode(4)

    head.next.next = ListNode(12)
    head.next.next.child = ListNode(20)
    head.next.next.child.child = ListNode(13)

    head.next.next.next = ListNode(7)
    head.next.next.next.child = ListNode(17)

    # Print the original linked list structure
    print("Original linked list:")
    printOriginalLinkedList(head, 0)

    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to flatten the linked list
    flattened = sol.flattenLinkedList(head)
    
    # Printing the flattened linked list
    print("\nFlattened linked list: ", end="")
    printLinkedList(flattened)

# optimal
# Establish base case conditions by checking if the head is null or has no next pointer. If either condition is met, return the head, as there is no further flattening or merging required.
# Recursively initiate the flattening process by calling flattenLinkedList on the next node (head -> next). The result of this recursive call will be the head of the flattened and merged linked list.
# Within the recursive call, perform merge operations by calling a merge function. This function merges the current list with the already flattened and merged list based on their data values. The merged list is then updated in the head and returned as the result of the flattening process.

class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    ''' Merge the two linked lists in a particular
     order based on the data value '''
    def merge(self, list1, list2):
        ''' Create a dummy node as a 
        placeholder for the result '''
        dummyNode = ListNode(-1)
        res = dummyNode

        # Merge the lists based on data values
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child
            res.next = None

        # Connect the remaining elements if any
        if list1:
            res.child = list1
        else:
            res.child = list2

        # Break the last node's link to prevent cycles
        if dummyNode.child:
            dummyNode.child.next = None

        return dummyNode.child

    # Function to flatten a linked list with child pointers 
    def flattenLinkedList(self, head):
        # If head is null or there is no next node
        if head is None or head.next is None:
            return head # Return head

        # Recursively flatten the rest of the linked list
        mergedHead = self.flattenLinkedList(head.next)

        # Merge the lists
        head = self.merge(head, mergedHead)
        return head

# Function to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.child
    print()

# Function to print the linked list in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head is not None:
        print(head.val, end="")

        ''' If child exists, recursively
         print it with indentation '''
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars for each level in the grid
        if head.next:
            print()
            for i in range(depth):
                print("| ", end="")
        
        head = head.next

if __name__ == "__main__":
    # Create a linked list with child pointers
    head = ListNode(5)
    head.child = ListNode(14)

    head.next = ListNode(10)
    head.next.child = ListNode(4)

    head.next.next = ListNode(12)
    head.next.next.child = ListNode(20)
    head.next.next.child.child = ListNode(13)

    head.next.next.next = ListNode(7)
    head.next.next.next.child = ListNode(17)

    # Print the original linked list structure
    print("Original linked list:")
    printOriginalLinkedList(head, 0)

    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to flatten the linked list
    flattened = sol.flattenLinkedList(head)
    
    # Printing the flattened linked list
    print("\nFlattened linked list: ", end="")
    printLinkedList(flattened)