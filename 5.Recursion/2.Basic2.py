# Problem Statement: You are given a stack of integers. Your task is to sort the stack in descending order using recursion, such that the top of the stack contains the greatest element. You are not allowed to use any loop-based sorting methods (e.g., quicksort, mergesort). You may only use recursive operations and the standard stack operations (push, pop, peek/top, and isEmpty).
# Example 1:
# Input:
#  stack = [4, 1, 3, 2]
# Output:
#  [4, 3, 2, 1]
# Explanation:
#  After sorting, the largest element (4) is at the top, and the smallest (1) is at the bottom.

# If the stack is empty, stop.
# Remove the top element of the stack.
# Sort the remaining stack recursively.
# Insert the removed element back into the stack while maintaining descending order.
# Use a helper function to place the element in its correct position.

def insert(stack, temp):
    # Base case: if the stack is empty or temp is larger than the top element
    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return
    
    # Pop the top element and recursively insert
    val = stack.pop()
    insert(stack, temp)
    
    # Push the popped element back
    stack.append(val)

def sortStack(stack):
    if stack:
        temp = stack.pop()
        sortStack(stack)
        insert(stack, temp)

# Main function
if __name__ == "__main__":
    stack = [4, 1, 3, 2]
    sortStack(stack)

    # Print the sorted stack
    print("Sorted stack (descending order):", stack)
