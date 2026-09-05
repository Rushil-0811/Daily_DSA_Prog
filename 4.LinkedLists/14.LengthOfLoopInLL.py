# Problem Statement: Given the head of a linked list, determine the length of a loop present in the linked list. If there's no loop present, return 0.

# brute method
# While traversing the linked list, employ a timer against each node to keep track of the number of nodes you've visited before it. Once a previously visited node is encountered again, the length of the loop can be determined by subtracting the timer values at the two instances of visiting that particular node.

# It's important to keep track of nodes and the timer value associated with them. This can be implemented using a hashmap with nodes as the key and the timer as the value.

# Initialize a temporary pointer to head which will be used to traverse the list. While traversing, keep track of the Visited nodes and the timer value associated in the map data structure.
# Continue traversing till a node that has already been visited is found. The difference between its timer value in the hashmap and the current timers value will be the length of loop in the linked list.
# If the traversal is completed, and we reach the last point of the linked list which is null, it means there was no loop, hence we return 0

# Node class represents a node in a linked list
class Node:
    # Constructor with both data and next node
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node
        self.next = next1


# Solution class containing the loop length function
class Solution:
    # Function to return the length of loop using hashing
    def lengthOfLoop(self, head):
        # Dictionary to store visited nodes and their timer values
        visitedNodes = {}

        # Pointer to traverse the linked list
        temp = head

        # Timer to track visited nodes
        timer = 0

        # Traverse the linked list till temp reaches None
        while temp is not None:
            # If revisiting a node, return the difference of timer values
            if temp in visitedNodes:
                # Calculate the length of the loop
                loopLength = timer - visitedNodes[temp]

                # Return the length of the loop
                return loopLength

            # Store the current node and its timer value
            visitedNodes[temp] = timer

            # Move to the next node
            temp = temp.next

            # Increment the timer
            timer += 1

        # If traversal is completed and we reach the end of the list
        # means there is no loop
        return 0


# Main driver code
if __name__ == "__main__":
    # Creating a sample linked list with a loop
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Linking the nodes
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # Creating a loop from fifth to second
    fifth.next = second

    # Creating a Solution object
    obj = Solution()

    # Getting the loop length
    loopLength = obj.lengthOfLoop(head)

    # Printing the result
    if loopLength > 0:
        print("Length of the loop:", loopLength)
    else:
        print("No loop found in the linked list.")


# optimal
# The previous method uses additional memory in order to find length of the loop. To enhance efficiency, the Tortoise and Hare Algorithm is introduced as an optimization.
# Initialise two pointers, slow and fast, to the head of the linked list. Slow will advance one step at a time, while fast will advance two steps at a time. These pointers will move simultaneously.
# Traverse the linked list with the slow and fast pointers. While traversing, repeatedly move slow one step and fast two steps at a time.
# Continue this traversal until either fast (or next node of fast) reaches null or both the pointers, slow and fast, meet.

# This is the point where the slow and fast have met proving that there is a loop in the linked list. From here onwards we start counting for the length of this loop.
# Initialise a counter with zero and traverse the linked list using the slow pointer again while incrementing the counter with each node visited.

# As the slow pointer reaches back at the fast pointer, the value of the counter will represent the length of the loop.

# Node class represents a node in a linked list
class Node:
    # Constructor with both data and next node
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node
        self.next = next1


# Solution class containing the loop length function
class Solution:
    # Function to return the length of loop using Floyd's Algorithm
    def lengthOfLoop(self, head):
        # Initialize slow and fast pointers
        slow = head
        fast = head

        # Loop until fast and slow meet
        while fast is not None and fast.next is not None:
            # Move slow by one step
            slow = slow.next

            # Move fast by two steps
            fast = fast.next.next

            # If slow and fast meet, loop detected
            if slow == fast:
                # Count the length of the loop
                return self.countLoopLength(slow)

        # No loop found
        return 0

    # Function to count loop length
    def countLoopLength(self, meetingPoint):
        # Start from meeting point
        temp = meetingPoint
        length = 1

        # Move until we meet again
        while temp.next != meetingPoint:
            temp = temp.next
            length += 1
        return length


# Main driver code
if __name__ == "__main__":
    # Creating a sample linked list with a loop
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Linking the nodes
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # Creating a loop from fifth to second
    fifth.next = second

    # Creating a Solution object
    obj = Solution()

    # Getting the loop length
    loopLength = obj.lengthOfLoop(head)

    # Printing the result
    if loopLength > 0:
        print("Length of the loop:", loopLength)
    else:
        print("No loop found in the linked list.")
