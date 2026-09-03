# Class representing a node in Doubly Linked List
class Node:
    # Constructor to initialize a node
    def __init__(self, data, next=None, prev=None):
        # Stores data of the node
        self.data = data

        # Pointer to the next node
        self.next = next

        # Pointer to the previous node
        self.prev = prev

# Initializing an array to create nodes
arr = [2, 5, 8, 7]

# Creating the head node of the doubly linked list
head = Node(arr[0])

# Printing the memory reference of head
print(head)

# Printing the data stored in head node
print(head.data)

# Node* prev : The introduction of the previous pointer is the key change from a singly linked list node. This pointer allows traversal in the backward direction, making it suitable for doubly linked lists.

# Constructors: Both constructors have been updated to initialize the new previous pointer. In the first constructor, Node(int data1, Node* next, Node* prev), prev is initialized with the provided value. In the second constructor, Node(int data1), the prev is initialized to nullptr, just like the next.

# These changes differentiate the Node class for a doubly linked list, allowing it to maintain bidirectional links between nodes, as opposed to the unidirectional links in a singly linked list node.

