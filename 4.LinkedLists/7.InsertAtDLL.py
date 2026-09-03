# To insert a new node before a given node in a doubly linked list, start by identifying the previous node of the given node. This is guaranteed because the node to be inserted before is never the head of the list.
# Create a new node with the specified value to be inserted before the given node. The back pointer of the new node should point to the previous node, and the next pointer of the new node should point to the given node.
# To properly integrate the new node into the list, update the next pointer of the previous node to point to the new node, and set the back pointer of the given node to point to the new node, ensuring the doubly linked list remains intact.
# To insert a new node at the end of the doubly linked list, begin by traversing the list from the head node until you reach the tail.
# Create a new node with the provided data, setting its back pointer to the current tail node and its next pointer to null, as this new node will become the tail of the list.
# Update the next pointer of the current tail node to point to the newly created node, making the new node the new tail of the list.
# Finally, return the head of the updated doubly linked list, which remains unchanged after this operation.

# Define a Node class for doubly linked list
class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

# Function to convert an array to a doubly linked list
def convertArr2DLL(arr):
    head = Node(arr[0])  # Create the head node with the first element
    prev = head  # Initialize 'prev' to the head node

    # Traverse the array to create the doubly linked list
    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)  # Create a new node
        prev.next = temp  # Set 'next' of the previous node to the new node
        prev = temp  # Move 'prev' to the new node

    return head  # Return the head of the doubly linked list

# Function to print the elements of the doubly linked list
def printList(head):
    while head:
        print(head.data, end=" ")  # Print the data of the current node
        head = head.next  # Move to the next node
    print()  # New line after printing the list

# Function to insert a new node at the tail of the doubly linked list
def insertAtTail(head, k):
    newNode = Node(k)  # Create a new node with data 'k'

    if not head:
        return newNode  # If the list is empty, return the new node as the head

    tail = head
    while tail.next:
        tail = tail.next  # Traverse to the last node of the list

    tail.next = newNode  # Connect the new node to the last node
    newNode.back = tail  # Set the 'back' pointer of the new node to the previous node
    return head  # Return the head of the modified list

# Driver code
if __name__ == "__main__":
    arr = [12, 5, 8, 7, 4]  # Initialize an array
    head = convertArr2DLL(arr)  # Convert the array to a doubly linked list

    print("Doubly Linked List Initially:")
    printList(head)  # Print the doubly linked list

    print("\nDoubly Linked List After Inserting at the tail with value 10:")
    head = insertAtTail(head, 10)  # Insert a node with value 10 at the end
    printList(head)  # Print the updated doubly linked list