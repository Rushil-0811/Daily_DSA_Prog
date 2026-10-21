# Given a binary search tree, find the lowest common ancestor node of two given nodes. The Lowest Common Ancestor of a Binary Search Tree is defined as the lowest node in the tree that has both of the given nodes as descendants. According to the standard definition, a node is allowed to be a descendant of itself.

# Example 1
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8

# Output: 6

# Explanation: The node 6 is the root. Since 2 is in the left subtree and 8 is in the right subtree, 6 is the lowest node that connects both of them.

# Example 2
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4

# Output: 2

# Explanation: Both 2 and 4 are in the left side of 6. The node 2 is the direct parent of 4. Since a node can be a descendant of itself, 2 is the lowest common ancestor.

# Brute Force Approach
# Think of a large company hierarchy where managers and employees have ID numbers. All employees with smaller IDs are placed in the left department, and employees with larger IDs are in the right department. If you need to find the lowest common manager for two specific employees, you start from the CEO.

# If both employees have smaller IDs than the CEO, their common manager must be somewhere down in the left department. If both have larger IDs, you look in the right department. As soon as you find a manager where one employee is on the left and the other is on the right, you have found the exact split point. This split point is the lowest common manager.

# Algorithm
# Start checking from the main root node.

# Compare the values of the two target nodes with the current node value.

# If both target values are smaller than the current node value, the answer must be in the left subtree. Move to the left child and repeat the process.

# If both target values are larger than the current node value, the answer must be in the right subtree. Move to the right child and repeat the process.

# If one value is smaller and the other is larger, or if the current node value matches one of the targets, we have found the split point.

# Return the current node as the answer.

# Python program to implement Lowest Common Ancestor of a Binary Search Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Uses recursion to find the split point where the two target nodes diverge
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case to handle empty trees or reaching a leaf
        if not root:
            return None
            
        # If both nodes are smaller, the ancestor exists in the left branch
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        # If both nodes are larger, the ancestor exists in the right branch
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            
        # The nodes branch off in different directions, so this is the lowest ancestor
        return root

# Driver code starts
if __name__ == "__main__":
    # Setup the root node of the binary search tree
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    p = root.left
    q = root.right
    
    sol = Solution()
    # Execute the function to find the lowest common ancestor
    lca = sol.lowestCommonAncestor(root, p, q)
    
    # Print the resulting value
    if lca:
        print(lca.val)

# Optimal Approach
# The recursive approach is simple to read, but it stores function calls in memory. This takes extra space based on the depth of the tree.

# We can achieve the exact same path traversal using a simple loop. This removes the extra memory overhead entirely.

# Instead of calling a function over and over to move down the tree, we can just update our current position directly. It is like walking down a nature path and reading directional signs. At each crossing, the sign tells you whether to take the left path or the right path. You do not need to remember the steps you took; you just keep walking forward until the sign tells you that you have arrived at your destination.

# Algorithm
# Start a loop that runs as long as the current node exists.

# If both target values are smaller than the current node value, update the current node to point to its left child.

# If both target values are larger than the current node value, update the current node to point to its right child.

# If neither condition is true, we have found the split point. Break out of the loop.

# Return the current node.

# Python program to implement Lowest Common Ancestor of a Binary Search Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Uses a loop to step down the tree without extra memory overhead
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Continue searching as long as there are nodes to inspect
        while root:
            # Move left if both targets are strictly smaller
            if p.val < root.val and q.val < root.val:
                root = root.left
            # Move right if both targets are strictly larger
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # The split point is found when the paths diverge
            else:
                return root
                
        return None

# Driver code starts
if __name__ == "__main__":
    # Setup the root node of the binary search tree
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    p = root.left
    q = root.right
    
    sol = Solution()
    # Execute the function to find the lowest common ancestor
    lca = sol.lowestCommonAncestor(root, p, q)
    
    # Print the resulting value
    if lca:
        print(lca.val)