# Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. Check whether the linked list values form a palindrome or not. Return true if it forms a palindrome, otherwise, return false. .

# A palindrome is a sequence that reads the same forward and backwards.

# Traverse the linked list from start to end, and push each node's value into a stack.
# Once done, start again from the head of the linked list.
# For each node, pop an element from the stack and compare it with the current node’s value.
# If any value doesn’t match, return false — it’s not a palindrome.
# If all values match till the end, return true — the list is a palindrome.

# Node class represents a node in a linked list
class Node:

    # Constructor with both data and next node as parameters
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


# Function to check if the linked list is a palindrome
def isPalindrome(head):

    # Create an empty stack to store values
    st = []

    # Initialize a temporary pointer to the head of the linked list
    temp = head

    # Traverse the linked list and push values onto the stack
    while temp is not None:

        # Push the data from the current node onto the stack
        st.append(temp.data)

        # Move to the next node
        temp = temp.next

    # Reset the temporary pointer back to the head of the linked list
    temp = head

    # Compare values by popping from the stack and checking against linked list nodes
    while temp is not None:

        # If values don't match, it's not a palindrome
        if temp.data != st[-1]:
            return False

        # Pop the value from the stack
        st.pop()

        # Move to the next node in the linked list
        temp = temp.next

    # If all values match, it's a palindrome
    return True


# Function to print the linked list
def printLinkedList(head):

    temp = head

    while temp is not None:

        # Print the current node's data
        print(temp.data, end=" ")

        # Move to the next node
        temp = temp.next

    print()


# Driver function

# Create a linked list with values 1, 5, 2, 5, and 1 (15251, a palindrome)
head = Node(1)
head.next = Node(5)
head.next.next = Node(2)
head.next.next.next = Node(5)
head.next.next.next.next = Node(1)

# Print the original linked list
print("Original Linked List:", end=" ")
printLinkedList(head)

# Check if the linked list is a palindrome
if isPalindrome(head):
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")

# optimal
# Return true if the list is empty or has only one node, since such lists are palindromes by default.
# Use two pointers ‘slow’ and ‘fast’ to find the middle node, where slow moves one step and fast moves two steps at a time.
# Reverse the second half of the linked list starting from the node after the middle (slow->next), preparing it for comparison.
# Set two pointers: one at the head of the list and the other at the head of the reversed second half, to compare both halves.
# Compare both halves node by node; if any mismatch occurs, return false, otherwise continue till the end of either list.
# Reverse the second half again to restore the original list structure, and return true if all nodes matched successfully.
# Node class represents a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data       # Data stored in the node
        self.next = next_node  # Pointer to the next node in the list

# Function to reverse a linked list using the recursive approach
def reverse_linked_list(head):
    if head is None or head.next is None:
        return head  # No change is needed; return the current head

    # Recursive step: Reverse the remaining part of the list and get the new head
    new_head = reverse_linked_list(head.next)

    # Store the next node in 'front' to reverse the link
    front = head.next

    # Update the 'next' pointer of 'front' to point to the current head
    front.next = head

    # Set the 'next' pointer of the current head to None to break the original link
    head.next = None

    return new_head  # Return the new head obtained from the recursion

# Function to check if the linked list is a palindrome
def is_palindrome(head):
    if head is None or head.next is None:
        return True  # It's a palindrome by definition

    slow = head
    fast = head

    # Traverse the linked list to find the middle using slow and fast pointers
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next      # Move slow pointer one step at a time
        fast = fast.next.next # Move fast pointer two steps at a time

    # Reverse the second half of the linked list starting from the middle
    new_head = reverse_linked_list(slow.next)

    first = head
    second = new_head

    # Compare data values of nodes from both halves
    while second is not None:
        if first.data != second.data:
            reverse_linked_list(new_head)  # Reverse the second half back to its original state
            return False

        first = first.next  # Move the first pointer
        second = second.next  # Move the second pointer

    # Reverse the second half back to its original state
    reverse_linked_list(new_head)

    return True  # The linked list is a palindrome

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")  # Print the current node's data
        temp = temp.next           # Move to the next node
    print()

# Driver code
if __name__ == "__main__":
    # Create a linked list with values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)

    # Check if the linked list is a palindrome
    if is_palindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")
