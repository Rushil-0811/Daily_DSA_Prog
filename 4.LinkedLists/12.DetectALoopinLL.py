# Given a Linked List, determine whether the linked list contains a cycle or not.

# brute method
# A loop in a linked list occurs when there's a node that, when followed, brings you back to it, indicating a closed loop in the list. Hence it's important to keep track of nodes that have already been visited so that loops can be detected. One common way to do this is by using hashing.
# Traverse the entire linked list using a temporary pointer.
# While traversing, keep a track of the visited nodes in the map data structure.
# If a previously visited node is encountered again, that proves that there is a loop in the linked list hence return true.
# If the traversal is completed, and we reach the last point of the list which is null, it means there was no loop, hence we return false.
# Storing the entire node in the map is essential to distinguish between nodes with identical values but different positions in the list. This ensures accurate loop detection and not just duplicate value checks.

# Node class represents a
# node in a linked list
class Node:
    # Constructor with both data and next node as parameters
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node in the list
        self.next = next1

# Solution class with detectLoop function
class Solution:
    # function to detect loop in linked list
    def detectLoop(self, head):
        # Initialize a pointer 'temp'
        # at the head of the linked list
        temp = head

        # Create a set to keep track of
        # encountered nodes
        nodeMap = {}

        # Step 2: Traverse the linked list
        while temp is not None:
            # If the node is already in the
            # map, there is a loop
            if temp in nodeMap:
                return True
            # Store the current node
            # in the map
            nodeMap[temp] = 1

            # Move to the next node
            temp = temp.next

        # Step 3: If the list is successfully traversed 
        # without a loop, return false
        return False

# Driver code
if __name__ == "__main__":
    # Create a sample linked list
    # with a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    sol = Solution()

    # Check if there is a loop 
    # in the linked list
    if sol.detectLoop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")


# optimal
# The earlier approach of using a hash map requires extra memory, which becomes costly when the linked list is very large. To optimize space, we use the Tortoise and Hare Algorithm (Floyd’s Cycle Detection). If the list contains a loop, both pointers will eventually enter the cycle. Since the hare is faster, it covers more distance and will eventually overtake the tortoise inside the loop, leading to a meeting point. On the other hand, if the list has no loop, the hare will simply reach the end, and the algorithm terminates without any meeting.
# To detect a cycle using the Tortoise and Hare method, we start by initializing two pointers, slow and fast, at the head of the linked list.
# The slow pointer moves forward one step at a time, while the fast pointer advances two steps at a time.
# If the fast pointer or its next becomes null, it means the end of the linked list has been reached. In this case, there is no loop, and the list is linear.
# If the slow and fast pointers eventually meet at the same node, it confirms that a cycle exists in the linked list.
# Storing the entire node in the map is essential to distinguish between nodes with identical values but different positions in the list. This ensures accurate loop detection and not just duplicate value checks.
# Definition of singly linked list:

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    # Function to detect a loop in a linked
    # list using the Tortoise and Hare Algorithm
    def hasCycle(self, head):
        # Initialize two pointers, slow and fast,
        # to the head of the linked list
        slow = head
        fast = head

        # Step 2: Traverse the linked list with
        # the slow and fast pointers
        while fast is not None and fast.next is not None:
            # Move slow one step
            slow = slow.next
            # Move fast two steps
            fast = fast.next.next

            # Check if slow and fast pointers meet
            if slow == fast:
                return True  # Loop detected

        # If fast reaches the end of the list,
        # there is no loop
        return False

# Main function to test the Solution
def main():
    # Create a sample linked list
    # with a loop for testing
    
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third 

    # Create an instance of the Solution class
    solution = Solution()

    # Check if there is a loop 
    # in the linked list
    if solution.hasCycle(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")

# Call the main function to execute the test
if __name__ == "__main__":
    main()
