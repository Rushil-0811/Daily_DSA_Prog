# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,2,3]

# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [1,2,4,5,6,7,3,8,9]

# The core idea of a preorder traversal is to visit the nodes of a binary tree in a specific, consistent order: Root, then Left subtree, and finally, Right subtree. This means we process a node's value before moving on to its children. This approach is a type of Depth-First Search (DFS), where we explore as far as possible down one branch before backtracking.

# The most straightforward way to implement this is using a recursive function. We'll create a helper function that performs the traversal.

# Base Case: The recursive function first checks if the current node is null. If it is, we've reached the end of a branch and simply return.

# Visit Root: If the node is not null, we "visit" it. For this problem, visiting means adding its value to our result vector. This happens before any recursive calls.

# Traverse Left: We then make a recursive call on the node's left child. This ensures that the entire left subtree is traversed completely before we move on.

# Traverse Right: Finally, we make a recursive call on the node's right child, completing the traversal of the current node's subtrees.

# This process naturally adheres to the "Root -> Left -> Right" order, building the preorder list as the recursion unfolds.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def preorder_helper(node):
            if not node:
                return
            result.append(node.val)
            preorder_helper(node.left)
            preorder_helper(node.right)

        preorder_helper(root)
        return result