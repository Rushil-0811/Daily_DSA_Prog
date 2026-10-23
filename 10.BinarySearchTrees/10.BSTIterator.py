# You need to implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST). The iterator provides two main functions. The next() function must return the next smallest number in the BST. The hasNext() function must return true if there are still unexplored numbers remaining in the tree, and false otherwise. The iterator is initialized with the root of the tree, and the pointer conceptually starts right before the smallest element.

# Example 1
# Input: Tree: root = [7, 3, 15, null, null, 9, 20]
# Calls: BSTIterator, next(), next(), hasNext(), next(), hasNext(), next(), hasNext(), next(), hasNext()

# Output: [null, 3, 7, true, 9, true, 15, true, 20, false]

# Explanation: explanation in order of each call :

# The in-order traversal of this tree produces the sorted sequence: 3, 7, 9, 15, 20.

# The first next() call returns the smallest element, 3.

# The second next() returns 7.

# hasNext() returns true because 9, 15, and 20 are still pending.

# We continue calling next() until we retrieve 20.

# The final hasNext() returns false because all elements have been exhausted.

# Brute Force Approach
# The simplest way to supply items in a specific order is to pre-calculate the entire order upfront. Think about preparing for a presentation. Instead of fetching data from the internet live while you are speaking, you download all the slides beforehand and put them in a strict sequence. During the presentation, you simply click "next" to show the next slide. We can do the exact same thing by performing a complete in-order traversal of the tree immediately upon initialization, storing all the values in a standard array list.

# Algorithm
# Create a dynamic array (or list) inside the class to hold the tree values.

# Maintain an integer index variable starting at 0 to track our current position in the list.

# In the constructor, write a standard recursive in-order traversal function that visits every node and pushes its value into the array.

# For the next() function, simply return the value located at the current index inside the array, and then increment the index by 1.

# For the hasNext() function, check if the index is strictly less than the total length of the array. If it is, there are more elements left.

# Dry Run

# Python program to implement Binary Search Tree Iterator

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    # Constructor initializes the array and fills it completely
    def __init__(self, root):
        self.nodesSorted = []
        self.index = 0
        self._inorder(root)
        
    # Standard recursive in-order traversal to populate the array
    def _inorder(self, root):
        if root is None:
            return
        self._inorder(root.left)
        self.nodesSorted.append(root.val)
        self._inorder(root.right)

    # Retrieves the current element and advances the internal pointer
    def next(self):
        val = self.nodesSorted[self.index]
        self.index += 1
        return val

    # Checks if the internal pointer has reached the end of the array
    def hasNext(self):
        return self.index < len(self.nodesSorted)

# Driver code starts here
if __name__ == "__main__":
    # Construct the sample tree
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    
    # Instantiate the iterator object
    obj = BSTIterator(root)
    
    # Simulate iterator calls
    print(obj.next())    # 3
    print(obj.next())    # 7
    print("true" if obj.hasNext() else "false") # true
    print(obj.next())    # 9

# Complexity Analysis
# Time Complexity: O(N) for initialization, because traversing the entire tree to fill the array takes linear time. next() and hasNext() strictly take O(1) time.

# Space Complexity: O(N), because we duplicate the entire tree's values inside a separate dynamic array, scaling directly with the total number of nodes.

# Optimal Approach
# The brute force approach works, but requires massive memory allocation. If a tree has ten million nodes, flattening it immediately creates an array of ten million items, consuming huge amounts of RAM right from the start. We can heavily optimize our memory by pausing the traversal. By manually controlling an explicit stack, we only ever store the nodes along the specific branch we are currently exploring, limiting our memory to the strict height of the tree. If you want to understand this in detail, check our guide on Inorder Traversal using Stacks.

# Think about navigating a maze by always hugging the left wall. You walk down a long hallway, marking the intersections you pass, until you hit a dead end on the far left. That dead end is your first stop. When you are asked for the next stop, you trace your steps backward to the last intersection you marked. If a right-side hallway exists there, you step into it, and then instantly start hugging the left wall again to find the next absolute minimum spot. We use a stack to act as our physical memory of the intersections we passed.

# Algorithm
# Initialize an empty stack structure to hold tree nodes.

# Create a helper function called pushAllLeft that takes a node, repeatedly pushes it onto the stack, and moves to its left child until it hits a null dead end.

# In the constructor, call pushAllLeft and pass the root node to load the initial far-left path.

# For the hasNext() function, simply check if the stack is completely empty. If it holds nodes, there are items left to process.

# For the next() function, pop the top node from the stack. This node is our current smallest value to return.

# Before returning the value, check if this popped node has a right child. If it does, call pushAllLeft on that right child to load its entire far-left path into the stack for future calls.

# Return the value of the popped node.

# Python program to implement Binary Search Tree Iterator

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    # Constructor initializes the state by loading the leftmost path
    def __init__(self, root):
        self.st = []
        self._pushAllLeft(root)
        
    # Helper function to push the current node and all its left children
    def _pushAllLeft(self, node):
        while node is not None:
            self.st.append(node)
            node = node.left

    # Retrieves the next smallest element and updates the stack state
    def next(self):
        # The top of the stack is always the next smallest value
        topNode = self.st.pop()
        
        # If the processed node has a right branch, load its leftmost path
        if topNode.right is not None:
            self._pushAllLeft(topNode.right)
            
        return topNode.val

    # Returns true as long as there are pending nodes in the stack
    def hasNext(self):
        return len(self.st) > 0

# Driver code starts here
if __name__ == "__main__":
    # Construct the sample tree
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    
    # Instantiate the iterator object
    obj = BSTIterator(root)
    
    # Simulate iterator calls
    print(obj.next())    # 3
    print(obj.next())    # 7
    print("true" if obj.hasNext() else "false") # true
    print(obj.next())    # 9