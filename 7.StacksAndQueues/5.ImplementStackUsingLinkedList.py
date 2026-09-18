# Problem Statement: Implement a Last-In-First-Out (LIFO) stack using a singly linked list. The implemented stack should support the following operations: push, pop, top, and isEmpty.

# Implement the LinkedListStack class:

# void push(int x): Pushes element x onto the stack.
# int pop(): Removes and returns the top element of the stack.
# int top(): Returns the top element of the stack without removing it.
# boolean isEmpty(): Returns true if the stack is empty, false otherwise.

# Node Structure:
# Define a node with:
# An integer to store data.
# A pointer to the next node.
# A constructor to initialize the data and the next pointer.

# tack Structure:
# Define a stack with:
# A pointer to the top node.
# An integer to keep track of the size.
# A constructor to initialize the top pointer and size.

# Push Operation:
# Create a new node with the given data and set the new node's next pointer to the current top node.
# Update the top pointer to the new node and increment the size.

# Pop Operation:
# Check if the stack is empty. If it is, return an error value (e.g., -1).
# Store the data of the top node and update the top pointer to the next node.
# Delete the old top node and decrement the size. Return the stored data.

# Peek Operation:
# Check if the stack is empty. If it is, return an error value (e.g., -1).
# Otherwise, return the data of the top node.

# Is Empty Operation:
# Check if the top pointer is null. Return true if it is, otherwise false.

# Size Operation:
# Return the size of the stack.

# Print Stack:
# Traverse from the top node and print each node's data until reaching the end of the list.

# Node structure
class Node:
    def __init__(self, d):
        self.val = d
        self.next = None

# Structure to represent stack
class LinkedListStack:
    def __init__(self):
        self.head = None  # Top of Stack
        self.size = 0  # Size

    # Method to push an element onto the stack
    def push(self, x):
        # Creating a node
        element = Node(x)
        
        element.next = self.head  # Updating the pointers
        self.head = element  # Updating the top
        
        # Increment size by 1
        self.size += 1

    # Method to pop an element from the stack
    def pop(self):
        # If the stack is empty
        if self.head is None:
            return -1  # Pop operation cannot be performed
        
        value = self.head.val  # Get the top value
        temp = self.head  # Store the top temporarily
        self.head = self.head.next  # Update top to next node
        del temp  # Delete old top node
        self.size -= 1  # Decrement size
        
        return value  # Return data

    # Method to get the top element of the stack
    def top(self):
        # If the stack is empty
        if self.head is None:
            return -1  # Top element cannot be accessed
        
        return self.head.val  # Return the top

    # Method to check if the stack is empty
    def isEmpty(self):
        return self.size == 0

# Creating a stack
st = LinkedListStack()

# List of commands
commands = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
# List of inputs
inputs = [[], [3], [7], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        st.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(st.pop(), end=" ")
    elif commands[i] == "top":
        print(st.top(), end=" ")
    elif commands[i] == "isEmpty":
        print("true" if st.is_empty() else "false", end=" ")
    elif commands[i] == "LinkedListStack":
        print("null", end=" ")