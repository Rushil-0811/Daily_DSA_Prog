# Given the root of a binary tree, modify the tree in-place so that it becomes a linked-list-like structure following the tree's preorder traversal.

# After flattening:

# Every node's left pointer must be null.

# Every node's right pointer must point to the next node in preorder.

# The original TreeNode structure must be reused.

# Return the root of the flattened tree.

# Example 1
# Input:
# root = [1, 2, 5, 3, 4, null, 6]

# Output:
# [1, null, 2, null, 3, null, 4, null, 5, null, 6]

# Explanation:
# The preorder traversal of the original tree is 1 -> 2 -> 3 -> 4 -> 5 -> 6. After flattening, every left pointer becomes null, while the right pointers connect the nodes in this preorder sequence.

# Example 2
# Input:
# root = [1, 2, 3]

# Output:
# [1, null, 2, null, 3]

# Explanation:
# The preorder traversal is 1 -> 2 -> 3, so the flattened tree contains the same sequence connected only through right pointers.

# Approach 1
# The flattened tree must follow exactly the same order as a preorder traversal:

# Root → Left → Right

# A straightforward approach is to first perform preorder traversal and store references to all visited nodes in a list. Once traversal is completed, the required ordering is already available.

# The stored nodes can then be reconnected so that every node points to the next node through its right pointer, while its left pointer is cleared.

# This keeps traversal and pointer modification separate, which makes the approach simple to understand, but storing all nodes requires additional linear space.

# Algorithm
# A preorder traversal is performed, and every visited node is stored in a list because preorder gives exactly the order required in the flattened tree.

# After traversal has been completed, consecutive nodes in the stored list are processed.

# For each node except the last one, its left pointer is set to null because the flattened structure must not contain left links.

# Its right pointer is connected to the next node in the preorder list so that the required sequence is preserved.

# For the final node, both child pointers are adjusted so that it becomes the end of the flattened structure.

# After all links have been rearranged, the original root is returned.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Stores nodes in the exact preorder
    # required by the flattened tree.
    def preorder(self, root, nodes):
        if root is None:
            return

        nodes.append(root)

        self.preorder(root.left, nodes)
        self.preorder(root.right, nodes)

    # Reconnects preorder nodes into
    # one right-linked chain.
    def flatten(self, root):
        if root is None:
            return None

        nodes = []

        self.preorder(root, nodes)

        # Consecutive preorder nodes are linked
        # using only their right pointers.
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        # The final node terminates
        # the flattened structure.
        nodes[-1].left = None
        nodes[-1].right = None

        return root


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    solution = Solution()
    root = solution.flatten(root)

    current = root

    while current is not None:
        print(current.val, end=" ")
        current = current.right