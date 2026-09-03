# # brute
# A brute-force approach involves replacing data in a doubly linked list. First, we traverse the list and store node data in a stack. Then, in a second pass, we assign elements from the stack to nodes, ensuring a reverse order replacement since stacks follow the Last-In-First-Out (LIFO) principle.
# Initialization a temp pointer to the head of the doubly linked list and a stack data structure to store the values from the list.
# Traverse the doubly linked list with the temp pointer and while traversing push the value at the current node temp onto the stack. Move the temp to the next node continuing until temp reaches null indicating the end of the list.
# Reset the temp pointer back to the head of the list and in this second iteration pop the element from the stack, replace the data at the current node with the popped value from the top of the stack and move temp to the next node. Repeat this step until temp reaches null or the stack becomes empty.

class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back

# Function to convert a list to a doubly linked list
def convertArr2DLL(arr):
    # Create head node
    head = Node(arr[0])
    
    # Pointer to track previous node
    prev = head

    # Traverse remaining elements
    for i in range(1, len(arr)):
        # Create new node with back reference to prev
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp

    # Return head of DLL
    return head

# Function to print the doubly linked list
def printDLL(head):
    # Traverse and print each node's data
    while head:
        print(head.data, end=" ")
        head = head.next

# Function to reverse the DLL using stack
def reverseDLL(head):
    # If list is empty or has one node, return as is
    if not head or not head.next:
        return head

    # Stack to hold node data
    stack = []

    # Pointer to traverse list
    temp = head

    # Push all node values to stack
    while temp:
        stack.append(temp.data)
        temp = temp.next

    # Reset temp to head
    temp = head

    # Replace node data with values from stack
    while temp:
        temp.data = stack.pop()
        temp = temp.next

    # Return reversed head
    return head

# Driver code
arr = [12, 5, 8, 7, 4]
head = convertArr2DLL(arr)
print("Doubly Linked List Initially:")
printDLL(head)
head = reverseDLL(head)
print("\nDoubly Linked List After Reversing:")
printDLL(head)

# optimal
# Instead of performing two separate traversals of the linked list and storing its node values in an external data structure, we can optimize our approach by directly modifying the links between the nodes within the doubly linked list We need to traverse on every node, and for every node change the next pointer and back pointer. If we can do this for all nodes, at the end of traversal, the doubly linked list will be reversed.
# Initialise two pointers that are needed for the reversal. Initialize a current pointer to the head of the linked list. This pointer will traverse the list as we reverse it. Initialize a second pointer last to null. This pointer will be used for temporary storage during pointer swapping, as we need a third variable while swapping two data.
# Traverse through the DLL by looping over all the nodes.
# While iterating over all nodes in the linked list, we make changes to set the backward pointer of a node to the next changing its previous link. Along with this, the forward pointer is adjusted to point to the previous node, reversing the next link. To prevent losing the last node in this process, we use a reference to the last node to retain it.
# Update the current node's back pointer to point to the next node (current->back = current->next). This step reverses the direction of the backward pointer.
# Update the current node's next pointer to point to the previous node (current->next = last). This step reverses the direction of the forward pointer.
# Move the current pointer one step forward (current = current->back). This allows us to continue the reversal process.
# After completing the traversal, the last node ends up at the second node in the reversed doubly linked list. To obtain the new head of the reversed list, we simply use the backward pointer of the last node, which points to the new head.
# To ensure that we handle the case where the traversal ended at the original list's end (i.e., the last pointer is not null), we update the head pointer to point to the new head of the reversed list, which is stored in the last pointer.
# Finally, we return the head pointer, now pointing to the head of the fully reversed doubly linked list.
# Class to represent a Node of a doubly linked list
class Node:
    def __init__(self, data):
        # Initialize the data
        self.data = data
        # Pointer to the next node
        self.next = None
        # Pointer to the previous node
        self.prev = None

# Function to convert a list into a doubly linked list
def convert_list_to_dll(arr):
    # Create the head node from the first element
    head = Node(arr[0])
    # Maintain a previous pointer to link backwards
    prev = head

    # Loop through the rest of the elements
    for i in range(1, len(arr)):
        # Create a new node with previous pointer set to 'prev'
        new_node = Node(arr[i])
        new_node.prev = prev
        # Link previous node's next to this node
        prev.next = new_node
        # Move prev forward
        prev = new_node

    # Return the head of the list
    return head

# Function to reverse the doubly linked list
def reverse_dll(head):
    # Initialize a temporary pointer to traverse the list
    temp = None
    # Start from the head
    current = head

    # Traverse till the end of the list
    while current is not None:
        # Swap the next and prev pointers
        temp = current.prev
        current.prev = current.next
        current.next = temp
        # Move to the next node in original list, which is prev now
        current = current.prev

    # After loop, temp will be pointing to the last node’s prev
    # So, adjust head to the new head of the reversed list
    if temp is not None:
        head = temp.prev

    # Return new head
    return head

# Function to print the doubly linked list
def print_dll(head):
    # Traverse and print each node's data
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

# Driver code
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    head = convert_list_to_dll(arr)
    print("Original DLL:")
    print_dll(head)
    head = reverse_dll(head)
    print("Reversed DLL:")
    print_dll(head)
