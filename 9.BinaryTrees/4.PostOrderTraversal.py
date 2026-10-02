# # Given the root of a binary tree, return the postorder traversal of its nodes' values.
# # Input: root = [1,null,2,3]

# # Output: [3,2,1]

# # Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# # Output: [4,6,7,5,2,9,8,3,1]

# To traverse a tree, we use two main strategies:

# Breadth-First Search (BFS): This strategy involves scanning the tree level by level from the top down, visiting nodes at higher levels before those at lower levels.

# Depth-First Search (DFS): This approach explores as far down a branch as possible before backtracking. It starts at the root, proceeds to a leaf, and then returns to explore other branches. DFS can be further categorized into:

# Preorder: Visit the root first, then the left subtree, followed by the right subtree.
# Inorder: Visit the left subtree first, then the root, and then the right subtree.
# Postorder: Visit the left subtree first, then the right subtree, and finally the root.

# Approach 1: Recursive Postorder Traversal

# Figure 2. Recursive DFS traversals.

# In this approach, we treat each node as the root of its subtree. We start by recursively traversing the left subtree. If the left child is not null, we continue exploring until the left subtree is fully traversed. Then, we move to the right subtree and repeat the process. After both subtrees are explored, we process the current node by adding its value to the result list.

# The base case occurs when the current node is null, indicating no further subtree to explore. At this point, we simply return and backtrack.

# Define a helper function postorderTraversalHelper:
# If currentNode is null, return to stop further recursion.
# Recursively call postorderTraversalHelper with currentNode->left to process the left subtree.
# Recursively call postorderTraversalHelper with currentNode->right to process the right subtree.
# Append currentNode->val to the result array to collect values in postorder.
# In the postorderTraversal function:
# Initialize an empty result array to store the postorder ordering of the nodes inroot.
# Call postorderTraversalHelper with the root node and result to start the traversal.
# Return the result array containing the postorder traversal.
# Approach 2: Manipulating Preorder Traversal (Iterative Hack)
# Intuition
# Let's take a creative leap in this approach by exploiting the relationship between preorder and postorder traversals. In a standard preorder traversal, we visit the root node before we visit the left and right subtrees. However, postorder traversal requires us to visit the left and right subtrees before the root node.

# We can adapt the preorder traversal by visiting nodes in the order of root, right subtree, and then left subtree. Reversing the resulting list from this modified preorder traversal gives us the correct postorder sequence.

# We use a stack to traverse the tree iteratively, starting with the root node. We push the current node onto the stack and add its value to the result list. Instead of moving to the left child, we move to the right child. If there's no right child, we pop a node from the stack and move to its left child. This approach processes the right subtree before the left subtree, aligning with the modified preorder traversal.

# After traversing the entire tree, we reverse the result list to get the postorder sequence: left subtree, right subtree, root.

# Initialize an empty result list to store the traversal result, a traversalStack for nodes, and set currentNode to root.
# While currentNode is not null or traversalStack is not empty:
# If currentNode is not null, add currentNode->val to the result list before processing its children.
# Push currentNode onto the traversalStack to revisit it later.
# Move currentNode to currentNode->right to continue traversal in the right subtree.
# If currentNode is null, pop the top node from traversalStack and set it to currentNode.
# Move currentNode to currentNode->left to process the left subtree.
# Reverse the result list to correct the order from preorder to postorder.
# Return the result list with postorder traversal values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root):
        # List to store the result of postorder traversal
        result = []
        # Stack to facilitate the traversal of nodes
        traversal_stack = []
        current_node = root

        # Traverse the tree while there are nodes to process
        while current_node or traversal_stack:
            if current_node:
                # Add current node's value to result list before going to its children
                result.append(current_node.val)
                # Push current node onto the stack
                traversal_stack.append(current_node)
                # Move to the right child
                current_node = current_node.right
            else:
                # Pop the node from the stack and move to its left child
                current_node = traversal_stack.pop()
                current_node = current_node.left
        # Reverse the result list to get the correct postorder sequence
        result.reverse()
        return result

# Approach 3: Two Stack Postorder Traversal (Iterative)
# Intuition
# Instead of relying on hacks and tricks, this time we will build on the idea that we need to control the order in which nodes are processed to achieve postorder traversal.

# To achieve postorder traversal without recursion, we use two stacks to control the node processing order systematically.

# First, we push the root node onto the first stack. This stack simulates the recursive traversal of the tree. To process nodes in postorder (left-right-root), we need a second stack to reverse the order. As we pop nodes from the first stack, we push them onto the second stack. This reversal ensures that nodes are processed in the correct order.

# After all nodes are transferred to the second stack, popping from it gives us the nodes in postorder sequence. This method efficiently achieves the desired traversal order by leveraging the two stacks to manage the processing sequence without needing a final reversal step.

# In summary, the two-stack approach uses the first stack for tree traversal and the second stack to reverse the order, resulting in a postorder traversal. Despite initially seeming like a manipulation of preorder traversal, the final order of nodes from the second stack aligns with postorder traversal.

# Algorithm
# Initialize an empty result list, and create mainStack and pathStack for nodes.
# Check if root is null; if so, return result immediately, indicating there are no nodes to process.
# Push root onto mainStack to start the traversal.
# While mainStack is not empty:
# Peek at the top of mainStack to examine the current node.
# If the top of pathStack is the same as the top of mainStack, add root->val to the result list.
# Pop the top node from both mainStack and pathStack after processing.
# Otherwise, push the current node onto pathStack.
# Push root->right and root->left onto mainStack if they exist to process their children.
# Return the result list containing postorder traversal values

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root):
        result = []

        # If the root is null, return an empty list
        if root is None:
            return result

        # Stack to manage the traversal
        main_stack = []
        # Stack to manage the path
        path_stack = []

        # Start with the root node
        main_stack.append(root)

        # Process nodes until the main stack is empty
        while main_stack:
            root = main_stack[-1]

            # If the node is in the path stack and it's the top, add its value
            if path_stack and path_stack[-1] == root:
                result.append(root.val)
                main_stack.pop()
                path_stack.pop()
            else:
                # Push the current node to the path stack
                path_stack.append(root)
                # Push right child if it exists
                if root.right is not None:
                    main_stack.append(root.right)
                # Push left child if it exists
                if root.left is not None:
                    main_stack.append(root.left)

        return result