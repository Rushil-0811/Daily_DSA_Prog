# Implement a Last-In-First-Out (LIFO) stack using an array. The implemented stack should support the following operations: push, pop, peek, and isEmpty.
# Example 1:
# Input:
  
# ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]  
# [[], [5], [10], [], [], []]  
# Output:
#   [null, null, null, 10, 10, false]  
# Explanation:
#   ArrayStack stack = new ArrayStack();  
# - stack.push(5);  
# - stack.push(10);  
# - stack.top(); // returns 10  
# - stack.pop(); // returns 10  
# - stack.isEmpty(); // returns false 

# Declare an Array of Particular Size: Initialize an array that will hold the elements of the stack. The size of the array is defined when the stack is created.
# Define a Variable “Top” and Initialize It as -1: The "top" variable keeps track of the index of the last added element in the stack. Initializing it to -1 indicates that the stack is empty.
# Push Operation (push(int x)): To push an element onto the stack:
# Increment the top index by one and insert the element at this position in the array.
# If the stack is full (top is equal to the last index of the array), throw a stack overflow exception.
# Pop Operation (pop()): To pop an element from the stack:
# Check if the stack is not empty by ensuring top is not equal to -1. If the stack is empty, throw a stack underflow exception.
# If the stack is not empty, return the element at the top index and then decrement the top index by one.
# Top Operation (top()): To get the top element without removing it:
# Check if the stack is not empty. If it is empty, throw an exception.
# If the stack is not empty, return the element at the top index.
# IsEmpty Operation (isEmpty()): To check if the stack is empty:
# Check if the top index is -1.
# Size Operation (size()): To get the current size of the stack:
# Return top + 1.

class ArrayStack:
    # Constructor
    def __init__(self, size=1000):
        # Array to hold elements
        self.stackArray = [0] * size
        # Maximum capacity
        self.capacity = size
        # Initialize stack as empty
        self.topIndex = -1

    # Pushes element x
    def push(self, x):
        if self.topIndex >= self.capacity - 1:
            print("Stack overflow")
            return
        self.topIndex += 1
        self.stackArray[self.topIndex] = x

    # Removes and returns top element
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            # Return invalid value
            return -1
        top_element = self.stackArray[self.topIndex]
        self.topIndex -= 1
        return top_element

    # Returns top element
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1
        return self.stackArray[self.topIndex]

    '''Returns true if the 
       stack is empty, false otherwise'''
    def isEmpty(self):
        return self.topIndex == -1

# Main function
if __name__ == "__main__":
    stack = ArrayStack()
    commands = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(stack.pop(), end=" ")
        elif commands[i] == "top":
            print(stack.top(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if stack.isEmpty() else "false", end=" ")
        elif commands[i] == "ArrayStack":
            print("null", end=" ")