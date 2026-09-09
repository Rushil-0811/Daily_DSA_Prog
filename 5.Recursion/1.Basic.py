# Problem Statement: You are given a stack of integers. Your task is to reverse the stack using recursion. You may only use standard stack operations (push, pop, top/peek, isEmpty). You are not allowed to use any loop constructs or additional data structures like arrays or queues.

# Your solution must modify the input stack in-place to reverse the order of its elements.
# Input:
#  stack = [4, 1, 3, 2]  
# Output:
#  [2, 3, 1, 4]

# Define a helper function insertAtBottom to insert a value at the bottom of the stack.
# If the stack is empty, push the value.
# If the stack is not empty, pop the top element, recursively call insertAtBottom, and push the popped element back.
# Define the main function reverseStack:
# If the stack is empty, return.
# Pop the top element, recursively reverse the rest of the stack.
# Use insertAtBottom to insert the popped element at the bottom of the stack.

# Function to insert element at the bottom of the stack
def insert_at_bottom(stack, val):
    # If stack is empty, append the value
    if not stack:
        stack.append(val)
        return

    # Pop the top element
    top_val = stack.pop()

    # Recurse for the rest of the stack
    insert_at_bottom(stack, val)

    # Push the popped element back
    stack.append(top_val)

# Function to reverse the stack
def reverse_stack(stack):
    # Base case: If stack is empty, return
    if not stack:
        return

    # Pop the top element
    top_val = stack.pop()

    # Recursively reverse the remaining stack
    reverse_stack(stack)

    # Insert the popped element at the bottom
    insert_at_bottom(stack, top_val)

def main():
    # Create a sample stack
    stack = [4, 1, 3, 2]

    # Reverse the stack
    reverse_stack(stack)

    # Print the reversed stack
    print("Reversed Stack:", stack)

if __name__ == "__main__":
    main()