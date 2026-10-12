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

# Approach 2
# Storing the complete preorder traversal can be avoided by creating the required links while recursion returns.

# The desired flattened order is:

# Root → Left → Right

# If the tree is processed in the reverse order:

# Right → Left → Root

# a pointer named previous can be maintained. The name represents the node that should appear immediately after the current node in the final flattened preorder sequence.

# Once both subtrees have been processed, the current node can be connected directly to previous.

# The following updates are performed:

# current.right = previous

# current.left = null

# previous = current

# In this way, the flattened structure is built backward while only the recursion stack is required.

# Algorithm
# A pointer named previous is maintained to represent the node that should immediately follow the current node in the final flattened preorder sequence.

# The right subtree is processed before the left subtree because the flattened list is being constructed in reverse preorder order.

# After both recursive calls have been completed, the current node's right pointer is connected to previous.

# The current node's left pointer is set to null because no left links are allowed in the flattened structure.

# previous is updated to the current node so that the next ancestor processed during recursion can be connected to it.

# Once the root has been processed, the complete preorder-linked structure has been formed.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Processes nodes in reverse preorder so
    # previous is always the next flattened node.
    def reverse_preorder(self, root):
        if root is None:
            return

        self.reverse_preorder(root.right)
        self.reverse_preorder(root.left)

        # previous is the node that must follow
        # the current node in normal preorder.
        root.right = self.previous
        root.left = None

        self.previous = root

    # Flattens the tree using reverse
    # preorder and recursion.
    def flatten(self, root):
        self.previous = None

        self.reverse_preorder(root)

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

# Approach 3
# The tree can also be flattened without storing nodes and without using recursion.

# A pointer named current is used to represent the node whose links are currently being rearranged.

# Whenever current has a left subtree, preorder traversal requires the entire left subtree to appear before the original right subtree:

# current → left subtree → right subtree

# Therefore, the left subtree must be moved to current.right.

# Before this can be done, the original right subtree must be preserved. A pointer can be moved to the rightmost node of the left subtree. This node is important because after the left subtree has been rewired into the right chain, it becomes the final node visited before preorder should continue into the original right subtree.

# The original right subtree is therefore attached to this rightmost node. The left subtree is then shifted to the right, and current.left is cleared.

# The process continues by moving current through the newly formed right pointers.

# Algorithm
# A pointer named current is initialized with the root so that the tree can be processed directly through its existing links.

# While current is not null, its local subtree structure is examined.

# If no left child exists, no rewiring is required at that node, and current is advanced to its right child.

# If a left subtree exists, its rightmost node is located because that node must connect to the original right subtree after the left subtree is moved.

# The original current.right subtree is attached to the right pointer of this rightmost node so that it is not lost.

# The left subtree is moved to current.right, and current.left is set to null, placing the former left subtree immediately after the current node in preorder.

# current is then advanced through its right pointer, and the process is continued until every node has been rewired.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Rewires the tree directly into preorder
    # using constant auxiliary space.
    def flatten(self, root):
        current = root

        while current is not None:

            if current.left is not None:
                rightmost = current.left

                # The rightmost node of the left subtree
                # must precede the original right subtree.
                while rightmost.right is not None:
                    rightmost = rightmost.right

                # The original right subtree is preserved
                # after the complete left subtree.
                rightmost.right = current.right

                # The left subtree is moved to the right
                # because preorder visits it next.
                current.right = current.left
                current.left = None

            current = current.right

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