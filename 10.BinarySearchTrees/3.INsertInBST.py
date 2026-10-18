# In the Insert into a Binary Search Tree problem, you are given the root node of a binary search tree and an integer value. Your task is to insert this new value into the tree as a new node. You must ensure that after the insertion, the tree remains a valid binary search tree, where all left children are smaller and all right children are larger than their parent. It is guaranteed that the new value does not already exist in the tree. You must return the root node of the tree after completing the insertion.

# Example 1
# Input: root = [4, 2, 7, 1, 3], val = 5

# Output: [4, 2, 7, 1, 3, 5]

# Explanation: The tree has a root of 4. We want to insert 5. Since 5 is greater than 4, it goes to the right side. Since 5 is less than 7, it becomes the left child of 7. The tree remains perfectly sorted.

# Example 2
# Input: root = [], val = 5

# Output: [5]

# Explanation: The original tree is completely empty. We simply create a new node with the value 5, and it becomes the new root of the tree.

# Brute Force Approach
# A binary search tree acts like a sorted hierarchy. Think about placing a new file into a highly organized folder system. If the file is alphabetically smaller than the current folder, you hand it off to the sub-folder on the left. If it is larger, you hand it off to the sub-folder on the right. You repeat this hand-off process until you reach an empty space where no sub-folder exists. That empty space is exactly where the new file belongs. We can write a recursive function that delegates the insertion to its left or right child until it hits a null spot.

# Algorithm
# Check the base case: if the current node is null, it means we have found our empty spot. We create a new node with our value and return it.

# If the value we want to insert is smaller than the current node's value, we make a recursive call to insert it into the left subtree. We then connect the returned result back to the left child pointer.

# If the value is larger than the current node's value, we make a recursive call to insert it into the right subtree. We connect the result back to the right child pointer.

# Finally, return the current node to keep the tree completely connected.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursively finds the correct empty position in the tree
    # and attaches a newly created node maintaining the rules
    def insertIntoBST(self, root, val):
        # Base case: we found the empty spot to place the new node
        if root is None:
            return TreeNode(val)
            
        # If the value is smaller, delegate insertion to the left branch
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # If the value is larger, delegate insertion to the right branch
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        # Return the current node to maintain the entire tree structure
        return root

# Helper function to print in-order traversal of the tree
def print_in_order(node):
    if node is None:
        return
    print_in_order(node.left)
    print(node.val, end=" ")
    print_in_order(node.right)

# Driver code starts here
if __name__ == "__main__":
    # Construct the initial tree: [4, 2, 7, 1, 3]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    # Instantiate the solution object
    obj = Solution()
    val = 5
    
    # Perform the recursive insertion
    result = obj.insertIntoBST(root, val)
    
    # Output the entire tree via in-order traversal
    print("In-order traversal:", end=" ")
    print_in_order(result)
    print()

# Optimal Approach
# The recursive approach is elegant and easy to read, but it inherently relies on system stack memory to keep track of its path. In an extremely deep and unbalanced tree, this could potentially cause a stack overflow error. We can optimize our space usage by eliminating recursion entirely. By using a single pointer to travel down the tree, we achieve the exact same insertion logic using strictly constant memory.

# Instead of repeatedly calling a function to move down the tree, imagine you are personally walking down the branching hallways of a building. You hold the new room you want to build in your hand. At each intersection, you read the sign. If your room number is smaller, you walk left. If it is larger, you walk right. When you finally reach a dead end where no hallway continues in your needed direction, you simply build the room right there, link it to the current intersection, and your job is done. You do not need to remember the entire path you took.

# Algorithm
# Handle the extreme edge case immediately: if the given tree is totally empty (root is null), return a brand new node as the root.

# Initialize a pointer to keep track of the current node, starting at the root.

# Start an infinite loop that will only break once we attach the new node.

# If the value to insert is smaller than the current node, we must move left. If the left child exists, we update our pointer to move to the left child. If the left child is null, we have found our spot, attach the new node, and break the loop.

# If the value to insert is larger than the current node, we must move right. If the right child exists, we update our pointer to move to the right child. If the right child is null, we attach the new node and break the loop.

# Finally, return the original root node.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iteratively navigates the tree to find the correct empty leaf
    # spot to attach the new node, avoiding stack overhead
    def insertIntoBST(self, root, val):
        # If the tree is entirely empty, the new node becomes the root
        if root is None:
            return TreeNode(val)
            
        # Pointer to traverse the tree downwards
        current = root
        
        # Continue moving down until we successfully attach the node
        while True:
            # Target belongs on the left side
            if val < current.val:
                # If there is space, attach it and stop searching
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                # Otherwise, keep moving down the left path
                current = current.left
            # Target belongs on the right side
            else:
                # If there is space, attach it and stop searching
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                # Otherwise, keep moving down the right path
                current = current.right
                
        # Return the unmodified root of the tree
        return root

# Helper function to print in-order traversal of the tree
def print_in_order(node):
    if node is None:
        return
    print_in_order(node.left)
    print(node.val, end=" ")
    print_in_order(node.right)

# Driver code starts here
if __name__ == "__main__":
    # Construct the initial tree: [4, 2, 7, 1, 3]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    # Instantiate the solution object
    obj = Solution()
    val = 5
    
    # Perform the optimized iterative insertion
    result = obj.insertIntoBST(root, val)
    
    # Output the entire tree via in-order traversal
    print("In-order traversal:", end=" ")
    print_in_order(result)
    print()