# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Initialize Data Structures:

# We start by initializing two data structures: a List<Integer> called result to store the inorder traversal result and a Stack<TreeNode> called stack to help us simulate the recursive process iteratively.
# We also initialize a TreeNode called curr and set it to the root of the binary tree.
# Main Loop:

# The main part of the code is a while loop that continues until curr becomes null (indicating we have traversed the entire tree) and the stack is empty (indicating we've processed all nodes).
# Traverse Left Subtree and Push Nodes onto the Stack:

# Within the while loop, we have another while loop to traverse the left subtree of the current node (curr) and push all encountered nodes onto the stack.
# We keep going left as long as curr is not null, pushing each encountered node onto the stack. This is done to simulate the left subtree traversal.
# Visit the Current Node and Move to the Right Subtree:

# Once we've traversed all the way to the left (or if curr is null), we pop a node from the stack. This node represents the current root of a subtree that needs to be processed.
# We add the value of the current node (curr.val) to the result list, as it's part of the inorder traversal.
# We then update curr to point to the right child of the current node. This will ensure that if there's a right subtree, we'll traverse it next. If there's no right subtree, this step will essentially move us up in the tree to the parent of the current node.
# Repeat:

# We repeat steps 3 and 4 until we've traversed the entire binary tree. This process effectively simulates an inorder traversal iteratively using a stack.
# Return Result:

# Finally, after the loop has finished, we return the result list, which contains the inorder traversal of the binary tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result
