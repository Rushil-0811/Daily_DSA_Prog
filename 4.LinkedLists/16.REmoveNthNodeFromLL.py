# Problem Statement: Given a linked list and an integer N, the task is to delete the Nth node from the end of the linked list and print the updated linked list.

# brute force
# The simplest way to delete the Nth node from the end is to delete the (L-N+1)th node from the start of the linked list, where L is the total length of the linked list. Therefore, this problem can be broken down into two sub-problems:
# The first part involves the calculation of the length of the linked list.
# The second part involves the deletion of the (L-N+1)th node from the start of the linked list.
# If N equals 1, this means we have to delete the tail of the linked list.
# If N equals the length of the linked list, we have to delete the head of the linked list.
# To calculate the length and delete the node we can follow the following steps:
# Initialize a temp pointer that will be used to traverse the list. Create a counter and increment it for every node while traversing.
# When the pointer reaches null, counter will store the length of linked list.
# To delete the (L-N+1)th node of the linked list, create a new temp pointer to the head. Initialize a variable res to L-N, and start iterating the linked list while decrementing res at each node. Once res equals 0, we know that temp will be pointing to the (L-N)th node, therefore, stop the traversal.
# To create a new link, point the (L-N)th node to the (L-N+2)th node of the linked list, effectively skipping the (L-N+1)th node.
# Finally, free up the memory being occupied by the (L-N+1)th node, thus deleting this node

# Class representing a node in the linked list
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Class to hold the solution logic
class Solution:
    # Function to print the linked list
    def printLL(self, head):
        while head:
            print(head.data, end=" ")
            head = head.next

    # Function to delete the Nth node from the end
    def deleteNthNodeFromEnd(self, head, N):
        # If list is empty
        if head is None:
            return None

        cnt = 0
        temp = head

        # Count total number of nodes
        while temp:
            cnt += 1
            temp = temp.next

        # If N equals total nodes → delete head
        if cnt == N:
            return head.next

        # Calculate position from start
        res = cnt - N
        temp = head

        # Traverse to the node before target
        while temp:
            res -= 1
            if res == 0:
                break
            temp = temp.next

        # Delete the node
        temp.next = temp.next.next

        return head


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3

    # Create linked list manually
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    sol = Solution()
    head = sol.deleteNthNodeFromEnd(head, N)
    sol.printLL(head)


# optimal method
# The brute force, in the worst case, has a time complexity of O(2*L), where L is the length of the linked list. Therefore, it is not the most efficient algorithm, as we are traversing the entire list twice.

# To enhance efficiency, we will involve two pointers, a fast pointer and a slow pointer. The fast-moving pointer will initially be exactly N nodes ahead of the slow-moving pointer. After which, both of them will move one step at a time. When the fast pointer reaches the last node, i.e., the L-th node, the slow is guaranteed to be at the (L-N)-th node, where L is the total length of the linked list.
# Initialize two pointers, slow and fast, to the head of the linked list. Initially, only fast will move till it crosses N nodes, after which both of the pointers will move simultaneously.
# Traverse the linked list till the fast pointer reaches the last node, that is, the Lth Node, at this stage, the slow pointer is guaranteed to be at the (L-N)th node.
# Point this slow pointer to the (L-N+2)th node, effectively skipping the Nth node from the end or the (L-N+1)th node from the start.
# Finally, free up the space occupied by this to delete it.

# Class representing a node in the linked list
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Class to hold the solution logic
class Solution:
    # Function to print the linked list
    def printLL(self, head):
        while head is not None:
            print(head.data, end=" ")
            head = head.next

    # Function to delete the Nth node from the end 
    # using the optimized two-pointer method
    def deleteNthNodeFromEnd(self, head, N):
        # Create a dummy node before head to handle edge cases
        dummy = Node(0, head)

        # Initialize slow and fast pointers at dummy
        slow = dummy
        fast = dummy

        # Move fast pointer N+1 steps ahead to create a gap
        for _ in range(N + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # Slow is now at node before target → delete target node
        slow.next = slow.next.next

        # Return updated head
        return dummy.next

# Main driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3

    # Create linked list manually
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    # Create Solution object
    sol = Solution()

    # Delete the Nth node from the end
    head = sol.deleteNthNodeFromEnd(head, N)

    # Print the modified linked list
    sol.printLL(head)
