# Implement Stack using single Queue


# 4

# Problem Statement: Implement a Last-In-First-Out (LIFO) stack using a single queue. The implemented stack should support the following operations: push, pop, top, and isEmpty.

# Implement the QueueStack class:

# push(int x): Pushes element x onto the stack.
# pop(): Removes and returns the top element of the stack.
# top(): Returns the top element of the stack without removing it.
# isEmpty(): Returns true if the stack is empty, false otherwise.

# Example 1:
# Input:
  
# ["QueueStack", "push", "push", "pop", "top", "isEmpty"]  
# [[], [4], [8], [], [], []]  
# Output:
#   [null, null, null, 8, 4, false]  
# Explanation:
#   QueueStack stack = new QueueStack();  
# - stack.push(4);  
# - stack.push(8);  
# - stack.pop(); // returns 8  
# - stack.top(); // returns 4  
# - stack.isEmpty(); // returns false 

# Data Structure Used: A single queue will be used to store the elements.
# Push(x): Insert the element x into the queue. To maintain the stack order:
# Run a loop that iterates size() - 1 times, where size() is the current number of elements in the queue.
# In each iteration, remove the front element and add it back to the rear of the queue. This ensures that the most recently added element is always at the front of the queue.
# Pop(): Remove and return the front element of the queue, which corresponds to the top of the stack.
# isEmpty(): Return true if the queue is empty, and false otherwise.

from queue import Queue

# Stack implementation using Queue
class QueueStack:
    def __init__(self):
        # Queue
        self.q = Queue()

    # Method to push element in the stack
    def push(self, x):
        # Get size
        s = self.q.qsize()
        # Add element
        self.q.put(x)

        # Move elements before new element to back
        for _ in range(s):
            self.q.put(self.q.get())

    # Method to pop element from stack
    def pop(self):
        # Get front element
        n = self.q.queue[0]
        # Remove front element
        self.q.get()
        # Return removed element
        return n

    # Method to return the top of stack
    def top(self):
        # Return front element
        return self.q.queue[0]

    # Method to check if the stack is empty
    def isEmpty(self):
        return self.q.empty()

if __name__ == "__main__":
    st = QueueStack()

    # List of commands
    commands = ["QueueStack", "push", "push", "pop", "top", "isEmpty"]
    inputs = [[], [4], [8], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            st.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(st.pop(), end=" ")
        elif commands[i] == "top":
            print(st.top(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if st.isEmpty() else "false", end=" ")
        elif commands[i] == "QueueStack":
            print("null", end=" ")