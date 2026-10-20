# Given the root of a binary tree, determine if it is a valid binary search tree. A Validate Binary Search Tree requires specific conditions to be true. The left subtree of a node must contain only nodes with keys strictly less than the node's key. The right subtree of a node must contain only nodes with keys strictly greater than the node's key. Furthermore, both the left and right subtrees must also be valid binary search trees themselves.

# Example 1
# Input: root = [2,1,3]

# Output: true

# Explanation: The root node is 2. The left child is 1, which is less than 2. The right child is 3, which is greater than 2. All conditions are satisfied.

# Example 2
# Input: root = [5,1,4,null,null,3,6]

# Output: false

# Explanation: The root node is 5. However, its right child is 4, which is strictly less than 5. This violates the property of a binary search tree.

# Brute Force Approach
# When checking if a tree is valid, it is not enough to just compare a parent node with its direct left and right children. A node deep in the right subtree might be greater than its immediate parent, but it still must be greater than the main root node of the entire tree.

# Consider a security checkpoint system where people are sorted into different zones based on their clearance levels. Once you are directed to the left wing, your clearance level has a strict maximum limit. If you are then directed to the right room within that wing, you gain a minimum limit, but your maximum limit from the previous step still applies.

# Similarly, we give each node a valid numerical range. As we travel left, we update the maximum allowed value. As we travel right, we update the minimum allowed value. If any node falls out of its allowed range, the entire tree is invalid.

# Algorithm
# Start at the root node and define the initial valid range from negative infinity to positive infinity.

# Check if the current node is empty. If it is, return true because an empty tree is valid.

# Check if the current node value falls strictly within the allowed minimum and maximum boundaries.

# If the value is out of bounds, return false.

# Recursively call the function for the left child, updating the maximum boundary to the current node value.

# Recursively call the function for the right child, updating the minimum boundary to the current node value.

# Return true only if both left and right subtree checks return true.

# Python program to implement Validate Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Validates if the tree is a BST by checking against a valid range
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkBST(root, float('-inf'), float('inf'))

    # Helper function to maintain the minimum and maximum boundaries
    def checkBST(self, node: TreeNode, min_val: float, max_val: float) -> bool:
        # Base case: an empty subtree is always valid
        if not node:
            return True
            
        # Node value must be strictly within the allowed range
        if node.val <= min_val or node.val >= max_val:
            return False
            
        # Traverse left updating maximum, traverse right updating minimum
        return self.checkBST(node.left, min_val, node.val) and self.checkBST(node.right, node.val, max_val)

# Driver code starts
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    result = sol.isValidBST(root)
    print(result)

# Optimal Approach
# Why the previous approach is inefficient The recursive range approach is highly efficient in time complexity. However, dealing with maximum and minimum infinity values can sometimes cause integer overflow issues in specific programming languages if not handled carefully.

# What improvement this approach brings This approach avoids passing extreme minimum and maximum values down the tree. Instead, it relies on a core property of binary search trees: an inorder traversal of a valid BST will always process the nodes in strictly increasing order.

# Think of reading books on a shelf arranged in alphabetical order. You process them one by one from left to right. If you ever pick up a book that comes alphabetically before the one you just read, you immediately know the shelf is disarrayed. By performing an inorder traversal which means visiting the left child, then the root, then the right child, we can maintain a reference to the previously visited node. If the current node is not greater than the previous node, the tree is invalid.

# Algorithm
# Create a variable to store the previously visited node, initially set to null.

# Perform a recursive inorder traversal starting from the root.

# Traverse the left subtree. If it returns false, propagate the false result upwards.

# Check the current node against the previously visited node. If the current node value is less than or equal to the previous value, return false.

# Update the previously visited node to be the current node.

# Traverse the right subtree and return its result.

# Python program to implement Validate Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None

    # Validates if the tree is a BST using inorder traversal
    def isValidBST(self, root: TreeNode) -> bool:
        # Base case: empty tree is valid
        if not root:
            return True
            
        # Check left subtree recursively
        if not self.isValidBST(root.left):
            return False
            
        # Compare current node with the previously visited node
        if self.prev and root.val <= self.prev.val:
            return False
            
        # Update previous node to current before moving right
        self.prev = root
        
        # Check right subtree recursively
        return self.isValidBST(root.right)

# Driver code starts
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    result = sol.isValidBST(root)
    print(result)