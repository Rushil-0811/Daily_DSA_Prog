# Problem Statement: Implement a First-In-First-Out (FIFO) queue using two stacks. The implemented queue should support the following operations: push, pop, peek, and isEmpty.

# Implement the StackQueue class:

# void push(int x): Adds element x to the end of the queue.
# int pop(): Removes and returns the front element of the queue.
# int peek(): Returns the front element of the queue without removing it.
# boolean isEmpty(): Returns true if the queue is empty, false otherwise.

# ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]  
# [[], [4], [8], [], [], []]  
# Output:
#  [null, null, null, 4, 8, false]  
# Explanation:
  
# StackQueue queue = new StackQueue();  
# - queue.push(4);  
# - queue.push(8);  
# - queue.pop(); // returns 4  
# - queue.peek(); // returns 8  
# - queue.isEmpty(); // returns false  

# push operation is o[n]
# Use Two Stacks: Maintain two stacks, stack1 and stack2.
# Push Operation:
# Transfer all elements from stack1 to stack2.
# Add the new element to stack1.
# Transfer all elements back from stack2 to stack1.
# This ensures the new element is always at the front for the next pop operation.
# Pop Operation: Remove and return the top element from stack1.
# Top Operation: Return the top element of stack1 without removing it.
# Size Operation: Return the size of stack1.

class StackQueue:
    def __init__(self):
        # Constructor
        self.st1 = []
        self.st2 = []

    # Method to push elements in the queue
    def push(self, x):
        '''Pop out elements from the first stack 
        and push on top of the second stack'''
        while self.st1:
            self.st2.append(self.st1.pop())

        # Insert the desired element
        self.st1.append(x)

        '''Pop out elements from the second stack 
        and push back on top of the first stack'''
        while self.st2:
            self.st1.append(self.st2.pop())

    # Method to pop element from the queue
    def pop(self):
        # Edge case
        if not self.st1:
            print("Stack is empty")
            return -1  # Representing empty stack

        # Get the top element
        top_element = self.st1.pop()  # Perform the pop operation
        return top_element  # Return the popped value

    # Method to get the front element from the queue
    def peek(self):
        # Edge case
        if not self.st1:
            print("Stack is empty")
            return -1  # Representing empty stack

        # Return the top element
        return self.st1[-1]

    # Method to find whether the queue is empty
    def is_empty(self):
        return not self.st1

if __name__ == "__main__":
    q = StackQueue()

    # List of commands
    commands = ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]
    # List of inputs
    inputs = [[], [4], [8], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            q.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(q.pop(), end=" ")
        elif commands[i] == "peek":
            print(q.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if q.is_empty() else "false", end=" ")
        elif commands[i] == "StackQueue":
            print("null", end=" ")

# push operation is o[1]

# Use Two Stacks: Maintain two stacks, inputStack and outputStack.
# Push Operation:
# Add the element to inputStack. This operation is efficient and always takes O(1) time.
# Pop Operation:
# If the outputStack is empty, move all elements from inputStack to outputStack. This reversal of order ensures that the oldest element is on top of the outputStack.
# Remove and return the top element from outputStack. This represents the oldest element in the queue.
# Top Operation:
# If the outputStack is empty, move all elements from inputStack to outputStack to access the oldest element.
# Return the top element of outputStack without removing it. This gives the element that has been in the queue the longest.
# Size Operation:
# Return the sum of the sizes of both stacks. This total gives the number of elements currently in the queue.

class StackQueue:
    def __init__(self):
        # Initialize your data structure here
        self.input = []  # Stack to push elements
        self.output = [] # Stack to simulate FIFO order

    # Push element x to the back of queue
    def push(self, x: int):
        self.input.append(x)

    # Removes the element from in front of queue and returns that element
    def pop(self) -> int:
        # Shift input to output if output is empty
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        # If queue is still empty, return -1 (or throw an error if preferred)
        if not self.output:
            print("Queue is empty, cannot pop.")
            return -1

        return self.output.pop()

    # Get the front element
    def peek(self) -> int:
        # Shift input to output if output is empty
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        # If queue is still empty, return -1 (or throw an error if preferred)
        if not self.output:
            print("Queue is empty, cannot peek.")
            return -1

        return self.output[-1]

    # Returns true if the queue is empty, false otherwise
    def isEmpty(self) -> bool:
        return not self.input and not self.output


# Main function to test the StackQueue implementation
if __name__ == "__main__":
    q = StackQueue()
    q.push(3)
    q.push(4)
    print("The element popped is", q.pop())
    q.push(5)
    print("The front of the queue is", q.peek())
    print("Is the queue empty?", "Yes" if q.isEmpty() else "No")
    print("The element popped is", q.pop())
    print("The element popped is", q.pop())
    print("Is the queue empty?", "Yes" if q.isEmpty() else "No")
