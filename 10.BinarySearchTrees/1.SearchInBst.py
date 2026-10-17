# In the Search in a Binary Search Tree problem, you are given the root node of a binary search tree and an integer target value. Your task is to find the specific node in the tree where the node value perfectly matches the target value. Once found, you must return the entire subtree rooted at that specific node. If the target value does not exist anywhere in the tree, the function should return null.

# Example 1
# Input: root = [4, 2, 7, 1, 3], val = 2

# Output: [2, 1, 3]

# Explanation: The tree has a root of 4. The target value 2 exists as the left child of 4. We locate the node containing 2 and return it, which also inherently includes its children 1 and 3.

# Example 2
# Input: root = [4, 2, 7, 1, 3], val = 5

# Output: []

# Explanation: We search the entire tree for the value 5. Since 5 does not exist in any node, we return an empty result (null).

# Brute Force Approach
# A Binary Search Tree is organized so that everything to the left of a node is strictly smaller, and everything to the right is strictly larger. Think about looking up a word in a physical dictionary. You open the book near the middle. If the word you want comes alphabetically before the page you are on, you completely ignore the right half of the book and only search the left half. You repeat this exact same process on the smaller section until you find the exact word. We can apply this exact logic recursively, checking the current node and moving left or right accordingly.

# Algorithm
# Check the base case: if the current node is null, it means we have reached the bottom without finding the value, so return null.

# Check if the current node value matches the target value. If it does, return the current node immediately.

# If the target value is smaller than the current node value, make a recursive call to search only the left subtree.

# If the target value is larger than the current node value, make a recursive call to search only the right subtree.

# Python program to implement Search in a Binary Search Tree

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursively traverses the tree by moving left or right
    # based on the binary search tree property
    def searchBST(self, root, val):
        # Base case: if the tree is empty or we hit a dead end
        if root is None:
            return None
            
        # Base case: if we find the exact target value, return this node
        if root.val == val:
            return root
            
        # If the target is strictly smaller, search only the left side
        if val < root.val:
            return self.searchBST(root.left, val)
            
        # If the target is strictly larger, search only the right side
        return self.searchBST(root.right, val)

# Driver code starts here
if __name__ == "__main__":
    # Constructing a sample binary search tree: [4, 2, 7, 1, 3]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    obj = Solution()
    target = 2
    
    # Perform the recursive search
    result = obj.searchBST(root, target)
    
    # Print the result to verify correctness
    if result is not None:
        print(result.val)
    else:
        print("Not found")

# Optimal Approach
# The recursive approach is simple to read, but it is technically inefficient regarding memory. Every time a recursive call is made, the program uses system stack space. For a very deep, skewed tree, this can cause a stack overflow error. We can vastly improve our space usage by eliminating recursion entirely and using a simple pointer to navigate down the tree iteratively.

# Consider navigating a physical branching hallway inside an office building. You start at the main entrance (the root). At every intersection, there is a numbered sign. If the office number you are looking for is smaller than the sign, you physically walk down the left hallway. If it is larger, you walk down the right hallway. You never need to remember the path you took to get there; you simply update your current location step-by-step until you reach the correct door.

# Algorithm
# Start a loop that runs as long as the current node is not null.

# Inside the loop, check if the current node value perfectly matches the target value. If yes, return the node immediately.

# If the target value is smaller than the current node value, update your current node pointer to the left child.

# If the target value is greater than the current node value, update your current node pointer to the right child.

# If the loop breaks because the node becomes null, it means the value does not exist. Return null.

# Python program to implement Search in a Binary Search Tree

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iteratively navigates down the tree using a single pointer
    # to completely avoid recursive memory overhead
    def searchBST(self, root, val):
        # Continue looping down the tree until we hit a dead end
        while root is not None:
            # If we find an exact match, stop and return the current node
            if root.val == val:
                return root
                
            # Shift the pointer left if the target is smaller
            if val < root.val:
                root = root.left
            # Shift the pointer right if the target is larger
            else:
                root = root.right
                
        # If the loop completely finishes, the value is not in the tree
        return None

# Driver code starts here
if __name__ == "__main__":
    # Constructing a sample binary search tree: [4, 2, 7, 1, 3]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    obj = Solution()
    target = 2
    
    # Perform the optimized iterative search
    result = obj.searchBST(root, target)
    
    # Print the result to verify correctness
    if result is not None:
        print(result.val)
    else:
        print("Not found")