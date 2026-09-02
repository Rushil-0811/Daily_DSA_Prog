# Node class represents a node in the linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data      # Data value
        self.next = next      # Pointer to next node

# Driver code
if __name__ == "__main__":
    # Create an array
    arr = [2, 5, 8, 7]

    # Create first node
    y = Node(arr[0])

    # Print memory reference of node
    print(y)

    # Print data stored in node
    print(y.data)


# The class has two data types: data which contains the value of the node and a pointer next, which points to the next node in the list.
# There is a constructor which assigns the values to a new node.
# A new keyword is used to dynamically allocate memory to a node with data as arr[0].

# A pointer is a variable that stores the memory address of another variable. In simpler terms, it "points" to the location in memory where data is stored. This allows you to indirectly access and manipulate data by referring to its memory address.

# Singly Linked Lists: In a singly linked list, each node points to the next node in the sequence. Traversal is straightforward but limited to moving in one direction, from the head to the tail.

# Doubly Linked Lists: In this each node points to both the next node and the previous node, thus allowing it for bidirectional connectivity.