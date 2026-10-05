# Given the root of a binary tree, determine whether the tree is symmetric around its center.

# A binary tree is symmetric when its left subtree is a mirror reflection of its right subtree. Therefore, nodes at mirrored positions must:

# Both exist or both be null.

# Contain the same value.

# An empty tree and a single-node tree are both considered symmetric.

# Example 1
# Input: root = [1, 2, 2, 3, 4, 4, 3]

# Output: true

# Explanation:
# The left and right subtrees are mirror images of each other. The outer nodes 3 match, the inner nodes 4 match, and the overall structure is symmetric.

# Example 2
# Input: root = [1, 2, 2, null, 3, null, 3]

# Output: false

# Explanation:
# Although corresponding nodes contain the same values, their positions are not mirrored. Therefore, the tree is not symmetric.

# Approach 1
# Symmetry is different from checking whether the left and right subtrees are identical in the same direction.

# For two nodes to be mirror images:

# Their values must match.

# The outer children must mirror each other:
# leftNode.left with rightNode.right.

# The inner children must mirror each other:
# leftNode.right with rightNode.left.

# This naturally forms a recursive relation because after checking one mirrored pair, the same condition must hold for the two smaller mirrored pairs below it.

# Algorithm
# If root is null, return true because an empty tree is symmetric.

# Use a helper to compare root.left and root.right as mirrored nodes.

# If both compared nodes are null, return true; if exactly one is null, return false because the structures differ.

# If both nodes exist but their values differ, return false.

# Recursively compare the outer pair leftNode.left with rightNode.right.

# Recursively compare the inner pair leftNode.right with rightNode.left, and return true only if both comparisons succeed.

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def _is_mirror(
        self,
        left_node: TreeNode | None,
        right_node: TreeNode | None
    ) -> bool:
        if left_node is None and right_node is None:
            return True

        # One missing node means the mirrored structures differ.
        if left_node is None or right_node is None:
            return False

        if left_node.val != right_node.val:
            return False

        # Mirror comparison crosses left and right directions.
        return (
            self._is_mirror(
                left_node.left,
                right_node.right
            )
            and self._is_mirror(
                left_node.right,
                right_node.left
            )
        )

    def is_symmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        return self._is_mirror(root.left, root.right)


if __name__ == "__main__":
    """
            1
           / \
          2   2
         /     \
        3       3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)

    solution = Solution()

    print(solution.is_symmetric(root))

# Approach 2
# The recursive solution keeps track of mirrored node pairs through function calls. The same information can instead be stored explicitly in a queue.

# Each queue entry contains two nodes that should occupy mirrored positions.

# Whenever a valid pair is processed, its children are inserted in crossed order:

# leftNode.left with rightNode.right

# leftNode.right with rightNode.left

# As long as every stored pair matches in both structure and value, the tree remains symmetric.

# Algorithm
# If root is null, return true.

# Push (root.left, root.right) into a queue because these nodes must mirror each other.

# Remove one pair at a time. If both nodes are null, continue; if exactly one is null, return false.

# If both nodes exist but their values differ, return false.

# Push the outside pair (leftNode.left, rightNode.right) and the inside pair (leftNode.right, rightNode.left) into the queue.

# If every pair is processed without finding a mismatch, return true.

from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def is_symmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        nodes_queue = deque([
            (root.left, root.right)
        ])

        while nodes_queue:
            left_node, right_node = nodes_queue.popleft()

            if left_node is None and right_node is None:
                continue

            # One missing node breaks the mirrored structure.
            if left_node is None or right_node is None:
                return False

            if left_node.val != right_node.val:
                return False

            # Store outside and inside positions as mirror pairs.
            nodes_queue.append(
                (left_node.left, right_node.right)
            )

            nodes_queue.append(
                (left_node.right, right_node.left)
            )

        return True


if __name__ == "__main__":
    """
            1
           / \
          2   2
         /     \
        3       3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)

    solution = Solution()

    print(solution.is_symmetric(root))

# Approach 3
# The recursive mirror comparison can also be reproduced using an explicit stack instead of the call stack.

# Each stack entry stores a pair of nodes that should mirror one another. The same structural and value checks are performed, but valid crossed-child pairs are pushed manually.

# The traversal order is depth-first, but correctness depends only on keeping the corresponding mirror positions paired together.

# Algorithm
# If root is null, return true.

# Push (root.left, root.right) into a stack.

# Pop one mirrored pair at a time. If both nodes are null, continue; if exactly one is null, return false.

# If both nodes exist but their values differ, return false.

# Push the crossed child pairs so corresponding mirror positions remain together.

# If the stack becomes empty without any mismatch, return true.

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def is_symmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        nodes_stack = [(root.left, root.right)]

        while nodes_stack:
            left_node, right_node = nodes_stack.pop()

            if left_node is None and right_node is None:
                continue

            # One missing node means the structure is not mirrored.
            if left_node is None or right_node is None:
                return False

            if left_node.val != right_node.val:
                return False

            # Keep corresponding mirrored positions paired.
            nodes_stack.append(
                (left_node.right, right_node.left)
            )

            nodes_stack.append(
                (left_node.left, right_node.right)
            )

        return True


if __name__ == "__main__":
    """
            1
           / \
          2   2
         /     \
        3       3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)

    solution = Solution()

    print(solution.is_symmetric(root))

    